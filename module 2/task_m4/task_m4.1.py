def amount_payment(payment):
    total_payment = 0
    for paym in payment:
        if paym > 0:
            total_payment += paym
    return total_payment

payments_list = [100, -50, 200, -25, 50]
final_payment = amount_payment(payments_list)
print("Сума платежу наприкінці місяця:", final_payment)