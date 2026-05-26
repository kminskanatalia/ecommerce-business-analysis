/*CREATE VIEW avg_revenue_city AS
SELECT 
c.customer_city,
AVG(p.payment_value) AS average_city_revenue,
COUNT(DISTINCT o.order_id) AS total_orders
FROM orders o

LEFT JOIN customers c ON o.customer_id = c.customer_id
LEFT JOIN payments p ON o.order_id = p.order_id

WHERE o.order_status = 'delivered'

GROUP BY c.customer_city
HAVING COUNT(DISTINCT o.order_id) > 50
ORDER BY average_city_revenue DESC;*/

SELECT *
FROM avg_revenue_city
ORDER BY average_city_revenue DESC
LIMIT 10;