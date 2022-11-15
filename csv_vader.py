import os
import pandas as pd
import csv
import re
import sys
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

#https://www.geeksforgeeks.org/python-sentiment-analysis-using-vader/
#https://www.geeksforgeeks.org/twitter-sentiment-analysis-on-russia-ukraine-war-using-python/
#https://towardsdatascience.com/are-you-scared-vader-understanding-how-nlp-pre-processing-impacts-vader-scoring-4f4edadbc91d


def rt(text): #remove tags and punctuations
    return re.sub("(@\w+)|([^\d\w \t])|(\w+:\/\/\S+)", " ", text)

def vader(df):
    #creates new column with cleaned text
#     df['text_rt'] = df['text'].str.lower().map(rt)

    #sentiment analysis using new text >> series
#     sentiment = df['text_rt'].apply(lambda x: SentimentIntensityAnalyzer().polarity_scores(x))
    sentiment = df['text'].apply(lambda x: SentimentIntensityAnalyzer().polarity_scores(x))

    #add the sentiment analysis to the dataframe
    df = pd.concat([df,sentiment.apply(pd.Series)],axis=1)
    return df

def single(directory_path):
    df = pd.read_csv(directory_path)
    df.drop_duplicates(inplace = True)
    df = df.loc[df['language']=='en'] #non-english tweets shows neutral... can't analyze
    df = vader(df)
#         df.sample(1000).to_csv(outdir + file)
    df.to_csv(outdir + file)

def csv_reader(indir, outdir):
    for file in os.listdir(indir):
        if file.endswith('.csv'):
            df = pd.read_csv(indir + file)
            df.drop_duplicates(inplace = True)
            df = df.loc[df['language']=='en'] #non-english tweets shows neutral... can't analyze
            df = vader(df)
    #         df.sample(1000).to_csv(outdir + file)
            df.to_csv(outdir + file)

if __name__ == '__main__':
    if len (sys.argv) > 2:
        indir = sys.argv[1]
        outdir = sys.argv[2]
        csv_reader(indir, outdir)

    else:
        print('Need input directory and output directory')
