SELECT

    d.year,
    d.month,
    d.month_name,

    COUNT(DISTINCT s.order_id) AS total_orders,

    SUM(s.quantity) AS total_quantity,

    ROUND(
        SUM(s.grand_total)::numeric,
        2
    ) AS total_revenue

FROM {{ ref('stg_sales') }} s

JOIN {{ ref('stg_date') }} d
    ON s.date_key = d.date_key

GROUP BY

    d.year,
    d.month,
    d.month_name

ORDER BY

    d.year,
    d.month