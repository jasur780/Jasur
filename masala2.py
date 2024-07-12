from os import system
system ("cls")

with open("product.txt", 'w') as file:
    with open("cheap_products.txt", 'w') as file2:
        for i in range(5):
            print()
            magsulot_nomi = input("Mahsulot nomi: ")
            file.write(f"Magsulot nomi: {magsulot_nomi}\n")
            magsulot_narxi = int(input("Narxi: "))
            file.write(f"Narxi:         {magsulot_narxi}\n")
            magsulot_soni = int(input("Magsulot soni: "))
            file.write(f"Magsulot soni: {magsulot_soni}\n")
            
            if magsulot_narxi <= 10:
                file2.write(f"Magsulot nomi: {magsulot_nomi}\nMagsulot narxi: {magsulot_narxi}\nMagsulot soni: {magsulot_soni}\n\n")