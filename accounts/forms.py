from django import forms

class TransactionForm(forms.Form):
    amount = forms.DecimalField(label='Amount (₹)', min_value=1.0)

from django import forms

class EMIForm(forms.Form):
    principal = forms.FloatField(min_value=1, label="Loan Amount (₹)")
    annual_rate = forms.FloatField(min_value=0.1, label="Annual Interest Rate (%)")
    tenure_years = forms.IntegerField(min_value=1, label="Loan Tenure (Years)")

class NetWorthForm(forms.Form):
    assets = forms.FloatField(min_value=0, label="Total Assets (₹)")
    liabilities = forms.FloatField(min_value=0, label="Total Liabilities (₹)")

class SIPForm(forms.Form):
    monthly_investment = forms.FloatField(min_value=1, label="Monthly Investment (₹)")
    annual_rate = forms.FloatField(min_value=0.1, label="Annual Interest Rate (%)")
    years = forms.IntegerField(min_value=1, label="Investment Period (Years)")

class FdForm(forms.Form):
    principal = forms.FloatField(min_value=1, label="FD Amount (₹)")
    annual_rate = forms.FloatField(min_value=0.1, label="Annual Interest Rate (%)")
    tenure_years = forms.IntegerField(min_value=1, label="FD Tenure (Years)")

class RdForm(forms.Form):
    monthly_deposit = forms.FloatField(min_value=1, label="Monthly Deposit (₹)")
    annual_rate = forms.FloatField(min_value=0.1, label="Annual Interest Rate (%)")
    months = forms.IntegerField(min_value=1, label="Investment Period (Months)")

class RetirementForm(forms.Form):
    current_savings = forms.FloatField(min_value=0, label="Current Savings (₹)")
    monthly_addition = forms.FloatField(min_value=1, label="Monthly Addition (₹)")
    annual_rate = forms.FloatField(min_value=0.1, label="Annual Interest Rate (%)")
    years = forms.IntegerField(min_value=1, label="Years to Retirement")

class LoanEligibilityForm(forms.Form):
    income = forms.FloatField(min_value=1, label="Monthly Income (₹)")
    expenses = forms.FloatField(min_value=0, label="Monthly Expenses (₹)")
    credit_score = forms.IntegerField(min_value=300, max_value=850, label="Credit Score")

class CreditCardForm(forms.Form):
    outstanding_balance = forms.FloatField(min_value=0, label="Outstanding Balance (₹)")
    annual_rate = forms.FloatField(min_value=0.1, label="Annual Interest Rate (%)")
    months = forms.IntegerField(min_value=1, label="Months for Payment")

class TaxableIncomeForm(forms.Form):
    income = forms.FloatField(min_value=0, label="Total Income (₹)")
    deductions = forms.FloatField(min_value=0, label="Deductions (₹)")

class BudgetForm(forms.Form):
    income = forms.FloatField(min_value=1, label="Monthly Income (₹)")
    expenses = forms.FloatField(min_value=0, label="Monthly Expenses (₹)")
    savings_goal = forms.FloatField(min_value=0, label="Savings Goal (₹)")

