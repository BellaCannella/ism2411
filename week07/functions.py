# --- Self Assessment ---
# 1. The first bug I spotted was the lack of ":". I noticed it when I 
#    first ran the code because it told me that it was expecting the colon.
#    I think for me that shows me that I'm able to read the error signs correctly
#    and that I'm improving my understanding.
# 2. This is a function that takes the original price and the cutsomers discount tier
#    that they apply to and return the discounted price. The inputs
#    would be the price and tier, and the final disount price is what it returns.
#    I think a colleague could understand it as long as they understand what the tier means.
# 3. AI Disclosure: I used ChatGPT to help me understand Python concepts 
#    including list indexing, variable scope, and functions. I used it to
#    recieve explanations on how certain lines of codes worked along with
#    finding errors to complete this lab.
#    The AI helped me build my undertsanding once I started using it to learn and not do it for me.



# --- Exercise 1 --- 

# defining the function
def calculate_tax(price, rate):
    return price * rate

# calling the function
tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax for $100 at 7%: ${tax1:.2f}")
print(f"Tax for $250 at 8%: ${tax2:.2f}")
print(f"Tax for $350 at 5%: ${calculate_tax(350, 0.05):.2f}")

# --- Exercise 2 ---

def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver": 
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price 
# Calling the function
original_price = 200

for tier in ["gold", "silver", "bronze", "none"]:
    print(f"{tier}: ${apply_discount(original_price, tier):.2f}")

# --- Exercise 3 ---

def final_price(price, tax_rate, discount_tier):
    discounted_price = apply_discount(price, discount_tier)
    tax = calculate_tax(discounted_price, tax_rate)
    return discounted_price + tax

# calling the function
print(f"final_price(200, 0.07, 'gold') = {final_price(200, 0.07, 'gold'):.2f}")

# --- Exercise 4 ---

rate = 0.07
orders = [(200, 'gold'), (150, 'silver'), (80, 'bronze'), (500, 'none')]


for price, tier in orders:
    total = final_price(price, rate, tier)
    print(f"price: ${price} | tier: {tier} | total: ${total:.2f}")

 # --- Exercise 6 ---

x = 100     # global variable
def double_it():
    x = 999    # local variable
    return x * 2

print(x)  # prints 100
print(double_it()) # prints 1998
print(x)  # prints 100 again

# A scope means where a variable is located and how it's accessed.
# Because the local variable is inside it's own function, it doesn't
# automatically change the gloable varibale because it's seperate.

