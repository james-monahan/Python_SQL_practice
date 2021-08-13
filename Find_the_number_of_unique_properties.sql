--Find how many the number of different property types in the dataset.  

SELECT 
DISTINCT(UNNEST(string_to_array(BTRIM(filter_room_types, ','), ',')))
FROM airbnb_searches
