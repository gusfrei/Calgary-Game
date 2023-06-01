print('''

'   ██████ █████ ██     ██████  █████ ████████    ██     ██████  █████ ███    ██████████ 
'  ██     ██   ████    ██      ██   ████   ████  ██     ██      ██   ██████  ██████      
'  ██     █████████    ██   ████████████████  ████      ██   ████████████ ████ ███████   
'  ██     ██   ████    ██    ████   ████   ██  ██       ██    ████   ████  ██  ████      
'   ████████   ███████████████ ██   ████   ██  ██        ██████ ██   ████      █████████ 
'                                                                                        
'                                                                                        

''')


print("Bem vindo ao Calgary Game.")
print("A sua missão é sobreviver ao inverno Canadense.\n") 


#Write your code below this line 👇

print("Parabéns, você chegou em Calgary de carro.\n")
f = input("Onde você quer ir primeiro? Canadian Tire ou IKEA?: \n" )
f_lower = f.lower()



if f_lower == "canadian tire": 
    s = input("\nVocê quer colocar pneu de neve ou comprar churrasqueira? Digite pneu de neve ou churrasqueira\n")
    s_lower = s.lower()
    if s_lower == "pneu de neve":
        print("\nPneu de neve trocados com sucesso.\n")
        t = input("Você quer jantar em qual restaurante? Digite Sushi, Captain Boil ou Hooters\n")
        t_lower = t.lower() 
        if t_lower == "sushi":
            print("\nSUSHINHO CAIU BEM HEIN.... PAI TÁ ON EM CALGARY. VOCÊ VENCEU O JOGO! \n")
        elif t_lower == "hooters":
            print("\nXiiiii... Aquela asinha não caiu bem. GAME OVER!")
        elif t_lower == "captain boil":
             print("\nXiiiiii...O camarão tava muito apimentado e deu caganeira. GAME OVER!")
        else:
            print("\nNão sabe nem digitar e quer jogar o joguinho? GAME OVER!")
    elif s_lower == "churrasqueira":
      print("\nXiiiii... teu prédio não permite churrasqueira. GAME OVER!\n")
    else:
      print("\nNão sabe nem digitar e quer jogar o joguinho? GAME OVER!")
elif f_lower == "ikea":  
  print("Você derrapou antes de chegar na IKEA. GAME OVER!")
else:
  print("Eu te dei só duas opções caralho. Tu é burro? GAME OVER!")
    




