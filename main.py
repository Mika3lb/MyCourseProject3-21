# INPUT PARAMS
# N3
# V_kr = 930 H = 11500 I = 5000 n = 200
# 1)Airbus A320 2)Boeing 757-200 3)Airbus A200B2 4) AB-1
n = 200
m_0 = [93500, 115680, 133000]
m_comm = [22000, 45000, 45000]
m_k = [28000, 42000, 44000]
m_cy = [8000, 9000, 14000]
m_t = [24000, 38000, 40000]
m_cl = [12000, 22000, 22000]
m_ob = [6000, 7500, 10000]
m_kr = [7000, 12000, 13000]
m_sh = [4000, 5000, 7000]
m_op = [5000, 6000, 7000]
m_f = [15000, 18000, 22000]
m_0_a = []
m_r_comm = []
m_r_k = []
m_r_cy = []
m_r_t = []
m_r_ob = []
m_r_kr = []
m_r_sh = []
m_r_op = []
m_r_f = []


def calculations():
    tmp = 120 * n
    m_comm.append(tmp)
    # First approximation
    for i in range(3):
        tmp = 0
        tmp = m_comm[i] / m_0[i]
        m_r_comm.append(tmp)
        tmp = 0
    for i in range(3):
        tmp += m_r_comm[i]
    tmp = tmp / 3
    m_r_comm.append(tmp)
    tmp = m_comm[3] / m_r_comm[3]
    m_0_a.append(tmp)
    # Second approximation
    for i in range(3):
        tmp = 0
        tmp = m_k[i] / m_0[i]
        m_r_k.append(tmp)
        tmp = 0
    for i in range(3):
        tmp = 0
        tmp = m_cy[i] / m_0[i]
        m_r_cy.append(tmp)
        tmp = 0
    for i in range(3):
        tmp = 0
        tmp = m_t[i] / m_0[i]
        m_r_t.append(tmp)
        tmp = 0
    for i in range(3):
        tmp = 0
        tmp = m_ob[i] / m_0[i]
        m_r_ob.append(tmp)
        tmp = 0
    for i in range(3):
        tmp += m_r_k[i]
    tmp = tmp / 3
    m_r_k.append(tmp)
    tmp = 0
    for i in range(3):
        tmp += m_r_cy[i]
    tmp = tmp / 3
    m_r_cy.append(tmp)
    tmp = 0
    for i in range(3):
        tmp += m_r_t[i]
    tmp = tmp / 3
    m_r_t.append(tmp)
    tmp = 0
    for i in range(3):
        tmp += m_r_ob[i]
    tmp = tmp / 3
    m_r_ob.append(tmp)
    tmp = 0
    for i in range(3):
        tmp += m_cl[i]
    tmp = tmp / 3
    m_cl.append(tmp)
    tmp = (m_cl[3] + m_comm[3]) / \
        (1 - (m_r_k[3] + m_r_cy[3] + m_r_t[3] + m_r_ob[3]))
    m_0_a.append(tmp)
    # Third approximation
    for i in range(3):
        tmp = 0
        tmp = m_kr[i] / m_0[i]
        m_r_kr.append(tmp)
        tmp = 0
    for i in range(3):
        tmp = 0
        tmp = m_sh[i] / m_0[i]
        m_r_sh.append(tmp)
        tmp = 0
    for i in range(3):
        tmp = 0
        tmp = m_f[i] / m_0[i]
        m_r_f.append(tmp)
        tmp = 0
    for i in range(3):
        tmp = 0
        tmp = m_op[i] / m_0[i]
        m_r_op.append(tmp)
        tmp = 0
    for i in range(3):
        tmp += m_r_kr[i]
    tmp = tmp / 3
    m_r_kr.append(tmp)
    tmp = 0
    for i in range(3):
        tmp += m_r_sh[i]
    tmp = tmp / 3
    m_r_sh.append(tmp)
    tmp = 0
    for i in range(3):
        tmp += m_r_f[i]
    tmp = tmp / 3
    m_r_f.append(tmp)
    tmp = 0
    for i in range(3):
        tmp += m_r_op[i]
    tmp = tmp / 3
    m_r_op.append(tmp)
    tmp = (m_cl[3] + m_comm[3]) / \
        (1 - (m_r_kr[3] + m_r_cy[3] + m_r_t[3] +
         m_r_ob[3] + m_r_sh[3] + m_r_f[3] + m_r_op[3]))
    m_0_a.append(tmp)


def output():
    print(m_r_kr)
    print(m_r_sh)
    print(m_r_f)
    print(m_r_op)
    print(m_0_a)
    print(f"{-(((m_0_a[1]/m_0_a[2])*100)-100)}%")


def main():
    calculations()
    output()


if __name__ == "__main__":
    main()
