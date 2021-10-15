import pandas as pd
import numpy as np
import plotly.express as ne
df=pd.read_csv("cups of coffee vs hours of sleep.csv")
cupsOfCoffee=df["Coffee in ml"].tolist()
sleep=df["sleep in hours"].tolist()
#graph=ne.scatter(df,x="Coffee in ml",y="sleep in hours")
#graph.show()
d={"x":cupsOfCoffee,"y":sleep}
corelate=np.corrcoef(d["x"],d["y"])
print(corelate)