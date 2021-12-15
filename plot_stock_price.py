import pandas as pd
import matplotlib.pyplot as plt


def main():
    df = pd.read_csv('data/KO.csv')
    print(df)
    df['Adj Close'].plot()
    plt.savefig('graphs/ko.png')

if __name__=="__main__":
    main()