# My Project

## CSV Data

Here’s the data from my CSV file:

| coloring                     | gender | name              | owner_person_id | species   | weight | weight_unit |
|------------------------------|--------|-------------------|-----------------|-----------|--------|-------------|
| grey                         | M      | Grey Wind         | 2               | direwolf  | 400    | kg          |
| brown grey                   | F      | Lady              | 3               | direwolf  | 350    | kg          |
| brown grey                   | F      | Nymeria           | 4               | direwolf  | 300    | kg          |
| black                        | M      | Shaggydog         | 6               | direwolf  | 375    | kg          |
| brown grey                   | M      | Summer            | 5               | direwolf  | 350    | kg          |
| white                        | M      | Ghost             | 108             | direwolf  | 400    | kg          |
| black red                    | M      | Drogon            | 44              | dragon    | 28000  | kg          |
| cream gold red orange        | M      | Viserion          | 44              | dragon    | 25000  | kg          |
| green bronze yellow orange   | M      | Rhaegal           | 44              | dragon    | 23000  | kg          |
| green black                  | null   | Unnamed Manticore | null            | manticore | 2      | kg          |
| black                        | null   | Unnamed Shadowcat | null            | shadowcat | 82     | kg          |


# SQL Queries and Their Corresponding Questions

Below are several SQL queries that I made myself based on the provided table data.

---

# What are the unique species of creatures in the gotcreatures table?

## 1. Unique Species (Using DISTINCT)

**Query:**

SELECT DISTINCT(species) FROM gotcreatures;

# What are the first 10 rows of data in the gothouses table by name?
## 2. First 10 Rows of Data from gotcreatures by name

**Query:**

SELECT * FROM gotcreatures LIMIT 10 order by name;

# What are the names and genders of the first 10 characters in the gotcreatures table?
## 3. Names and Genders of the First 10 Characters

**Query:**

SELECT name, gender FROM gotcreatures LIMIT 10 order by name;

---