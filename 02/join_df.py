import pandas as pd

def main():
    start_date ='2020-12-22'
    end_date = '2021-01-26'
    dates = pd.date_range(start=start_date, end=end_date)
    df1 = pd.DataFrame(index=dates)
    dfRBLX = pd.read_csv('data/RBLX.csv',
                          index_col='Date', 
                          parse_dates=True,
                          usecols=['Date', 'Adj Close'])

    df1 = df1.join(dfRBLX).dropna()
    print(df1)

if __name__=="__main__":
    main()