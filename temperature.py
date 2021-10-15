import pandas as pd
import numpy as np
import plotly.express as pe
df=pd.read_csv("Ice-Cream vs Cold-Drink vs Temperature - Ice Cream Sale vs Temperature data.csv")
temperature=df["Temperature"].tolist()
IceCreamSales=df["Ice-cream Sales( ₹ )"].tolist()
#graph=pe.scatter(df,x="Temperature",y="Ice-cream Sales( ₹ )")
#graph.show()
d={"x":temperature,"y":IceCreamSales}
corelation=np.corrcoef(d["x"],d["y"])
print(corelation)