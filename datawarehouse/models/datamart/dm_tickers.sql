WITH ticker_data AS (
    SELECT
        ticker,
        ROUND(AVG(valor_fechamento)::numeric, 2) AS media_fechamento_USD
    FROM
        {{ ref('stg_tickers') }}
    GROUP BY
        ticker
)

SELECT * FROM ticker_data