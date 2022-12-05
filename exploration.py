import csv
import os
import sklearn as sks
import sys
import pandas as pd
import regex as re
import seaborn as sns
import matplotlib.pyplot as plt
import hdbscan
from sklearn.cluster import KMeans
import time
import datetime

SCAN = False
CLUSTER = True
PLOT = True

def csv_reader(directory_path:str="/UkraineWar", fileno="0906"):
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):
        df = pd.read_csv(
            "UkraineWarCombined/export.csv",
            lineterminator='\n')
        df = df.astype({'retweetcount':'int'})
        df = df[df["retweetcount"] > 5]
        df = df[df["compound"] != 0]
        new_df = pd.to_datetime(df['tweetcreatedts'], infer_datetime_format=True).astype(int) / 10**9
        df = pd.concat([df[['compound']],new_df], axis=1)
        df["tweetcreatedts"] = (df["tweetcreatedts"] - 1662447600) / 20000 # normalize timestamp

        if SCAN:
            sns.scatterplot(data=df, x="tweetcreatedts", y="compound")
            plt.show()

        if CLUSTER:
            clusterer = hdbscan.HDBSCAN(min_cluster_size=4, gen_min_span_tree=True)
            clusterer.fit(df)

            if PLOT:
                clusterer.minimum_spanning_tree_.plot(edge_cmap='viridis',
                                              edge_alpha=0.6,
                                              node_size=80,
                                              edge_linewidth=2)
                plt.show()
                clusterer.single_linkage_tree_.plot(cmap='viridis', colorbar=True)
                plt.show()
                clusterer.condensed_tree_.plot()
                plt.show()
                clusterer.condensed_tree_.plot(select_clusters=True, selection_palette=sns.color_palette())
                plt.show()
            palette = sns.color_palette()
            cluster_colors = [sns.desaturate(palette[col], sat)
                              if col >= 0 else (0.5, 0.5, 0.5) for col, sat in
                              zip(clusterer.labels_, clusterer.probabilities_)]
            sns.scatterplot(data=df, x="tweetcreatedts", y="compound", c=cluster_colors)
            plt.show()
            # if PLOT:

if __name__ == "__main__":
    csv_reader()
