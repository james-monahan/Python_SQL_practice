/*COMPANY X employees are trying to find the cheapest flights to upcoming conferences. 
When people fly long distances, a direct city-to-city flight is often more expensive than taking 
two flights with a stop in a hub city. Travelers might save even more money by breaking the trip 
into three flights with two stops. But for the purposes of this challenge, let's assume that no 
one is willing to stop three times! You have a table with individual airport-to-airport flights, 
which contains the following columns:

   • id - the unique ID of the flight;
   • origin - the origin city of the current flight;
   • destination - the destination city of the current flight;
   • cost - the cost of current flight.

Your task is to produce a trips table that lists all the cheapest possible trips that can be done in two or fewer stops. 
This table should have the columns origin, destination, stops (indicating the number of stops in current trip), 
and total_cost. If two trips cost the same but have a different number of stops, include the one with the fewest stops. 
Sort the output table by origin, then by destination. The cities are all represented by an abbreviation composed of three 
uppercase English letters. Note: A flight from SFO to JFK is considered to be different than a flight from JFK to SFO.

Example of the output:
origin | destination | stops | total_cost 
DFW | JFK | 0 | 200*/


WITH connected_flights1 AS (SELECT df1.origin, df2.destination, 
1 AS connections, df1.cost+df2.cost AS cost
FROM da_flights df1
JOIN da_flights df2
ON df1.destination = df2.origin),

connected_flights2 AS (SELECT df1.origin, df2.destination, 
2 AS connections, df1.cost+df2.cost AS cost
FROM da_flights df1
JOIN connected_flights1 df2
ON df1.destination = df2.origin)

SELECT origin,destination, connections, cost
FROM
(SELECT *,
RANK() OVER(PARTITION BY origin, destination ORDER BY cost) pricing
FROM
(SELECT origin, destination, 0 AS connections, cost
FROM da_flights
UNION
SELECT *
FROM connected_flights1
UNION
SELECT *
FROM connected_flights2) t) j
WHERE pricing = 1
ORDER BY 1,2

