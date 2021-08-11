/*Count the subpopulations across datasets. Assume that a subpopulation is a group of users 
sharing a common interest (ex: Basketball, Food). Output the percentage of overlapping 
interests for two posters along with those poster's IDs. Calculate the percentage from 
the number of poster's interests. The poster column in the dataset refers to the user 
that posted the comment.*/


WITH base AS (SELECT DISTINCT poster, keyword
FROM
  (SELECT *, 
  UNNEST(STRING_TO_ARRAY(BTRIM(post_keywords, '[##]'), ',')) keyword
  FROM facebook_posts) t
  WHERE keyword != 'spam'
  ORDER BY 1)

SELECT poster1, MAX(poster2) poster2, SUM(count2)::DECIMAL/SUM(count1) ratio
FROM
  (SELECT b1.poster poster1, b2.poster poster2, 
  COUNT(b1.keyword) count1, COUNT(b2.keyword) count2
  FROM base b1
  LEFT JOIN base b2
  ON b1.keyword = b2.keyword AND b1.poster != b2.poster
  GROUP BY b1.poster, b2.poster) t
GROUP BY poster1


