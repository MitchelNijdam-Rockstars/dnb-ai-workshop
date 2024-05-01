import streamlit as st


def collect_financial_data():
    st.subheader("Enter your financial details")

    data = st.session_state.get('financial_data', {})

    # Default values
    income = data['income'] if 'income' in data else 0.0
    expenses = data['expenses'] if 'expenses' in data else 0.0
    savings = data['savings'] if 'savings' in data else 0.0
    debt = data['debt'] if 'debt' in data else 0.0

    # Collect financial inputs
    income = st.number_input("Monthly Income (€):", min_value=0.0, format="%.2f", step=100.0, value=income)
    expenses = st.number_input("Monthly Expenses (€):", min_value=0.0, format="%.2f", step=100.0, value=expenses)
    savings = st.number_input("Total Savings (€):", min_value=0.0, format="%.2f", step=100.0, value=savings)
    debt = st.number_input("Total Debt (€):", min_value=0.0, format="%.2f", step=100.0, value=debt)

    # Save inputs to session state if validation passes
    st.session_state['financial_data'] = {
        'income': income,
        'expenses': expenses,
        'savings': savings,
        'debt': debt
    }
    return income, expenses, savings, debt