/*Each record in the table is a reported health issue and its classification is categorized by the facility 
type, size, risk score which is found in the pe_description column.

If we limit the table to only include businesses with Cafe, Tea, or Juice in the name, 
which businesses belong to the categories (pe_descriptions) tying for third in overall inspections? 
Output the name of the facilities found in the facility_name column.*/

SELECT facility_name
FROM
  (SELECT *,
  DENSE_RANK() OVER(ORDER BY insp DESC) ranking
  FROM
    (SELECT facility_name, pe_description,
    COUNT(*) OVER (PARTITION BY pe_description) insp
    FROM los_angeles_restaurant_health_inspections
    WHERE LOWER(facility_name) LIKE '%cafe%'
    OR LOWER(facility_name) LIKE '%tea%'
    OR LOWER(facility_name) LIKE '%juice%') t) j
WHERE ranking = 3

