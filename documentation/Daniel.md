# Daniel Pfurner

> - [Github](https://github.com/dpfurners)
> - [Discord](https://discord.gg/user/GozZzer#1245)
> - [Mail](mailto:dpfurner@tsn.at)

## Daily-Work
#### 31.12.2022
    Setting up the basic structure of the Project
    Creating the first version of the documentation

#### 05.01.2023
    Changing the system to an asyncronous system Initializing the Database Interface (not really used yet)
    Initializing basic LogicBase and define models (games, users)
    Setting up basic logic connections

#### 06.01.2023
    FInd out that async is not working as expected, because pygame is synchronous and I was not able to find a way to make it work
    Changing the system to a synchronous system -> Game Logic basically done (no win condition defined yet) No GUI yet
    
#### 09.01.2023
    Laptop cable was broken and Laptop was not working anymore, so I comitted the code to github to store it
    I also added a GUI by myself (for testing) and comitted that to github (not expected)

#### 10.01.2023
    Defining the first Blue-Print for Leon (username_input) -> Welcome Screen

#### 16.01.2023
    Creating GameDisplay GUI Blue-Print -> using the defined functions in the logic

#### 22.01.2023
    Updating the GameLogic according to the updated GUI (new arguments in some functions, ...)
    squares in GameDisplay is now an dict instead of a list -> get the rect in a different way

#### 27.01.2023
    Check if a field is empty or not -> if not, you can select the piece
                                     -> if yes, you can place the piece there if a piece is already selected
    Piece is only moved when the field it should go to is pressed two times
    Adding Win Condition -> show_check added to the GameDisplay to display the checked piece and wich piece is checking it
    Another Blue-Print for Leon (end_screen) -> End Screen
    Abillity to play again (against the same player/another player) when clicking on a button on the end screen 
    Error: One Player is not getting the board the other Send
        Why is this Error happening?
            The pickled version of the board is getting bigger and bigger every move,
            It got up to 1MB of data to transfer every 1/60 seconds (60FPS)
        Solution: Client gets a new board where there is just the fen of the other player

#### 28.01.2023
    Checking when the other player wants to play again and only then the player can play again
    When no decision is made, waiting for an decision

#### 30.01.2023
    Fixing the order the pieces are displayed on the board
    Change Move Sound to a better one -> Thomas uploaded a better one
    Fixing some mistakes at the login screen
    Fixing last errors, Making code more readable, Displaying right win text, Remove debugging print statements
    Add requirements.txt to tell a user what he needs to install to run the game

### 31.01.2023
    Finishing the documentation -> adding the daily work (according to the commits)
    Adding funcions that should be implemented in the future (not sure if these implementations will be done)
    Writing a short description of the project (README.md)
    Writing about how the whole project was for me (Solution)
    Finishing the project

## Functions that should be implemented
 - [ ] Starting to search for another player when you want a revenge and the other doesn't want to play again
 - [ ] Actually using the Database Interface (currently just adding a new user to the database every time the game starts) and not changing any data
 - [ ] Adding a lobby overview where you can see all the hosts that are currently searching for a game


## Solution

#### What I learned
* It is sometimes difficult to work with partners, because you have to communicate with them and you have to make sure that you both understand what you are doing
* It is not so hard to make a game with pygame, even when having multiple Logics
* Errors are sometimes hard to find, because you don't know where they are coming from -> Debugging is important
* It is important to have a good structure in your project, so you can find things easily

#### What I would do differently
* Work alone, because it is easier to work alone (and the timetable is easier when you just have to consider your own time)
* Make a better time plan, to get done with the project before the deadline
* Make a clear separation between the work tasks of the team partners

#### What I would do the same
* First create a core (Base) to build your application on
* Create a good structure in your project
* Create Blueprints for your partner to exactly define what he has to do, what arguments are passed and what is returned
* Committing your code to github, and writing useful commit messages

## Conclusion

#### What I liked
    I Liked it that i was able to work on a project, even if it was hard sometimes (team partners, time plan, ...)
    I also liked it that I was able to create a game with pygame, even if it was not the best game ever (but it was fun to play)

#### Some Thoughts
    Working with a group is fine, because you can separate the task into smaller tasks and you can work on them at the same time.
    On the other side it can be difficult if there is no strict plan who has to do what and when.
    
    Another Thougth is that even if the game is playable, I see so many things to improve (database, structure, ...)
    When we got the project I was very excited to work on it, but since it was during the christmas holidays, 
    there were so many other things to do and I started to work on the project later and later. 

## Questions I asked myself

#### Should the Game be asynchronous?
    Basically No, but to test out new parts of python Programming I thought that I 
    want to use async/await to learn new things.

#### Why is it not necessary for the game to be asynchronous?
    The game is very simple, just sending one message after each other to the host 
    and getting a response if the message was accepted. 
    
    If the game would be more advanced and needs a huge amount of simultaneous messages
    to/from the server you should consider using asynchronous programming.

#### Why does async not work for us?
    I am not able to find out/understand how it works with the pygame loop and so ...
