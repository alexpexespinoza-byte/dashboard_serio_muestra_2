import streamlit as st
import plotly.express as px
import main 
import met_script as met_s

st.set_page_config(
    page_title="Analytics",
    layout="wide"
)

st.markdown(
    """
    <style>
        .block-container {
            padding-top: 30px !important;
            padding-bottom: 10px !important;
            padding-left: 10px !important;
            padding-right: 10px !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)


general_data = main.f_ex__general_data()

st.sidebar.subheader("General Filters")

estado = st.sidebar.selectbox(
    "Select State",
    ["All States"] + general_data["e"]
)

general_data = main.f_ex__general_data(estado)

ciudad = st.sidebar.selectbox(
    "Select City",
    ["All Cities"] + general_data["c"]
)

mes = st.sidebar.selectbox(
    "Select Month",
    ["All Months"] + general_data["m"]
)

st.subheader(f"Metrics based on the parameters selected in the select box ({estado}, {ciudad}, {mes})")



#metricas ↓

met_data = main.f_ex__met_pg_2_data(estado, ciudad, mes)

c1, c2, c3, c4, c5, c6 = st.columns(6)

with (c1):
    met_s.f_ex__kpi_script_data(
        data={
            "Total Sales" : {
                "v" : met_data["met_1"],
                "f" : "$",
                "c" : "#FF0000" 
            }
        }
    )
with (c2):
    met_s.f_ex__kpi_script_data(
        data={
            "Total Quantity of Products Sold" : {
                "v" : met_data["met_2"],
                "c" : "#BB00FF"
            }
        }
    )
with (c3):
    met_s.f_ex__kpi_script_data(
        data={
            "Amount of Orders" : {
                "v" : met_data["met_3"],
                "c" : "#FF0000" 
            }
        }
    )
with (c4):
    met_s.f_ex__kpi_script_data(
        data={
            "Best Category" : {
                "v" : met_data["met_4"],
                "c" : "#BB00FF"
            }
        }
    )
with (c5):
    met_s.f_ex__kpi_script_data(
        data={
            "Most used Payment Method" : {
                "v" : met_data["met_5"],
                "c" : "#FF0000" 
            }
        }
    )
with (c6):
    met_s.f_ex__kpi_script_data(
        data={
            "Avarege Score" : {
                "v" : f"{met_data["met_6"]:,.2f}",
                "c" : "#BB00FF"
            }
        }
    )



#grafica 1

grf_1_data = main.f_ex__grf_1_pg_2_data(estado, ciudad, mes)

grf_1 = px.bar(
    grf_1_data,
    x="City",
    y="Sales ($)",
    color="State",
    title="Sales by city"
)
grf_1.update_xaxes(
    categoryorder="array",
    categoryarray=grf_1_data["City"]
)

st.plotly_chart(grf_1)

print(grf_1_data)


#columans grafica 2, grafica 3, grafica 4 ↓

c1, c2, c3 = st.columns(3)

#grafica 2 ↓

grf_2_data = main.f_ex__grf_2_pg_2_data(estado, ciudad, mes)

grf_2 = px.pie(
    grf_2_data,
    names="State",
    values="Sales ($)",
    title="Distribution of sales in each state"
)
grf_2.update_traces(
    textinfo="label + value",
    texttemplate="%{label}<br>$%{value:,.2f}"
)
grf_2.update_layout(
    showlegend=False
)

with (c1):
    st.plotly_chart(grf_2)


#grafica 3 ↓

grf_3_data = main.f_ex__grf_3_pg_2_data(estado, ciudad, mes)

grf_3 = px.pie(
    grf_3_data,
    names="Category",
    values="Sales ($)",
    title="Distribution of sales in each category"
)
grf_3.update_traces(
    textinfo="label + value",
    texttemplate="%{label}<br>$%{value:,.2f}",
    textfont=dict(size=10)
)
grf_3.update_layout(
    showlegend=False
)

with (c2):
    st.plotly_chart(grf_3)


#grafica 4 ↓

grf_4_data = main.f_ex__grf_4_pg_2_data(estado, ciudad, mes)

grf_4 = px.pie(
    grf_4_data,
    names="Payment Method",
    values="Sales ($)",
    title="Distribution of sales in each payment method"
)
grf_4.update_traces(
    textinfo="label + value",
    texttemplate="%{label}<br>$%{value:,.2f}"
)
grf_4.update_layout(
    showlegend=False
)

with (c3):
    st.plotly_chart(grf_4)