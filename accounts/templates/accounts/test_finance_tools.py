# test_finance_tools.py
import unittest
import final_project.banking_system.accounts.finance_tools as finance_tools # Import the module

class TestFinanceTools(unittest.TestCase):

    def test_calculate_emi(self):
        # Test case 1: Valid input
        self.assertAlmostEqual(finance_tools.calculate_emi(100000, 10, 1), 8791.59, places=2)
        # Test case 2: Another valid input
        self.assertAlmostEqual(finance_tools.calculate_emi(200000, 12, 2), 9444.62, places=2)
        # Test case 3:  principal = 0
        with self.assertRaises(ValueError):
            finance_tools.calculate_emi(0, 10, 1)
        # Test case 4: rate = 0
        with self.assertRaises(ValueError):
            finance_tools.calculate_emi(1000, 0, 1)
        # Test case 5: tenure = 0
        with self.assertRaises(ValueError):
            finance_tools.calculate_emi(1000, 10, 0)
        # Test case 6: negative input
        with self.assertRaises(ValueError):
            finance_tools.calculate_emi(-1000, 10, 1)

    def test_calculate_sip(self):
        self.assertAlmostEqual(finance_tools.calculate_sip(1000, 12, 1), 12713.13, places=2)
        self.assertAlmostEqual(finance_tools.calculate_sip(500, 10, 5), 38571.75, places=2)
        with self.assertRaises(ValueError):
            finance_tools.calculate_sip(1000, -5, 1)
        with self.assertRaises(ValueError):
            finance_tools.calculate_sip(1000, 5, -1)
        with self.assertRaises(ValueError):
            finance_tools.calculate_sip(-1000, 5, 1)

    def test_calculate_fd(self):
        self.assertAlmostEqual(finance_tools.calculate_fd(100000, 7, 2), 114490.0, places=1)
        self.assertAlmostEqual(finance_tools.calculate_fd(50000, 8, 3), 63000.0, places=1)
        with self.assertRaises(ValueError):
            finance_tools.calculate_fd(-100000, 7, 2)
        with self.assertRaises(ValueError):
            finance_tools.calculate_fd(100000, -7, 2)
        with self.assertRaises(ValueError):
            finance_tools.calculate_fd(100000, 7, -2)

    def test_calculate_rd(self):
        self.assertAlmostEqual(finance_tools.calculate_rd(1000, 7, 2), 25890.0, delta=100)
        self.assertAlmostEqual(finance_tools.calculate_rd(500, 6, 3), 20910.0, delta=100)
        with self.assertRaises(ValueError):
            finance_tools.calculate_rd(1000, -7, 2)
        with self.assertRaises(ValueError):
            finance_tools.calculate_rd(1000, 7, -2)
        with self.assertRaises(ValueError):
            finance_tools.calculate_rd(-1000, 7, 2)

    def test_estimate_retirement_corpus(self):
        self.assertAlmostEqual(finance_tools.estimate_retirement_corpus(100000, 1000, 10, 10), 318543.89, places=2)
        self.assertAlmostEqual(finance_tools.estimate_retirement_corpus(200000, 2000, 15, 20), 2471271.84, places=2)
        with self.assertRaises(ValueError):
            finance_tools.estimate_retirement_corpus(100000, -1000, 10, 10)
        with self.assertRaises(ValueError):
            finance_tools.estimate_retirement_corpus(100000, 1000, -10, 10)
        with self.assertRaises(ValueError):
            finance_tools.estimate_retirement_corpus(100000, 1000, 10, -10)
        with self.assertRaises(ValueError):
            finance_tools.estimate_retirement_corpus(-100000, 1000, 10, 10)

    def test_estimate_home_loan_eligibility(self):
        self.assertEqual(finance_tools.estimate_home_loan_eligibility(50000, 20000), 1800000.0)
        self.assertEqual(finance_tools.estimate_home_loan_eligibility(60000, 25000), 1740000.0)
        with self.assertRaises(ValueError):
            finance_tools.estimate_home_loan_eligibility(0, 20000)
        with self.assertRaises(ValueError):
            finance_tools.estimate_home_loan_eligibility(50000, -20000)
        with self.assertRaises(ValueError):
            finance_tools.estimate_home_loan_eligibility(50000, 20000, credit_score=200)
        with self.assertRaises(ValueError):
            finance_tools.estimate_home_loan_eligibility(50000, 20000, credit_score=900)

    def test_calculate_credit_card_balance(self):
        result1 = finance_tools.calculate_credit_card_balance(10000, 18, 6)
        self.assertGreater(result1, 0)
        result2 = finance_tools.calculate_credit_card_balance(5000, 15, 12)
        self.assertGreater(result2, 0)
        with self.assertRaises(ValueError):
            finance_tools.calculate_credit_card_balance(10000, -18, 6)
        with self.assertRaises(ValueError):
            finance_tools.calculate_credit_card_balance(10000, 18, -6)
        with self.assertRaises(ValueError):
            finance_tools.calculate_credit_card_balance(-10000, 18, 6)

    def test_calculate_taxable_income(self):
        self.assertEqual(finance_tools.calculate_taxable_income(500000, 100000), 400000)
        self.assertEqual(finance_tools.calculate_taxable_income(100000, 200000), 0)
        self.assertEqual(finance_tools.calculate_taxable_income(500000, 0), 500000)
        with self.assertRaises(ValueError):
            finance_tools.calculate_taxable_income(100000, -10000)
        with self.assertRaises(ValueError):
            finance_tools.calculate_taxable_income(-100000, 10000)

    def test_plan_budget(self):
        result1 = finance_tools.plan_budget(50000, 20000, 10000)
        self.assertIn("surplus", result1)
        self.assertIn("Savings", result1)
        result2 = finance_tools.plan_budget(20000, 50000, 10000)
        self.assertIn("deficit", result2)
        self.assertIn("Reduce", result2)
        result3 = finance_tools.plan_budget(50000, 50000, 10000)
        self.assertIn("equal", result3)
        self.assertIn("Consider", result3)
        with self.assertRaises(ValueError):
            finance_tools.plan_budget(-1000, 1000, 1000)
        with self.assertRaises(ValueError):
            finance_tools.plan_budget(1000, -1000, 1000)
        with self.assertRaises(ValueError):
            finance_tools.plan_budget(1000, 1000, -1000)

    def test_calculate_net_worth(self):
        self.assertEqual(finance_tools.calculate_net_worth(100000, 50000), 50000)
        self.assertEqual(finance_tools.calculate_net_worth(200000, 100000), 100000)
        with self.assertRaises(ValueError):
            finance_tools.calculate_net_worth(-100000, 50000)
        with self.assertRaises(ValueError):
            finance_tools.calculate_net_worth(100000, -50000)
