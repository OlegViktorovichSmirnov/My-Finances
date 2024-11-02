# Расчёт финансов для выплаты долга
#
# Необходимо составить программу, которая делает:
# расчёт сумм пополнений счёта,
# подсчитывает прибыль получаемую от торговли,
# подсчитывает изменения по кредиту выданному брокерской фирмой,
# высчитывает новые кредиты, взятые для выплаты кредита взятого от брокерской компании
# вычисляет изменения по балансу
# определяет тип пополнения собственные средства\заёмные
# постоянно высчитывает суммы, которые необходимо отдать и сумму собственных средств
# вычисляет среднюю сумму получаемой прибыли в день и неделю
# вносит календарное деление день недели, дата
# Комментарий необходимо переработать в соответствии с составленной задачей

# Replenishment of the Balance

Replenishment_of_the_Balance = [179.57, 51.3, 112.87, 205.54, 225.55, 3000, 1003.52, 1000.5, 395]
R = sum(Replenishment_of_the_Balance)
print(f'Replenishment of the Balance: {R} USDT')

# Profit

Profit = [442.42, 34.94, 163.4, 175.96, 209.93, 167.99, 100.04, 101.64, 133.34, 143.76, 2037.15]
P = sum(Profit)
print(f'Profit: {P} USDT')

# Loans

Broker_Loan = [3000]
People_loan = [0] # Not important now. Need to pay 1000 USDT later
Loans = sum(Broker_Loan + People_loan)
Loan_Repayment = [1000, 1000, 395]
LR = sum(Loan_Repayment)
Existing_Loan = Loans - LR

# We need to know what sum of loans I still need to pay

if Existing_Loan > 0:
    print(f'Existing loan: {Existing_Loan} USDT')
else:
    print(f'Loan is paid of')

# Balance

Balance = (R + P) - LR
print(f'Balance: {Balance} USDT')

# My own money

Own_Money = Balance - Existing_Loan
print(f'My own money: {Own_Money} USDT')



