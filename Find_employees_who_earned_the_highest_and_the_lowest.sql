/*Find employees who earned the highest and the lowest total pay without any benefits.
Output the employee name along with the total pay.
Order records based on the total pay in descending order.*/

WITH base AS
(SELECT employeename, totalpay,
RANK() OVER(ORDER BY totalpay) ranking
FROM sf_public_salaries
WHERE benefits IS NULL or benefits=0)

SELECT employeename, totalpay 
FROM base
WHERE ranking IN 
    ((SELECT MAX(ranking) FROM base), (SELECT MIN(ranking) FROM base)) 
ORDER BY 2 DESC;




