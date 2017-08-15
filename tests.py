import unittest
from collections import OrderedDict
from ledger_utils import ledger


class TestLedger(unittest.TestCase):
    """
    A class for testing a ledger system's ability to return balances
    for specific accounts on specific dates.
    """
    @classmethod
    def test_get_day1_balance_zero(cls):
        anna = ledger.Account("anna")
        anna.balance = -360.58
        anna.records = OrderedDict([('2015-01-16', 0.0), ('2015-01-17', 0.0),
                                    ('2015-01-18', -359.59),
                                    ('2015-01-19', -359.59),
                                    ('2015-01-20', -360.58)])
        assert anna.get_date_balance(
            '2015-01-16') == '{0}{1:.2f}'.format(u'\u00A7', 0.00)

    @classmethod
    def test_get_day1_balance_negative(cls):
        john = ledger.Account("john")
        john.balance = -119.51
        john.records = OrderedDict([('2015-01-16', -125.0),
                                    ('2015-01-17', -145.0),
                                    ('2015-01-18', -95.0),
                                    ('2015-01-19', -95.0),
                                    ('2015-01-20', -119.51)])
        assert john.get_date_balance(
            '2015-01-16') == '{0}{1:.2f}'.format(u'\u00A7', -125.00)

    @classmethod
    def test_get_day1_balance_positive(cls):
        mary = ledger.Account("mary")
        mary.balance = 125.00
        mary.records = OrderedDict([('2015-01-16',
                                     125.0),
                                    ('2015-01-17',
                                     25.0),
                                    ('2015-01-18',
                                     14.25),
                                    ('2015-01-19',
                                     9.25),
                                    ('2015-01-20',
                                     9.25)])
        assert mary.get_date_balance(
            '2015-01-16') == '{0}{1:.2f}'.format(u'\u00A7', 125.00)

    def test_get_balance_invalid_date(self):
        empty = ledger.Account("empty")
        empty.balance = 0.00
        empty.records = OrderedDict([])
        self.assertRaises(
            KeyError, empty.get_date_balance('2015-01-20'))

    def test_account_no_transactions(self):
        self.assertRaises(
            NameError,
            lambda: nobody.get_date_balance('2015-01-19'))

    @classmethod
    def test_get_balance_later_date(cls):
        pizza = ledger.Account("pizza")
        pizza.balance = 25.50
        pizza.records = OrderedDict([('2015-01-16', 0.0), ('2015-01-17', 0.0),
                                     ('2015-01-18', 0.0), ('2015-01-19', 0.0),
                                     ('2015-01-20', 25.5)])
        assert pizza.get_date_balance(
            '2015-01-20') == '{0}{1:.2f}'.format(u'\u00A7', 25.50)

    @classmethod
    def test_get_balance_positive_noninteger(cls):
        supermarket = ledger.Account("supermarket")
        supermarket.balance = 30.75
        supermarket.records = OrderedDict([('2015-01-16', 0.0),
                                           ('2015-01-17', 20.0),
                                           ('2015-01-18', 30.75),
                                           ('2015-01-19', 30.75),
                                           ('2015-01-20', 30.75)])
        assert supermarket.get_date_balance(
            '2015-01-18') == '{0}{1:.2f}'.format(u'\u00A7', 30.75)

    @classmethod
    def test_get_balance_negative_noninteger(cls):
        sarah = ledger.Account("sarah")
        sarah.balance = -360.58
        sarah.records = OrderedDict([('2015-01-16', 0.0), ('2015-01-17', 0.0),
                                     ('2015-01-18', -90.42),
                                     ('2015-01-19', -85.42),
                                     ('2015-01-20', -85.42)])
        assert sarah.get_date_balance(
            '2015-01-19') == '{0}{1:.2f}'.format(u'\u00A7', -85.42)


if __name__ == '__main__':
    unittest.main()
