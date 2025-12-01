import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv("student-por.csv")
'''print(df.shape)
print(df.info())
print(df.describe())
print(df.columns)
#print(df.head(5))
#649 rows and 33 column'''
df.rename(columns={"famsize":"Family Size","Medu" : "Mother Education","Fedu":"Father Education","Mjob":"Mother Job","Fjob":"Father Job"},inplace=True)
index=np.arange(0,649)
df["indexCol"]=index
df.set_index("indexCol",inplace=True)
print(df.head(2))

'''for col in df.columns:
    p=df[col].isnull().mean()
    print(p*100)
    if(p*0.3):
        df.drop(col,axis=1,inplace=True)
#Contains No NaN'''


df.drop(["Family Size","Pstatus","Mother Education","Father Education","romantic"],axis=1,inplace=True)
#print(df.shape)

#removed unrequired columns
df["Average Grade"]=df[["G1","G2","G3"]].mean(axis=1)
#print(df["Average Grade"].dtype)
condition=[
    df["Average Grade"]<7.0,
    df["Average Grade"]>=7.0
    ]
values=["Fail","Pass"]
df["Result"]=np.select(condition,values,default="No Grade")
#print(df["Average Grade"].head(6))
print(df["Result"].tail(20))
#Created a result colmun with pass/fail

#print(df.value_counts("Father Job"))
#print(df.value_counts("Mother Job"))

#To get the percetnage

#print(df["Father Job"].value_counts(normalize=True)*100)
#print(df["Mother Job"].value_counts(normalize=True)*100)

'''Father Job
other       56.548536
services    27.889060
at_home      6.471495
teacher      5.546995
health       3.543914'''

'''Mother Job
other       39.753467
services    20.955316
at_home     20.801233
teacher     11.093991
health       7.395994'''

'''print(df["guardian"].value_counts())

guardian
mother    455
father    153
other      41  
print(df.columns)

x=pd.pivot_table(columns="studytime",index="sex",aggfunc=sum,values="traveltime",data=df)
print(x)'''
#all unique value of index and column is used to create column index, and for Index sex F and studytime 1 the sum of travel time is 146
'''studytime    1    2    3   4
sex
F          146  303  110  32
M          206  164   32  25

print(df.groupby("sex")["Average Grade"].max())
sex
F    18.666667
M    18.000000
print(df["Average Grade"].max())

print(df.groupby("sex")["Average Grade"].mean())
sex
F    11.904265
M    11.223058


m=df["studytime"]>2
print(df[m]["Average Grade"])
filters the df shows average grade of rows whose study time is > 2


df.drop_duplicates("traveltime",inplace=True)
df.plot(y="studytime",x="traveltime",xlabel="Gender",ylabel="Study Time",title="Travel time vs study time",kind="bar",figsize=(10,20))
plt.savefig("Travel time vs Study Time")
plt.show()


df.drop_duplicates("guardian",inplace=True)
df.plot(kind="box",y="Average Grade")
plt.savefig("boxplot for average grade")
plt.show()
'''

#I want to make visulizations more informative using iplot but isn't working








