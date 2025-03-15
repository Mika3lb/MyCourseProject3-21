import csv

import pandas as pd

from main import *

FILENAME = 'input.csv'


def readCSV():
    with open(FILENAME, 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            print(row)


def openCSV():
    with open(FILENAME, 'a', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["Serial Number", "m_0", "m_comm", "m_k",
                            "m_cy", "m_t", "m_cl", "m_ob", "m_kr", "m_sh", "m_op", "m_f"])
        for i in range(3):
            csv_writer.writerow([i, m_0[i], m_comm[i], m_k[i], m_cy[i],
                                m_t[i], m_cl[i], m_ob[i], m_kr[i], m_sh[i], m_op[i], m_f[i]])


def pandasWork():
    df = pd.read_csv(FILENAME)

    print(df.to_string())

    tmp = df['m_0'][0]

    print(tmp)


if __name__ == "__main__":
    pandasWork()
