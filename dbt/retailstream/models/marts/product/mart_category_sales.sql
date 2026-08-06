SELECT

    p.category,

    COUNT(DISTINCT s.order_id) AS total_orders,

    SUM(s.quantity) AS total_quantity,

    ROUND(
        SUM(s.grand_total)::numeric,
        2
    ) AS total_revenue,

    ROUND(
        SUM(s.quantity * p.cost_price)::numeric,
        2
    ) AS total_cost,

    ROUND(
        (
            SUM(s.grand_total)
            -
            SUM(s.quantity * p.cost_price)
        )::numeric,
        2
    ) AS total_profit

FROM {{ ref('stg_product') }} p

JOIN {{ ref('stg_sales') }} s
    ON p.product_key = s.product_key

GROUP BY
    p.category