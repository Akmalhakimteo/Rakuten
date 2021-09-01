
# Rakuten Assignment August 2021


## Requirements 

Python3

## TASK 1

| Activity | Completed     |
| :-------- | :------- |
| Get duration in Minutes and volume in MB from UsedAmount| Yes | 
| Normalize BNUM to have format without 00 / + | Yes | 
| Calculate Charge for each record | Yes | 
| Get total duration per day | Yes | 
| Get duration in Minutes and volume in MB from UsedAmount| Yes | 


### How to run
```bash
  cd rakuten-app/src/Input
  python3 fileParser.py
```

## TASK 2 

### Get Minimum distance between 2 points

*NOTE*: The graphs were initialized based on the assignment given.

```http
  GET /getMinDistance
```
| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `fromQuery`      | `string` | **Required**. Position of starting node |
| `toQuery`      | `string` | **Required**. Position of ending node |


  ### How to run
```bash
  cd rakuten-app/src/Input
  python3 task2.py
  curl -X GET http://127.0.0.1:5000/getMinDistance?fromQuery=A&toQuery=B
```

*NOTE*: You may change the fromQuery and toQuery in the query request to desired nodes.


    