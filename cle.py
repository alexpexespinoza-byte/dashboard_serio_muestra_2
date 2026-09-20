import pandas as pd
import random as rd

df = pd.read_csv("data_raw.csv")


estados_y_municipios = {
    "Jalisco": [
        "Guadalajara",
        "Zapopan",
        "Tlaquepaque",
        "Tonalá",
        "Puerto Vallarta"
    ],
    "Nuevo León": [
        "Monterrey",
        "San Pedro Garza García",
        "San Nicolás de los Garza",
        "Apodaca",
        "Guadalupe"
    ],
    "Edomex": [
        "Toluca",
        "Ecatepec de Morelos",
        "Naucalpan de Juárez",
        "Nezahualcóyotl",
        "Metepec"
    ],
    "Veracruz": [
        "Xalapa",
        "Veracruz",
        "Coatzacoalcos",
        "Orizaba",
        "Poza Rica de Hidalgo"
    ],
    "Yucatán": [
        "Mérida",
        "Valladolid",
        "Tizimín",
        "Progreso",
        "Izamal"
    ]
}


df["City"] = [(rd.choice(estados_y_municipios[e])) for e in df["State"]]

df.to_csv("data_raw.csv", index=False)