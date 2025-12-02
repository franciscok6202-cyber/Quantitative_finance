import pandas as pd 
import numpy as np 
import scipy.stats as stats 
from .backend import market_prices

def portfolio_volatility(df:pd.DataFrame,vector_w:np.array) -> float:

    """
    Calculo de la volatilidad de un portafolio
    de invrsiones
    df data fram
    """ 
    # matriz var-covar
    m_cov = df.cov()
    #vector traspuesto
    vector_w_t = np.array([vector_w])

    #varianza
    vector_cov = np.dot(m_cov,vector_w)
    varianza = np.dot(vector_w_t,vector_cov)

    #volatilidad

    vol= np.sqrt(varianza)

    return vol [0]

def portfolio_returns(
        tickers: list,
        start: str,
        end: str
        ) -> pd.DataFrame:
        """
        descarga desde la base de datos los precios de los intrumentos indicados en el rango de fechas
        ticker(list):lista de intrumentos nemos que componen el portfolio 
        start (str)
        fechas de inicio de precios
        end(str)
        fecha de terminos de precios
        return(pd.dataframe): dataframe de retornos diarios
        """
        #descargar precios
        df= market_prices(
            start_date=start,
            end_date=end,
            tickers=tickers
            )
        #pivot retornos
        # pivot table
        df_pivot = pd.pivot_table(
        data=df, 
        index="FECHA",
        columns="TICKER", 
        values="PRECIO_CIERRE", 
        aggfunc="max"
        )   
        df_pivot = df_pivot.pct_change().dropna()
        return df_pivot

def VaR(sigma:float, confidence:float) -> float:
        """
        calculo de value at risk al nivel de confianza indicado. Con supuesto de media cero
        """

        #estadistico  z al nivel de confianza
        z_score = stats.norm.ppf(confidence)
        
        #var

        var = z_score * sigma
        return var
    
    