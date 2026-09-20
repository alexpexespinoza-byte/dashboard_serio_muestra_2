import pandas as pd
import streamlit as st



#Variables globales ↓

meses = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]






@st.cache_data
def f_ex__met_data():
    df = pd.read_csv("data_raw.csv")

    total_ventas = df["Sales"].sum()

    total_cantidad = df["Quantity"].sum()

    total_ordenes = len(df)

    mejor_estado = df.groupby(df["State"])["Sales"].sum().idxmax()

    mejor_ciudad = df.groupby(df["City"])["Sales"].sum().idxmax()

    mes_nombre = (
        pd.to_datetime(df["Date"], errors="coerce").dt.month_name()
    )
    df["Month name"] = mes_nombre
    mejor_mes = df.groupby(df["Month name"])["Sales"].sum().idxmax()


    data = {
        "met_1" : total_ventas,
        "met_2" : total_cantidad,
        "met_3" : total_ordenes,
        "met_4" : mejor_estado,
        "met_5" : mejor_ciudad,
        "met_6" : mejor_mes
    }

    return (data)



@st.cache_data
def f_ex__general_data(estado="All States", ciudad="All Cities"):
    df = pd.read_csv("data_raw.csv")

    rango_min_max = (int(df["Sales"].min()), int(df["Sales"].max()))

    estados = list(df["State"].unique())
    if (estado != "All States"):
        df = f_ex_filtrar_df(df, estado=estado)

    ciudades = list(df["City"].unique())

    if (ciudad != "All Cities"):
        df = f_ex_filtrar_df(df, ciudad=ciudad)

    meses_u = list(pd.to_datetime(df["Date"], errors="coerce").dt.month_name().unique())
    meses_u = pd.Categorical(meses_u, meses)
    meses_u = list(meses_u.sort_values())

    tipo_clientes = list(df["Customer type"].unique())

    generos = list(df["Gender"].unique())

    categorias = list(df["Product line"].unique())

    metodo_pagos = list(df["Payment"].unique())

    
    data = {
        "df_g_1" : rango_min_max,
        "e" : estados,
        "c" : ciudades,
        "m" : meses_u,
        "t_c" : tipo_clientes,
        "g" : generos,
        "ca" : categorias,
        "m_p" : metodo_pagos
    }

    return (data)



@st.cache_data
def f_ex__grf_1_data():
    df = pd.read_csv("data_raw.csv")

    ciudad_ventas = pd.pivot_table(df, values=["Sales", "Quantity"], index="City", aggfunc="sum")
    ciudad_ventas["Category"] = [(df[df["City"] == e].iloc[0]["State"]) for e in ciudad_ventas.index]


    df_c_v = pd.DataFrame({
        "index" : list(ciudad_ventas.index),
        "quantity" : list(ciudad_ventas["Quantity"]),
        "sales" : list(ciudad_ventas["Sales"]),
        "category" : list(ciudad_ventas["Category"])
    })

    data = df_c_v

    return (data)



@st.cache_data
def f_ex__grf_2_data():
    df = pd.read_csv("data_raw.csv")

    df["Month name"] = pd.to_datetime(df["Date"], errors="coerce").dt.month_name()
    meses_ventas = df.groupby(df["Month name"])["Sales"].sum()
    meses_ventas.index = pd.Categorical(meses_ventas.index, meses)
    meses_ventas = meses_ventas.sort_index().to_dict()


    data = pd.DataFrame({
        "Months" : list(meses_ventas.keys()),
        "Sales ($)" : list(meses_ventas.values())
    })

    return (data)



@st.cache_data
def f_ex__df_data(rango=(0, 0)):
    df = pd.read_csv("data_raw.csv")

    df = df[(df["Sales"] >= rango[0]) & (df["Sales"] <= rango[1])]


    return (df)




@st.cache_data
def f_ex_filtrar_df(
    df, 
    ciudad="All Cities", estado="All States", mes="All Months",
    cliente="All Customers", genero="All Genders", categoria="All Categories", metodo_pago="All Payment Methods"
):
    if (estado != "All States"):
        df = df[df["State"] == estado]

    if (ciudad != "All Cities"):
        df = df[df["City"] == ciudad]

    mes_nombre = (
        pd.to_datetime(df["Date"], errors="coerce").dt.month_name()
    )
    df["Month name"] = mes_nombre
    if (mes != "All Months"):
        df = df[df["Month name"] == mes]

    if (cliente != "All Customers"):
        df = df[df["Customer type"] == cliente]

    if (genero != "All Genders"):
        df = df[df["Gender"] == genero]

    if (categoria != "All Categories"):
        df = df[df["Product line"] == categoria]

    if (metodo_pago != "All Payment Methods"):
        df = df[df["Payment"] == metodo_pago]


    return (df)


