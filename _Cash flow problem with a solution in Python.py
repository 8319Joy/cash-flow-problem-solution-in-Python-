#!/usr/bin/env python
# coding: utf-8

# # Problem:
# You run a small business, and you want to analyze your cash flow for the next 12 months. Each month, you expect some inflows and outflows of cash. Your goal is to calculate:
# 
# The net cash flow for each month.
# The cumulative cash balance over time.
# Identify any months where your cash balance becomes negative.
# Here's a breakdown of the problem:
# 
# You are provided with two lists:
# A list of cash inflows for 12 months.
# A list of cash outflows for 12 months.
# You start with an initial balance of Rs.10,000.
# You need to compute:
# 
# Monthly net cash flow (inflow - outflow).
# Monthly cash balance.
# Highlight months where the cash balance becomes negative.

# In[8]:


# Data: Inflows and Outflows for each month (for simplicity, use sample data)
cash_inflows = [5000, 7000, 6000, 8000, 7500, 5000, 4500, 5200, 6100, 7200, 6700, 7000]
cash_outflows= [4000, 6500, 5500, 7000, 8000, 6000, 5000, 4800, 5900, 6400, 6300, 6800]

# Starting balance
initial_balance = 10000

# Initialize lists for storing results
net_cash_flow =[]
cash_balance =[]

# Loop through each month to calculate net cash flow and balance
balance = initial_balance
for i in range(12):
    # Calculate the net cash flow (inflow - outflow)
    net_flow = cash_inflows[i] - cash_outflows[i]
    net_cash_flow.append(net_flow)
    
    # Update balance for the month
    balance += net_flow
    cash_balance.append(balance)

# Print Results
print("Month\tInflows\tOutflows\tNet Flow\tBalance")
for i in range(12):
    print(f"{i+1}\tRs.{cash_inflows[i]}\tRs.{cash_outflows[i]}\t\tRs.{net_cash_flow[i]}\t\tRs.{cash_balance[i]}")
    
# Highlight months where the balance is negative
negative_months = [i+1 for i in range(12) if cash_balance[i] < 0]
if negative_months:
    print("\nWarning: Negative cash balance in months:",negative_months)
else:
    print("\nNo months with negative cash balance.")


# Explanation:
# cash_inflows and cash_outflows are the monthly inflows and outflows respectively.
# We calculate the net_cash_flow by subtracting outflows from inflows.
# We update the cash_balance by adding the net cash flow to the previous balance.
# Finally, we print the monthly details and warn the user if the cash balance goes negative in any month.

# You can adjust the cash_inflows and cash_outflows lists as per your data. This script will help analyze cash flow and detect any potential liquidity issues.

# In[ ]:




