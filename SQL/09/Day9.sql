select t1.house_name,t2.name from gothouses t1 join gotnamed_swords t2 on t1.house_id=t2.house_id where t2.value>=5000;
select t1.house_name,t1.name from (SELECT x1.house_name,x2.name from gothouses x1 join gotnamed_swords x2 on x1.house_id=x2.house_id where x2.value>=5000) t1; 
select house_name from gothouses where house_id IN(select house_id from gotnamed_swords where value>=5000);