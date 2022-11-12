
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from tslearn.metrics import dtw
from tslearn.metrics import soft_dtw
from tslearn.clustering import TimeSeriesKMeans

from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import minmax_scale
from sklearn.preprocessing import MaxAbsScaler
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import RobustScaler
from sklearn.preprocessing import Normalizer
from sklearn.preprocessing import QuantileTransformer
from sklearn.preprocessing import PowerTransformer

import sys

def kmeans(csv,k,k_seeds,xaxis, yaxis,x_scaler = None, y_scaler= None):
  
  # preprossing 
  df = pd.read_csv(f'{csv}')
  df = df.dropna()
  df['Day'] = df.index +1

  
  # scaling options: MinMaxScaler,minmax_scale,MaxAbsScaler,StandardScaler,RobustScaler,Normalizer,QuantileTransformer,PowerTransformer
  if x_scaler is not None:
    df[[f'{xaxis}']] = x_scaler().fit_transform(df[[f'{xaxis}']])
  if y_scaler is not None:
    df[[f'{yaxis}']] = y_scaler().fit_transform(df[[f'{yaxis}']])



  #assuming first column is the datetime column
  df.iloc[:,0]= pd.to_datetime(df.iloc[:,0])

  data = df[[f'{xaxis}',f'{yaxis}']].reset_index().drop('index',axis=1)
  model = TimeSeriesKMeans(n_clusters=k, metric="dtw", max_iter=10,random_state = k_seeds)
  model.fit(data)

  #data you want to predict
  y=model.predict(data)

  # date data
  x = df['Day']

  centroids = model.cluster_centers_

  #plotting the data
  plt.style.use('seaborn')
  plt.rcParams['font.family'] = 'Times New Roman' 
  plt.rcParams['font.size'] = 14 
  plt.rcParams['axes.labelsize'] = 12 
  plt.rcParams['axes.labelweight'] = 'bold' 
  plt.rcParams['image.cmap'] = 'jet' 
  plt.rcParams['image.interpolation'] = 'none' 
  plt.rcParams['figure.figsize'] = (12, 10) 
  plt.rcParams['axes.grid']=True
  data_c = df.copy()
  data_c['Class']=y

  sns.scatterplot(x=f"{xaxis}",y=f'{yaxis}',hue='Class',data=data_c,palette='plasma')
  plt.scatter(centroids[:,0] , centroids[:,1] , s = 250, color = 'k',alpha = 0.9)

  dtw_score = dtw(x, y)
  print("The DTW score is", dtw_score)

  return plt.show()


if __name__ == "__main__":
  # example input: kmeans("Month_Value_1.csv",2,3,"Day","Sales_quantity",StandardScaler,StandardScaler)
  # input function parameters kmeans(str,str,int,int,str,str,no quotes or None, no quotes or None)
  graph = kmeans(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6],sys.argv[7])
