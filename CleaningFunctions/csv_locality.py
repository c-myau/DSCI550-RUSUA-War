import csv
import os
import sklearn as sks
import sys
import pandas as pd
import regex as re

location_set = ["Kiev", "Ukraine", "Kherson", "Kyiv", "Russia", "Moscow"]

def engineer(df):
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):
        loca_df_1 = df.loc[df['location'].isin(location_set)]
        patternDel = '[А-я]+'
        loca_df_crylic = df[df['location'].str.contains(patternDel, na=False)]
        local_df = pd.concat([loca_df_1, loca_df_crylic])
        local_df.to_csv("UkraineWarLocal/export.csv", index=False)
        export_df = pd.read_csv(
            "UkraineWarLocal/export.csv",
            lineterminator='\n')

        return export_df

if __name__ == "__main__":
    engineer()
