def count_capital(string):
    return sum(1 for letter in string
               if letter.isupper())


string = "Baby Queen (You've grown up)"
print(count_capital(string))
