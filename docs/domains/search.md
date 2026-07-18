# Search #

## **What is a Search?** ##

An ability to find a match for a player who asked for it . It has a dynamic matching style which can be tweaked based on the needs. 

## **What responsibilities / capabilities does a Search have?** ##

1- Check if player is eligible for a new match.

2- Check the pool of players.

3- Check other player's availability.

4- Create a match.

5- Update player's status.


## **What can't a Search do? (invariants)** ##

1- Change a match result.

2- Create a tournament.

3- Create a match without a player.

4- Modify player or match data.


## **When is a Search invalid?**

1- When there are two matches for a player at the same time .

2- When there is no player eligible for a match.

3- When there is no player available in the pool.


## **What data belongs to Search?** ##

1- ID

2- Player ID

3- Status (initiated, matched, etc...)

4- Timestamps (created, updated, etc...)

## **What data doesn't?** ## 

1- Match data

2- Tournament data

3- Leaderboard data

## **Who cares about it ?** ##

1- Players

2- Match entity

## **How is it related to other entities?** ##

1- Search can create a match.

2- Search can update &/ check player's status.

