/* CREATE VIEW purchase_volume_monthly AS
SELECT
DATE_TRUNC('month', order_purchase_timestamp) AS month,
COUNT(order_id) AS order_count
FROM orders
WHERE order_status = 'delivered'
GROUP BY month
ORDER BY month;*/

SELECT * FROM purchase_volume_monthly
WHERE month IS NOT NULL
ORDER BY month DESC;