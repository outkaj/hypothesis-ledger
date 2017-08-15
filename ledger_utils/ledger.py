"""
A module containing two classes, Transaction and Account, and associated
methods. These classes represent components of
a ledger system that keeps track of payments between various parties,
including individuals and organizations.
"""

from collections import OrderedDict


class Transaction(object):
    """

    A class for storing financial transactions.
    Attributes:
        date: A string representing the date of the transaction.
        payer: A string representing the party who paid.
        payee: A string representing the party who was paid.
        amount: A float representing the amount that was paid.

    """

    def __init__(self, date, payer, payee, amount):
        """
        Return a Transaction object whose date is *date*, payer is *payer*,
        payee is *payee*, and amount is *amount*.
        """
        self.date = date
        self.payer = payer
        self.payee = payee
        self.amount = amount

    def __repr__(self):
        """
        Return a string representation of a Transaction with section character
        attached and float precision fixed to two decimal places.
        """
        return '{0},{1},{2},{3}{4:.2f}'.format(self.date, self.payer,
                                               self.payee, u'\u00A7',
                                               self.amount)


class Account(object):
    """

    A class for storing information about a party's bank account over time.
    Attributes:
        name: A string representing the name of the party who owns the account.
        starting_balance: A float representing the account's starting balance,
        which is always 0.00.
        records: A dictionary whose key-value pairs represent dates
        of the party's transactions and the balance on those dates.

    """

    def __init__(self, name):
        """
        Return an Account object whose name is *name*, balance is 0.00
        and records is an empty OrderedDict().
        """
        self.name = name
        self.balance = 0.00
        self.records = OrderedDict()

    def __repr__(self):
        """
        Return a string representation of an Account with section character
        attached and float precision fixed to two decimal places.
        """
        return '{0},{1}{2:.2f},{3}'.format(self.name, u'\u00A7',
                                           self.balance, self.records)

    def withdraw(self, amount):
        """Subtract amount from balance and return the balance."""
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        """Add amount to balance and return the balance."""
        self.balance += amount
        return self.balance

    def get_date_balance(self, date):
        """
        Return the balance for a given account on a given date. Raise an error
        if the key is not found.
        """
        try:
            return '{0}{1:.2f}'.format(u'\u00A7', self.records[date])
        except KeyError:
            print("Looks like that date is invalid. Try again!")

    def add_record(self, date, balance):
        """
        Add a record whose date is *date* and balance is *balance* to *records*.
        """
        self.records[date] = balance
