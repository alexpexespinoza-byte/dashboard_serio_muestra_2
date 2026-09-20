import streamlit as st
import plotly.express as px
import main 
import met_script as met_s

st.set_page_config(
    page_title="Filtred CSV",
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

st.subheader("Filtred CSV")

st.markdown("**General Filters**")

#filtros generales ↓

c1, c2, c3 = st.columns(3)

with (c1):
    estado = st.selectbox(
        "Select State",
        ["All States"] + general_data["e"]
    )

general_data = main.f_ex__general_data(estado)

with (c2):
    ciudad = st.selectbox(
        "Select City",
        ["All Cities"] + general_data["c"]
    )

general_data = main.f_ex__general_data(estado, ciudad)

with (c3):
    mes = st.selectbox(
        "Select Month",
        ["All Months"] + general_data["m"]
    )


#filtros avanzados ↓

st.markdown("**Advanzed Filters**")

c1, c2, c3, c4 = st.columns(4)

with (c1):
    tipo_cliente = st.selectbox(
        "Select Type of Client",
        ["All Customers"] + general_data["t_c"]
    )
with (c2):
    genero = st.selectbox(
        "Select Gender",
        ["All Genders"] + general_data["g"]
    )
with (c3):
    categoria = st.selectbox(
        "Select Category",
        ["All Categories"] + general_data["ca"]
    )
with (c4):
    metodo_pago = st.selectbox(
        "Select Payment Method",
        ["All Payment Methods"] + general_data["m_p"]
    )

rango = st.slider(
    "Select a range of sales",
    min_value=general_data["df_g_1"][0],
    max_value=general_data["df_g_1"][1],
    value=(general_data["df_g_1"][0], general_data["df_g_1"][1])
)



#dataframe ↓

df_data = main.f_ex__df_pg_2_data(ciudad=ciudad, estado=estado, mes=mes, cliente=tipo_cliente, genero=genero, categoria=categoria, metodo_pago=metodo_pago, rango=rango)

st.dataframe(df_data)

csv_data = main.f_ex__descargar_csv_data(df_data)

st.sidebar.download_button(
    ":material/download: Download filtred CSV",
    data = csv_data,
    file_name="filtred_data.csv",
    mime="text/csv"
)