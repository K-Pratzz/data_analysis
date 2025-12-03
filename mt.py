import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("Housing.csv")

fig,ax=plt.subplots(2,1,figsize=(12,4))
ax[0].scatter(df["bedrooms"],df["price"])
ax[0].set_title("SUB PLOT 1")
ax[0].grid(True)

ax[1].bar(df["bedrooms"],df["price"])
ax[1].set_title("SUB PLOT 2")
ax[1].set_xlabel("Distribution of x")
ax[1].set_ylabel("Distribution of y")

plt.show()







'''plt.scatter(df["bedrooms"],df["price"])
l=["AREA","PRICE"]
#plt.boxplot(df["area"])
plt.show()'''


'''x=df["furnishingstatus"].value_counts()
un=178
sm=227
fur=140
color=["red","green","blue"]
label=["Unfurnished","Semi-Furnished","Furnished"]
explode=(0,.1,.4)
plt.pie([178,227,140],labels=label,colors=color,autopct="%.2f %%",pctdistance=0,explode=explode)
plt.title("PIE CHART USING ")
plt.xlabel("TYPES OF FURNISHING STATUS")
plt.ylabel("THRIR FREQUENCIES")

plt.show()'''

#plt.show()
'''plt.bar(df["area"],df["price"],color="purple",label="2xxxxx",width=600)
plt.xlabel("AREA OF HOUSE")
plt.ylabel("PRICE OF HOUSE")
plt.title("PRICE VS AREA PLOT")
plt.figure(figsize=(6,3),dpi=50)
plt.legend()
plt.show()'''


'''import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Dummy data
X = [1, 2, 3, 4, 5, 6]
y = [10, 20, 15, 25, 30, 28]

fig, ax = plt.subplots(1, 2, figsize=(12, 4))

# LEFT plot
ax[0].scatter(X, y)
ax[0].plot(X, y)
ax[0].set_title("Main Plot")
ax[0].set_xlim(0, 7)
ax[0].set_ylim(5, 35)
ax[0].set_xlabel("hiiiiiiiiiiiiiiiiiiiiiii")
#ax[0].grid(True)

# RIGHT plot
ax[1].hist(y)
ax[1].set_title("Distribution of Y")
ax[1].grid(True)

plt.show()'''


'''import matplotlib.pyplot as plt

plt.plot([1, 2, 3], [4, 5, 4])
plt.ylim(0, 7) # Set y-limit for better visibility

# Annotate the point (2, 5)
plt.annotate(
    'Local Max',       # The text to display
    xy=(2, 5),         # The point being annotated (arrow head)
    xytext=(1, 6),     # The position for the text (arrow tail)
    arrowprops=dict(
        facecolor='black',
        shrink=0.05,
        width=1,
        headwidth=8
    )
)

plt.show()'''