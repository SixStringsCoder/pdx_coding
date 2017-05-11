"""
ATM interface by Steve Hanlon May 
Create Class in main and message functions in function.py file
"""
class Account:
    def __init__(self, _balance: int, _balance_ch: int, _interest: int):
        """
        make two private attributes
        :param _balance: 
        :param _interest: 
        """

        self._balance = _balance
        self._balance_ch = _balance_ch
        self._interest = _interest

    def __repr__(self):
        message = f"{self.__class__.__name__}, {self._balance}, {self._balance_ch} {self._interest}"
        return message

    def __str__(self):
        message = f"""Your account has a Savings balance of ${self._balance} 
and a Checking balance of {self._balance_ch} 
at a rate of {self._interest}% interest."""
        return message


    def get_funds(self) -> int:
        """
        Return account balance for Savings
        :return: 
        """

        return self._balance

    def get_funds_ch(self) -> int:
        """
        Return account balance for Checking
        :return: int
        """

        return self._balance_ch


    def deposit(self, amount: int) -> int:
        """
        Deposit to the account
        :return: int
        """

        if amount > 0:
            self._balance += amount
            return self._balance
        else:
            raise ValueError("You can't deposit a negative amount!")

    def deposit_ch(self, amount: int) -> int:
        """
        Deposit to the account
        :return: int
        """

        if amount > 0:
            self._balance_ch += amount
            return self._balance_ch
        else:
            raise ValueError("You can't deposit a negative amount!")


    def check_withdrawal(self, amount: int) -> bool:
        """
        Return `True` if large enough balance for a SAVINGS withdrawal
        :return: bool
        """

        if amount > self._balance:
            return False
        else:
            return True

    def withdrawal(self, amount: int) -> int:
        """
        Withdraw an allowed amount; raise a `ValueError` if insufficient SAVINGS balance

        :return: None
        """
        if amount < 0:
            raise ValueError("You can't deposit a negative amount!")

        if self.check_withdrawal(amount):
            self._balance -= amount
        else:
            raise ValueError(f"Insufficient funds. Your savings account balance is {self._balance}.")

        return amount


    def check_withdrawal_ch(self, amount: int) -> bool:
        """
        Return `True` if large enough balance for a CHECKING withdrawal
        :return: bool
        """

        if amount > self._balance_ch:
            return False
        else:
            return True

    def withdrawal_ch(self, amount: int) -> int:
        """
        Withdraw an allowed amount; raise a `ValueError` if insufficient SAVINGS balance
        
        :return: None
        """
        if amount < 0:
            raise ValueError("You can't deposit a negative amount!")

        if self.check_withdrawal_ch(amount):
            self._balance_ch -= amount
        else:
            raise ValueError(f"Insufficient funds. Your checking account balance is {self._balance_ch}.")

        return amount


    def calc_interest(self) -> int:
        """
        Calculate and return interest on the current account balance
        :return: 
        """

        bal_w_int = self._balance * self._interest

        return bal_w_int

    def calc_interest_ch(self) -> int:
        """
        Calculate and return interest on the current account balance
        :return: 
        """

        bal_w_int_ch = self._balance_ch * self._interest

        return bal_w_int_ch