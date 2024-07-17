# Projeto DBT-Core para Data Warehouse dos principais Tickers do setor de Energia

Este projeto utiliza DBT (Data Build Tool) para gerenciar e transformar dados de um Data Warehouse (DW). O objetivo é criar um pipeline de dados robusto e eficiente que trata e organiza os dados e suas movimentações para análise.

**Cenário:** Queremos a média dos 5 principais tickers do setor de energia dos últimos 5 dias.

**Solução:** [Link do Relatório](https://tickers-energia-5d-avg.streamlit.app/)


## Estrutura do Projeto

```mermaid
graph TD;
    A[Início] --> B[Extrair Dados]
    B --> C[Transformar Dados]
    C --> D[Carregar Dados no PostgreSQL]
    D --> E[Fim]

    subgraph Extrair
        B1[Buscar Dados de cada ticker]
        B2[Adicionar Dados na Lista]
    end

    subgraph Transformar
        C1[Concatenar Todos os Dados]
        C2[Preparar DataFrame]
    end

    subgraph Carregar
        D1[Salvar DataFrame no PostgreSQL]
    end

    B --> B1
    B1 --> B2
    B2 --> C
    C --> C1
    C1 --> C2
    C2 --> D
    D --> D1
```

### 1. Seeds

Os seeds são dados estáticos que são carregados no Data Warehouse a partir de arquivos CSV.

### 2. Models

Os models definem as transformações de dados usando SQL. Eles são divididos em duas camadas principais: staging e datamart.

#### Staging

A camada de staging é responsável por preparar e limpar os dados antes que eles sejam carregados nas tabelas finais de análise.

- **stg_tickers.sql**: Trata e formata os dados dos tickers extraídos da API.

#### Datamart

A camada de datamart é onde os dados finais de análise são armazenados. Eles são baseados nos dados preparados pela camada de staging.

- **dm_tickers.sql**: Integra os dados tratados, criando um modelo de dados final para análise.

### 3. Sources

Os sources são as tabelas ou arquivos de origem dos dados que o DBT utiliza para realizar as transformações.

### 4. Snapshots

Os snapshots são utilizados para manter um histórico de como os dados mudam ao longo do tempo.

## Estrutura de Diretórios

```plaintext
├── models
│   ├── staging
│   │   └── stg_tickers.sql
│   └── datamart
│       └── dm_tickers.sql
├── seeds
├── dbt_project.yml
└── README.md
```

## Executando o Projeto

### Requisitos

- Python 3.7+
- DBT

### Passos para Execução

1. **Clonar o Repositório**:
   ```bash
   git clone <URL-do-Repositório>
   cd <Nome-do-Repositório>
   ```

2. **Instalar o DBT**:
   ```bash
   pip install dbt-core dbt-postgres
   ```

3. **Configurar o DBT**:
   - Configure o arquivo `profiles.yml` para se conectar ao seu Data Warehouse. O arquivo deve estar no diretório `~/.dbt/` ou no diretório especificado pela variável de ambiente `DBT_PROFILES_DIR`.

   Exemplo de `profiles.yml`:
   ```yaml
   databasesales:
     target: dev
     outputs:
       dev:
         type: postgres
         host: <DB_HOST_PROD>
         user: <DB_USER_PROD>
         password: <DB_PASS_PROD>
         port: <DB_PORT_PROD>
         dbname: <DB_NAME_PROD>
         schema: <DB_SCHEMA_PROD>
         threads: 1
   ```

4. **Executar os Seeds do DBT**:
   ```bash
   dbt seed
   ```

5. **Executar as Transformações do DBT**:
   ```bash
   dbt run
   ```

6. **Verificar o Estado do Projeto**:
   ```bash
   dbt test
   ```

## Contribuição

Para contribuir com o projeto, por favor, faça um fork do repositório e envie um pull request com suas alterações.

---

### Descrição dos Models

#### stg_tickers.sql

Este model é responsável por tratar e formatar os dados dos principais tickers do setor de energia extraídos da API. Ele faz a limpeza e transformação necessárias para preparar os dados para o datamart.

#### dm_tickers.sql

Este model integra os dados tratados, criando um modelo de dados final para análise. Ele calcula métricas e agrega os dados para facilitar a análise no dashboard.