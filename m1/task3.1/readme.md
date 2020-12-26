##### DevOps_online_Lviv_2020Q42021Q1
# TASK 2.2

### Module 3 Database Administration

## PART 1

This time I worked with databases. Exactly with the MySQL database. First, I installed the *mysql server* on my VB Linux machine. 

![image](./images/MySQL_Installed.png)

I decided to create a base for a vehicle workshop. I named it shop.

![image](./images/DB_shop.png)

This a base contain 3 tables - client, car, work.

![image](./images/DB_Tables2.png)

Then I made a few entries in these tables and execute SELECT operator with : *WHERE*, *GROUP BY* and *ORDER BY*

- [*WHERE*](./images/select_WHERE.png)
- [*GROUP BY* ](./images/select_GROUP_BY.png)
- [*ORDER BY*](./images/ORDER_BY.png)
- [*MODIFY*](./images/MODIFY.png)
- [*DELETE*](./images/DELETE.png)

Next step I created a new users ([*admin*](./images/created_admin.png), [*user*](./images/created_user.png)) with different privileges and made different actions with tables.

With *admin* I successfully tried to add data to the table *car* and see changes. Next I wanted to change the data type for one of the columns in this table. Access *denied*. 

![image](./images/admin_denied.png)

Initially, I only give the *user* permission to SELECT, INSERT, DELETE and UPDATE for table *car*.

![image](./images/user_car.png)
![image](./images/user_car_insert.png)

Then I only granted access to view the contents of the table *client*.

![image](./images/user_chang_priv.png)
![image](./images/user_client_insert_denied.png)

As a result, I got a database *shop*.

![image](./images/shop_tables.png)

With such content:

![image](./images/select_Tabeles.png)

___

## PART 2

I created a backup from the current database *shop.sql*.

![image](./images/mysqldump.png)

I deleted the table *work*,

![image](./images/drop_work.png)

and recovered DB from backup with a command *< mysql -u root -p shop < shop.sql >*

![image](./images/restored_work.png)

I created DB on the AWS RDS service.

![image](./images/AWS-RDS_created.png)

I transfered my local database to RDS AWS, connected to it and make *SELECT*.

![image](./images/AWS-RDS_restored.png)

![image](./images/AWS-RDS_tables.png)

Than I created the dump of database from AWS RDS.

![image](./images/AWS-RDS_dump.png)

___

## PART 3

I created and entered data into an Amazon DynamoDB table.

![image](./images/DynamoDB.png)

Queried an Amazon DynamoDB table using Query

![image](./images/DynamoDB_query.png)

and Scan

![image](./images/DynamoDB_scan.png)




#### Thanks!
