import pandas as pd

def get_max_close(symbol):
    """
    returns company stock max close price
    """
    df = pd.read_csv(f'data/{symbol}.csv')
    return df['Close'].max()
    
def main():
    print("Max Close:")
    for  symbol in ['KO']:
        print(symbol + ":", get_max_close(symbol))

if __name__=='__main__':
    main()