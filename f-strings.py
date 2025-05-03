letter = "Hey my name is {1} and I am from {0}"
name = "Ujjwal"
country = "India" 

# print(letter.format(name, country))
# print(letter.format(country, name))
print(f"We use f-strings like this:Hey my name is {{name}} and I am from {{country}}")  
price = 49.09999  
txt = f"For only {price:.2f} dollars!"
print(txt)
# print(txt.format())

print(type(f"{2 * 30}"))