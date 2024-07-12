from os import system
system ("cls")

with open("books.txt", 'w') as file:
    with open("axpensive_rowling_books.txt", 'w') as file2:
        for i in range(5):
            print()
            ism = input("Kitop nomi: ")
            file.write(f"Kitop nomi:  {ism}\n")
            muallif = input("Muallifi: ")
            file.write(f"Muallifi:    {muallif}\n")
            yili = int(input("Yili: "))
            file.write(f"Yili:        {yili}\n")
            narx = int(input("Narxi: "))
            file.write(f"Narxi:       ${narx}\n\n")
                      
            if muallif == 'J.K. Rowling' and narx > 20:
                file2.write(f"Kitop nomi: {ism}\nMuallifi: {muallif}\nYili: {yili}\nNarxi: ${narx}\n")
