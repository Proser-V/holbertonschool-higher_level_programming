-- A script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending).

USE hbtn_0c_0;

SELECT city, AVG(value) as avg_temp
FROM temperatures
WHERE month IN (7, 8)
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
