This program processes ledger text files where each line represents a financial
transaction in the format [date,payer,payee,amount]. For an example of this
format, see below:

```
2015-01-16,john,mary,125.00
2015-01-17,john,supermarket,20.00
2015-01-17,mary,insurance,100.00
```

It provides utilities for returning the balance for a given account on a given date.
The fictional currency is equivalent to USD apart from a &#00A7 character in
front of the amount.

Dependencies can be installed by running `pip install -r requirements.txt`.
The only dependency (besides Python 3+) is the
[more_itertools](https://github.com/erikrose/more-itertools) library.

The program itself can be run by from the `ledger_utils` directory
with the command `python process_ledger.py`. The tests can be run from the root directory
with the command `python tests.py`.
