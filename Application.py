import streamlit as st
from main import *
import text
tip = text.tip

st.code(tip, language=None)
st.warning("Введите все нужные данные !")
st.write("Кол-во пассажиров")
n = st.number_input(
    "n", min_value=0, max_value=1000, value=0, step=10, key="n")
st.write("Взлетная масса")
coll1_m_0, coll2_m_0, coll3_m_0 = st.columns(3)
m_0[0] = coll1_m_0.number_input(
    "m_0_1", min_value=0, max_value=500000, value=0, step=1000, key="m_0_1")
m_0[1] = coll2_m_0.number_input(
    "m_0_2", min_value=0, max_value=500000, value=0, step=1000, key="m_0_2")
m_0[2] = coll3_m_0.number_input(
    "m_0_3", min_value=0, max_value=500000, value=0, step=1000, key="m_0_3")
st.write("Масса коммерческой нагрузки")
coll1_m_comm, coll2_m_comm, coll3_m_comm = st.columns(3)
m_comm[0] = coll1_m_comm.number_input(
    "m_comm_1", min_value=0, max_value=500000, value=0, step=1000, key="m_comm_1")
m_comm[1] = coll2_m_comm.number_input(
    "m_comm_2", min_value=0, max_value=500000, value=0, step=1000, key="m_comm_2")
m_comm[2] = coll3_m_comm.number_input(
    "m_comm_3", min_value=0, max_value=500000, value=0, step=1000, key="m_comm_3")
st.write("Масса конструкции")
coll1_m_k, coll2_m_k, coll3_m_k = st.columns(3)
m_k[0] = coll1_m_k.number_input(
    "m_k_1", min_value=0, max_value=500000, value=0, step=1000, key="m_k_1")
m_k[1] = coll2_m_k.number_input(
    "m_k_1", min_value=0, max_value=500000, value=0, step=1000, key="m_k_2")
m_k[2] = coll3_m_k.number_input(
    "m_k_1", min_value=0, max_value=500000, value=0, step=1000, key="m_k_3")
st.write("Масса силовой установки")
coll1_m_cy, coll2_m_cy, coll3_m_cy = st.columns(3)
m_cy[0] = coll1_m_cy.number_input(
    "m_cy_1", min_value=0, max_value=500000, value=0, step=1000, key="m_cy_1")
m_cy[1] = coll2_m_cy.number_input(
    "m_cy_1", min_value=0, max_value=500000, value=0, step=1000, key="m_cy_2")
m_cy[2] = coll3_m_cy.number_input(
    "m_cy_1", min_value=0, max_value=500000, value=0, step=1000, key="m_cy_3")
st.write("Масса топлива")
coll1_m_t, coll2_m_t, coll3_m_t = st.columns(3)
m_t[0] = coll1_m_t.number_input(
    "m_t_1", min_value=0, max_value=500000, value=0, step=1000, key="m_t_1")
m_t[1] = coll2_m_t.number_input(
    "m_t_1", min_value=0, max_value=500000, value=0, step=1000, key="m_t_2")
m_t[2] = coll3_m_t.number_input(
    "m_t_1", min_value=0, max_value=500000, value=0, step=1000, key="m_t_3")
st.write("Масса служебной нагрузки")
coll1_m_cl, coll2_m_cl, coll3_m_cl = st.columns(3)
m_cl[0] = coll1_m_cl.number_input(
    "m_cl_1", min_value=0, max_value=500000, value=0, step=1000, key="m_cl_1")
m_cl[1] = coll2_m_cl.number_input(
    "m_cl_1", min_value=0, max_value=500000, value=0, step=1000, key="m_cl_2")
m_cl[2] = coll3_m_cl.number_input(
    "m_cl_1", min_value=0, max_value=500000, value=0, step=1000, key="m_cl_3")
st.write("Масса оборудования")
coll1_m_ob, coll2_m_ob, coll3_m_ob = st.columns(3)
m_ob[0] = coll1_m_ob.number_input(
    "m_ob_1", min_value=0, max_value=500000, value=0, step=1000, key="m_ob_1")
m_ob[1] = coll2_m_ob.number_input(
    "m_ob_1", min_value=0, max_value=500000, value=0, step=1000, key="m_ob_2")
m_ob[2] = coll3_m_ob.number_input(
    "m_ob_1", min_value=0, max_value=500000, value=0, step=1000, key="m_ob_3")
st.write("Масса крыла")
coll1_m_kr, coll2_m_kr, coll3_m_kr = st.columns(3)
m_kr[0] = coll1_m_kr.number_input(
    "m_kr_1", min_value=0, max_value=500000, value=0, step=1000, key="m_kr_1")
m_kr[1] = coll2_m_kr.number_input(
    "m_kr_1", min_value=0, max_value=500000, value=0, step=1000, key="m_kr_2")
m_kr[2] = coll3_m_kr.number_input(
    "m_kr_1", min_value=0, max_value=500000, value=0, step=1000, key="m_kr_3")
st.write("Масса шасси")
coll1_m_sh, coll2_m_sh, coll3_m_sh = st.columns(3)
m_sh[0] = coll1_m_sh.number_input(
    "m_sh_1", min_value=0, max_value=500000, value=0, step=1000, key="m_sh_1")
m_sh[1] = coll2_m_sh.number_input(
    "m_sh_1", min_value=0, max_value=500000, value=0, step=1000, key="m_sh_2")
m_sh[2] = coll3_m_sh.number_input(
    "m_sh_1", min_value=0, max_value=500000, value=0, step=1000, key="m_sh_3")
st.write("Масса оперения")
coll1_m_op, coll2_m_op, coll3_m_op = st.columns(3)
m_op[0] = coll1_m_op.number_input(
    "m_op_1", min_value=0, max_value=500000, value=0, step=1000, key="m_op_1")
m_op[1] = coll2_m_op.number_input(
    "m_op_1", min_value=0, max_value=500000, value=0, step=1000, key="m_op_2")
m_op[2] = coll3_m_op.number_input(
    "m_op_1", min_value=0, max_value=500000, value=0, step=1000, key="m_op_3")
st.write("Масса фюзеляж")
coll1_m_f, coll2_m_f, coll3_m_f = st.columns(3)
m_k[0] = coll1_m_f.number_input(
    "m_f_1", min_value=0, max_value=500000, value=0, step=1000, key="m_f_1")
m_f[1] = coll2_m_f.number_input(
    "m_f_1", min_value=0, max_value=500000, value=0, step=1000, key="m_f_2")
m_f[2] = coll3_m_f.number_input(
    "m_f_1", min_value=0, max_value=500000, value=0, step=1000, key="m_f_3")
if st.button("RUN"):
    getApproximations()
    text = getOutputFunc()
    st.code(text, language=None)
