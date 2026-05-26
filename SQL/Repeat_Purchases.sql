/* CREATE VIEW repeat_purchases AS
SELECT
    c.customer_unique_id,
    t.product_category_name_english AS category,
    COUNT(*) AS purchase_count
FROM orders o

LEFT JOIN customers c
ON o.customer_id = c.customer_id

LEFT JOIN items i
ON o.order_id = i.order_id

LEFT JOIN products p
ON i.product_id = p.product_id

LEFT JOIN translations t
ON p.product_category_name = t.product_category_name

WHERE o.order_status = 'delivered'

GROUP BY
c.customer_unique_id,
t.product_category_name_english

HAVING COUNT(*) > 1; */

SELECT 
repeat_purchases.category,
SUM(purchase_count) AS purchase_counted
FROM repeat_purchases
WHERE purchase_count IS NOT NULL
GROUP BY repeat_purchases.category
ORDER BY purchase_counted DESC
LIMIT 10;