import os
import pandas as pd
import csv
import re
import sys
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def vader(df):
    #creates new column with cleaned text

    sentiment = df['text'].apply(lambda x: SentimentIntensityAnalyzer().polarity_scores(x))
    df = pd.concat([df,sentiment.apply(pd.Series)],axis=1)
    return df

def engineer(df):
    df = df.loc[df['language']=='en'] #non-english tweets shows neutral... can't analyze
    df = vader(df)
    return df

def csv_reader(indir, outdir):
    for file in os.listdir(indir):
        if file.endswith('.csv'):
            df = pd.read_csv(indir + file)
            df.drop_duplicates(inplace = True)
            df = df.loc[df['language']=='en'] #non-english tweets shows neutral... can't analyze
            df = vader(df)
            df.to_csv(outdir + file)

if __name__ == '__main__':
    if len (sys.argv) > 2:
        indir = sys.argv[1]
        outdir = sys.argv[2]
        csv_reader(indir, outdir)

    else:
        print('Need input directory and output directory')
