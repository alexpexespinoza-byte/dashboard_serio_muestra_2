import streamlit as st
import plotly.express as px
import main 
import met_script as met_s

st.set_page_config(page_title="Home", layout="wide")

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

st.subheader("Dashboard Supermarket Sales 📊")



#metricas ↓

met_data = main.f_ex__met_data()

c1, c2, c3, c4, c5, c6 = st.columns(6)

with (c1):
    met_s.f_ex__kpi_script_data(
        data={
            "Total Sales" : {
                "v" : met_data["met_1"],
                "f" : "$",
                "c" : "#BB00FF"
            }
        }
    )
with (c2):
    met_s.f_ex__kpi_script_data(
        data={
            "Total Quantity of Products Sold" : {
                "v" : met_data["met_2"],
                "c" : "#FF0000"
            }
        }
    )
with (c3):
    met_s.f_ex__kpi_script_data(
        data={
            "Amount of Orders" : {
                "v" : met_data["met_3"],
                "c" : "#BB00FF"
            }
        }
    )
with (c4):
    met_s.f_ex__kpi_script_data(
        data={
            "Best State" : {
                "v" : met_data["met_4"],
                "c" : "#FF0000"
            }
        }
    )
with (c5):
    met_s.f_ex__kpi_script_data(
        data={
            "Best City" : {
                "v" : met_data["met_5"],
                "c" : "#BB00FF"
            }
        }
    )
with (c6):
    met_s.f_ex__kpi_script_data(
        data={
            "Best Month" : {
                "v" : met_data["met_6"],
                "c" : "#FF0000"
            }
        }
    )



#Columnas graifca 1, grafica 2 ↓

c1, c2, c3 = st.columns([2, 2, 1])



#data frame ↓

general_data = main.f_ex__general_data()

with (c1):
    rango = st.slider(
        "Select a range of sales",
        min_value=general_data["df_g_1"][0],
        max_value=general_data["df_g_1"][1],
        value=(general_data["df_g_1"][0], general_data["df_g_1"][1])
    )

df_data = main.f_ex__df_data((rango[0], rango[1]))

with (c1):
    st.markdown("**Table of the .csv filtred by the range**")
    st.dataframe(
        df_data,
        height=250
    )



#grafica 1 ↓

grf_1_data = main.f_ex__grf_1_data()

grf_1 = px.scatter(
    grf_1_data,
    x="sales",
    y="quantity",
    hover_name="index",
    color="category",
    title="Sales and quantity of every city grouped by state"
)

print(grf_1_data)

with (c2):
    st.plotly_chart(grf_1)



#grafica 2 ↓

grf_2_data = main.f_ex__grf_2_data()

grf_2 = px.line(
    grf_2_data,
    x="Months",
    y="Sales ($)",
    color_discrete_sequence=["#BB00FF"],
    markers=True,
    title="Sales by month"
)

grf_2.update_traces(
    marker=dict(color="#000000")
)

with (c3):
    st.plotly_chart(grf_2)