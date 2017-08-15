### Description

This program processes ledger text in the format `[date,payer,payee,amount]` and
returns the balance for a given account on a given date.

For example, given the input below in a text file, the program can determine
that John's balance on January 16th was §-125.00, but Mary's was §125.00.

```
2015-01-16,john,mary,125.00
2015-01-17,john,supermarket,20.00
2015-01-17,mary,insurance,100.00
```

The fictional currency is equivalent to the amount in USD with a § character replacing the $ sign.

If an account has multiple transactions within a given day, the balance returned
corresponds to the latest balance. 

### Instructions

Dependencies can be installed by running `pip install -r requirements.txt`.
The only dependency (besides Python 3+) is the
[more_itertools](https://github.com/erikrose/more-itertools) library.

The program itself can be run by from the `ledger_utils` directory
with the command `python process_ledger.py`. The tests can be run from the root directory
with the command `python tests.py`.
