# Leetcode

### [1294. ](https://leetcode-cn.com/problems/weather-type-in-each-country/) [Weather Type in Each Country](https://leetcode-cn.com/problems/weather-type-in-each-country)   

Difficulty: **简单**

Table: `Countries`

```text
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| country_id    | int     |
| country_name  | varchar |
+---------------+---------+
country_id is the primary key for this table.
Each row of this table contains the ID and the name of one country.
```

Table: `Weather`

```text
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| country_id    | int     |
| weather_state | varchar |
| day           | date    |
+---------------+---------+
(country_id, day) is the primary key for this table.
Each row of this table indicates the weather state in a country for one day.
```

Write an SQL query to find the type of weather in each country for November 2019.

The type of weather is **Cold** if the average `weather_state` is less than or equal 15, **Hot** if the average `weather_state` is greater than or equal 25 and **Warm** otherwise.

Return result table in any order.

The query result format is in the following example:

```text
Countries table:
+------------+--------------+
| country_id | country_name |
+------------+--------------+
| 2          | USA          |
| 3          | Australia    |
| 7          | Peru         |
| 5          | China        |
| 8          | Morocco      |
| 9          | Spain        |
+------------+--------------+
Weather table:
+------------+---------------+------------+
| country_id | weather_state | day        |
+------------+---------------+------------+
| 2          | 15            | 2019-11-01 |
| 2          | 12            | 2019-10-28 |
| 2          | 12            | 2019-10-27 |
| 3          | -2            | 2019-11-10 |
| 3          | 0             | 2019-11-11 |
| 3          | 3             | 2019-11-12 |
| 5          | 16            | 2019-11-07 |
| 5          | 18            | 2019-11-09 |
| 5          | 21            | 2019-11-23 |
| 7          | 25            | 2019-11-28 |
| 7          | 22            | 2019-12-01 |
| 7          | 20            | 2019-12-02 |
| 8          | 25            | 2019-11-05 |
| 8          | 27            | 2019-11-15 |
| 8          | 31            | 2019-11-25 |
| 9          | 7             | 2019-10-23 |
| 9          | 3             | 2019-12-23 |
+------------+---------------+------------+
Result table:
+--------------+--------------+
| country_name | weather_type |
+--------------+--------------+
| USA          | Cold         |
| Austraila    | Cold         |
| Peru         | Hot          |
| China        | Warm         |
| Morocco      | Hot          |
+--------------+--------------+
Average weather_state in USA in November is (15) / 1 = 15 so weather type is Cold.
Average weather_state in Austraila in November is (-2 + 0 + 3) / 3 = 0.333 so weather type is Cold.
Average weather_state in Peru in November is (25) / 1 = 25 so weather type is Hot.
Average weather_state in China in November is (16 + 18 + 21) / 3 = 18.333 so weather type is Warm.
Average weather_state in Morocco in November is (25 + 27 + 31) / 3 = 27.667 so weather type is Hot.
We know nothing about average weather_state in Spain in November so we don't include it in the result table.
```

**Solution**

Language: **MySQL**

```sql
-- # Write your MySQL query statement below
-- SELECT b.country_name, 
--     (CASE WHEN weath_state <=15 THEN "Cold"
--             WHEN weath_state>=25 THEN "Hot"
--             ELSE  "Warm" END) as weather_type 
-- FROM (
-- SELECT country_id, AVG(weather_state) weath_state
-- FROM Weather 
-- WHERE DATE_FORMAT(day, "%Y-%m") = "2019-11"
-- GROUP BY country_id, DATE_FORMAT(day, "%Y-%m")) a JOIN Countries b 
-- ON a. country_id = b.country_id 
-- date_format, date
SELECT country_name, 
    (CASE WHEN AVG(weather_state)<=15 THEN "Cold"
        WHEN AVG(weather_state)>=25 THEN "Hot"
            ELSE "Warm" END) as weather_type
FROM Countries c JOIN Weather w 
ON c.country_id = w.country_id AND YEAR(day) = 2019 AND MONTH(day) = 11
GROUP BY country_name
```



### [1308. ](https://leetcode-cn.com/problems/running-total-for-different-genders/) [Running Total for Different Genders](https://leetcode-cn.com/problems/running-total-for-different-genders)   

Difficulty: **中等**

Table: `Scores`

```text
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| player_name   | varchar |
| gender        | varchar |
| day           | date    |
| score_points  | int     |
+---------------+---------+
(gender, day) is the primary key for this table.
A competition is held between females team and males team.
Each row of this table indicates that a player_name and with gender has scored score_point in someday.
Gender is 'F' if the player is in females team and 'M' if the player is in males team.
```

Write an SQL query to find the total score for each gender at each day.

Order the result table by gender and day

The query result format is in the following example:

