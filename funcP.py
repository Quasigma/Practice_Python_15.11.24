wallet = {
    'dol': 456,
    'euro': 789,
    'tenge': 123
}
def deposit(wallet, currency, amount):
    if currency in wallet:
        wallet[currency] += amount
    else:
        wallet[currency] = amount
    print(f"Вы успешно внесли {amount} {currency}. Ваш новый баланс: {wallet[currency]} {currency}.")

def withdraw(wallet, currency, amount):
    if currency not in wallet:
        print(f"У вас нет средств в валюте {currency}.")
    elif wallet[currency] >= amount:
        wallet[currency] -= amount
        print(f"Вы успешно сняли {amount} {currency}. Ваш новый баланс: {wallet[currency]} {currency}.")
    else:
        print("Недостаточно средств для снятия.")

def check(wallet, currency):
    if currency in wallet:
        print(f"Ваш баланс: {wallet[currency]} {currency}")
    else:
        print(f"У вас нет средств в валюте {currency}.")

def main_program():
        action = input("Do you want to withdraw or deposit money? (Withdraw/Deposit/)\n")


        currency = input("Enter the currency (dol/euro/tenge):\n")
        try:
            amount = float(input("Enter an amount:\n"))
        except ValueError:
            print("Некорректная сумма.")

        if action == 'Withdraw':
            withdraw(wallet, currency, amount)
        elif action == 'Deposit':
            deposit(wallet, currency, amount)

        balance = input("Do you want to check your balance? (Yes/No)\n")

        if balance == 'Yes':
            check(wallet, currency)

main_program()

#--------------------------------------

def power(a, n):
    if n == 0:
        return 1

    return a * power(a, n - 1)

numbers = input("Enter numbers: ").split()
a = int(numbers[0])
n = int(numbers[1])

result = power(a, n)
print(f"{a} to the {n} power is {result}")

#--------------------------------------

def range_sum(a, b):
    if a > b:
        return 0
    return a + range_sum(a + 1, b)

numbers = input("Enter numbers: ").split()
a = int(numbers[0])
b = int(numbers[1])

result = range_sum(a, b)
print(f"Sum from {a} to {b} is {result}")

