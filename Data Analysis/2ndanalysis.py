import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("Housing.csv")

print(df.columns)

'''Index(['price', 'area', 'bedrooms', 'bathrooms', 'stories', 'mainroad',
       'guestroom', 'basement', 'hotwaterheating', 'airconditioning',
       'parking', 'prefarea', 'furnishingstatus'],
      dtype='object')'''


df["guestroom"]=df["guestroom"].replace({"no":0,"yes":1})
df["airconditioning"]=df["airconditioning"].replace({"no":0,"yes":1})
df["hotwaterheating"]=df["hotwaterheating"].replace({"no":0,"yes":1})

sns.kdeplot(data=df,x="price")

sns.heatmap(data=df[["price","area","bathrooms","bedrooms","guestroom","hotwaterheating","airconditioning"]].corr(),annot=True,cmap="Blues",linecolor="orange",linewidths=4)


sns.violinplot(data=df,x="bathrooms",y="price") 

sns.boxplot(data=df,x="bedrooms",y="price") 

sns.countplot(data=df,x="airconditioning") 

sns.countplot(data=df,x="furnishingstatus") 

sns.countplot(data=df,x="guestroom")

sns.countplot(data=df,x="hotwaterheating") 

sns.countplot(data=df,x="bathrooms")

sns.countplot(data=df,x="bedrooms")

sns.barplot(data=df,x="bathrooms",y="price",estimator=np.mean)

sns.barplot(data=df,x="guestroom",y="price",estimator=np.mean) 

sns.barplot(data=df,x="bedrooms",y="price",estimator=np.mean)
sns.lineplot(data=df,x="area",y="price") 

#-------------------DATA ANALYSIS & VISUALIZATION USING reg PLOT--------------------------

sns.regplot(data=df,x="area",y="price",line_kws={'color':"red","linewidth":3},scatter_kws={'color':'green',"marker":"*","edgecolor":"black","s":50}) 


#-------------------DATA ANALYSIS & VISUALIZATION USING Strip and swarm PLOT--------------------------

sns.stripplot(data=df,x="furnishingstatus",y="price")


sns.swarmplot(data=df,x="furnishingstatus",y="price",hue="bedrooms")


#-------------------DATA ANALYSIS & VISUALIZATION USING SCATTER PLOT--------------------------
sns.scatterplot(data=df,x="area",y="price")
plt.show()