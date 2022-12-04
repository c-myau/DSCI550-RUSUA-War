import csv
import os
import sys
import pandas as pd
import regex as re
import CleaningFunctions.csv_locality as cl
import CleaningFunctions.csv_vader as cv

def read(path="UkraineWar/0905_UkraineCombinedTweetsDeduped.csv"):
    return pd.read_csv(path,lineterminator='\n')

def execute(func:[]):
    df = read()
    for feature in func:
        if feature == "Local":
            df = cl.engineer(df)
        if feature == "Sentiment":
            df = cv.engineer(df)
    df.to_csv("UkraineWarCombined/export2.csv")

if __name__ == "__main__":
    execute(["Local", "Sentiment"])
