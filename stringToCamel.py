# def to_camel_case(string):
#     chars = list(string)
    
#     while '_' in chars or '-' in chars:
#         if '_' in chars:
#             chars = delete_seperator(chars, '_')
#         if '-' in chars:
#             chars = delete_seperator(chars, '-')

#     return ''.join(chars)

# def delete_seperator(chars, seperator):
#     index = chars.index(seperator)
#     del chars[index]
#     chars[index] = chars[index].upper()
#     return chars

def to_camel_case(string):
    result = []
    capitalize_next = False

    for char in string:
        if char in ['_', '-']:
            capitalize_next = True
        else:
            if capitalize_next:
                result.append(char.upper())
                capitalize_next = False
            else:
                result.append(char)

    return ''.join(result)



print('Should be \"\"')
to_camel_case(""), ""
print('Should be \"theStealthWarrior\"')
print(to_camel_case("the_stealth_warrior"))
print('Should be \"TheStealthWarrior\"')
print(to_camel_case("The-Stealth-Warrior"))
print('Should be "ABC"')
print(to_camel_case("A-B-C"))