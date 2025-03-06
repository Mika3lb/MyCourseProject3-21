import pandas as pd
import numpy as np

if __name__ == "__main__":
    d = {"A": 1,
         "B": 2,
         "C": 4}
    data = pd.DataFrame(d, index=list("123"), columns=["A320", "B757", "A300"])
    print(data)
