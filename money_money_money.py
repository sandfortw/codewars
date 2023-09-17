def calculate_years(principal, interest, tax, desired):
    year = 0
    while principal < desired:
        earned_interest = principal * interest
        principal = principal + ((1 - tax) * earned_interest)
        year += 1
    return year
    
print("Should be 3:")
print(calculate_years(1000, 0.05, 0.18, 1100))
print("Should be 14:")
print(calculate_years(1000,0.01625,0.18,1200))
print("Should be 0:")
print(calculate_years(1000,0.05,0.18,1000))