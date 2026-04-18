import streamlit as st
import pandas as pd
from src.logic import calculate_monthly_summary, get_category_distribution
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Page Config
st.set_page_config(page_title="FinTrack DS", layout="wide")
st.title(" Smart saver: Data-Driven Expense Manager")

# Data Persistence Logic
DATA_PATH = "data/expenses.csv"
if not os.path.exists('data'): os.makedirs('data')
if not os.path.exists(DATA_PATH):
    pd.DataFrame(columns=['Date', 'Category', 'Amount', 'Note']).to_csv(DATA_PATH, index=False)

# --- SIDEBAR: INPUT DATA ---
st.sidebar.header("📥 Log New Transaction")
with st.sidebar.form("input_form", clear_on_submit=True):
    date = st.date_input("Date")
    cat = st.selectbox("Category", ["Food", "Travel", "Rent", "Shopping", "Bills", "Health"])
    amt = st.number_input("Amount (₹)", min_value=0.0)
    note = st.text_input("Note")
    if st.form_submit_button("Add to Ledger"):
        new_row = pd.DataFrame([[date, cat, amt, note]], columns=['Date', 'Category', 'Amount', 'Note'])
        new_row.to_csv(DATA_PATH, mode='a', header=False, index=False)
        st.sidebar.success("Recorded!")

# --- MAIN DASHBOARD ---
df = pd.read_csv(DATA_PATH)

if not df.empty:
    # 1. Summary Metrics
    total = df['Amount'].sum()
    st.metric("Total Life-Time Spend", f"₹{total:,.2f}")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader(" Spending Breakdown")
        dist = get_category_distribution(df)
        fig, ax = plt.subplots()
        ax.pie(dist, labels=dist.index, autopct='%1.1f%%', colors=sns.color_palette("viridis"))
        st.pyplot(fig)

    with col2:
        st.subheader("📅 Monthly Trend")
        monthly = calculate_monthly_summary(df)
        st.line_chart(monthly)

    st.subheader("📑 Transaction History")
    st.dataframe(df.sort_values(by="Date", ascending=False), use_container_width=True)

else:
    st.warning("No data found. Start by adding an expense in the sidebar!")