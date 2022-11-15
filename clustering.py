import pandas as pd
from sklearn.cluster import KMeans
from sklearn import metrics
from scipy.spatial.distance import cdist
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

#TODO: feature engineering

def cluster(df, k):
    df = df[["extractedts", "compound"]]
    print(df.head())
    return [df, k]