```text
Scores table:
+-------------+--------+------------+--------------+
| player_name | gender | day        | score_points |
+-------------+--------+------------+--------------+
| Aron        | F      | 2020-01-01 | 17           |
| Alice       | F      | 2020-01-07 | 23           |
| Bajrang     | M      | 2020-01-07 | 7            |
| Khali       | M      | 2019-12-25 | 11           |
| Slaman      | M      | 2019-12-30 | 13           |
| Joe         | M      | 2019-12-31 | 3            |
| Jose        | M      | 2019-12-18 | 2            |
| Priya       | F      | 2019-12-31 | 23           |
| Priyanka    | F      | 2019-12-30 | 17           |
+-------------+--------+------------+--------------+
Result table:
+--------+------------+-------+
| gender | day        | total |
+--------+------------+-------+
| F      | 2019-12-30 | 17    |
| F      | 2019-12-31 | 40    |
| F      | 2020-01-01 | 57    |
| F      | 2020-01-07 | 80    |
| M      | 2019-12-18 | 2     |
| M      | 2019-12-25 | 13    |
| M      | 2019-12-30 | 26    |
| M      | 2019-12-31 | 29    |
| M      | 2020-01-07 | 36    |
+--------+------------+-------+
For females team:
First day is 2019-12-30, Priyanka scored 17 points and the total score for the team is 17.
Second day is 2019-12-31, Priya scored 23 points and the total score for the team is 40.
Third day is 2020-01-01, Aron scored 17 points and the total score for the team is 57.
Fourth day is 2020-01-07, Alice scored 23 points and the total score for the team is 80.
For males team:
First day is 2019-12-18, Jose scored 2 points and the total score for the team is 2.
Second day is 2019-12-25, Khali scored 11 points and the total score for the team is 13.
Third day is 2019-12-30, Slaman scored 13 points and the total score for the team is 26.
Fourth day is 2019-12-31, Joe scored 3 points and the total score for the team is 29.
Fifth day is 2020-01-07, Bajrang scored 7 points and the total score for the team is 36.
```

**Solution**

Language: **MySQL**

```sql
​-- SELECT s1.gender, s1.day, sum(s2.score_points) total 
-- FROM Scores s1, Scores s2 
-- WHERE s1.gender = s2.gender AND 
--     s1.day >= s2. day
-- GROUP BY s1.gender, s1.day 
-- ORDER BY s1.gender, s1.day

-- window function
SELECT gender,
        day,
        SUM(score_points) OVER (PARTITION BY gender ORDER BY day) total
FROM Scores
```



### [1321. Restaurant Growth](https://leetcode-cn.com/problems/restaurant-growth/)

Difficulty: **中等**

Table: `Customer`

```text
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| customer_id   | int     |
| name          | varchar |
| visited_on    | date    |
| amount        | int     |
+---------------+---------+
(customer_id, visited_on) is the primary key for this table.
This table contains data about customer transactions in a restaurant.
visited_on is the date on which the customer with ID (customer_id) have visited the restaurant.
amount is the total paid by a customer.
```

You are the restaurant owner and you want to analyze a possible expansion \(there will be at least one customer every day\).

Write an SQL query to compute moving average of how much customer paid in a 7 days window \(current day + 6 days before\) .

The query result format is in the following example:

Return result table ordered by visited\_on.

`average_amount`should be **rounded to 2 decimal places**, all dates are in the format \('YYYY-MM-DD'\).

```text
Customer table:
+-------------+--------------+--------------+-------------+
| customer_id | name         | visited_on   | amount      |
+-------------+--------------+--------------+-------------+
| 1           | Jhon         | 2019-01-01   | 100         |
| 2           | Daniel       | 2019-01-02   | 110         |
| 3           | Jade         | 2019-01-03   | 120         |
| 4           | Khaled       | 2019-01-04   | 130         |
| 5           | Winston      | 2019-01-05   | 110         | 
| 6           | Elvis        | 2019-01-06   | 140         | 
| 7           | Anna         | 2019-01-07   | 150         |
| 8           | Maria        | 2019-01-08   | 80          |
| 9           | Jaze         | 2019-01-09   | 110         | 
| 1           | Jhon         | 2019-01-10   | 130         | 
| 3           | Jade         | 2019-01-10   | 150         | 
+-------------+--------------+--------------+-------------+

Result table:
+--------------+--------------+----------------+
| visited_on   | amount       | average_amount |
+--------------+--------------+----------------+
| 2019-01-07   | 860          | 122.86         |
| 2019-01-08   | 840          | 120            |
| 2019-01-09   | 840          | 120            |
| 2019-01-10   | 1000         | 142.86         |
+--------------+--------------+----------------+

1st moving average from 2019-01-01 to 2019-01-07 has an average_amount of (100 + 110 + 120 + 130 + 110 + 140 + 150)/7 = 122.86
2nd moving average from 2019-01-02 to 2019-01-08 has an average_amount of (110 + 120 + 130 + 110 + 140 + 150 + 80)/7 = 120
3rd moving average from 2019-01-03 to 2019-01-09 has an average_amount of (120 + 130 + 110 + 140 + 150 + 80 + 110)/7 = 120
4th moving average from 2019-01-04 to 2019-01-10 has an average_amount of (130 + 110 + 140 + 150 + 80 + 110 + 130 + 150)/7 = 142.86
```

**Solution**

Language: **MySQL**

```sql
​# Write your MySQL query statement below
SELECT c1.visited_on, SUM(c2.amount) amount, ROUND(SUM(c2.amount)/7, 2) average_amount
FROM (
    SELECT DISTINCT visited_on FROM Customer
    WHERE visited_on>=adddate((SELECT min(visited_on) 
                                FROM Customer), interval 6 day)
    ) c1, Customer c2 
WHERE c1.visited_on>= c2.visited_on AND datediff(c1.visited_on, c2.visited_on)<=6
GROUP BY c1.visited_on 
-- HAVING COUNT(c2.visited_on)>=7
ORDER BY c1.visited_on, c2.visited_on;
```

