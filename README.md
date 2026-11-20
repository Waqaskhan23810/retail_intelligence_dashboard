# 🛍️ Retail Intelligence Dashboard

A comprehensive sales and profitability analysis dashboard built with Streamlit. This application helps retail businesses analyze their performance, identify trends, and make data-driven decisions.

---

## 🚀 Live Dashboard

**Access the live dashboard here:**

### ➡️ [Open Retail Intelligence Dashboard](https://retailintelligencedashboard-mbnlzd75pvfsnkju4lfxxd.streamlit.app/)

Click the link above to view the interactive dashboard in your browser. No installation required!

**URL:** `https://retailintelligencedashboard-mbnlzd75pvfsnkju4lfxxd.streamlit.app/`

---

## 📊 About This Project

This dashboard provides real-time insights into your retail business performance. It processes retail transaction data and presents key metrics, trends, and detailed analytics through an intuitive web interface.

The application reads your cleaned retail dataset, applies advanced filters, and visualizes sales and profitability metrics with interactive charts and KPI cards.

---

## ✨ Features

### 📈 **Key Performance Indicators (KPIs)**
- Total sales overview
- Profit analysis and margins
- Real-time performance metrics

### 🔍 **Advanced Filtering**
- Filter by **Region** - Analyze specific geographic areas
- Filter by **Category** - Focus on product categories
- Filter by **Customer Age** - Segment by age groups
- **Search functionality** - Find products, categories, or regions quickly

### 📉 **Analytics & Trends**
- Timeline sales trends - Track performance over time
- Profit trends - Monitor profitability patterns
- Detailed order table - Review individual transactions

### 💡 **User-Friendly Interface**
- Interactive charts and visualizations
- Responsive design that works on all devices
- Real-time data updates

---

## 🛠️ Project Structure

```
retail_intelligence_dashboard/
├── app.py                    # Main Streamlit application file
├── retail_filtered.csv       # Cleaned retail transaction dataset
├── requirements.txt          # Python dependencies
├── README.md                 # This file
├── .gitignore               # Git ignore rules
├── .streamlit/              # Streamlit configuration
│   ├── config.toml          # Streamlit settings
│   └── README.md            # Quick reference
├── tests/                   # Test files
│   └── test_app.py          # Smoke tests for data and logic
└── .devcontainer/           # Development container configuration
```

### File Descriptions

- **`app.py`** - The main Streamlit application containing all dashboard logic, visualizations, and filters
- **`retail_filtered.csv`** - Your retail transaction dataset with cleaned and processed data
- **`requirements.txt`** - List of Python packages needed to run the application
- **`tests/test_app.py`** - Automated tests to verify data loading and calculations

---

## 🚀 Getting Started Locally

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git

### Installation & Setup

**Step 1: Clone the Repository**
```bash
git clone https://github.com/Waqaskhan23810/retail_intelligence_dashboard.git
cd retail_intelligence_dashboard
```

**Step 2: Create a Virtual Environment**
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python -m venv venv
source venv/bin/activate
```

**Step 3: Install Dependencies**
```bash
pip install -r requirements.txt
```

**Step 4: Run the Dashboard**
```bash
streamlit run app.py
```

**Step 5: View in Browser**
- Streamlit will automatically open your browser
- If not, visit: `http://localhost:8501`

---

## 📊 Data Source

The dashboard uses the **`retail_filtered.csv`** file included in this repository. This dataset contains:
- Retail transaction records
- Sales figures
- Product categories
- Regional information
- Customer demographics
- Profitability metrics

The data has been cleaned and preprocessed for optimal dashboard performance.

---

## 🧪 Running Tests

To verify that the application is working correctly, run the test suite:

```bash
pytest tests/test_app.py
```

Tests include:
- Data loading verification
- Summary calculations validation
- Data integrity checks

---

## 🔧 Configuration

The dashboard configuration is managed in `.streamlit/config.toml`:

```toml
[server]
headless = true
port = 8501
enableCORS = false
enableXsrfProtection = false
```

Adjust these settings if needed for your deployment environment.

---

## 📝 Usage Tips

1. **Start with KPIs** - Review the key metrics at the top of the dashboard
2. **Apply Filters** - Use the sidebar to filter by region, category, or age
3. **Search Products** - Use the search feature to find specific products or categories
4. **Analyze Trends** - Check the timeline charts to identify sales patterns
5. **Review Details** - Scroll to the order table for transaction-level details

---

## 📚 Development Notes

This repository has been cleaned and rebuilt as a proper, production-ready Streamlit application. It replaces the previous static HTML dashboard approach with a dynamic, interactive web application that:

- ✅ Loads and processes data efficiently
- ✅ Provides real-time filtering and search
- ✅ Generates interactive visualizations
- ✅ Includes automated testing
- ✅ Follows Python best practices

---

## 📦 Dependencies

Main packages used (see `requirements.txt` for versions):
- **streamlit** - Web application framework
- **pandas** - Data analysis and manipulation
- **plotly** - Interactive visualizations
- **pytest** - Testing framework

---

## 🤝 Contributing

To contribute to this project:
1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Test your changes (`pytest tests/`)
5. Commit your changes (`git commit -m 'Add improvement'`)
6. Push to your fork (`git push origin feature/improvement`)
7. Open a Pull Request

---

## 📞 Support

For issues, questions, or suggestions:
- Open an issue on GitHub
- Check existing issues for solutions
- Review the code comments for implementation details

---

## 📄 License

This project is available under the MIT License.

---

## 🎯 Quick Links

- 🌐 **Live Dashboard:** [https://retailintelligencedashboard-mbnlzd75pvfsnkju4lfxxd.streamlit.app/](https://retailintelligencedashboard-mbnlzd75pvfsnkju4lfxxd.streamlit.app/)
- 💻 **GitHub Repository:** [https://github.com/Waqaskhan23810/retail_intelligence_dashboard](https://github.com/Waqaskhan23810/retail_intelligence_dashboard)
- 📊 **Streamlit Documentation:** [https://docs.streamlit.io](https://docs.streamlit.io)

---

**Last Updated:** November 20, 2026

Happy analyzing! 📊✨
