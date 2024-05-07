import pandas as pd
import numpy as np
import math

E: float = math.e

def I (p, n): 
    if p == 0 or n == 0: 
        return 0
    return (-p / (p + n) * math.log(p / (p + n), E)) - (n / (p + n) * math.log(n / (p + n), E))

def gini_index(file_name: str, type: str) -> float:
    data = pd.read_csv(file_name)
    s = data[type].unique()
    p: int = len(data[data[type] == s[0]])
    n: int = len(data[data[type] == s[1]])
    return I(p, n)

def E (df, A): 
    n: int = len(df[A])
    ans: float = 0
    s = df[A].unique()
    for i in s: 
        tmp = df[df[A] == i]
        k = list(tmp['Class'].unique())
        if (len(k) == 1): k.append(0)
        p: int = len(tmp)
        n_1 = len(tmp[tmp['Class'] == k[0]])
        n_2 = len(tmp[tmp['Class'] == k[1]])
        ans += p / n * I(n_1, n_2)
    return ans;

def Gain (df, type: str) -> float:
    global res
    return res - E(df, type)

def cal (A) -> float: 
    res: float = 0
    Sum = sum(A)
    for i in A: 
        res += -i / Sum * math.log2(i / Sum)
    return res

def split_gain (df, type: str) -> float:
    s = df[type].unique()
    res: float = 0
    tmp = []
    for i in s: 
        tmp.append(len(df[df[type] == i]))
    res = cal(tmp)
    return res

def Gain_ratio (df, type) -> float: 
    return Gain(df, type) / split_gain(df, type)

# df = pd.read_csv('hw6.csv')
# res = gini_index('hw6.csv', 'Class')
# print(f"Gini Index: {res:.6f}\n")

# print(f"Gain (Car Type): {Gain(df, 'Car Type'):.6f}");
# print(f"Gain (Gender): {Gain(df, 'Gender'):.6f}");
# print()

# print(f"Gain Ratio (Car Type): {Gain_ratio(df, 'Car Type'):.6f}");
# print(f"Gain Ratio (Gender): {Gain_ratio(df, 'Gender'):.6f}");
# print()

# tt = ""
# print(f"{tt:-^30}")
# print()


# df3 = pd.read_csv('hw6_2.csv')
# res = gini_index('hw6_2.csv', 'Class')

# print(f"Gini Index: {res:.6f}\n")

# print(f"Gain (a1): {Gain(df3, 'a1'):.6f}");
# print(f"Gain (a2): {Gain(df3, 'a2'):.6f}");
# print(f"Gain (a3): {Gain(df3, 'a3'):.6f}");
# print()

# print(f"Gain Ratio (a1): {Gain_ratio(df3, 'a1'):.6f}");
# print(f"Gain Ratio (a2): {Gain_ratio(df3, 'a2'):.6f}");
# print(f"Gain Ratio (a3): {Gain_ratio(df3, 'a3'):.6f}");

if __name__ == "__main__": 
    print(1/9 * math.log2(0.5))