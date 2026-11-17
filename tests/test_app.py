from app import compute_summary, filter_data, load_data


def test_load_data_has_expected_columns():
    df = load_data()

    required = {"OrderID", "OrderDate", "Region", "Category", "Sales", "Profit"}
    assert required.issubset(df.columns)


def test_filter_data_and_summary_are_valid():
    df = load_data()
    filtered = filter_data(df, region="North", category="Electronics")
    summary = compute_summary(filtered)

    assert not filtered.empty
    assert summary["total_sales"] > 0
    assert summary["total_profit"] >= 0
