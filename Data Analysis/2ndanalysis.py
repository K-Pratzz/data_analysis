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

#sns.heatmap(data=df[["price","area","bathrooms","bedrooms","guestroom","hotwaterheating","airconditioning"]].corr(),annot=True,cmap="Blues",linecolor="orange",linewidths=4) area bathroom airconditioning  bedroom shows strong +ve correlation with price, hotwater heating and guestrrom has less +ve correlation with price


#sns.violinplot(data=df,x="bathrooms",y="price") for 1 no of bathroom , iqr is less it is more predictable, for 3 iqr is greatest making it difficult to predict, the median increases from 1 to 3 suggesting positive correlation b/w bathroom and price, there is horizontal line for 4 which shows that it is very rare in dataset

#sns.boxplot(data=df,x="bedrooms",y="price") meduan increaes with no of bedrooms ,IQR for 5 is biggger,making it least predictable, 1 and 2 are most predictable as the IQR range is not wide spread, there are few outliers in 2 3 4, bedroom with 4 tends to have the highest value

#sns.countplot(data=df,x="airconditioning") 370 no ac 160 has ac

#sns.countplot(data=df,x="furnishingstatus") 230 semifurnished 180  unfurnished and 140 furnished

#sns.countplot(data=df,x="guestroom") 400 above has no h=guestroom less than 100 has one guestroom

#sns.countplot(data=df,x="hotwaterheating") #above 500  has not very few only approx 30 has have hotwaterheating in them

#sns.countplot(data=df,x="bathrooms") #most is 1 then 2 least is 4 ( approx 400 has 1 bathroom , approx 120 has 2 ,approx 10 has 3 and approx 4,5 has 4 bathrooms)

#sns.countplot(data=df,x="bedrooms")# most frequent no of bedrooms 3 then 2 , least is 6 and 1

#sns.barplot(data=df,x="bathrooms",y="price",estimator=np.mean,dodge=True) #positive cirrelation with price

#sns.barplot(data=df,x="guestroom",y="price",estimator=np.mean,dodge=True) positive correlation

#sns.barplot(data=df,x="bedrooms",y="price",estimator=np.mean,dodge=True) #greater the no of 

# bedrooms higher is theAVG PRICE however for 6 no of roooms avg is less than 5,4..thats because no of bedrooms doesnt soley depicts price 



#sns.lineplot(data=df,x="area",y="price") #depicts that area afefects the price however for greater area prices fall also this volatility is because price  is affected by other features like no of rooms bathroom kitchen furnishing status and all

#-------------------DATA ANALYSIS & VISUALIZATION USING reg PLOT--------------------------

#sns.regplot(data=df,x="area",y="price",line_kws={'color':"red","linewidth":3},scatter_kws={'color':'green',"marker":"*","edgecolor":"black","s":50}) #trend line shows positive correlatin between area and price



#-------------------DATA ANALYSIS & VISUALIZATION USING Strip and swarm PLOT--------------------------

#sns.stripplot(data=df,x="furnishingstatus",y="price") #for furnished data points are concentreated at higher prices while for semi furnished and unfurniswd more concentrated at lower prices which suggests that furnished homes tends to be more expensive


#sns.swarmplot(data=df,x="furnishingstatus",y="price",hue="bedrooms")


#-------------------DATA ANALYSIS & VISUALIZATION USING SCATTER PLOT--------------------------
#sns.scatterplot(data=df,x="area",y="price") #it shows as the area increases price increases +ve correlataion however not perfect at certain places prices are too high which tells price doent not soley depends on area, most of the data is concentreated till 8000 in area,there are few outliers that deviate from the concentreated region 
plt.show()