def solve(string):
    vowels = ('a', 'e', 'i', 'o', 'u')
    counter = 0
    counts = []
    last_letter = ''
    while len(string) > 0:
        current_letter = string[0]
        if current_letter in vowels and last_letter in vowels:
            counter += 1 
        elif current_letter in vowels: 
            counter = 1
        else:
            counts.append(counter)
            counter = 0
        string = string[1:]
        last_letter = current_letter
    return max(counts)
    
        
print("Should be 2:")
print(solve("codewarriors"))