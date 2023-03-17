# Codewars 

def descending_order(num):
    return int("".join(sorted([num for num in num], reverse=True)))

print(descending_order("42145"))