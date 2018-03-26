#! python3

available_toppings =    ['mushrooms','olives','green peppers',
                        'pepperoni','pineapple','extra cheese']
requested_toppings = ['mushrooms','french fries','extra cheese']

for topping in requested_toppings:
    if topping in available_toppings:
        print("Adding " + topping + ".")
    else:
        print("Sorry, we don't have " + topping + ".")

print("\nFinished making your pizza!")
