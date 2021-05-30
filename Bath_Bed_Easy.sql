/*Find the average number of bathrooms and bedrooms 
for each city’s property types. Output the result 
along with the city name and the property type.*/

select city, property_type,
AVG(bathrooms), AVG(bedrooms)
from airbnb_search_details
GROUP BY city, property_type;
