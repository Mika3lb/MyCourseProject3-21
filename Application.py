import streamlit as st
import main

st.image("https://github.com/Mika3lb/MyCourseProject3-21/blob/main/IMG/HEAD.png")
tip = '''
n - Количество пассажиров
m_0 - Взлетная масса
m_comm - Масса коммерческой нагрузки
m_k - Масса конструкции
m_cy - Масса силовой установки
m_t - Масса топлива
m_cl - Масса служебной нагрузки
m_ob - Масса оборудования
m_kr - Масса крыла
m_sh - Масса шасси
m_op - Масса оперения
m_f - Масса фюзеляж
m_0_a - Взлетная масса нашего самолета при приближениях
m_r_comm - Относительная масса коммерческой нагрузки
m_r_k - Относительная масса конструкции
m_r_cy - Относительная масса силовой
m_r_t - Относительная масса топлива
m_r_ob - Относительная масса оборудования
m_r_kr - Относительная масса крыла
m_r_sh - Относительная масса шасси
m_r_op - Относительная масса оперения
m_r_f - Относительная масса фюзеляж
'''

st.code(tip, language=None)
st.warning("Введите все нужные данные !")
st.write("Кол-во пассажиров")
main.n = st.number_input(
    "n", min_value=0, max_value=1000, value=0, step=10, key="n")
st.write("Взлетная масса")
coll1_m_0, coll2_m_0, coll3_m_0 = st.columns(3)
main.m_0[0] = coll1_m_0.number_input(
    "m_0_1", min_value=0, max_value=500000, value=0, step=1000, key="m_0_1")
main.m_0[1] = coll2_m_0.number_input(
    "m_0_2", min_value=0, max_value=500000, value=0, step=1000, key="m_0_2")
main.m_0[2] = coll3_m_0.number_input(
    "m_0_3", min_value=0, max_value=500000, value=0, step=1000, key="m_0_3")
st.write("Масса коммерческой нагрузки")
coll1_m_comm, coll2_m_comm, coll3_m_comm = st.columns(3)
main.m_comm[0] = coll1_m_comm.number_input(
    "m_comm_1", min_value=0, max_value=500000, value=0, step=1000, key="m_comm_1")
main.m_comm[1] = coll2_m_comm.number_input(
    "m_comm_2", min_value=0, max_value=500000, value=0, step=1000, key="m_comm_2")
main.m_comm[2] = coll3_m_comm.number_input(
    "m_comm_3", min_value=0, max_value=500000, value=0, step=1000, key="m_comm_3")
st.write("Масса конструкции")
coll1_m_k, coll2_m_k, coll3_m_k = st.columns(3)
main.m_k[0] = coll1_m_k.number_input(
    "m_k_1", min_value=0, max_value=500000, value=0, step=1000, key="m_k_1")
main.m_k[1] = coll2_m_k.number_input(
    "m_k_1", min_value=0, max_value=500000, value=0, step=1000, key="m_k_2")
main.m_k[2] = coll3_m_k.number_input(
    "m_k_1", min_value=0, max_value=500000, value=0, step=1000, key="m_k_3")
st.write("Масса силовой установки")
coll1_m_cy, coll2_m_cy, coll3_m_cy = st.columns(3)
main.m_cy[0] = coll1_m_cy.number_input(
    "m_cy_1", min_value=0, max_value=500000, value=0, step=1000, key="m_cy_1")
main.m_cy[1] = coll2_m_cy.number_input(
    "m_cy_1", min_value=0, max_value=500000, value=0, step=1000, key="m_cy_2")
main.m_cy[2] = coll3_m_cy.number_input(
    "m_cy_1", min_value=0, max_value=500000, value=0, step=1000, key="m_cy_3")
st.write("Масса топлива")
coll1_m_t, coll2_m_t, coll3_m_t = st.columns(3)
main.m_t[0] = coll1_m_t.number_input(
    "m_t_1", min_value=0, max_value=500000, value=0, step=1000, key="m_t_1")
