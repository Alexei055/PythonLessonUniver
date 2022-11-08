import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def firs_task():
    data = pd.read_csv("YP.csv")
    print(f"\033[31m{data.head(10)}\n{'-' * 50}\033[32m")
    print(f"{data.info()}\n{'-' * 50}")
    print(f"\033[33m{data.columns}\n{'-' * 50}")
    print(f"\033[34m{data.isna().sum()}\n{'-' * 50}")
    print(f"\033[35m{data.duplicated().sum()}\n{'-' * 50}")


# firs_task()


def second_task():
    data = pd.read_csv("visits.csv", sep='\t')
    plt.boxplot(data)
    plt.show()


# second_task()


def third_task():
    pur_time = pd.Series(
        [40, 76, 23, 68, 26, 48, 32, 47, 57, 21, 52, 52, 55, 68, 47, 42, 73, 70, 38, 42, 48, 79, 36, 72, 62, 64, 78, 24,
         52, 46, 43, 43, 63, 42, 63, 61, 21, 74, 66, 48, 63, 59, 42, 77, 26, 52, 40, 61, 37, 54])

    plt.hist(pur_time,
             edgecolor='black',
             bins=[15, 30, 45, 60, 75, 90],
             alpha=0.7)

    plt.show()


third_task()
