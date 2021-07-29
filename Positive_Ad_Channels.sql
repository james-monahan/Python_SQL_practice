--Find the advertising channel with the smallest maximum yearly spending that still brings in more than 1500 customers each year.

SELECT advertising_channel
FROM uber_advertising
GROUP BY advertising_channel
HAVING MIN(customers_acquired) >= 1500
ORDER BY MAX(money_spent)
LIMIT 1
