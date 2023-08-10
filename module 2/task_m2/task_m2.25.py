PERCENT = 0.05

deposit = 100
waiting_year = 10

print(round(deposit * (1 + PERCENT / 12) ** (12 * 10), 2))


for year in range(1, waiting_year + 1):
    new_deposit = deposit * (1 + PERCENT / 12) ** 12
    deposit = new_deposit

print(round(deposit,2))
