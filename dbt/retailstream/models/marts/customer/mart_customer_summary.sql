SELECT

    c.customer_key,
    c.customer_id,

    CONCAT(c.first_name, ' ', c.last_name) AS customer_name,

    c.city,
    c.state,
    c.country,

    COUNT(DISTINCT s.order_id) AS total_orders,

    SUM(s.quantity) AS total_quantity,

    ROUND(
        SUM(s.grand_total)::numeric,
        2
    ) AS total_revenue,

    ROUND(
        SUM(s.grand_total)
        /
        NULLIF(COUNT(DISTINCT s.order_id), 0)
    ) AS average_order_value

FROM {{ ref('stg_customer') }} c

JOIN {{ ref('stg_sales') }} s
    ON c.customer_key = s.customer_key

GROUP BY

    c.customer_key,
    c.customer_id,
    c.first_name,
    c.last_name,
    c.city,
    c.state,
    c.country