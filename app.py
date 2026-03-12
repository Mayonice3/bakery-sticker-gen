import streamlit as st
from datetime import datetime, timedelta

# 1. Setup & Data
item_params = {
    "CHOCOLATE CHUNK COOKIE": {"shelf_life": 14, "storage": "Store chilled"},
    "HOT CHOCOLATE FUDGE": {"shelf_life": 7, "storage": "Store chilled"},
    "DBC SPONGE": {"shelf_life": 5, "storage": "Store chilled"},
    "DARK CHOCOLATE DESSERT JAR - RM": {"shelf_life": 10, "storage": "Store chilled"},
    "CHOCOLATE KUNAFA JAR": {"shelf_life": 7, "storage": "Store chilled"},
    "LOTUS BISCOFF CHEESECAKE JAR": {"shelf_life": 5, "storage": "Store chilled"},
    "STRAWBERRIES & CHOCOLATE GATEAUX JAR": {"shelf_life": 4, "storage": "Store chilled"},
    "STRAWBERRY SHORTCAKE JAR": {"shelf_life": 4, "storage": "Store chilled"}
}

st.set_page_config(page_title="Bakery Sticker Gen", page_icon="🧁")
st.title("🧁 Sticker Generator")

# 2. UI Inputs
with st.form("sticker_form"):
    item_name = st.selectbox("Select Item", options=list(item_params.keys()))
    total_qty = st.number_input("Total Quantity", min_value=0, value=702)
    
    # Allows selecting multiple non-consecutive dates
    selected_dates = st.date_input(
        "Select Production Dates",
        value=[],  # Starts empty
        help="Select all dates that apply for this production run."
    )
    
    start_batch = st.number_input("Starting Batch Number", min_value=1, value=63)
    submit = st.form_submit_button("Generate Stickers")

if submit:
    if not selected_dates:
        st.error("Please select at least one date from the calendar.")
    else:
        params = item_params[item_name]
        # selected_dates returns a list when multiple are picked
        daily_qty = round(total_qty / len(selected_dates), 1)
        
        st.subheader(f"Stickers for {item_name}")
        for i, mfd_date in enumerate(sorted(selected_dates)):
            exp_date = mfd_date + timedelta(days=params["shelf_life"])
            batch_num = str(start_batch + i).zfill(4)
            
            # Displaying in a clean, copyable block
            st.code(f"""
{item_name}
MFD: {mfd_date.strftime('%d/%m/%y')}
EXP: {exp_date.strftime('%d/%m/%y')}
{params['storage']}
Batch: {batch_num}

No of Stickers: {daily_qty}
            """)