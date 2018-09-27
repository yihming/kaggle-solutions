import numpy as np
import pandas as pd

def load_data():
    market = pd.read_csv("./marketdata_sample.csv")
    news = pd.read_csv("./news_sample.csv")

    return market, news

def main():
    market, news = load_data()

if __name__ == "main":
    main()
