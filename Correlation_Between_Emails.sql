/*There are two tables with user activities. The 'google_gmail_emails` table 
contains information about emails being sent to users. Each row in that 
table represents a message with an unique identifier in the `id` field. The 
`google_fit_location` table contains user activity logs from the Google Fit app. 
Find the correlation between the number of emails received and the total 
exercise per day. The total exercise per day is calculated by counting the 
number of user sessions per day.*/

WITH messages_per_day AS 
(SELECT to_user, day, COUNT(*) AS messages
FROM google_gmail_emails
GROUP BY to_user, day),

exercise_per_day AS
(SELECT user_id, day, COUNT(DISTINCT(session_id)) AS sessions
FROM google_fit_location
GROUP BY user_id, day)

SELECT
CORR(mpd.messages, epd.sessions)
FROM messages_per_day AS mpd
JOIN exercise_per_day AS epd
ON mpd.to_user = epd.user_id
AND mpd.day = epd.day