main.m_t[1] = coll2_m_t.number_input(
    "m_t_1", min_value=0, max_value=500000, value=0, step=1000, key="m_t_2")
main.m_t[2] = coll3_m_t.number_input(
    "m_t_1", min_value=0, max_value=500000, value=0, step=1000, key="m_t_3")
st.write("Масса служебной нагрузки")
coll1_m_cl, coll2_m_cl, coll3_m_cl = st.columns(3)
main.m_cl[0] = coll1_m_cl.number_input(
    "m_cl_1", min_value=0, max_value=500000, value=0, step=1000, key="m_cl_1")
main.m_cl[1] = coll2_m_cl.number_input(
    "m_cl_1", min_value=0, max_value=500000, value=0, step=1000, key="m_cl_2")
main.m_cl[2] = coll3_m_cl.number_input(
    "m_cl_1", min_value=0, max_value=500000, value=0, step=1000, key="m_cl_3")
st.write("Масса оборудования")
coll1_m_ob, coll2_m_ob, coll3_m_ob = st.columns(3)
main.m_ob[0] = coll1_m_ob.number_input(
    "m_ob_1", min_value=0, max_value=500000, value=0, step=1000, key="m_ob_1")
main.m_ob[1] = coll2_m_ob.number_input(
    "m_ob_1", min_value=0, max_value=500000, value=0, step=1000, key="m_ob_2")
main.m_ob[2] = coll3_m_ob.number_input(
    "m_ob_1", min_value=0, max_value=500000, value=0, step=1000, key="m_ob_3")
st.write("Масса крыла")
coll1_m_kr, coll2_m_kr, coll3_m_kr = st.columns(3)
main.m_kr[0] = coll1_m_kr.number_input(
    "m_kr_1", min_value=0, max_value=500000, value=0, step=1000, key="m_kr_1")
main.m_kr[1] = coll2_m_kr.number_input(
    "m_kr_1", min_value=0, max_value=500000, value=0, step=1000, key="m_kr_2")
main.m_kr[2] = coll3_m_kr.number_input(
    "m_kr_1", min_value=0, max_value=500000, value=0, step=1000, key="m_kr_3")
st.write("Масса шасси")
coll1_m_sh, coll2_m_sh, coll3_m_sh = st.columns(3)
main.m_sh[0] = coll1_m_sh.number_input(
    "m_sh_1", min_value=0, max_value=500000, value=0, step=1000, key="m_sh_1")
main.m_sh[1] = coll2_m_sh.number_input(
    "m_sh_1", min_value=0, max_value=500000, value=0, step=1000, key="m_sh_2")
main.m_sh[2] = coll3_m_sh.number_input(
    "m_sh_1", min_value=0, max_value=500000, value=0, step=1000, key="m_sh_3")
st.write("Масса оперения")
coll1_m_op, coll2_m_op, coll3_m_op = st.columns(3)
main.m_op[0] = coll1_m_op.number_input(
    "m_op_1", min_value=0, max_value=500000, value=0, step=1000, key="m_op_1")
main.m_op[1] = coll2_m_op.number_input(
    "m_op_1", min_value=0, max_value=500000, value=0, step=1000, key="m_op_2")
main.m_op[2] = coll3_m_op.number_input(
    "m_op_1", min_value=0, max_value=500000, value=0, step=1000, key="m_op_3")
st.write("Масса фюзеляж")
coll1_m_f, coll2_m_f, coll3_m_f = st.columns(3)
main.m_k[0] = coll1_m_f.number_input(
    "m_f_1", min_value=0, max_value=500000, value=0, step=1000, key="m_f_1")
main.m_f[1] = coll2_m_f.number_input(
    "m_f_1", min_value=0, max_value=500000, value=0, step=1000, key="m_f_2")
main.m_f[2] = coll3_m_f.number_input(
    "m_f_1", min_value=0, max_value=500000, value=0, step=1000, key="m_f_3")
if st.button("RUN"):
    main.getApproximations()
    text = main.getOutputFunc()
    st.code(text, language=None)
