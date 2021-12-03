# Programme qui converti la température Celcius en Fahrenheit

# Demande et calcule la température Celcius en Fahrenheit
def temp_Cel_En_Fah():
    tempCelcius = float(input("Inscrivez la température en Celcius : "))
    tempFahrenheit = (tempCelcius*9/5)+32
    return tempFahrenheit

# Affiche les résultats
tempFahrenheit = temp_Cel_En_Fah()
print("{0} degrées Fahrenheit".format(tempFahrenheit))

tempFahrenheit = temp_Cel_En_Fah()
print("{0} degrées Fahrenheit".format(tempFahrenheit))

tempFahrenheit = temp_Cel_En_Fah()
print("{0} degrées Fahrenheit".format(tempFahrenheit))

tempFahrenheit = temp_Cel_En_Fah()
print("{0} degrées Fahrenheit".format(tempFahrenheit))
