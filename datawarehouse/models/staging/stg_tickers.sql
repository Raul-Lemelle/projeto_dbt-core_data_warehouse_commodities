with source as (
    select
        "Date",
        "Close",
        "tck"
    from {{ source ('database00', 'tickers') }}
),

renamed as (
    select
        cast("Date" as date) as data,
        "Close" as valor_fechamento,
        "tck" as ticker
    from source
)

select * from renamed