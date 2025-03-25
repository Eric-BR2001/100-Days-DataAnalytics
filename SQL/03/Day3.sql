SELECT title,rating,ratinglevel FROM netflix where ratinglevel like "Parent%" limit 100;
Select CONCAT(name,' ', year),year,battle_number from got_battles
select CONCAT(host_name,' - ',host_neighbourhood),LENGTH(host_name),LENGTH(CONCAT(host_name,' - ',host_neighbourhood)) from boston_airbnb_listings limit 10;
select CONCAT(host_name,' - ',host_neighbourhood),LENGTH(host_name),LENGTH(CONCAT(host_name,' - ',host_neighbourhood)),LEFT(host_name,5),RIGHT(host_name,5) from boston_airbnb_listings limit 10