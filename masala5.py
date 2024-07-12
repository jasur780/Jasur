from os import system
system ("cls")

with open("transactions.txt", 'w') as file:
    with open("big_spenders.txt", 'w') as file2:
        for i in range(2):
            print()
            nomi = input("Magsulot nomini kiriting: ")
            file.write(f"Magsulot nomi: {nomi}\n")
            id = int(input("ID: "))
            file.write(f"Magsulot ID si: {id}\n")
            narxi = int(input("Magsulot narxi: "))
            file.write(f"Magsulot narxi: {narxi}\n")
            soni = int(input("Soni: "))
            file.write(f"Magsulot soni: {soni}")
            

            
            if soni > 100:
                file2.write(f"Magsulot nomi: {nomi}\nMagsulot ID si: {id}\nNarxi: ${narxi}\nMagsulot soni: {soni}\n\n")