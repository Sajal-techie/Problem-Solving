-- Write your PostgreSQL query statement below
select p.firstName, p.lastName, a.city, a.state from Person as p left join Address as a on a.personId=p.personId