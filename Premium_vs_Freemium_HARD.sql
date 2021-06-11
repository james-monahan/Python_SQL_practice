/*Find the total number of downloads for paying and non-paying users by date. 
Include only records where non-paying customers have more downloads than paying customers. 
The output should be sorted by earliest date first and contain 3 columns date, non-paying downloads, paying downloads.*/

WITH base_q AS
(select date, downloads, paying_customer
from ms_download_facts AS mdf
JOIN ms_user_dimension AS mud
ON mdf.user_id = mud.user_id
JOIN ms_acc_dimension AS mad
ON mud.acc_id = mad.acc_id),

paying AS
(SELECT date AS d1, SUM(downloads) AS paying
FROM base_q
WHERE paying_customer = 'yes'
GROUP BY date, paying_customer),

nonpaying AS
(SELECT date AS d2, SUM(downloads) AS non_paying
FROM base_q
WHERE paying_customer = 'no'
GROUP BY date, paying_customer)

SELECT d2 AS date, non_paying, paying
FROM nonpaying np
JOIN paying p
ON np.d2 = p.d1
WHERE np.non_paying > p.paying
ORDER BY 1
