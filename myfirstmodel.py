import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


df=pd.read_csv("student-por.csv")
#print(df.columns)
df["Total Marks"]=df[["G1","G2","G3"]].mean(axis=1)
print(df["Total Marks"].head(5))
x=df[["studytime","traveltime"]] #independent variables
y=df["Total Marks"] #Dependent  variable

'''x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=56)
model=LinearRegression()
model.fit(x_train,y_train)'''
#("R2",model.score(x_test,y_test)) #0.061 when test size=20% very poor

#will now try to find the best split

'''testSizes=[0.1,0.2,0.3,0.4] #test size <0.5 so that model has enough data to train on
for t in testSizes:
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=t,random_state=56)
    model=LinearRegression()
    model.fit(x_train,y_train)
    score=model.score(x_test,y_test)
    print(f"{t}, R2 is {score}")'''

'''0.1, R2 is 0.10368425310417662
0.2, R2 is 0.06124346307349815
0.3, R2 is 0.0723736556281418
0.4, R2 is 0.051443304827660685
 
0.1 GAVE THE BEST RESULT AS R2 IS GREATER

'''

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.1,random_state=48)
model=LinearRegression()
model.fit(x_train,y_train)
score=model.score(x_test,y_test)
first=model.predict([[3,1]])
print(first) #[13.00780641]

second=model.predict([[1,3]])
print(second) #[9.95087664]


