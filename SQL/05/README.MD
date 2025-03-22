# Social Media Engagement Data

This repository contains a dataset of social media posts, their corresponding messages, and user engagement metrics such as the number of likes and angry reactions.

## Table Overview

| Name | Message | Likes Count | Angry Count |
|------|---------|------------|------------|
| World's 'saddest' polar bear kept in China mall for selfies | No words. | 28071 | 38492 |
| Two men 'surfing' on a turtle may face fine | 'Surfed a tortoise...' photo sparks outrage in Australia. | 13841 | 27517 |
| Dog found buried alive with nail in head | 'I have never known anything so horrifying and inexplicably cruel.' | 9523 | 21827 |
| NULL | Parents in remote parts of Malawi are sending their daughters to be sexually initiated by local men - called 'hyenas' - when they reach puberty. Meet Eric, he’s proud of his role as a 'hyena'. Learn more: [BBC Article](http://bbc.in/2ab9vLz) | 5572 | 15133 |
| 'The day I killed my rapist' | 'I killed my rapist when he came back for my sister.' [#ShameOnline](http://bbc.in/2e2YnzH) | 39664 | 14822 |
| People hunting 'canned' lions in South Africa | They call them 'canned lions' - bred in captivity to be hunted. We've been given this exclusive footage from South Africa. [More Info](http://bbc.in/2cKFl2S) | 7661 | 14139 |
| Yulin dog meat festival begins in China | 10,000 dogs and cats are expected to be killed and eaten. | 8828 | 13316 |
| Trump courts the terminally ill vote | At a Nevada rally Donald J. Trump has urged the terminally ill to 'hang on' until Election Day and vote for him. [Read More](http://bbc.in/2dyB5k7) | 13452 | 13165 |
| Black US doctor's anger at Delta Air Lines 'snub' | The black doctor was told 'oh no sweetie, put your hand down, we are looking for actual physicians' on the Delta flight. | 13359 | 11763 |
| Florida policeman shoots autistic man's unarmed black therapist | 'As long as I've got my hands up, they're not going to shoot me... Wow, was I wrong.' | 16088 | 11464 |

## "What are the top 30 social media posts (from cbs_news_131459315949_2 and bbc_228735667216_2) with more than 1,000 likes, ordered by the highest number of angry reactions?"

### Query 

SELECT name, message, likes_count, angry_count FROM (SELECT name, message, likes_count, angry_count FROM cbs_news_131459315949_2 WHERE likes_count > 1000 UNION SELECT name, message, likes_count, angry_count FROM bbc_228735667216_2 WHERE likes_count > 1000) t1 ORDER BY angry_count DESC LIMIT 30;

# Campaign Performance Data

This repository contains a dataset of digital advertising campaign performance, including various metrics such as impressions, clicks, spend, and revenue.

## Table Overview

| Campaign ID | Timestamp         | Date       | Inventory Type | Ad Type  | Available Impressions | Matched Queries | Impressions | Clicks | Spend  | Fee  | Revenue  | CTR   | CPM  | CPC  |
|------------|------------------|------------|----------------|---------|----------------------|----------------|------------|--------|--------|-----|---------|------|------|-----|
| 121001     | 2014-09-03-10     | 2014-09-03 | Format1        | Inter217 | 4229052              | 2719650        | 2652364    | 5800   | 4054.6 | 0.33 | 2716.58 | 0.0022 | 1.53  | 0.7  |
| 121002     | 2014-09-03-13     | 2014-09-03 | Format2        | Inter217 | 22425309             | 12316305       | 11949634   | 23280  | 19739.63 | 0.23 | 15199.52 | 0.0019 | 1.65  | 0.85 |
| 121003     | 2014-09-03-06     | 2014-09-03 | Format2        | Inter218 | 3990076              | 2491170        | 2407854    | 3719   | 4880.0 | 0.33 | 3270.0  | 0.0015 | 2.0   | 1.0  |
| 121004     | 2014-09-02-19     | 2014-09-02 | Format3        | Inter217 | 3810657              | 1421610        | 1315055    | 8809   | 1985.86 | 0.35 | 1290.81 | 0.0067 | 1.51  | 0.23 |

### Query 

select campaign_id,timestamp,date,inventorytype,ad_type,available_impressions,matched_queries,impressions,clicks,spend,fee,revenue,ctr,cpm,cpc from ads_data_revenue_1 UNION  select campaign_id,timestamp,date,inventorytype,ad_type,available_impressions,matched_queries,impressions,clicks,spend,fee,revenue,ctr,cpm,cpc from ads_data_revenue_2 ORDER BY campaign_id limit 50

# Product Cost Data

## Table Overview

| Product Code | Company | Type | Cost |
|-------------|---------|------|------|
| 10043 | Hyundai Group | Auto | 29.92 |
| 10215 | GM Group | Auto | 38.38 |
| 11054 | UNSW | Edu | 39.07 |
| 12022 | Southern Cross | Edu | 26.08 |
| 12554 | Phillips | Prod | 23.02 |
| 13860 | Renault Group | Auto | 36.07 |
| 14472 | Inchcape | Foods | 28.00 |
| 14726 | Tata Group | Auto | 37.20 |

### Query

SELECT  t1.product_code, t1.company, t1.type, t2.cost FROM products_type t1 JOIN products_cost t2 on t1.product_code=t2.product_code