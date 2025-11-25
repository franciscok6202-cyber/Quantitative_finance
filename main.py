import numpy as np
from modules.financials_functions import portfolio_volatility, portfolio_returns, VaR


if __name__ == "__main__":
    #datos del portfolio
    tickers = ["IEF", "SPTL", "TLT", "VGLT"]
    start = "2023-01-01"
    end = "2024-12-31"

    #descargar retornos portfolio
    df = portfolio_returns(tickers=tickers, start=start, end=end)
    print(df.head(5))
    
    #calculo volatilidad
    vector_w = np.array([1/len(tickers)] * len(tickers))
    sigma = portfolio_volatility(df,vector_w)
    print(sigma)

    #value at risk
    confidence= 0.05
    var= VaR(sigma= sigma, confidence= confidence)
    print(var)