import pandas as pd
import numpy as np
import plotly.express as pe
df=pd.read_csv("Student Marks vs Days Present.csv")
marks=df["Marks In Percentage"].tolist()
daysPresent=df["Days Present"].tolist()
d={"x":marks,"y":daysPresent}
corelate=np.corrcoef(d["x"],d["y"])
print(corelate)