import unittest
from money import Money
from portfolio import Portfolio


class TestPortfolio(unittest.TestCase):
    def testAddition(self):
        fiveDollars = Money(5, "USD")
        tenDollars = Money(10, "USD")
        fifteenDollars = Money(15, "USD")
        portfolio = Portfolio()
        portfolio.add(fiveDollars, tenDollars)
        self.assertEqual(fifteenDollars, portfolio.evaluate("USD"))

    def testAdditionOfDollarsAndEuros(self):
        fiveDollars = Money(5, "USD")
        tenEuros = Money(10, "EUR")
        portfolio = Portfolio()
        portfolio.add(fiveDollars, tenEuros)
        expectedValue = Money(17, "USD")
        actualValue = portfolio.evaluate("USD")
        self.assertEqual(expectedValue, actualValue, "%s != %s" % (expectedValue, actualValue))
    
    def testAdditionOfDollarsAndWons(self):
        oneDollar = Money(1, "USD")
        elevenHundredWon = Money(1100, "KRW")
        portfolio = Portfolio()
        portfolio.add(oneDollar, elevenHundredWon)
        expectedValue = Money(2200, "KRW")
        actualValue = portfolio.evaluate("KRW")
        self.assertEqual(expectedValue, actualValue, "%s != %s" % (expectedValue, actualValue))

    def testAdditionWithMultipleMissingExchangeRates(self):
        oneDollar = Money(1, "USD")
        oneEuro = Money(1, "EUR")
        oneWon = Money(1, "KRW")
        portfolio = Portfolio()
        portfolio.add(oneDollar, oneEuro, oneWon)
        with self.assertRaisesRegex(
                Exception,
                "Missing exchange rate\(s\):\[USD->Kalganid,EUR->Kalganid,KRW->Kalganid\]"):
            portfolio.evaluate("Kalganid")
