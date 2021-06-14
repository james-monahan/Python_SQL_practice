/*Our goal is to develop a naïve forecast for a new metric called "distance per dollar" 
defined as the (distance_to_travel/monetary_cost) in our dataset and measure its accuracy.
To develop this forecast, aggregate 'distance per dollar' values at a monthly level.
The next step is to populate the forecasted value for each month. 
This can be achieved simply by getting the previous month's value in a separate column. 
Now, we have actual and forecasted values. This is your naïve forecast. 
Let’s evaluate our model by calculating an error matrix called root mean squared error (RMSE).*/


WITH q1 AS
(SELECT yr_month, SUM(distance_to_travel)/SUM(monetary_cost) AS avg_dpd
FROM
(select DATE_TRUNC('month', request_date) AS yr_month, 
distance_to_travel,	monetary_cost
from uber_request_logs) t
GROUP BY yr_month)


SELECT ROUND(SQRT(AVG(POWER(avg_dpd - prior,2)))::DECIMAL,2) AS RMSE
FROM
(SELECT *,
LAG(avg_dpd) OVER(ORDER BY yr_month) AS prior
FROM q1 ) j
