import streamlit as st


# Documentacion de que hace cada cosa de la funcion xd ↓
#
#   llave "v" señala el valor
#   llave "tv" señala el tamaño del valor
#   llave "f" señala el formato del valor
#   llave "c" señala el color del valor
#   llave "d" señala si existe un valor delta dentro del valor
#       el valor de la llave "d" es una list con dos valores ["", ""], el primer elemento signfica el valor 
#       numerico del delta, el segundo elemento significa su texto
#   llave "grf" señala si hay una grafica (beta)
#
#   Para crear submetricas dentro de la metrica se puede hacer directamente agregando un
#   segundo elemento dentro del diccionario, pero si se quiere agregar un "titulo" para la metrica
#   general se debe usar el paramaetro div en la funcion, y en ela gregar el texto (esto se usa a 
#   la hora de usar submetricas, no confundir nombres con titulo)
#   
#   El parametro color_borde significa pues el colro borde nomames, si quieres que tenga color,
#   solo asignale un valor, y si no pues no, se quedara con el blanco predeterminado


@st.cache_data
def f_ex__kpi_script_data(data=None, div=None, color_borde=None):

    r_text = f"""<div style="padding: 5px; border: 1px solid {(color_borde) if (color_borde != None) else ("")}; font-family: Arial">"""

    if (div):
        r_text += f"""<div style="font-size: 20px; padding: 15px; border: 1px solid">{div}</div>"""
        r_text += "<div>ㅤ<div>"

    for k, v in data.items():
        r_text += f"""<div style="font-size: 15px">{k}</div>"""


        if ("f" in v):
            if (v["f"] == "$"):
                v["v"] = f"$ {v["v"]:,.2f}"
            elif (v["f"] == "kg"):
                v["v"] = f"{v["v"]:,.2f} kg"
            elif (v["f"] == "%"):
                v["v"] = f"{v["v"]:,.3f} %"
        else:
            None

        tamaño_valor = ((25) if ("tv" not in v) else (v["tv"]))

        if ("c" in v):
            color = f"color: {v["c"]}"
        else:
            color = ""

        r_text += f"""<div style="font-size: {tamaño_valor}px; {color}">{v["v"]}</div>"""

        if ("d" in v):
            delta_color = f"color: {("#00FF00") if (v["d"][0] > 0) else ("#FF0000")}"
            r_text += f"""<div style="font-size: 12px; {delta_color}">{v["d"][1]}</div>"""
        
        if ("grf" in v):
            r_text += (
                f"""
                    <svg viewbox="0 0 {150} {100}">
                        <path d="{v["grf"]}" fill="none" stroke="#FFFFFF">
                    </svg>
                """
            )

    r_text += "</div>"

    r_text += f"""<div style="font-size: 15px">ㅤ</div>"""

    st.markdown(r_text, unsafe_allow_html=True)