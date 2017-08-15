"""
A module for processing a text file representing a ledger, converting the
contents into Transactions and Accounts as described in the ledger module,
updating the Transactions and Accounts based on the text file's contents,
and returning the balance for accounts on specified days.
"""

import ledger
from more_itertools import unique_everseen


def read_ledger(filename):
    """Read a file into a list, splitting its lines, and return the list."""
    ledger_output = []
    with open(filename) as file:
        for line in file:
            transaction = [x.strip() for x in line.split(',')]
            ledger_output.append(transaction)
    return ledger_output


def convert_ledger_contents(items):
    """Return a list of Transaction objects for each row of *ledger*."""
    return [ledger.Transaction
            (row[0], row[1], row[2], float(row[3])) for row in items]


def extract_account_names(transactions):
    """
    Extract account holder names from the list of Transaction() objects
    and return the names as a set.
    """
    payers = set(transaction.payer for transaction in transactions)
    payees = set(transaction.payee for transaction in transactions)
    return set.union(payers, payees)


def create_accounts(account_names):
    """Return an Account() object for each name in *account_names*."""
    return [ledger.Account(name) for name in account_names]


def update_account_records(transactions, accounts):
    """
    Populate account records from the payer and
    payee information in *transactions.*
    Return the accounts.
    """
    for transaction in transactions:
        for account in accounts:
            if account.name == transaction.payer:
                account.add_record(transaction.date,
                                   account.withdraw(transaction.amount))
            elif account.name == transaction.payee:
                account.add_record(transaction.date,
                                   account.deposit(transaction.amount))
            else:
                account.add_record(transaction.date, account.balance)
    return accounts


def main():
    """
    Demonstrate the basic functionality of the ledger system and print test
    output showing the account balances for each account each day.
    """
    ledger_file = read_ledger("ledger.txt")
    transactions = convert_ledger_contents(ledger_file)
    account_names = extract_account_names(transactions)
    empty_accounts = create_accounts(account_names)
    filled_accounts = update_account_records(transactions, empty_accounts)
    output = list()
    for transaction in transactions:
        for account in filled_accounts:
            output.append(str(transaction.date + " " + account.name +
                              " " + account.get_date_balance(transaction.date)))
    final = list(unique_everseen(output))
    for item in final:
        print(item)


if __name__ == '__main__':
    main()
