print('''

'   ██████ █████ ██     ██████  █████ ████████    ██     ██████  █████ ███    ██████████ 
'  ██     ██   ████    ██      ██   ████   ████  ██     ██      ██   ██████  ██████      
'  ██     █████████    ██   ████████████████  ████      ██   ████████████ ████ ███████   
'  ██     ██   ████    ██    ████   ████   ██  ██       ██    ████   ████  ██  ████      
'   ████████   ███████████████ ██   ████   ██  ██        ██████ ██   ████      █████████ 
'                                                                                        
'                                                                                        

''')

print("Welcome to the Calgary Game.")
print("Your mission is to survive the Canadian winter.\n")

print("Congratulations, you've arrived in Calgary by car.\n")
f = input("Where do you want to go first? Canadian Tire or IKEA?: \n")
f_lower = f.lower()

if f_lower == "canadian tire":
    s = input("\nDo you want to get snow tires or buy a barbecue? Type snow tires or barbecue\n")
    s_lower = s.lower()
    if s_lower == "snow tires":
        print("\nSnow tires changed successfully.\n")
        t = input("Where do you want to eat dinner? Type Sushi, Captain Boil or Hooters\n")
        t_lower = t.lower()
        if t_lower == "sushi":
            print("\nSushi hit the spot! YOU WIN THE GAME! \n")
        elif t_lower == "hooters":
            print("\nOuch! Those wings didn't agree with you. GAME OVER!")
        elif t_lower == "captain boil":
            print("\nYikes! The shrimp was too spicy. GAME OVER!")
        else:
            print("\nGAME OVER!")
    elif s_lower == "barbecue":
        print("\nOops! Your building doesn't allow barbecues. GAME OVER!\n")
    else:
        print("\n GAME OVER!")
elif f_lower == "ikea":
    print("You slipped before reaching IKEA. GAME OVER!")
else:
    print("I only gave you two options. GAME OVER!")


