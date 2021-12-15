import pandas as pd
import matplotlib.pyplot as plt


def main():
    df = pd.read_csv('data/KO.csv')
    print(df)
    df[['Close', 'Adj Close']].plot()
    plt.savefig('graphs/multycol.png')

if __name__=="__main__":
    main()