SELECT
p.product_category_name,
SUM(pay.payment_value) AS revenue
FROM orders o

LEFT JOIN order_items oi ON o.order_id = i.order_id
LEFT JOIN products p ON i.product_id = p.product_id
LEFT JOIN payments pay ON o.order_id = pay.order_id

GROUP BY p.product_category_name
ORDER BY revenue DESC;

SELECT * FROM revenue_by_category
WHERE category IS NOT NULL
ORDER BY revenue DESC;