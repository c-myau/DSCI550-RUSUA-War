import csv
import os
import sklearn as sks
import sys
import pandas as pd
import clustering as c
import matplotlib.pyplot as plt
import seaborn as sns


def import_csv(directory_path="/UkraineWarSampled", file="/UkraineWarSampled_0.csv"):
    df = pd.read_csv(f"{directory_path}/{file}", lineterminator='\n')
    return df

def execute(directory_path: str, N: int, M: int, L: int):
    if L >= M:
        df = import_csv(directory_path)
        run_list = []
        for i in range(N):
            for j in range(M, L + 1):
                run_list.append(c.cluster(df, j))
        return run_list
    else:
        raise ValueError

def visualize(directory_path="UkraineWarSampled", file="UkraineWarSampled_0.csv"):
    df = pd.read_csv(f"{directory_path}/{file}", lineterminator='\n')
    ax1 = sns.scatterplot(data=df, x="extractedts", y="compound")
    plt.show()



if __name__ == "__main__":
    directory_path = sys.argv[1]
    N = sys.argv[2]
    M = sys.argv[3]
    L = sys.argv[4]

    # output = execute(directory_path, int(N), int(M), int(L))
    visualize(directory_path)
