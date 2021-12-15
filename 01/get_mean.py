import pandas as pd

def get_mean(symbol):
    df = pd.read_csv(f'data/{symbol}.csv')
    return df['Volume'].mean()

def main():
    print('Mean VOlume\n')
    print('-' * 10)
    for symbol in ['KO']:
        print(symbol + ': ', get_mean(symbol))

if __name__=="__main__":
    main()