"""
ATM interface by Steve Hanlon May 
Create Class in main and message functions in function.py file
"""

import chalk
import string
from main import Account


act = Account


def clear():                        # Clear the screen
    spacer = '\n'
    george = spacer * 50
    print(george)


def prizes(account: act):
    """
    prizes to include with interest to maintain customer base

    :return:
    """

    prize_vault = ['GI Joe with a Kung Fu grip',
                 'bluetooth toaster',
                 'microwavable frisbee',
                 'bottle of Ode to Sweaty Pitts'
                 'brand new pink lamborghini'
                 'Siri: Punk-Pierced Version']


def withdrawal_acc(account: act) -> int:
    """
    ask Savings or Checking
    use string constant to reject anything but integer
    
    :param account: 
    :return: 
    """

    acc_type = input("""Withdrawal money from which account:
    ________________________
    | Type 's' >> SAVINGS  |
    | Type 'c' >> CHECKING |
        """)

    try:
        amount_withd = int(input("How much? "))
    except ValueError:
        clear()
        chalk.red("It must a positive number. Try again!")    # Error for non-integers
        withdrawal_acc(account)

    if acc_type != 's':                 # If Checking account
        account.withdrawal_ch(amount_withd)
        new_b_withd_ch = account.get_funds_ch()
        clear()
        chalk.red(f"The amount of ${amount_withd} has been withdrawn.\nCHECKING BALANCE: ${new_b_withd_ch}.")
    else:                               # If Savings account
        account.withdrawal(amount_withd)
        new_b_withd = account.get_funds()
        clear()
        chalk.red(f"""The amount of ${amount_withd} has been withdrawn.\nSAVINGS BALANCE:  ${new_b_withd}.""")
    print()
    menu_screen(account)


    # except ValueError as e:
    #     print(e.args[0])      # Error for negative integers



def deposit_acc(account: act) -> int:
    """
    ask Savings or Checking
    

    :return: int
    """

    acc_type = input("""Deposit money in which account:
________________________
| Type 's' >> SAVINGS  |
| Type 'c' >> CHECKING |
    """)

    try:
        amount_dep = int(input("How much to deposit? "))
        clear()
    except ValueError:
        print("It must a positive number!")


    if acc_type != 's':
        clear()
        account.deposit_ch(amount_dep)
        new_chkb_dep = account.get_funds_ch()
        bal_w_int_ch = account.calc_interest_ch()
        chalk.green(f"""The amount of ${amount_dep} has been deposited.\n--Your new Checking balance is ${new_chkb_dep}.\n--You've potentially made ${bal_w_int_ch} in interest.""")
        print()
        menu_screen(account)
    else:
        account.deposit(amount_dep)
        new_savb_dep = account.get_funds()
        new_bal_int = account.calc_interest()
    chalk.green(f"""The amount of ${amount_dep} has been deposited.\n--Your new Savings balance is ${new_savb_dep}.\n--You've potentially made ${new_bal_int} in interest.""")
    print()
    menu_screen(account)

    # except ValueError as e:
    #     print(e.args[0])



def menu_screen(account: act) -> str:

    chalk.cyan("""$$$$---BANK OF MOOLA MENU---$$$$
        
Type s >> See My Savings Balance
Type c >> See My Checking Balance
Type d >> Deposit Moola
Type w >> Withdrawal Moola
    """)
    start_menu_choice = input("How may we help you? >>> ")

    if start_menu_choice == 's':
        clear()     # makes space in terminal view
        funds = account.get_funds()
        chalk.red(f"You're Savings balance is ${funds}.")
        chalk.red('--------------------------------')
        menu_screen(account)
    elif start_menu_choice == 'c':
        clear()
        funds_ch = account.get_funds_ch()
        chalk.red(f"You're Checking balance is ${funds_ch}.")
        chalk.red('--------------------------------')
        menu_screen(account)

    elif start_menu_choice == 'd':
        clear()
        deposit_acc(account)
    elif start_menu_choice == 'w':
        clear()
        withdrawal_acc(account)




def start_acc():
    open = input(""" 
    
BANK OF MOOLA has a SPECIAL 1-MINUTE OFFER 
of a free savings and checking 
with $1000 deposited into each!!!!

Only 20, 19, 18 seconds left... 

Would you like to open an account? (y or n) """)
    
    if open != 'n':
        clear()    # makes space in terminal view
        account = Account(1000, 1000, 0.001)
        menu_screen(account)
    else:
        clear()
        chalk.red("You're on the road to ruin.  Good luck, chief!")


    
start_acc()
