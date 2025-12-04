import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#df=sns.load_dataset("student-por.csv") #sns cant load local files use pd
df=pd.read_csv("student-por.csv")
sns.set_style("darkgrid")
sns.set_context("paper")
df=df[["studytime","age","traveltime","G1","G2","G3"]]
col=["studytime","age","traveltime","G1","G2","G3"] #only for numerical data not categorical
sns.pairplot(data=df,hue="studytime",diag_kind="hist")
plt.savefig("seaborn/pairplot.png",dpi=150)

#sns.rugplot(data=df,x="age",y="G2",hue="sex")
#plt.savefig("seaborn/rugplot.png",dpi=150)
#sns.heatmap(data=df[col].corr(),cmap="Reds",annot=True,linecolor="black",linewidths=0.4)
#plt.savefig("seaborn/heatmap.png",dpi=150)
#print(df[["studytime","age","traveltime","G1","G2","G3"]].corr())
#sns.kdeplot(data=df,x="age",hue="sex",fill=True,palette=["pink","blue"])
#plt.savefig("seaborn/kdeplot.png",dpi=150)


#sns.violinplot(data=df,x="sex",y="G3",hue="sex",split=False,palette=["pink","blue"])
#plt.savefig("seaborn/violinplot.png",dpi=150)
#sns.boxplot(data=df,x="sex",y="G3",hue="sex")
#plt.savefig("seaborn/boxplot.png",dpi=150)
#sns.countplot(data=df,x="Fjob",hue="age",palette="Set1")
#plt.savefig("seaborn/countplot.png",dpi=150)

#sns.barplot(data=df,x="studytime",y="G1",hue="sex",dodge=True,palette=["yellow","green"],estimator=np.sum)
#plt.savefig("seaborn/barplot.png",dpi=150)
#sns.jointplot(data=df,x="traveltime",y="studytime",hue="sex",kind="scatter")
#plt.savefig("seaborn/jointplot.png",dpi=30)
#sns.lineplot(data=df,x="age",y="G2",hue="sex")
#plt.savefig("seaborn/lineplot.png")

#sns.regplot(data=df,x="studytime",y="traveltime",scatter=True)
#plt.savefig("seaborn/regplot.png",dpi=20)

#sns.histplot(data=df,x="age",hue="sex",multiple="dodge")
#plt.savefig("seaborn/histplot.png",dpi=50)
#sns.stripplot(data=df,x="age",y="G3",hue="sex",dodge=True,jitter=True)
#sns.scatterplot(data=df,x="age",y="G3",hue="sex",palette="pastel")

#sns.swarmplot(data=df,x="age",y="G3",hue="sex",dodge=True)
#plt.savefig("seaborn/scatterplot.png",dpi=100)
#sns.stripplot(data=df,x="age",y="G3",hue="sex",dodge=True,jitter=True)

#sns.scatterplot(data=df,x="age",y="G3",hue="sex",palette="pastel") #for all age groups female are top performing
plt.show()
#print(df.head(2))