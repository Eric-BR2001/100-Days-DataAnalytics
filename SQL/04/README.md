# Game of Thrones Data Queries

This repository contains tables related to battles, characters, and creatures from the *Game of Thrones* universe. Below, you will find the tables with their respective columns and some SQL queries to extract relevant information.

## Battles in Game of Thrones

| Name | Year | Battle Number | Attacker King | Defender King | Attacker 1 | Attacker 2 | Attacker 3 | Attacker 4 | Defender 1 | Defender 2 | Defender 3 | Defender 4 | Attacker Outcome | Battle Type | Major Death | Major Capture | Attacker Size | Defender Size | Attacker Commander | Defender Commander | Summer | Location | Region | Note |
|------|------|---------------|---------------|---------------|------------|------------|------------|------------|------------|------------|------------|------------|-----------------|-------------|-------------|--------------|--------------|--------------|----------------|----------------|---------|----------|--------|------|
| Battle of the Golden Tooth | 298 | 1 | Joffrey/Tommen Baratheon | Robb Stark | Lannister |  |  |  | Tully |  |  |  | win | pitched battle | true | false | 15000 | 4000 | Jaime Lannister | Clement Piper, Vance | true | Golden Tooth | The Westerlands |  |
| Battle at the Mummer's Ford | 298 | 2 | Joffrey/Tommen Baratheon | Robb Stark | Lannister |  |  |  | Baratheon |  |  |  | win | ambush | true | false |  | 120 | Gregor Clegane | Beric Dondarrion | true | Mummer's Ford | The Riverlands |  |
| Battle of Riverrun | 298 | 3 | Joffrey/Tommen Baratheon | Robb Stark | Lannister |  |  |  | Tully |  |  |  | win | pitched battle | false | true | 15000 | 10000 | Jaime Lannister, Andros Brax | Edmure Tully, Tytos Blackwood | true | Riverrun | The Riverlands |  |
| Battle of the Green Fork | 298 | 4 | Robb Stark | Joffrey/Tommen Baratheon | Stark |  |  |  | Lannister |  |  |  | loss | pitched battle | true | true | 18000 | 20000 | Roose Bolton, Wylis Manderly, Medger Cerwyn, Harrion Karstark, Halys Hornwood | Tywin Lannister, Gregor Clegane, Kevan Lannister, Addam Marbrand | true | Green Fork | The Riverlands |  |
| Battle of the Whispering Wood | 298 | 5 | Robb Stark | Joffrey/Tommen Baratheon | Stark | Tully |  |  | Lannister |  |  |  | win | ambush | true | true | 1875 | 6000 | Robb Stark, Brynden Tully | Jaime Lannister | true | Whispering Wood | The Riverlands |  |

## Characters in Game of Thrones

| Birth Year | Character Name | Gender | House ID | Person ID |
|------------|---------------|--------|----------|-----------|
| 263 | Eddard Stark | M | 100 | 1 |
| 283 | Robb Stark | M | 100 | 2 |
| 286 | Sansa Stark | F | 100 | 3 |
| 291 | Tommen Baratheon | M | 400 | 32 |
|  | Stannis Baratheon | M | 400 | 33 |
|  | Renly Baratheon | M | 400 | 34 |
|  | Gendry | M | 400 | 35 |
|  | Barra | F | 400 | 36 |
|  | Edric Storm | M | 400 | 37 |
| 259 | Rhaegar Targaryen | M | 500 | 41 |
| 284 | Daenerys Targaryen | F | 500 | 44 |
|  | Viserys Targaryen | M | 500 | 45 |
| 198 | Maester Aemon | M | 500 | 46 |

## Animals in Game of Thrones

| Coloring | Gender | Name | Owner Person ID | Species | Weight | Weight Unit |
|----------|--------|------|----------------|---------|--------|-------------|
| grey | M | Grey Wind | 2 | direwolf | 400 | kg |
| brown, grey | F | Lady | 3 | direwolf | 350 | kg |
| brown, grey | F | Nymeria | 4 | direwolf | 300 | kg |
| black | M | Shaggydog | 6 | direwolf | 375 | kg |
| brown, grey | M | Summer | 5 | direwolf | 350 | kg |
| white | M | Ghost | 108 | direwolf | 400 | kg |
| black, red | M | Drogon | 44 | dragon | 28000 | kg |
| cream, gold, red, orange | M | Viserion | 44 | dragon | 25000 | kg |
| green, bronze, yellow, orange | M | Rhaegal | 44 | dragon | 23000 | kg |
| green, black | null | Unnamed Manticore |  | manticore | 2 | kg |
| black | null | Unnamed Shadowcat |  | shadowcat | 82 | kg |

## SQL Queries

1. **List all characters whose names end with "Stark" (alphabetical order)**
   ```sql
   SELECT character_name FROM got_characters WHERE character_name LIKE "%Stark" ORDER BY 1;
   ```

2. **Find characters whose names start with "Jon"**
   ```sql
   SELECT character_name FROM got_characters WHERE character_name LIKE "Jon%";
   ```

3. **Find characters whose names contain "ae"**
   ```sql
   SELECT character_name FROM got_characters WHERE character_name LIKE "%ae%";
   ```

4. **List creatures whose names contain "grey"**
   ```sql
   SELECT * FROM gotcreatures WHERE name LIKE "%grey%";
   ```

5. **List battles where House Baratheon attacked and the defending king was Stark**
   ```sql
   SELECT * FROM got_battles WHERE attacker_1 LIKE "%Baratheon%" AND defender_king LIKE "%Stark%";
   ```

6. **List battles that occurred in summer where the attacking king was Joffrey**
   ```sql
   SELECT * FROM got_battles WHERE summer=TRUE AND attacker_king LIKE "%Joffrey%";
   ```

   ---