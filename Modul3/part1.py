var = 0
print(var == 0)

n = int(input("Please type a number:"))
if n > 100:
    print(True)
else:
    print(False)

the_weather_is_good = 'On Monday'
nice_restaurant_is_found = 'In Timisoara'
tickets_are_available = ''
check_for_price = 0
if the_weather_is_good:
    if nice_restaurant_is_found:
        print("have_lunch")
    else:
        print("We will eat_a_sandwich!")
else:
    if tickets_are_available:
        check_for_price = 100
    else:
        print("Go_shopping!")

