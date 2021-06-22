/*You’re given a table of Uber rides that contains the mileage and the purpose for the business expense.  
You’re asked to find business purposes that generate the most miles driven for passengers that use 
Uber for their business transportation. Find the top 3 business purpose categories by total mileage.*/

WITH business AS
(select * from my_uber_drives
WHERE category = 'Business')

SELECT DISTINCT(purpose), SUM(miles) OVER(PARTITION BY purpose)
FROM business
WHERE purpose IS NOT NULL
ORDER BY 2 DESC LIMIT 3
