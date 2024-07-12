from os import system
system ("cls")

with open("employees.txt", 'w') as file:
    with open("manager_time.txt", 'w') as file2:
        for i in range(2):
            print()
            ism = input("Ismi: ")
            file.write(f"Ismi: {ism}\n")
            fam = input("familyasi: ")
            file.write(f"Familyasi: {fam}\n")
            lavozim = input("Lavozimi: ")
            file.write(f"Lavozimi: {lavozim}\n")
            oyligi = input("Ish haqqi: ")
            file.write(f"Ish haqqi: {oyligi}\n")
            

            
            if lavozim == 'manager':
                file2.write(f"Ismi: {ism}\nFamilyasi: {fam}\nLvozimi: {lavozim}\nIsh haqqi: {oyligi}\n\n")