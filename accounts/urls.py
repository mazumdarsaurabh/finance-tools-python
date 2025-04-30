
from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required # Import the login_required decorator

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('', views.dashboard, name='home'),
    path('login/', views.login_user, name='login'),
    path('register/', views.register_user, name='register'),
    path('logout/', views.logout_user, name='logout'),

    # Apply login_required to the deposit and withdraw views
    path('balance/', login_required(views.account_balance), name='account_balance'),
    path('deposit/', login_required(views.deposit), name='deposit'),
    path('withdraw/', login_required(views.withdraw), name='withdraw'),

    # Financial tools -  These don't require login
    path('tools/emi/', views.emi_calculator, name='emi'),
    path('tools/networth/', views.networth_calculator, name='networth'),
    path('tools/sip/', views.sip_calculator, name='sip'),
    path('tools/fd/', views.fd_calculator, name='fd'),
    path('tools/rd/', views.rd_calculator, name='rd'),
    path('tools/retirement/', views.retirement_calculator, name='retirement'),
    path('tools/loan_eligibility/', views.loan_eligibility_calculator, name='home_loan_eligibility'),
    path('tools/credit_card/', views.credit_card_calculator, name='credit_card'),
    path('tools/taxable_income/', views.taxable_income_calculator, name='taxable_income'),
    path('tools/budget/', views.budget_planner, name='budget'),
]
