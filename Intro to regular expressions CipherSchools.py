
string matching:
Like, REGEXP(skip)

##LIKE:
% - any no. of characters
_ - match a single char

select * From [Customers]
where ContactName like "%n%"

select * From [Customers]
where ContactName like "M__d"

Ques:
select all the phone nos ending with 5 in supplier's table?
Select * from [Suppliers]
ehere phone like '%5'

##REGEXP: more flexibility
select * From [Customers]
where ContactName like "%n%"

select * From [Customers]
where ContactName REGEXP "m"

- by default - any no of char before and after

^ - beginning
$ - ending
| - or / pipe
[] - matches any one is the brackets

select * From Customers
where city regexp "M"

select * From Customers
where city regexp "d$"

select * From Customers
where city regexp "^M" and city regexp "d$"

select * From Customers
where city regexp "^M|d$"

select * From Customers
where city regexp "a|b|c"

select * From Customers
where city regexp "^a|mac|d$"

select * From Customers
where city regexp "[abc]i"
