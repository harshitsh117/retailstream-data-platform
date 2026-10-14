SELECT

    d.year,
    d.quarter,
    d.month,
    d.month_name,

    COUNT(DISTINCT s.order_id) AS total_orders,

    SUM(s.quantity) AS total_quantity,

    ROUND(
        SUM(s.discount_amount)::numeric,
        2
    ) AS total_discount,

    ROUND(
        SUM(s.tax_amount)::numeric,
        2
    ) AS total_tax,

    ROUND(
        SUM(s.grand_total)
        /
        NULLIF(COUNT(DISTINCT s.order_id), 0)
    ) AS total_revenue,

    ROUND(
        AVG(s.grand_total)::numeric,
        2
    ) AS average_order_value

FROM {{ ref('stg_sales') }} s

JOIN {{ ref('stg_date') }} d
    ON s.date_key = d.date_key

GROUP BY

    d.year,
    d.quarter,
    d.month,
    d.month_name

ORDER BY

    d.year,
    d.month