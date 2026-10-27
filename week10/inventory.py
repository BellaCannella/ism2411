# Reflection Questions

# 1. The most surprising this is how lists in brackets are able to be freely changed.
#   I would expect brackets to be more like fixed variables compared.
#
#  2. At my current job as a lifeguard at USF, we have to manually put in our time cards and submit them.
#   With a list and loops to organize the information and calculate total hours worked along with how large 
#   the paycheck will be.




# Exercise 1: build a list

inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))

# Exercise 2: Index practice

print(inventory[0])
print(inventory[-1])

middle = len(inventory) //2
print(inventory[middle])

# Exercise 3: slicing

print(inventory[:3])
print(inventory[-2:])
print(inventory[::2])

# Excercise 4: Modify

inventory.append("envelope")
inventory.append("tape")
print(inventory)

inventory.remove("tape")
print(inventory)

inventory.sort()
print(inventory)

# Exercise 5: Tuple comparison

coords = (40.7128, -74.0060) # NYC coords

try:
    coords[0] = 99
except TypeError as error:
    print(f"TypeError caught: {error}")
    print("Tuples protect coordinates from being changed on accident")

# Exercise 6: Average list of sales

sales = [100, 250, 75, 480, 200]
total = sum(sales)
count = len(sales)
average = total / count 
print(f"Total Sales: {total}")
print(f"Number of Sales: {count}")
print(f"Average Sales: {average}")
print(f"Best Sale: {max(sales)}")
print(f"Worst Sale: {min(sales)}")

best = sales[0]
worst = sales[0]

for amount in sales:
    if amount > best:
        best = amount
    if amount < worst:
        worst = amount

print(f"Best sale (loop): {best}")
print(f"Worst sale (loop): {worst}")


# Exercise 7: Accumulator pattern

prices = [9.99, 14.99, 4.99, 24.99, 1.99]

discounted = []
for price in prices:
    discounted.append(round(price * 0.09,2))

print(prices)
print(discounted)


# Exercise 8: Filter

sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]
high_sales = []

for amount in sales:
    if amount > 300:
        high_sales.append(amount)

print(high_sales)
print(f"Count: {len(high_sales)}")
print(f"Average: {sum(high_sales)/len(high_sales):.2f}")







