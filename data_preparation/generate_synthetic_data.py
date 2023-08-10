import pandas as pd
import numpy as np

# Number of users (rows) in the dataset
num_users = 10000

# Generate random user IDs
user_ids = range(1, num_users + 1)

# Generate random last loan amounts between $100 and $10,000
loan_amounts = np.random.randint(100, 10001, num_users)

# Generate random loan terms between 1 month to 5 years
loan_terms = np.random.randint(30, 1826, num_users)

# Generate random last loan durations based on the loan term with some randomness
loan_durations = [np.random.randint(term-15, term+16) for term in loan_terms]

# Determine if user defaulted on their last loan
defaulted = [1 if duration > term + 30 else 0 for duration, term in zip(loan_durations, loan_terms)]  # Considered a default if late by more than 30 days

# Create a DataFrame
df = pd.DataFrame({
    'User_ID': user_ids,
    'Last_Loan_Amount': loan_amounts,
    'Last_Loan_Term': loan_terms,
    'Last_Loan_Duration': loan_durations,
    'Defaulted': defaulted
})

# Save the DataFrame to a CSV file
df.to_csv('synthetic_loan_data.csv', index=False)

