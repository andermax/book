def sort_and_print_list(names):
    names.sort()
    for name in names:
        print(name.title())
def make_pizza(*toppings):
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)