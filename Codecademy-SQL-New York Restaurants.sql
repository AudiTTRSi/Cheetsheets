--1.step--
SELECT *
FROM nomnom;

--2.step - neighborhood --
select distinct neighborhood
from nomnom;

--3.step --
select distinct cuisine
from nomnom;

--4.step --
select *
from nomnom
where cuisine = 'Chinese';

--5.step --
select *
from nomnom
where review >= 4;

--6.step --
select *
from nomnom
where cuisine='Italian' and price='$$$';

--7.step --
select *
from nomnom
where name like '%meatball%';

--8.step --
select *
from nomnom
where neighborhood in ('Midtown','Downtown','Chinatown');

--9.step --
select *
from nomnom
where health is NULL;

--10.step --
select *
from nomnom
order by review desc
limit 10;

--11.step --
SELECT name,
 CASE
  WHEN review > 4.5 THEN 'Extraordinary'
  WHEN review > 4 THEN 'Excellent'
  WHEN review > 3 THEN 'Good'
  WHEN review > 2 THEN 'Fair'
  ELSE 'Poor'
 END AS 'Review'
FROM nomnom;