# import
import os
import pandas as pd

from sqlalchemy import create_engine
from dotenv import load_dotenv

import yfinance as yf

# import env variable
load_dotenv()

periodo = "5d"
intervalo = "1d"
tickers = ["XOM", "NEE", "DUK", "GE", "TSLA", "XLE", "ICLN"]

DB_HOST = os.getenv('DB_HOST_PROD')
DB_PORT = os.getenv('DB_PORT_PROD')
DB_NAME = os.getenv('DB_NAME_PROD')
DB_USER = os.getenv('DB_USER_PROD')
DB_PASS = os.getenv('DB_PASS_PROD')
DB_SCHEMA = os.getenv('DB_SCHEMA_PROD')

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL)

# get content YFinance
def buscar_dados_tickers(tickers: list, periodo: str =  periodo, intervalo: str = intervalo) -> pd.DataFrame:
    ticker = yf.Ticker(tickers)
    dados = ticker.history(period=periodo, interval=intervalo)[['Close']]
    dados['tck'] = tickers
    return dados 

# grouped content
def buscar_todos_dados_tickers(tickers: list) -> pd.DataFrame:
    todos_dados = []
    for ticker in tickers:
        dados = buscar_dados_tickers(ticker)
        todos_dados.append(dados)
    return pd.concat(todos_dados)

# save on database
def save_postgres(df, schema='public'):
    df.to_sql('tickers', engine, if_exists='replace', index=True, index_label='Date', schema=schema)


if __name__ == "__main__":
    dados_grouped = buscar_todos_dados_tickers(tickers)
    save_postgres(dados_grouped, schema='public')