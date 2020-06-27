import yfinance as yf
import pandas as pd
def save_stock_data(df,ticker,start,end,interval):
  df.to_csv('data/%s_%s_%s_%s.csv' %(ticker,start,end,interval))


def grab():
  def get_stock_data(ticker,start,end,interval,progress=False):
    return yf.download('RDSA.L', 
                        start=start, 
                        end=end,
                        interval=interval,
                        progress=True)

  def save_stock_data(df,ticker,start,end,interval):
    df.to_csv('data/%s_%s_%s_%s.csv' %(ticker,start,end,interval))

  ticker = 'RDSA.L'
  start='2000-01-01'
  end='2020-06-19'
  interval = '1h'


  df = get_stock_data('RDSA.L', 
                        start, 
                        end,
                        interval, 
                        progress=True)
  print(len(df))
  save_stock_data(df,ticker,start,end,interval)

def grab2():

  rdsa = yf.Ticker("RDSA.L")
  print(rdsa)

  print(rdsa.info)

  hist = rdsa.history(period="max")
  print(type(hist))
  save_stock_data(hist, 'RDSA.L','20200622','max','1d')



grab()
# df = pd.read_csv(r'data/RDSA.L_2010-01-01_2020-06-19.csv')
# print((df.head()))