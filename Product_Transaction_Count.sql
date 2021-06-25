/*Find the number of transactions that occurred for each product. 
Output the product name along with the corresponding number of 
transactions and order records by the product id in ascending order. 
You can ignore products without transactions.*/

SELECT asid.product_name, t.n_trans
FROM
(select COUNT(transaction_id) AS n_trans, product_id
from excel_sql_transaction_data
GROUP BY product_id) t
JOIN excel_sql_inventory_data AS asid
ON t.product_id = asid.product_id
ORDER BY t.product_id
