import unittest
from main import Category, create_spend_chart

class TestCategory(unittest.TestCase):

    def setUp(self):
        self.food = Category("Food")
        self.entertainment = Category("Entertainment")
        self.business = Category("Business")

    def test_deposit(self):
        self.food.deposit(1000, "Initial deposit")
        self.assertEqual(self.food.ledger[0]['amount'], 1000)
        self.assertEqual(self.food.ledger[0]['description'], "Initial deposit")

    def test_withdraw(self):
        self.food.deposit(1000, "Initial deposit")
        result = self.food.withdraw(200, "Groceries")
        self.assertTrue(result)
        self.assertEqual(self.food.ledger[1]['amount'], -200)
        self.assertEqual(self.food.ledger[1]['description'], "Groceries")

    def test_transfer(self):
        self.food.deposit(1000, "Initial deposit")
        result = self.food.transfer(300, self.entertainment)
        self.assertTrue(result)
        self.assertEqual(self.food.ledger[1]['amount'], -300)
        self.assertEqual(self.food.ledger[1]['description'], "Transfer to Entertainment")
        self.assertEqual(self.entertainment.ledger[0]['amount'], 300)
        self.assertEqual(self.entertainment.ledger[0]['description'], "Transfer from Food")

    def test_get_balance(self):
        self.food.deposit(1000, "Initial deposit")
        self.food.withdraw(200, "Groceries")
        self.assertEqual(self.food.get_balance(), 800)

    def test_check_funds(self):
        self.food.deposit(500, "Initial deposit")
        self.assertTrue(self.food.check_funds(300))
        self.assertFalse(self.food.check_funds(600))

    def test_str_representation(self):
        self.food.deposit(1000, "Initial deposit")
        self.food.withdraw(200, "Groceries")
        expected_output = (
            "*************Food*************\n" +
            "Initial deposit        1000.00\n" +
            "Groceries              -200.00\n" +
            "Total: 800.0"
        )
        self.assertEqual(str(self.food), expected_output)

    def test_create_spend_chart(self):
        self.food.deposit(1000, "Initial deposit")
        self.food.withdraw(300, "Groceries")
        self.entertainment.deposit(1000, "Initial deposit")
        self.entertainment.withdraw(200, "Movies")
        self.business.deposit(1000, "Initial deposit")
        self.business.withdraw(100, "Supplies")
        
        expected_output = (
            "Percentage spent by category\n" +
            "100|          \n" +
            " 90|          \n" +
            " 80|          \n" +
            " 70|          \n" +
            " 60|          \n" +
            " 50|    o     \n" +
            " 40|    o     \n" +
            " 30|    o     \n" +
            " 20|    o  o  \n" +
            " 10|    o  o  \n" +
            "  0| o  o  o  \n" +
            "    ----------\n" +
            "     F  E  B  \n" +
            "     o  n  u  \n" +
            "     o  t  s  \n" +
            "     d  e  i  \n" +
            "        r  n  \n" +
            "        t  e  \n" +
            "        a  s  \n" +
            "        i     \n" +
            "        n     \n" +
            "        m     \n"
        )
        self.assertEqual(create_spend_chart([self.food, self.entertainment, self.business]), expected_output)

if __name__ == "__main__":
    unittest.main()
