# Smart Saver: AI-Powered Personal Finance Analytics

[![Python](https://img.shields.io/badge/Python-3.14-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/UI-Streamlit-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Pandas](https://img.shields.io/badge/Data-Pandas-150458?logo=pandas&logoColor=white)](https://pandas.pydata.org/)

## 📌 Project Overview
**FinTrack** is a modular Data Science application developed to transform raw financial transactions into actionable spending insights. Built as an industry-oriented project, it solves the problem of "invisible spending" by providing a centralized dashboard for expense logging, categorical breakdown, and monthly trend analysis.

## 🚀 Key Features
- **Persistent Data Logging:** Uses a local CSV-based database system to ensure data survives application restarts.
- **Categorical Intelligence:** Automatically aggregates expenses into categories (Food, Travel, Rent, etc.) using **Pandas**.
- **Interactive Visualizations:** - **Pie Charts:** For immediate category-wise spending distribution.
  - **Line Graphs:** For tracking financial trajectory over time.
- **Modular Architecture:** Separation of backend logic (`src/logic.py`) from frontend UI (`app.py`).

## 🛠️ Technical Stack
| Component | Technology |
| :--- | :--- |
| **Language** | Python 3.14 |
| **Data Processing** | Pandas, NumPy |
| **Visualization** | Matplotlib, Seaborn |
| **Web Framework** | Streamlit |

## 📂 Project Structure
```text
Expense-Tracker-DS/
├── data/               
│   └── expenses.csv       # Persistent Ledger Storage
├── src/
│   └── logic.py           # Core Analytics Engine (Modular Logic)
├── app.py                 # Main Streamlit Dashboard UI
├── requirements.txt       # Dependencies
└── README.md              # Project Documentation
```
## Data Science Logic Flow
Ingestion: User inputs transaction details via the Streamlit sidebar.

Persistence: Data is appended to a structured CSV file using mode='a'.

Processing: The logic.py module cleans and groups data using Pandas .groupby() and .strftime() functions.

Insight: Matplotlib generates statistical plots to visualize the user's financial behavior.

## 🏁 Installation & Usage
Clone the Repo:

PowerShell
git clone [https://github.com/YOUR_USERNAME/Expense-Tracker-DS.git](https://github.com/pruthvilr/Expense-Tracker-DS.git)
Install Tools:

PowerShell
python -m pip install -r requirements.txt
Run App:

PowerShell
python -m streamlit run app.py
## 👨‍💻 Author
Pruthvi

First Year ISE Student

Siddaganga Institute of Technology (SIT), Tumakuru
