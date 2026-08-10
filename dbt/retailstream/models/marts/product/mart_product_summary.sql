SELECT

    p.product_key,
    p.product_id,
    p.product_name,
    p.category,
    p.sub_category,
    p.brand,

    COUNT(DISTINCT s.order_id) AS total_orders,

    SUM(s.quantity) AS quantity_sold,

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

    p.product_key,
    p.product_id,
    p.product_name,
    p.category,
    p.sub_category,
    p.brand