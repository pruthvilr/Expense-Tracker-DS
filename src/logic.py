import pandas as pd

def calculate_monthly_summary(df):
    """Aggregates expenses by Month and Type"""
    if df.empty:
        return pd.DataFrame()
    
    # Ensure Date is datetime objects
    df['Date'] = pd.to_datetime(df['Date'])
    summary = df.groupby(df['Date'].dt.strftime('%Y-%m'))['Amount'].sum()
    return summary

def get_category_distribution(df):
    """Calculates percentage spent per category"""
    if df.empty:
        return pd.Series()
    
    return df.groupby('Category')['Amount'].sum()

def detect_overspending(df, threshold=5000):
    """Returns categories where spending exceeds a certain limit"""
    cat_totals = df.groupby('Category')['Amount'].sum()
    overspent = cat_totals[cat_totals > threshold]
    return overspent