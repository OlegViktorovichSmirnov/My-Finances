# # Profit
#
# Write code to describe all source of income
# Show how fast each income is generating: day, week, month, year
# Sort incomes by types

# Calculating RoboBot profit
# Currency is USD
RB_invested_sum = 5000
RB_profit_percentage = 13
# Duration calculate in month
RB_duration_of_investing = 6
RB_profit = ((RB_invested_sum*RB_profit_percentage)/100)*RB_duration_of_investing
RB_total_sum = RB_invested_sum + RB_profit
print(f'-----')
print(f'Profit will be: {RB_profit}$')
print(f'Duration of investment will be: {RB_duration_of_investing} month')
print(f'Total sum will be: {RB_total_sum}$')
print(f'-----')

# OTTO
# OTTO_Money_in_use
# OTTO_profit
# SberInvesting
# SberInvesting_Money_in_use
# SberInvesting_profit