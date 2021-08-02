/*Find the top 2 highest paid City employees for each job title. 
Output the job title along with the corresponding highest and second-highest paid employees.*/

WITH base_table AS 
(SELECT employeename,jobtitle, totalpaybenefits,
ROW_NUMBER() OVER(PARTITION BY jobtitle ORDER BY totalpaybenefits DESC) pay_rank
FROM sf_public_salaries)

SELECT t.jobtitle, 
t.employeename AS highest, j.employeename AS second_highest
FROM
  (SELECT * 
  FROM base_table
  WHERE pay_rank = 1) t
  LEFT JOIN
  (SELECT * 
  FROM base_table
  WHERE pay_rank = 2) j
  ON t.jobtitle = j.jobtitle


