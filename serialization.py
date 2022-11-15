import csv
import os
import sklearn as sks
import sys
import pandas as pd
import clustering

def import_csv(directory_path, file=None, all=False):
    if file:
        df = pd.read_csv(f"{directory_path}/{file}", lineterminator='\n')
    else:
        for filename in os.listdir(directory_path):
            df = pd.read_csv(f"{directory_path}/{filename}", lineterminator='\n')
    return df

def execute(directory_path: str, N: int, M: int, L: int):
    if L >= M:
        df = import_csv(directory_path)
        print(len(df))
        for i in range(N):
            for i in range(M, L + 1):
                print(i)
        return None
    else:
        raise ValueError

if __name__ == "__main__":
    directory_path = sys.argv[1]
    N = sys.argv[2]
    M = sys.argv[3]
    L = sys.argv[4]

    execute(directory_path, int(N), int(M), int(L))
