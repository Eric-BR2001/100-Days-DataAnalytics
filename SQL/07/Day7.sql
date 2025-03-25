select jobtitle,ROUND(AVG(totalpay),2) from san_francisco_salaries group by jobtitle;
select jobtitle,ROUND(SUM(totalpay),2) SUM from san_francisco_salaries group by jobtitle;
select employeename,MAX(totalpay),MIN(totalpay) from san_francisco_salaries group by jobtitle;
select jobtitle,MAX(totalpay),MIN(totalpay) from san_francisco_salaries group by jobtitle;
select year,CONCAT(year,' - ',AVG(totalpaybenefits)) from san_francisco_salaries group by year;
select COUNT(id),jobtitle from san_francisco_salaries group by jobtitle;
select id,employeename,jobtitle,CAST(basepay as DECIMAL),CAST(overtimepay as DECIMAL),CAST(otherpay as DECIMAL),benefits,totalpay,totalpaybenefits,year,notes,agency,status from san_francisco_salaries;