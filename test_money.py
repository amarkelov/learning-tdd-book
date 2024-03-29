import unittest
from money import Money


class TestMoney(unittest.TestCase):
    def testMultiplicationInEuros(self):
        tenEuros = Money(10, "EUR")
        twentyEuros = tenEuros.times(2)
        self.assertEqual(twentyEuros, tenEuros.times(2))

    def testMultiplicationInDollars(self):
        fiver = Money(5, "USD")
        tenner = fiver.times(2)
        self.assertEqual(tenner, fiver.times(2))

    def testDivision(self):
        originalMoney = Money(4002, "KRW")
        actualMoneyAfterDivision = originalMoney.divide(4)
        expectedMoneyAfterDivision = Money(1000.5, "KRW")
        self.assertEqual(expectedMoneyAfterDivision.amount,
                         actualMoneyAfterDivision.amount)
        self.assertEqual(expectedMoneyAfterDivision.currency,
                         actualMoneyAfterDivision.currency)

    def testAddMoneyDirectly(self):
        self.assertEqual(Money(15, "USD"), Money(5, "USD") + Money(10, "USD"))
        self.assertEqual(Money(15, "USD"), Money(10, "USD") + Money(5, "USD"))
        self.assertEqual(None, Money(5, "USD") + Money(10, "EUR"))
        self.assertEqual(None, Money(5, "USD") + None)
