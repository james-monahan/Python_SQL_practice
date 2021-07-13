--Find the lowest order cost of each customer.
--Output the customer id along with the first name and the lowest order price.

SELECT DISTINCT(t.cust_id), c.first_name, MIN(t.order_total) as min_order
FROM
(SELECT cust_id, id, SUM(order_cost) AS order_total
FROM orders
GROUP BY cust_id, id) t 
JOIN customers AS c
ON t.cust_id = c.id
GROUP BY t.cust_id, c.first_name



