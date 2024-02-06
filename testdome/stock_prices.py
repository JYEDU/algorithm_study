import pandas as pd
import numpy as np

def most_corr(prices):
    """
    stock prices
    link : https://www.testdome.com/questions/python-data-science/stock-prices/84848
    
    :param prices: (pandas.DataFrame) A dataframe containing each ticker's 
                    daily closing prices.
    :returns: (container of strings) A container, containing the two tickers that 
                are the most highly (linearly) correlated by daily percentage change.
    """
    # Calculate daily percentage changes
    # pct_change는 한 객체 내에서 행과 행의 차이를 현재값과의 백분율로 출력하는 메서드
    # DataFrame.pct_change(periods=1, fill_method='pad', limit=None, freq=None, kwargs)
    daily_returns = prices.pct_change()

    # Compute the correlation matrix
    # corr메서드는 각 열 간의 상관 계수를 반환하는 메서드
    # DataFrame.corr(method='pearson', min_periods=1)
    corr_matrix = daily_returns.corr()

    # Flatten the upper triangle of the correlation matrix to a list of tuples (excluding diagonal)
    #corr_matrix2=[]
    #for i in range(len(corr_matrix)):
    #    for j in range(i+1, len(corr_matrix)):
    #        corr_matrix2.append((corr_matrix.index[i], corr_matrix.columns[j], corr_matrix.iloc[i,j]))  
    corr_pairs = [(corr_matrix.index[i], corr_matrix.columns[j], corr_matrix.iloc[i, j])
                    for i in range(len(corr_matrix)) for j in range(i + 1, len(corr_matrix))]

    # Find the pair with the highest correlation
    most_corr_pair = max(corr_pairs, key=lambda x: x[2])

    # Return the tickers as a set
    return (most_corr_pair[0], most_corr_pair[1])

#For example, the code below should print: ('FB', 'MSFT')
print(most_corr(pd.DataFrame.from_dict({
    'GOOG' : [
        742.66, 738.40, 738.22, 741.16,
        739.98, 747.28, 746.22, 741.80,
        745.33, 741.29, 742.83, 750.50
    ],
    'FB' : [
        108.40, 107.92, 109.64, 112.22,
        109.57, 113.82, 114.03, 112.24,
        114.68, 112.92, 113.28, 115.40
    ],
    'MSFT' : [
        55.40, 54.63, 54.98, 55.88,
        54.12, 59.16, 58.14, 55.97,
        61.20, 57.14, 56.62, 59.25
    ],
    'AAPL' : [
        106.00, 104.66, 104.87, 105.69,
        104.22, 110.16, 109.84, 108.86,
        110.14, 107.66, 108.08, 109.90
    ]
})))