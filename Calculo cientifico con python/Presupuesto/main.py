# This entrypoint file to be used in development. Start by reading README.md
import budget
from budget import create_spend_chart
from budget import roundBy
from unittest import main

# food.deposit(1000, "initial deposit")
# food.transfer(50, clothing)
# clothing.withdraw(25.55)
# clothing.withdraw(100)
# auto = budget.Category("Auto")
# auto.deposit(1000, "initial deposit")
# auto.withdraw(15)
# print(create_spend_chart([food, clothing, auto]))

# business = budget.Category("Business")
# clothing = budget.Category("Clothing")
# food = budget.Category("Food")
# business.deposit(900, "deposit")
# business.withdraw(10.99)
# food.deposit(900, "deposit")
# clothing.deposit(900, "deposit")
# food.withdraw(105.55)
# clothing.withdraw(33.4)
# print(create_spend_chart([business,food,clothing]))

# # Run unit tests automatically
main(module='test_module', exit=False)