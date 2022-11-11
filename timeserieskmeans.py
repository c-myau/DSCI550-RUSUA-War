# -*- coding: utf-8 -*-
"""TimeSeriesKMeans

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gMoRoACt_ai41MktAwIxyq38Q0ic4bv-
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from tslearn.metrics import dtw
from tslearn.metrics import soft_dtw
from tslearn.metrics import dtw
from tslearn.metrics import soft_dtw

def kmeans(csv,k,k_seeds,xaxis, yaxis, x_lower=None,x_upper=None,y_lower=None,y_upper=None):
  df = pd.read_csv(f'{csv}')
  df = df.dropna()

  df['Day'] = df.index +1


  #assuming first column is the datetime column
  df.iloc[:,0]= pd.to_datetime(df.iloc[:,0])

  data = df[[f'{xaxis}',f'{yaxis}']].reset_index().drop('index',axis=1)
  model = TimeSeriesKMeans(n_clusters=k, metric="dtw", max_iter=10,random_state = k_seeds)
  model.fit(data)

  #data you want to predict
  y=model.predict(data)

  # date data
  x = df.Period

  centroids = model.cluster_centers_

  #plotting the data
  plt.style.use('seaborn')
  plt.rcParams['font.family'] = 'Times New Roman' 
  plt.rcParams['font.size'] = 14 
  plt.rcParams['axes.labelsize'] = 12 
  plt.rcParams['axes.labelweight'] = 'bold' 
  plt.rcParams['axes.titlesize'] = 12 
  plt.rcParams['xtick.labelsize'] = 12 
  plt.rcParams['ytick.labelsize'] = 12 
  plt.rcParams['legend.fontsize'] = 12 
  plt.rcParams['figure.titlesize'] = 12 
  plt.rcParams['image.cmap'] = 'jet' 
  plt.rcParams['image.interpolation'] = 'none' 
  plt.rcParams['figure.figsize'] = (12, 10) 
  plt.rcParams['axes.grid']=True
  plt.rcParams['lines.linewidth'] = 2 
  plt.rcParams['lines.markersize'] = 8
  data_c = df.copy()
  data_c['Class']=y

  if x_lower and x_upper is not None:
    plt.xlim(x_lower, x_upper)
  elif y_lower and y_upper is not None:
    plt.ylim(y_lower,y_upper)


  sns.scatterplot(x=f"{xaxis}",y=f'{yaxis}',hue='Class',data=data_c,palette='plasma')
  plt.scatter(centroids[:,0] , centroids[:,1] , s = 250, color = 'k',alpha = 0.9)

  dtw_score = dtw(x, y)
  print("The DTW score is", dtw_score)