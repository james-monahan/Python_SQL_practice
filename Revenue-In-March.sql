select cust_id, SUM(order_quantity*order_cost) AS order_revenue 
from orders
WHERE order_date >= '2019-03-01'
AND order_date < '2019-04-01'
GROUP BY 1
ORDER BY 2 DESC;


-- WHERE DATE_PART('month', order_date) = 3
-- WHERE order_date BETWEEN '2019-03-01' AND '2019-03-31'
