from cs50 import get_float
total = 0
while (total <= 0):
    total = get_float("Change owed: ")
total = total * 100
penny = 0
nickel = 0
dime = 0
quarter = 0
while (total > 0):
    if total >= 25:
        total -= 25
        quarter += 1
    elif total >= 10:
        total -= 10
        dime += 1
    elif total >= 5:
        total -= 5
        nickel += 1
    elif total >= 1:
        total -= 1
        penny += 1
print(penny + nickel + dime + quarter)
        
    
