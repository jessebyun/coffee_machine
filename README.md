<h2>Coffee Machine</h2>

This program will simulate the function of a coffee machine. The coffee machine dispenses 3 caffeinated beverages (esspress, latte, cappuccino). Once the user chooses a beverage, the coffee machine will ask for payment in coins (quarters, dimes, nickels, and pennies). The machine will count the money received and return change back to the user. There is only a set amount of resources inside the machine to make the beverages. Once an ingredient has run out, it will notify user that there is not enough of that ingredient left in the machine to make the chosen beverage. 

The machine can enter service mode by typing "report". Report will print out how much resources of each ingredient is left inside the machine. It will also print out how much money it has collected. The machine can be turned off by typing "off". 

First I wrote the program using procedural code. Then I converted the program using Object Oriented Programming. I made 3 Classes (menu, coffee_maker, money_machine). The menu class contains the attributes of each beverage such as the ingredients it takes to make the beverage and the cost. This class has a method to return all names of available menu items to the user and another method to find a drink from the menu for to be utilized by another class object. There is a money_machine class that has a method to process and count coins received and another method to determine if user has paid enough to buy a drink. The coffee_maker class will hold the default amount of resources, have a method to print out a report, a method to make a drink and deduct from avail resources. 


<img src="https://i.imgur.com/UCyyFIF.png" alt="image" />
