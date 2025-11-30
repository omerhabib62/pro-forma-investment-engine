import streamlit as st
import pandas as pd
import numpy as np

# Page Config
st.set_page_config(page_title="Investment Portfolio Architect", layout="wide")

st.title("💰 Investment Portfolio Modeler")
st.markdown("### Pro-Forma Analysis Engine (Internal Tool Prototype)")

# Sidebar: Investment Inputs (The "Star Schema" Inputs)
with st.sidebar:
    st.header("📝 New Investment Input")
    inv_name = st.text_input("Investment Name", "Apartment Complex A")
    sponsor = st.text_input("Sponsor", "Blackstone")
    
    st.subheader("Financial Drivers")
    amount = st.number_input("Capital Allocation ($)", 50000, 5000000, 100000, step=10000)
    hold_period = st.slider("Hold Period (Years)", 1, 10, 5)
    cash_flow_yield = st.slider("Annual Cash Flow (%)", 0.0, 15.0, 8.0) / 100
    exit_moic = st.slider("Target MOIC (Equity Multiple)", 1.0, 4.0, 2.0)

# The Calculation Engine (Pandas)
def calculate_waterfall(amount, years, yield_pct, moic):
    # 1. Annual Cash Flows (Calculate the Rent)
    annual_cf = amount * yield_pct
    # Translation: My $100k * 8% = $8,000 rent per year.
    
    # 2. Exit Value (Principal * MOIC)
    # Note: MOIC usually includes cash flow, but for simple modeling:
    # Exit Equity = (Amount * MOIC) - (Total Cash Flow Received)
    total_return_target = amount * moic
    # Translation: Client wants a 2.0x return. So $100k * 2.0 = $200,000 is the goal.

    # 3. Calculate how much rent we already got
    total_cf_received = annual_cf * years
    # Translation: $8,000 rent * 5 years = $40,000 collected so far.
    
    # 4. The Final Payday (Exit)
    exit_lump_sum = total_return_target - total_cf_received
    # Translation: 
    # The Goal is $200,000. 
    # We already got $40,000 in rent. 
    # So when we sell the building, we need to sell it for $160,000 to hit the goal.

    # Create Schedule
    schedule = []
    for year in range(1, years + 1):
        is_exit = (year == years)
        cash_out = annual_cf + (exit_lump_sum if is_exit else 0)
        schedule.append({
            "Year": year,
            "Cash Flow": annual_cf,
            "Exit Event": exit_lump_sum if is_exit else 0,
            "Total Distribution": cash_out
        })
    
    return pd.DataFrame(schedule)

# Run Logic
df = calculate_waterfall(amount, hold_period, cash_flow_yield, exit_moic)

# Display Metrics
col1, col2, col3 = st.columns(3)
col1.metric("Total Invested", f"${amount:,.0f}")
col2.metric("Projected Exit Value", f"${df['Total Distribution'].sum():,.0f}")
col3.metric("Net Profit", f"${df['Total Distribution'].sum() - amount:,.0f}", delta=f"{exit_moic}x MOIC")

# Visuals
st.divider()
st.subheader(f"📊 Waterfall Projection: {inv_name}")
st.bar_chart(df.set_index("Year")["Total Distribution"])

st.dataframe(df, use_container_width=True)

# The "Upsell" Note
st.info("💡 **Developer Note:** This engine handles the basic 'Waterfall'. Next steps: Integrate PDF export via WeasyPrint and Sector-based risk analysis.")