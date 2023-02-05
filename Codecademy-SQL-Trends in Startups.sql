-- 1 --
SELECT *
FROM startups;

-- 2 --
SELECT count(name)
FROM startups;

-- 3 --
select sum(valuation)
from startups;

-- 4 --
select name,max(raised)
from startups;

-- 5 --
select name,max(raised)
from startups
where stage='Seed';

-- 6 --
select name, min(founded)
from startups;

-- 7 --
select avg(valuation)
from startups;

-- 8 --
select category,avg(valuation)
from startups
group by category;

-- 9 --
select category,round(avg(valuation),2)
from startups
group by category;

-- 10 --
select category,round(avg(valuation),2)
from startups
group by category
order by 2 desc;

-- 11 --
select category,count(name)
from startups
group by category;

-- 12 --
select category,count(name)
from startups
group by category
having count(name) > 3;

-- 13 --
select  location, avg(employees)
from startups
group by location; 

-- 14 --
select  location, avg(employees)
from startups
group by location
having avg(employees) > 500; 