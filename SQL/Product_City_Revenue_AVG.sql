/* CREATE VIEW avg_revenue_by_city AS
SELECT c.customer_city,
AVG(p.payment_value) AS average_city_revenue
FROM orders o

LEFT JOIN customers c ON o.customer_id = c.customer_id
LEFT JOIN payments p ON o.order_id = p.order_id

WHERE o.order_status = 'delivered'
GROUP BY c.customer_city
ORDER BY average_city_revenue DESC; */

SELECT *
FROM avg_revenue_by_city
ORDER BY average_city_revenue DESC
LIMIT 20;