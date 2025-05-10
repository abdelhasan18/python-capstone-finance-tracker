# python-capstone-finance-tracker
Capstone Project for Cognizant GenAI Externship

Features:
  Robust program with constructive error handling
  Combats case insensivity in inputs
  Color coded outputs
  Navigatable menus that do not cramp user's screen

How to use:
  On start-uo, four menu items pop up. You may type in 1-4 to select any of the menu items.
  Appropriate verification occurs and the user will know exactly what they need to change if an issue arises.

  1. Add Expenses
       Expenses should be added by inputing a single line in the form "category, amount, description".
       Error messages for incompatible type (non numeric amount value) or insufficient/surplus comma seperated items are implemented.
       A green success message will output and you can continue to add expenses.
       Typing "back" will exit the while loop and send you back to the main menu.
  2. View Expenses
       You may input any number of category names in a comma seperated list.
       All entered category names will result in an attempt to return the expenses of that category.
       Unsuccessful attempts will not cease the execution of the rest of the input.
       To return all expenses, you may just press enter immediately at the prompt.
       Typing "back" will exit the while loop and send you back to the main menu.
  3. View Summary (very similar to viewing expenses)
       You may input any number of category names in a comma seperated list.
       All entered category names will result in an attempt to return the summary of that category.
       Unsuccessful attempts will not cease the execution of the rest of the input.
       To return all summaries, you may just press enter immediately at the prompt.
       Typing "back" will exit the while loop and send you back to the main menu.
  4. Exit Program
       Ceases the program entirely, if you need to execute the program again you must run it like normal.

Concepts Used:
  Loops were used to iterate through all categories in the functionality of 2 and 3, as well as allowing for continuous inputs.
  String functions made input parsing trivial, as well as allowing for ANSI color code escapes for a prettier environment.
  Dictionary object was used for its ability to allow you to search for registered keys within the object, a list of tuples allows
    us to infinitely append more expense tuples with a key entry.
  Functions were used to make the match-case blocks less clunky and thus more readable.
  Try-except blocks lets us safely cast inputs and catch any predictable, yet undefinable inputs (such as any random string combination).

All concepts were blended together to make this project run smoothly.
