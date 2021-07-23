/*From users who had their first session as a viewer, how many streamer sessions have they had? 
Return the user id and number of sessions in descending order. In case there are users with 
the same number of sessions, order them by ascending user id.*/

SELECT user_id, SUM(sessions) streaming_session
FROM
(SELECT *,
CASE WHEN session_type = 'viewer' THEN 0 ELSE 1 END sessions
FROM twitch_sessions
WHERE user_id IN
    (SELECT user_id
    FROM
        (SELECT *, 
        RANK() OVER(PARTITION BY user_id ORDER BY session_start) first_session
        FROM twitch_sessions) t
        WHERE first_session = 1
        AND session_type = 'viewer')) j
GROUP BY user_id
ORDER BY 1
