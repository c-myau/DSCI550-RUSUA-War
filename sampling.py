import csv
import os
import sklearn as sks
import sys
import pandas as pd

def csv_reader(directory_path:str) -> dict:
    df_dict = {}
    x, c = 0,0
    for filename in os.listdir(directory_path):
        if filename.endswith('.csv'):
            try:
                df = pd.read_csv(
                    f"{directory_path}/{filename}",
                    lineterminator='\n')
                df = df.loc[df['language']=='en']
                x += len(df)
                c += 1
                df_dict[filename] = df
            except Exception as e: print(e)
    return [df_dict, x/c]

def weighted_sample(d:dict, weight:float, random_state:int=None):
    df_list = []
    for key in d.keys():
        df_list.append(d[key].sample(int(len(d[key]) * weight),random_state=random_state))
    return pd.concat(df_list)

def execute(directory_path: str, export_path: str, sample_size: int=100, runs: int=1, random_state:int=None):
    [data_full, avg_len] = csv_reader(directory_path)
    for i in range(runs):
        data_sampled_combined = weighted_sample(data_full, float(sample_size/avg_len), random_state)
        data_sampled_combined.to_csv(f"{export_path}/UkraineWarSampled_{i}.csv")

if __name__ == "__main__":
    directory_path = sys.argv[1]
    export_path = sys.argv[2]
    sample_size = sys.argv[3]
    runs = sys.argv[4]

    execute(directory_path, export_path, int(sample_size), int(runs))



    #Execute Training Here
