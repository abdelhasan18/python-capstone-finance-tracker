# ansi escape code print modifications, makes interactivity easier for user
def print_red(str):
    print(f'\033[91m{str}\033[0m')
def print_green(str):
    print(f'\033[92m{str}\033[0m')
def print_yellow(str):
    print(f'\033[93m{str}\033[0m')
def input_blue(str):
    return input(f'\033[94m{str}\033[0m')

def add_expense(category, amount, description):
    # string formatting, combats case sensitivity
    cat = str(category).lstrip().rstrip().lower().capitalize()
    des = str(description).lstrip().rstrip().lower().capitalize()

    # tries to cast amount to numeric, handles by returning a status code
    # ERROR 0
    # SUCCESS 1
    try:
        amount = float(amount)
    except:
        print_red('Oops, amount must be a numeric, please try again.\n')
        return 0
    
    # creates array object in dict entry if new category, appends to array if not new
    if cat not in dict:
        dict[cat] = [(des, amount)]
    else:
        dict[cat].append((des, amount))
    return 1

def view_expenses(category):
    # string formatting, combats case sensitivity
    cat = str(category).lstrip().rstrip().lower().capitalize()

    # checks if input is a key in dict, prints output if it is
    if cat not in dict:
        print(f'\033[91mSorry, category \'\033[93m{cat}\033[91m\' was not recognized.\033[0m')
    else:
        print_green(f'Category: \033[93m{cat}')
        for expense in dict[cat]:
            print(f' - {expense[0]}: ${expense[1]}')

def view_summary(category):
    # string formatting, combats case sensitivity
    cat = str(category).lstrip().rstrip().lower().capitalize()

    # checks if input is a key in dict, prints output if it is
    if cat not in dict:
        print(f'\033[91mSorry, category \'\033[93m{cat}\033[91m\' was not recognized.\033[0m')
    else:
        sum = 0
        for expense in dict[cat]:
            sum += expense[1]
        print_yellow(f'{cat}:\033[92m $' + str(round(sum, 0)))
    


print('Hello! Welcome to the Personal Finance Tracker!')
dict = {}
while True:
    # menu items
    print_yellow('What would you like to do?')
    print('1. Add Expense')
    print('2. View Expenses')
    print('3. View Summary')
    print('4. Exit')
    op = input_blue('Option: ')

    # error catching for non-integer menu input
    try:
        op = int(op)
    except:
        print_red('Oops, we were expecting a different input, please try again.\n')
        continue

    # menu input handling
    match op:
        # adding expenses
        case 1:
            print('\nPlease enter your expense in colon seperated string like so:')
            print('"Category, Amount, Description"')
            print('Input \'back\' to access previous menu.')
            while True:
                inp = input_blue('Expense: ')

                # seperates input by delimiter
                args = inp.split(',')

                # handles input based on number of arguments parsed
                if len(args) == 3:
                    if add_expense(*args):
                        print_green('Expense added successfully\n')
                    else:
                        continue
                elif len(args) == 1:
                    # handles 'back' keyword
                    if str(args[0]).lower() == 'back':
                        print()
                        break
                    else:
                        print_red('All sections must be filled out, check for any extra commas.\n')
                else:
                    print_red('All sections must be filled out, check for any extra commas.\n')
            continue

        # viewing expenses
        case 2:
            print('\nPlease input the categories of expense you would like to view in')
            print('a comma separated list, input \'back\' to access previous menu,')
            print('leave blank to view expenses for all categories:')
            while True:
                inp = input_blue('Categories: ')

                # seperates input by delimiter
                args = inp.split(',')

                # handling 'back' keyword
                if str(args[0]).lower() == 'back':
                    print()
                    break
                print()
                if not inp:
                    for cat in dict:
                        view_expenses(cat)
                else:
                    for cat in args:
                        view_expenses(cat)
                print()

        # viewing summary
        case 3:
            print('\nPlease input the category summaries you would like to view in')
            print('a comma separated list, input \'back\' to access previous menu,')
            print('leave blank to view summaries for all categories:')
            while True:
                inp = input_blue('Categories: ')

                # seperates input by delimiter
                args = inp.split(',')

                # handling 'back' keyword
                if str(args[0]).lower() == 'back':
                    print()
                    break

                # both cases below result in robust execution
                print()
                if not inp:
                    for cat in dict:
                        view_summary(cat)
                else:
                    for cat in args:
                        view_summary(cat)
                print()

        # exit
        case 4:
            print_green('\nHave a lovely day!')
            break

        # numeric but non-menu option input handling
        case _:
            print_red('Sorry, this is not a menu option, please try again.\n')
            continue