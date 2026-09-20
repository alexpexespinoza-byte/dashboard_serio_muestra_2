import streamlit as st

#cd "C:\Users\Leonel Espinoza\Desktop\archivos_de_py\dashboard_serio_muestra_2"
#streamlit run "visu.py"

pg_1 = st.Page("pages/pg_1.py", title="Home")
pg_2 = st.Page("pages/pg_2.py", title="Analytics")
pg_3 = st.Page("pages/pg_3.py", title="Filtred CSV")

nav = st.navigation([pg_1, pg_2, pg_3])

nav.run()

