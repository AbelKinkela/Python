I learned that this design pattern can be used to overcome challenges In
memory and processing power when we have repetitive tasks such as generating units objects in a game.

In the game example supose we are dealing with 2 types of units to be generated depending on the game level

Knights units of level 1 are the same and we are generating many of them and same goes for Archer

Everytime a unit object is created we need to go to the db and load its properties.
If we are generating many of them, which is the point of the game, then the memory and processing 
resources will be huge.

With the prototype pattern we build an abstract class Protoptype with a clone method that every child class
must implement. the goal of this clone method is to return a deepcopy of the unit.

Knight class implementing the prototype implements the clone method which return a deepcopy of a knight unit instance
Archer class also does the same.

since knights and archers are generated in a places called barracks. The Barracks class instanciates all the 
relavant knights(of level 1 and 2) and all relavant Archers(of level 1 and 2) and keeps them in a datastructure(list or dict,etc)

Now everytime we want a unit generated we can get a deepcopy of that unit from our list. 
no more need to open a file, db connection,etc.
