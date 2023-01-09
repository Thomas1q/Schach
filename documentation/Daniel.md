# Daniel Pfurner

> - [Github](https://github.com/dpfurners)
> - [Discord](https://discord.gg/user/GozZzer#1245)
> - [Mail](mailto:dpfurner@tsn.at)

## Change-Log

## Daily-Work
#### 31.12.2022
- 14:15 Setting up the project (Filestructure, database, documentation)
- 14:24 Adding links to my documentation
- 14:58 Simple setup of the Database Interface

#### 05.01.2023
- 10:26 Changing the Database Interface to an asynchronous Database Interface so that we can create an asynchronous Game
- 10:33 Describing why I choose asynchronous programming
- 10:45 Created LogicBase Class
- 10:47 User/Enemy Data should be stored in the logic too
- 11:09 Asynchronous Event Handling in python
- 11:21 Finished basic Logic Setup (Not working jet but ability to select host/client is given)
- 11:57 Define Models matching a database row (games, users)
- 13:39 Create LogicHost and resolve User-Data of the self user

#### 06.01.2023
- 02:12 Finishing the Logic (not checking if someone won)

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