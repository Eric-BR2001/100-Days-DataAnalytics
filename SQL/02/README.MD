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
## What are the creatures with weight between 300 and 400 kg?

### Query:

SELECT name, weight, weight_unit FROM gotcreatures WHERE weight BETWEEN 300 AND 400;


## What are the creatures with names alphabetically between "Ghost" and "Lady"?

### Query:

SELECT name, weight, weight_unit FROM gotcreatures WHERE name BETWEEN "Ghost" AND "Lady";


## Which creatures weigh exactly 350 kg or 400 kg?

### Query:

SELECT name, weight, weight_unit FROM gotcreatures WHERE weight IN (400, 350);

## What are the creatures with names alphabetically between "Ghost" and "Lady" that weigh 300 kg or 400 kg?

### Query:

SELECT name, weight, weight_unit FROM gotcreatures WHERE name BETWEEN "Ghost" AND "Lady" AND weight IN (300, 400);


