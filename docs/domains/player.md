# Player (user) #

## **Who is a Player?** ## 

A player is an entity that can play the game and report the result of the match. 

## **What responsibilities / capabilities does a Player have?** ##

1- Can play the game

2- Can report the result of the match

3- Can be ranked

4- Can join a tournament

5- Can have a profile

6- Can have achievements


## **What can't a Player do? (invariants)** ##

1- Can't create a tournament

2- Can't match with a specific player

3- Can't put money on the line 

4- Can't play without authentication


## **When is a Player invalid?** ##

1- When the player is banned

2- When the player is not verified

## **What data belongs to Player?** ##

1- ID

2- Profile with name, avatar, etc...

3- Financial data for prize money

4- Game data like rank, achievements, etc...

5- Contact info like email, phone number, etc...

## **What data doesn't?** ## 

1- Public leaderboard data like rank, score, etc...

2- Site statistics like number of players, number of matches, etc...

## **Who cares about it ?** ##

1- Site manager

2- Player itself

3- Observer

## **How is it related to other entities?** ##

1- Player can have many matches.

2- Player can have many tournaments.

3- Player can have many achievements.

4- Player can have one profile.

5- Player can have one financial data.

6- Player can't have multiple matches at the same time.

7- Player can't cheat.(redflag system)