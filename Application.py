import streamlit as st
import main


st.warning("Введите все нужные данные !")
st.write("Взлетная масса")
coll1, coll2, coll3 = st.columns(3)
main.m_0[0] = coll1.number_input(
    "1", min_value=10000, max_value=300000, value=100000, step=1000)
main.m_0[1] = coll2.number_input(
    "2", min_value=10000, max_value=300000, value=100000, step=1000)
main.m_0[2] = coll3.number_input(
    "3", min_value=10000, max_value=300000, value=100000, step=1000)
if st.button("RUN"):
    st.write(str(main.m_0))
