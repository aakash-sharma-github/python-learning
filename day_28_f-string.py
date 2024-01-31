# Day 28
# f-string : String formating
# Example of string sormating
ex = "My name is {} and my email is {}" # this is string formating.
ex = "My name is {1} and my email is {0}" # using index string formating.
name = "Aakash"
email = "aakashsharma9855@gmail.com"
print(ex.format(name, email))
print(ex.format(email, name)) # In this case you can use indexing to place variables in correct place.

# Example of f-string
name1 = "Aakash"
fac = "CSE"
ex1 = f"my name is {name1} and I am a student of {fac}" #Put f before starting string.

print(ex1)

# numbers in f-string
price = 34.4567
text = f"price is {price: .2f} only" 
print(text)

# you can perform any expression in f-String
print(f"{2 * 4}")

