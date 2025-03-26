# Game of Thrones Great Houses

This document contains a table listing major noble houses from the world of *Game of Thrones*, along with their mottos, seats, and sigils.

## Houses Overview

| Domain | House ID | House Name | Motto | Seat | Sigil |
|--------|---------|------------|--------------------------------|---------------|------------------------------------------------|
| The North | 100 | Stark | Winter is Coming | Winterfell | A grey direwolf running across an ice-white field |
| The Riverlands | 200 | Tully | Family, Duty, Honor | Riverrun | A silver trout leaping across red and blue striped field |
| The Westerlands | 300 | Lannister | Hear Me Roar | Casterly Rock | A golden lion on a crimson field |
| The Stormlands & Seven Kingdoms | 400 | Baratheon | Ours is the Fury | Storm's End | A crowned black stag on a gold field |
| | 500 | Targaryen | Fire and Blood | King's Landing | A red three-headed dragon on a black field |
| The Iron Islands | 600 | Greyjoy | We Do Not Sow | Pyke | A golden kraken on a black field |
| The Reach | 700 | Tyrell | Growing Strong | Highgarden | A golden rose on a green field |
| The Vale | 800 | Arryn | As High as Honor | The Eyrie | A white falcon and crescent moon on a blue field |
| Dorne | 900 | Martell | Unbowed, Unbent, Unbroken | Sunspear | A red sun pierced by a golden spear |
| Allegiance to House Stark | 1000 | Bolton | Our Blades are Sharp | The Dreadfort | A red flayed man on a pink field |
| Allegiance to House Tully | 1100 | Frey | | The Twins | A pair of blue towers, connected by a blue bridge on a field of silver-grey |
| Allegiance to House Martell | 1200 | Dayne | | Starfall | A sword and a falling star on a lavender background |
| Allegiance to House Stark | 1300 | Mormont | Here We Stand | Bear Island | A black bear in a green wood |

## Valyrian Steel & Notable Weapons

| House ID | Material | Name | Value | Value Currency |
|----------|------------|--------------|-------|---------------|
| 500 | Valyrian steel | Blackfyre | 3000 | Gold Dragon |
| 300 | Valyrian steel | Brightroar | 4500 | Gold Dragon |
| 500 | Valyrian steel | Dark Sister | 3000 | Gold Dragon |
| 100 | Unknown | Needle | 25 | Gold Dragon |
| 1200 | Meteorite | Dawn | 100 | Gold Dragon |
| 400 | Unknown | Heateater | 50 | Gold Dragon |
| 100 | Valyrian steel | Ice | 5000 | Gold Dragon |
| 1300 | Valyrian steel | Longclaw | 3000 | Gold Dragon |

## Query-Based Questions

1. **Which houses possess a named sword with a value of at least 5000 Gold Dragons?**
```sql
select t1.house_name,t2.name from gothouses t1 join gotnamed_swords t2 on t1.house_id=t2.house_id where t2.value>=5000
```

2. **What are the names of the swords that belong to houses with weapons valued at 5000 Gold Dragons or more?**
```sql
select t1.house_name,t1.name from (SELECT x1.house_name,x2.name from gothouses x1 join gotnamed_swords x2 on x1.house_id=x2.house_id where x2.value>=5000) t1 
```

3. **Which houses own at least one named sword valued at 5000 Gold Dragons or more?**
```sql
select house_name from gothouses where house_id IN(select house_id from gotnamed_swords where value>=5000)
```



