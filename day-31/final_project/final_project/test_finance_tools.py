import unittest
import final_project.banking_system.accounts.finance_tools as finance_tools

class TestFinanceTools(unittest.TestCase):

    def test_calculate_emi(self):
        self.assertAlmostEqual(finance_tools.calculate_emi(100000, 10, 1), 8791.59, places=2)
        with self.assertRaises(ValueError):
            finance_tools.calculate_emi(-1000, 10, 1)

    def test_calculate_sip(self):
        self.assertAlmostEqual(finance_tools.calculate_sip(1000, 12, 1), 12713.13, places=2)
        with self.assertRaises(ValueError):
            finance_tools.calculate_sip(1000, -5, 1)

    def test_calculate_fd(self):
        self.assertAlmostEqual(finance_tools.calculate_fd(100000, 7, 2), 114490.0, places=1)
        with self.assertRaises(ValueError):
            finance_tools.calculate_fd(-100000, 7, 2)

    def test_calculate_rd(self):
        self.assertAlmostEqual(finance_tools.calculate_rd(1000, 7, 2), 25890.0, delta=100)
        with self.assertRaises(ValueError):
            finance_tools.calculate_rd(1000, -7, 2)

    def test_estimate_retirement_corpus(self):
        self.assertGreater(finance_tools.estimate_retirement_corpus(100000, 1000, 10, 10), 0)
        with self.assertRaises(ValueError):
            finance_tools.estimate_retirement_corpus(100000, -1000, 10, 10)

    def test_estimate_home_loan_eligibility(self):
        self.assertEqual(finance_tools.estimate_home_loan_eligibility(50000, 20000), 1800000.0)
        with self.assertRaises(ValueError):
            finance_tools.estimate_home_loan_eligibility(0, 20000)

    def test_calculate_credit_card_balance(self):
        result = finance_tools.calculate_credit_card_balance(10000, 18, 6)
        self.assertGreater(result, 0)
        with self.assertRaises(ValueError):
            finance_tools.calculate_credit_card_balance(10000, -18, 6)

    def test_calculate_taxable_income(self):
        self.assertEqual(finance_tools.calculate_taxable_income(500000, 100000), 400000)
        self.assertEqual(finance_tools.calculate_taxable_income(100000, 200000), 0)
        with self.assertRaises(ValueError):
            finance_tools.calculate_taxable_income(100000, -10000)

    def test_plan_budget(self):
        result = finance_tools.plan_budget(50000, 30000)
        self.assertEqual(result, {"savings": 10000.0, "investment": 10000.0})
        with self.assertRaises(ValueError):
            finance_tools.plan_budget(-50000, 30000)

    def test_calculate_net_worth(self):
        self.assertEqual(finance_tools.calculate_net_worth(100000, 50000), 50000)
        with self.assertRaises(ValueError):
            finance_tools.calculate_net_worth(-100000, 50000)

if __name__ == '__main__':
    unittest.main()