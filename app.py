from __future__ import annotations

from pathlib import Path

import pandas as pd
import streamlit as st


DATA_PATH = Path(__file__).parent / "retail_filtered.csv"


@st.cache_data
def load_data() -> pd.DataFrame:
    df = pd.read_csv(DATA_PATH)
    df["OrderDate"] = pd.to_datetime(df["OrderDate"], errors="coerce")
    df["Sales"] = pd.to_numeric(df["Sales"], errors="coerce")
    df["Profit"] = pd.to_numeric(df["Profit"], errors="coerce")
    df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")
    df["CustomerAge"] = pd.to_numeric(df["CustomerAge"], errors="coerce")
    return df.dropna(subset=["OrderDate", "Region", "Category", "Product"]).reset_index(drop=True)


@st.cache_data
def filter_data(
    df: pd.DataFrame,
    region: str | None = None,
    category: str | None = None,
    min_age: int = 18,
    max_age: int = 80,
    search_term: str = "",
) -> pd.DataFrame:
    filtered = df.copy()

    if region and region != "All":
        filtered = filtered[filtered["Region"] == region]
    if category and category != "All":
        filtered = filtered[filtered["Category"] == category]

    filtered = filtered[(filtered["CustomerAge"] >= min_age) & (filtered["CustomerAge"] <= max_age)]

    if search_term:
        term = search_term.strip().lower()
        if term:
            filtered = filtered[
                filtered["Product"].str.lower().str.contains(term, na=False)
                | filtered["Category"].str.lower().str.contains(term, na=False)
                | filtered["Region"].str.lower().str.contains(term, na=False)
            ]

    return filtered.reset_index(drop=True)


@st.cache_data
def compute_summary(df: pd.DataFrame) -> dict[str, float | int | str]:
    total_sales = float(df["Sales"].sum())
    total_profit = float(df["Profit"].sum())
    total_orders = int(df.shape[0])
    avg_profit_margin = float(df["Profit"].sum() / df["Sales"].sum() * 100) if df["Sales"].sum() else 0.0
    top_category = df["Category"].mode().iloc[0] if not df.empty else "N/A"

    return {
        "total_sales": total_sales,
        "total_profit": total_profit,
        "total_orders": total_orders,
        "avg_profit_margin": avg_profit_margin,
        "top_category": top_category,
    }


def render_sidebar(df: pd.DataFrame) -> tuple[str | None, str | None, int, int, str]:
    st.sidebar.header("Filters")

    regions = ["All", *sorted(df["Region"].dropna().unique().tolist())]
    regions_list = [str(item) for item in regions]
    region = st.sidebar.selectbox("Region", regions_list, index=0)

    categories = ["All", *sorted(df["Category"].dropna().unique().tolist())]
    category = st.sidebar.selectbox("Category", [str(item) for item in categories], index=0)

    age_min, age_max = st.sidebar.slider(
        "Customer age range",
        min_value=int(df["CustomerAge"].min()),
        max_value=int(df["CustomerAge"].max()),
        value=(int(df["CustomerAge"].min()), int(df["CustomerAge"].max())),
    )

    search_term = st.sidebar.text_input("Search product/category/region", placeholder="e.g. Laptop")
    return region, category, age_min, age_max, search_term


def main() -> None:
    st.set_page_config(page_title="Retail Intelligence Dashboard", layout="wide")
    df = load_data()

    st.title("Retail Intelligence Dashboard")
    st.caption("Monitor sales, profit, and customer behavior across key retail categories.")

    region, category, min_age, max_age, search_term = render_sidebar(df)
    filtered = filter_data(df, region=region, category=category, min_age=min_age, max_age=max_age, search_term=search_term)
    summary = compute_summary(filtered)

    st.markdown("---")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Sales", f"${summary['total_sales']:,.2f}")
    col2.metric("Total Profit", f"${summary['total_profit']:,.2f}")
    col3.metric("Orders", f"{summary['total_orders']:,}")
    col4.metric("Avg Margin", f"{summary['avg_profit_margin']:.2f}%")

    st.markdown("### Business performance")
    c1, c2 = st.columns(2)

    monthly = filtered.groupby(filtered["OrderDate"].dt.to_period("M")).agg(
        sales=("Sales", "sum"), profit=("Profit", "sum")
    )
    monthly.index = monthly.index.astype(str)
    c1.line_chart(monthly[["sales"]], color="#2E86DE")
    c2.bar_chart(monthly[["profit"]], color="#27AE60")

    category_sales = filtered.groupby("Category")["Sales"].sum().sort_values(ascending=False)
    region_sales = filtered.groupby("Region")["Sales"].sum().sort_values(ascending=False)

    c1, c2 = st.columns(2)
    c1.bar_chart(category_sales)
    c2.bar_chart(region_sales)

    st.markdown("### Detailed table")
    st.dataframe(
        filtered[["OrderID", "OrderDate", "Region", "Category", "Product", "Quantity", "Sales", "Profit", "CustomerAge", "PaymentMode"]].sort_values("OrderDate", ascending=False),
        use_container_width=True,
    )

    if filtered.empty:
        st.warning("No records match the selected filters. Try broadening the filter values.")


if __name__ == "__main__":
    main()
