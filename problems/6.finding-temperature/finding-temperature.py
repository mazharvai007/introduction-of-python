get_temperature = int(input("Enter temperature (-40 - 60): "))

if get_temperature >= -40 and get_temperature <= 0:
    print("It's too cold.")
elif get_temperature >= 1 and get_temperature <= 25:
    print("It's cold.")
elif get_temperature >= 26 and get_temperature <= 30:
    print("It's normal.")
elif get_temperature >= 31 and get_temperature <= 40:
    print("It's warm.")
elif get_temperature >= 41 and get_temperature <= 60:
    print("It's too warm.")
else:
    print("Invalid temperature")
