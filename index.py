
# Given an array of intergers, find the sum of its elements

# pseudo
# 1. define the array
# 2.create a variable
# 3 use for loop to iterate through

array = [2,5,10 ,7]
sum = 0

for i in array:
    sum += i

print(sum)    


# Julia conducted a days of learning SQL contest. The start date of the contest was March 01, 2016
# and the end date was March 15, 2016.
# Write a query to print total number of unique hackers who made at least submission each day
# (starting on the first day of the contest), and
# find the hacker_id and name of the hacker who made maximum number of submissions each day.
# If more than one such hacker has a maximum number of submissions, print the lowest hacker_id. 
# The query should print this information for each day of the contest, sorted by the date.



# PSEUDO
# 1 create submission table with ID, name , submission attempts
# 2 find the hacker with one submission attempt
# 3 find one with max. number of submissions attempt per day
# 4 if those with max. number tie , select the lowest hackerID




SELECT
submission_date AS day,
COUNT(DISTINCT hacker_id) AS unique_hackers,(
  
    SELECT hacker_id
    FROM submissions
    WHERE submission_date = day
    GROUP BY hacker_id
    ORDER BY COUNT(*) DESC, hacker_id ASC
    LIMIT 1
  ) AS hacker_id,(

    SELECT name
    FROM hackers
    WHERE hacker_id = (
      SELECT hacker_id
      FROM submissions
      WHERE submission_date = day
      GROUP BY hacker_id
      ORDER BY COUNT(*) DESC, hacker_id ASC
      LIMIT 1
    )
  ) AS hacker_name

# FROM submissions
# WHERE submission_date BETWEEN '2016-03-01' AND '2016-03-15'
# GROUP BY submission_date
# ORDER BY submission_date ASC;






































