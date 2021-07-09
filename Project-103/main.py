#importing modules
import pandas as pd
import plotly_express as px

#reading the comma seperated values(csv)
df = pd.read_csv("corona.csv")

#making of the graph of the csv file
fig = px.scatter(df , x = 'date' , y = 'cases' , color = 'country' , title= "Corona Cases of the countries from 2019.")
fig.show()