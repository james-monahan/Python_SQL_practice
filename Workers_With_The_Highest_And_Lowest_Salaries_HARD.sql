/*Find the titles of workers that earn the highest and the lowest salaries. 
Output the highest paid titles in one column and lowest paid titles in another column.*/

WITH best AS
(SELECT worker_title AS best_paid
FROM worker w
JOIN title t
ON w.worker_id = t.worker_ref_id
WHERE w.salary = (select MAX(salary) from worker)),

worst AS
(SELECT worker_title AS worst_paid
FROM worker w
JOIN title t
ON w.worker_id = t.worker_ref_id
WHERE w.salary = (select MIN(salary) from worker))

SELECT *
FROM best w1
FULL OUTER JOIN worst w2
ON w1.best_paid = w2.worst_paid
