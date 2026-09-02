print("Simple Budget Program")

total_budget = int(input("Enter total budget: "))
hall_rent = int(input("Enter hall rent: "))
food_budget = int(input("Enter food budget: "))
trophies_budget = int(input("Enter trophies budget: "))

total_spent = hall_rent + food_budget + trophies_budget
remaining_budget = total_budget - total_spent

print("Remaining budget:", remaining_budget)
