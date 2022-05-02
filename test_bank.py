import unittest
from bank import Bank
from money import Money


class TestBank(unittest.TestCase):
    def testConversion(self):
        bank = Bank()
        bank.addExchangeRate("EUR", "USD", 1.2)
        tenEuros = Money(10, "EUR")
        self.assertEqual(bank.convert(tenEuros, "USD")[0], Money(12, "USD"))

    def testConversionWithMissingExchangeRate(self):
        bank = Bank()
        tenEuros = Money(10, "EUR")
        result, missingKey = bank.convert(tenEuros, "Kalganid")
        self.assertIsNone(result)
        self.assertEqual(missingKey, "EUR->Kalganid")
