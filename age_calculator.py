nombre = input ("Ingresas tu nombre: ")
year = int(input ("¿En qué año naciste? "))
age = 2024 - year
if year >= 1930 and year <= 1948:
    print("Hola,", nombre, "Tienes", age, "años y eres un niño de la posguerra")
elif year >= 1949 and year <= 1968: 
    print("Hola,", nombre, "Tienes", age, "años y eres un Baby Boomer")
elif year >= 1969 and year <= 1980: 
    print("Hola,", nombre, "Tienes", age, "años y eres generación X")
elif year >= 1981 and year <= 1993: 
    print("Hola,", nombre, "Tienes", age, "años y eres un Millenial")
elif year >= 1994 and year <= 2010:
    print("Hola,", nombre, "Tienes", age, "años y eres generación Z")
elif year >= 2011:
    print("Hola,", nombre, "Tienes", age, "años y eres gneración Alfa")