@st.cache_data
def f_ex__met_pg_2_data(estado="All States", ciudad="All Cities", mes="All Months"):
    df = pd.read_csv("data_raw.csv")
    df = f_ex_filtrar_df(df, ciudad, estado, mes)

    total_ventas = df["Sales"].sum()

    total_cantidad = df["Quantity"].sum()

    total_ordenes = len(df)

    mejor_categoria = df.groupby(df["Product line"])["Sales"].sum().idxmax()

    mejor_metodo_pago = df["Payment"].value_counts().idxmax()

    calificacion_promedio = df["Rating"].mean()


    data = {
        "met_1" : total_ventas,
        "met_2" : total_cantidad,
        "met_3" : total_ordenes,
        "met_4" : mejor_categoria,
        "met_5" : mejor_metodo_pago,
        "met_6" : calificacion_promedio
    }

    return (data)



@st.cache_data
def f_ex__grf_1_pg_2_data(estado="All States", ciudad="All Cities", mes="All Months"):
    df = pd.read_csv("data_raw.csv")
    df = f_ex_filtrar_df(df, ciudad, estado, mes)

    ciudades_ventas = df.groupby(df["City"])["Sales"].sum().sort_values().to_dict()

    estados_ciudades = [(df[df["City"] == e].iloc[0]["State"]) for e in ciudades_ventas.keys()]


    data = pd.DataFrame({
        "City" : list(ciudades_ventas.keys()),
        "Sales ($)" : list(ciudades_ventas.values()),
        "State" : estados_ciudades
    })

    return (data)



@st.cache_data
def f_ex__grf_2_pg_2_data(estado="All States", ciudad="All Cities", mes="All Months"):
    df = pd.read_csv("data_raw.csv")
    df = f_ex_filtrar_df(df, ciudad, estado, mes)

    categoria_ventas = df.groupby(df["Product line"])["Sales"].sum().to_dict()


    data = pd.DataFrame({
        "Category" : list(categoria_ventas.keys()),
        "Sales ($)" : list (categoria_ventas.values())  
    })

    return (data)



@st.cache_data
def f_ex__grf_2_pg_2_data(estado="All States", ciudad="All Cities", mes="All Months"):
    df = pd.read_csv("data_raw.csv")
    df = f_ex_filtrar_df(df, ciudad, estado, mes)

    estado_ventas = df.groupby(df["State"])["Sales"].sum().to_dict()


    data = pd.DataFrame({
        "State" : list(estado_ventas.keys()),
        "Sales ($)" : list (estado_ventas.values())  
    })

    return (data)



@st.cache_data
def f_ex__grf_3_pg_2_data(estado="All States", ciudad="All Cities", mes="All Months"):
    df = pd.read_csv("data_raw.csv")
    df = f_ex_filtrar_df(df, ciudad, estado, mes)

    categoria_ventas = df.groupby(df["Product line"])["Sales"].sum().to_dict()


    data = pd.DataFrame({
        "Category" : list(categoria_ventas.keys()),
        "Sales ($)" : list (categoria_ventas.values())  
    })

    return (data)



@st.cache_data
def f_ex__grf_4_pg_2_data(estado="All States", ciudad="All Cities", mes="All Months"):
    df = pd.read_csv("data_raw.csv")
    df = f_ex_filtrar_df(df, ciudad, estado, mes)

    metodo_pago_ventas = df.groupby(df["Payment"])["Sales"].sum().to_dict()


    data = pd.DataFrame({
        "Payment Method" : list(metodo_pago_ventas.keys()),
        "Sales ($)" : list (metodo_pago_ventas.values())  
    })

    return (data)



@st.cache_data
def f_ex__df_pg_2_data(
    estado="All States", ciudad="All Cities", mes="All Months",
    cliente="All Customer", genero="All Genders", categoria="All Categories", metodo_pago="All Payment Methods",
    rango=(0, 0)
):
    df = pd.read_csv("data_raw.csv")
    df = f_ex_filtrar_df(df, ciudad, estado, mes, cliente, genero, categoria, metodo_pago)

    df = df[(df["Sales"] >= rango[0]) & (df["Sales"] <= rango[1])]

    return (df)

print(f_ex__df_pg_2_data())



@st.cache_data
def f_ex__descargar_csv_data(df):
    return (df.to_csv())