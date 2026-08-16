### Variants:
1- A search can find only one player for the match.

2- A player cannot have two simultaneous match.

3- A player can only be matched with another player if and only if they are not involved in another match (in any state other than ENDED).

4- A player cannot be matched with themselves.

5- A player can only make a matchmaking call if they have ACTIVE status inside the system.

6- A player can be matched for a premium search if they have enough credit.

7- A player can only be matched or make the search if they are not playing/involved in a tournament (even if their game is over they have to wait till the tournament is concluded).

8- A player can only initiate a search request if they don't already have one.

9- There is a time limit of 15 minutes for finding an opponent (otherwise the search times out).

10- A faker can only be matched if the last 3 matches were real players.

11- A search cannot be cancelled (at least due to the queue runners for now).



### UseCases: 

1- Check if search is doable (check availability and viability of the player)

4- Initiate the search

### Events:

1- SearchInitiated

2- OpponentFound (matched)

3- SearchExpired

### Dependencies

1- Matchmaking is the owner of the search entity

2- Matchmaking does not need Match entity and only omits the event to let the Match know it can now create the match record.

3- Matchmaking depends on:

Identity -> Player state

Credits -> Eligibility

Tournament & Match -> Availability


### Failure possibilities

1- a<->b and b<->c get matched simultaneously.

2- Redis lock dies.

3- Queue workers die.

4- Potential mixed matches in high concurrency.

### Architecture details and challenges:

Controller is going to get the request and do some preflight validation using either VO or simple DTO,

and then it passes the data to the use-case(s) to start the matchmaking process.

I see Search as a dependent entity because it does not exist without matchmaking.

We are going to need policies (domain services) in order to be able to match two players exp: 1- CanMatch 2- IsPlayerAvailable 3- IsPlayerInAnActiveTournament etc..

I believe only one use-case suffices and that would be MatchTwoPlayers, 

I also have changed the directory structure from search being a separate domain to search being a dependent entity of the matchmaking domain. 

### Uncertainties

1- How to effectively prevent concurrency issues and lock the process properly so that it does not match one player in two separate matches .


### Here is the diagram of responsibilities : 

Identity
    Player

↓

Matchmaking
    Search
    Policies
    Pairing

↓

OpponentMatched

↓

Matches
    Match
    Reports
    Confirmation

↓

MatchCreated

↓

Chat
    Conversation

↓

Notifications