import pandas as pd
import yfinance as yf
from pandas.io.parsers import read_csv
import plotly
import plotly.graph_objects as go

tsla_df = yf.download('TSLA', period='1d', interval='1d', group_by ='ticker', prepost=False, start="2021-03-09", end="2021-03-16", threads=True, progress=True)

tsla_df.to_csv(r'c:\Users\Carlton Osinde\Desktop\Discord Stock Bot\TELSA-DATA.csv', index=True, header=True)

tsla_df = pd.read_csv('TELSA-DATA.csv')

data = tsla_df

plotly.offline.plot({
    "data" : [go.Scatter(x = data['Datetime'], y = data['High'])],

    "layout" : go.Layout(title='Tesla Share Prices from March 9th - March 16th',
                   plot_bgcolor='rgb(230, 230,230)',
                   showlegend=True)

})
