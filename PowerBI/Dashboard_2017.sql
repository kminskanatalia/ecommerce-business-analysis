/*CREATE VIEW analytics_orders_2017 AS
SELECT

    o.order_id,
    o.customer_id,
    DATE(o.order_purchase_timestamp) AS purchase_date,
    DATE_TRUNC('month', o.order_purchase_timestamp) AS purchase_month,

    c.customer_city AS city,

    i.product_id,
    p.product_category_name AS category,

    i.order_item_id AS item_number,

    (i.price + i.freight_value) AS item_revenue,

	EXTRACT(MONTH FROM o.order_purchase_timestamp) AS order_month,
	EXTRACT(YEAR FROM o.order_purchase_timestamp) AS order_year

FROM orders o

JOIN items i
    ON o.order_id = i.order_id

JOIN customers c
    ON o.customer_id = c.customer_id

JOIN products p
    ON i.product_id = p.product_id

WHERE EXTRACT(YEAR FROM o.order_purchase_timestamp) = 2017;*/

/*SELECT DISTINCT order_month
FROM analytics_orders_2017
ORDER BY order_month DESC;*/