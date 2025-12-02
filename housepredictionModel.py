import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df=pd.read_csv("Housing.csv")
#print(df.columns)
#print(df.shape)  545 rows and 13 columns
#guestroom column has yes no value need to convert to numeric

df["guestroom"]=df['guestroom'].replace({"yes":1,"no":0})

x=df[['bedrooms','bathrooms','guestroom','area','parking']] 
y=df['price']
'''
testSplit=[0.2,0.3,0.4,0.5,0.6,0.7,0.8]
for ts in testSplit:
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=ts,random_state=30)
    model=LinearRegression()
    model.fit(x_train,y_train)
    score=model.score(x_test,y_test)
    print(f"for trainsplit {ts}, the r2 is {score}")'''

'''  
for trainsplit 0.2, the r2 is 0.4088456632423709
for trainsplit 0.3, the r2 is 0.4149051164355885
for trainsplit 0.4, the r2 is 0.4356635819415565
for trainsplit 0.5, the r2 is 0.46685116087251477
for trainsplit 0.6, the r2 is 0.48041316331250883
for trainsplit 0.7, the r2 is 0.4642674416934641
for trainsplit 0.8, the r2 is 0.4562058757751195

FOR 0.6 R2 VALUE IS 0.48 ****

'''

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.6,random_state=37)
model=LinearRegression()
model.fit(x_train,y_train)
first=model.predict([[4,1,0,5700,2]])
print(first) #[5037908.49240023]
second=model.predict([[2,0,0,3000,1]])
print(second) #[1609442.69868152]
third=model.predict([[3,2,1,6000,2]])
print(third) #[7141048.84698548]
