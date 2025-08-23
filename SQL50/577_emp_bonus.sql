select
a.name as name
b.bonus as bonus
from employee as e
left join 
bonus b
on a.empId = b.empId
where a.bonus < 1000
and b.bonus is null