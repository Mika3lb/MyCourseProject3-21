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
    print("Первое приближение: \n")
    for i in range(3):
        print(f"m_0_{i+1} = {m_0[i]} кг", end=" | ")
    print("\n")
    for i in range(3):
        print(f"m_comm_{i+1} = {m_comm[i]} кг", end=" | ")
    print("\n")
    for i in range(3):
        print(
            f"m_r_comm_{i+1} = {m_comm[i]} кг / {m_0[i]} кг => {m_r_comm[i]:.3f}")
    print(f"\nm_comm = 120 кг * {n} => {m_comm[3]} кг")
    print(
        f"\nm_r_comm = ({m_r_comm[0]:.3f} + {m_r_comm[1]:.3f} + {m_r_comm[2]:.3f}) / 3 => {m_r_comm[3]:.3f}")
    print(f"\nm_0 = {m_comm[3]} кг / {m_r_comm[3]:.3f} => {int(m_0_a[0])} кг")
    print("\n----------------------------------\n")
    print("Второе приближение: \n")
    for i in range(3):
        print(f"m_comm_{i+1} = {m_comm[i]} кг", end=" | ")
    print("\n")
    for i in range(3):
        print(f"m_k_{i+1} = {m_k[i]} кг", end=" | ")
    print("\n")
    for i in range(3):
        print(f"m_cy_{i+1} = {m_cy[i]} кг", end=" | ")
    print("\n")
    for i in range(3):
        print(f"m_t_{i+1} = {m_t[i]} кг", end=" | ")
    print("\n")
    for i in range(3):
        print(f"m_ob_{i+1} = {m_ob[i]} кг", end=" | ")
    print("\n")
    for i in range(3):
        print(f"m_cl_{i+1} = {m_cl[i]} кг", end=" | ")
    print("\n")
    for i in range(3):
        print(
            f"m_r_k_{i+1} = {m_k[i]} кг / {m_0[i]} кг => {m_r_k[i]:.3f}")
    print("")
    for i in range(3):
        print(
            f"m_r_cy_{i+1} = {m_cy[i]} кг / {m_0[i]} кг => {m_r_cy[i]:.3f}")
    print("")
    for i in range(3):
        print(
            f"m_r_t_{i+1} = {m_t[i]} кг / {m_0[i]} кг => {m_r_t[i]:.3f}")
    print("")
    for i in range(3):
        print(
            f"m_r_ob_{i+1} = {m_ob[i]} кг / {m_0[i]} кг => {m_r_ob[i]:.3f}")
    print(
        f"\nm_cl = {m_cl[0]} кг + {m_cl[1]} кг + {m_cl[2]} кг => {int(m_cl[3])} кг")
    print(
        f"\nm_r_k = ({m_r_k[0]:.3f} + {m_r_k[1]:.3f} + {m_r_k[2]:.3f}) / 3 => {m_r_k[3]:.3f}")
    print(
        f"\nm_r_cy = ({m_r_cy[0]:.3f} + {m_r_cy[1]:.3f} + {m_r_cy[2]:.3f}) / 3 => {m_r_cy[3]:.3f}")
    print(
        f"\nm_r_t = ({m_r_t[0]:.3f} + {m_r_t[1]:.3f} + {m_r_t[2]:.3f}) / 3 => {m_r_t[3]:.3f}")
    print(
        f"\nm_r_ob = ({m_r_ob[0]:.3f} + {m_r_ob[1]:.3f} + {m_r_ob[2]:.3f}) / 3 => {m_r_ob[3]:.3f}")
    print(f"\nm_0 = {int(m_cl[3])} кг + {m_r_comm[3]:.3f} кг / 1 - ({m_r_k[3]:.3f} + {m_r_cy[3]:.3f} + {m_r_t[3]:.3f} + {m_r_ob[3]:.3f}) => {int(m_0_a[1])} кг")
    print("\n----------------------------------\n")
    print("Третье приближение: \n")
    for i in range(3):
        print(f"m_comm_{i+1} = {m_comm[i]} кг", end=" | ")
    print("\n")
    for i in range(3):
        print(f"m_kr_{i+1} = {m_kr[i]} кг", end=" | ")
    print("\n")
    for i in range(3):
        print(f"m_f_{i+1} = {m_f[i]} кг", end=" | ")
    print("\n")
    for i in range(3):
        print(f"m_sh_{i+1} = {m_sh[i]} кг", end=" | ")
    print("\n")
    for i in range(3):
        print(f"m_op_{i+1} = {m_op[i]} кг", end=" | ")
    print("\n")
    for i in range(3):
        print(f"m_cy_{i+1} = {m_cy[i]} кг", end=" | ")
    print("\n")
    for i in range(3):
        print(f"m_t_{i+1} = {m_t[i]} кг", end=" | ")
    print("\n")
    for i in range(3):
        print(f"m_ob_{i+1} = {m_ob[i]} кг", end=" | ")
    print("\n")
    for i in range(3):
        print(f"m_cl_{i+1} = {m_cl[i]} кг", end=" | ")
    print("\n")
    for i in range(3):
        print(
            f"m_r_kr_{i+1} = {m_kr[i]} кг / {m_0[i]} кг => {m_r_kr[i]:.3f}")
    print("")
    for i in range(3):
        print(
            f"m_r_f_{i+1} = {m_f[i]} кг / {m_0[i]} кг => {m_r_f[i]:.3f}")
    print("")
    for i in range(3):
        print(
            f"m_r_sh_{i+1} = {m_sh[i]} кг / {m_0[i]} кг => {m_r_sh[i]:.3f}")
    print("")
    for i in range(3):
        print(
            f"m_r_op_{i+1} = {m_op[i]} кг / {m_0[i]} кг => {m_r_op[i]:.3f}")
    print("")
    for i in range(3):
        print(
            f"m_r_cy_{i+1} = {m_cy[i]} кг / {m_0[i]} кг => {m_r_cy[i]:.3f}")
    print("")
    for i in range(3):
        print(
            f"m_r_t_{i+1} = {m_t[i]} кг / {m_0[i]} кг => {m_r_t[i]:.3f}")
    print("")
    for i in range(3):
        print(
            f"m_r_ob_{i+1} = {m_ob[i]} кг / {m_0[i]} кг => {m_r_ob[i]:.3f}")
    print(
        f"\nm_cl = {m_cl[0]} кг + {m_cl[1]} кг + {m_cl[2]} кг => {int(m_cl[3])} кг")
    print(
        f"\nm_r_kr = ({m_r_kr[0]:.3f} + {m_r_kr[1]:.3f} + {m_r_kr[2]:.3f}) / 3 => {m_r_kr[3]:.3f}")
    print(
        f"\nm_r_f = ({m_r_f[0]:.3f} + {m_r_f[1]:.3f} + {m_r_f[2]:.3f}) / 3 => {m_r_f[3]:.3f}")
    print(
        f"\nm_r_sh = ({m_r_sh[0]:.3f} + {m_r_sh[1]:.3f} + {m_r_sh[2]:.3f}) / 3 => {m_r_sh[3]:.3f}")
    print(
        f"\nm_r_op = ({m_r_op[0]:.3f} + {m_r_op[1]:.3f} + {m_r_op[2]:.3f}) / 3 => {m_r_op[3]:.3f}")
    print(
        f"\nm_r_cy = ({m_r_cy[0]:.3f} + {m_r_cy[1]:.3f} + {m_r_cy[2]:.3f}) / 3 => {m_r_cy[3]:.3f}")
    print(
        f"\nm_r_t = ({m_r_t[0]:.3f} + {m_r_t[1]:.3f} + {m_r_t[2]:.3f}) / 3 => {m_r_t[3]:.3f}")
    print(
        f"\nm_r_ob = ({m_r_ob[0]:.3f} + {m_r_ob[1]:.3f} + {m_r_ob[2]:.3f}) / 3 => {m_r_ob[3]:.3f}")
    print(f"\nm_0 = {int(m_cl[3])} кг + {m_r_comm[3]:.3f} кг / 1 - ({m_r_kr[3]:.3f} + {m_r_f[3]:.3f} + {m_r_sh[3]:.3f} + {m_r_op[3]:.3f} + {m_r_cy[3]:.3f} + {m_r_t[3]:.3f} + {m_r_ob[3]:.3f}) => {int(m_0_a[2])} кг")
    print(
        f"\nПогрешность второго и третьего приблежения: {-(((m_0_a[1]/m_0_a[2])*100)-100):.2f} %")


def main():
    calculations()
    output()


if __name__ == "__main__":
    main()
