/*Whole Foods would like to segment their store brands into Low, Medium, and High segmentation. 
The segments are to be based on a customer's average basket size which is defined as (total sales / count of transactions), per customer.

The segment thresholds are as follows:
- If average basket size is more than $30, then Segment is “High”.
- If average basket size is between $20 and $30, then Segment is “Medium”.
- If average basket size is less than $20, then Segment is “Low”.

Summarize the number of unique customers, the total number of transactions, total sales, and average basket size, grouped by store brand and segment for 2017.

Your output should include the brand, segment, number of customers, total transactions, total sales, and average basket size*/


WITH base_table AS (SELECT *,
CASE
    WHEN basket > 30 THEN 'High'
    WHEN basket < 20 THEN 'Low'
    ELSE 'Medium'
    END AS segment
FROM
(SELECT customer_id, store_brand,
SUM(sales) total_sales, COUNT(DISTINCT(transaction_id)) transactions,
SUM(sales)/COUNT(DISTINCT(transaction_id)) basket
FROM
(SELECT wt.*, ws.store_brand
FROM wfm_transactions wt
JOIN wfm_stores ws
ON wt.store_id = ws.store_id
WHERE EXTRACT(YEAR FROM wt.transaction_date)=2017) t 
GROUP BY customer_id, store_brand) j)

SELECT store_brand, segment, 
COUNT(DISTINCT customer_id) as customers, SUM(transactions) as trans,
SUM(total_sales) total_sales, SUM(total_sales)/SUM(transactions) basket
FROM base_table
GROUP BY store_brand, segment
