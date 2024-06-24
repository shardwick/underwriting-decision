# import packages

import numpy as np
import pandas as pd

# Number of users (rows) in the dataset
num_users = 10000

# Total number of loans
total_loans = num_users * 3  # 3 loans per user

# Generate random user IDs (repeated for 3 loans each)
user_ids = np.array(list(range(1, num_users + 1)) * 3)

# Generate random last loan amounts between $100 and $10,000
loan_amounts = np.random.randint(100, 10001, total_loans)

# Generate random loan terms between 1 week (approx. 1 month) to 260 weeks (5 years)
loan_terms = np.random.randint(1, 261, total_loans)

# Generate random last loan durations based on the loan term with some randomness
loan_durations = [
    np.random.randint(term - 1, term + 2) for term in loan_terms
]  # Duration can vary within 1 week before or after the loan term

# Determine if user defaulted on their last loan
# We'll shuffle the array to ensure randomness and set the top 10% as defaulted
default_flags = np.array([1] * int(0.1 * total_loans) + [0] * int(0.9 * total_loans))
np.random.shuffle(default_flags)
defaulted = [
    1 if duration > term + 4 or flag else 0
    for duration, term, flag in zip(loan_durations, loan_terms, default_flags)
]  # Considered a default if late by more than 4 weeks

# Create a DataFrame
df = pd.DataFrame(
    {
        "User_ID": user_ids,
        "Last_Loan_Amount": loan_amounts,
        "Last_Loan_Term_Weeks": loan_terms,
        "Last_Loan_Duration_Weeks": loan_durations,
        "Defaulted": defaulted,
    }
)

# Save the DataFrame to a CSV file
df.to_csv("../data_preparation/synthetic_loan_data_enhanced.csv", index=False)
