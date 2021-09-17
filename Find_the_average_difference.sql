/*Find the average number of days between the booking and check-in dates for AirBnB hosts. 
Order the results based on the average number of days in descending order.
avg_days_between_booking_and_checkin DESC*/

SELECT id_host, AVG(days_between) 
FROM
(select id_host, ts_booking_at, ds_checkin,
ds_checkin::DATE-ts_booking_at::DATE days_between
from airbnb_contacts
WHERE ts_booking_at IS NOT NULL) t
GROUP BY id_host
ORDER BY 2 DESC
