import csv
import nltk
import os
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

def weighted_sample(d:dict, weight:float):
    df_list = []
    for key in d.keys():
        df_list.append(d[key].sample(int(len(d[key]) * weight)))
    return pd.concat(df_list)

def execute(directory_path: str, export_path: str, sample_size: int, runs: int):
    [data_full, avg_len] = csv_reader(directory_path)
    for i in range(runs):
        data_sampled_combined = weighted_sample(data_full, float(int(sample_size)/avg_len))
        data_sampled_combined.to_csv(f"{export_path}/UkraineWarSampled_{i}.csv")

if __name__ == "__main__":
    directory_path = sys.argv[1]
    export_path = sys.argv[2]
    sample_size = sys.argv[3]
    runs = sys.argv[4]

    execute(directory_path, export_path, sample_size, int(runs))



    #Execute Training Here
