import os
import pandas as pd
import streamlit as st
from sqlalchemy import create_engine
from sqlalchemy.exc import ProgrammingError
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Obter as variáveis do arquivo .env
DB_HOST = os.getenv('DB_HOST_PROD')
DB_PORT = os.getenv('DB_PORT_PROD')
DB_NAME = os.getenv('DB_NAME_PROD')
DB_USER = os.getenv('DB_USER_PROD')
DB_PASS = os.getenv('DB_PASS_PROD')
DB_SCHEMA = os.getenv('DB_SCHEMA_PROD')

# Criar a URL de conexão do banco de dados
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Criar o engine de conexão com o banco de dados
engine = create_engine(DATABASE_URL)

def get_data():
    query = f"""
    SELECT
        *
    FROM
        public.dm_tickers
    """
    df = pd.read_sql(query, engine)
    return df

# Configurar a página do Streamlit
st.set_page_config(page_title='Tickers Energia', layout='wide')

# Título do Dashboard
st.title('Média do Valor de Fechamento dos últimos 5 dias - Tickers Energia')

# Descrição
st.write("""
### Empresas:
- **Exxon Mobil (XOM)**: Uma das maiores empresas de petróleo e gás.
- **NextEra Energy (NEE)**: Uma grande empresa de energia renovável.
- **Duke Energy (DUK)**: Uma empresa de eletricidade e gás natural.
- **General Electric (GE)**: Fabrica turbinas e outros equipamentos de geração de energia.
- **Tesla (TSLA)**: Envolvida na fabricação de baterias e armazenamento de energia.
    
### ETFs:
- **Energy Select Sector SPDR Fund (XLE)**: Um ETF que rastreia o setor de energia do S&P 500.
- **iShares Global Clean Energy ETF (ICLN)**: Um ETF que rastreia empresas globais no setor de energia limpa.
""")

# Obter os dados
df = get_data()

st.dataframe(df)