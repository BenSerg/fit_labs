money_capital = 20000
salary = 5000
spend = 6000
increase = 0.05
months_count = 0
while money_capital + salary >= spend:
    months_count += 1
    money_capital -= spend - salary
    spend *= 1 + increase
print("Количество месяцев, которое можно протянуть без долгов:", months_count)
