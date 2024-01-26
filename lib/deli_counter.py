katz_deli = []

def line (katz_deli):
    pass
    # shows everyone their place in line => "The line is currently: {1}. {Ada} {2}. {Grace} ..."
    # if empty return => "The line is currently empty"
    if len(katz_deli) == 0:
        print("The line is currently empty.")
    else:
        listed = []
        for name in katz_deli:
            x = katz_deli.index(name) + 1
            listed.append(f"{x}. {name}")
        x = " ".join(listed)
        print(f"The line is currently: {x}")
    
def take_a_number (katz_deli, name):
    katz_deli.append(name)
    number = katz_deli.index(name) + 1
    print(f"Welcome, {name}. You are number {number} in line.")
    return katz_deli

def now_serving (katz_deli):
    pass
    if len(katz_deli) == 0:
        print("There is nobody waiting to be served!")
    else:
        print(f"Currently serving {katz_deli[0]}.")
        del katz_deli[0]
    return katz_deli