from os import system
system ("cls")

with open("students.txt", 'w') as file:
    with open("high_achievers.txt", 'w') as file2:
        for i in range(5):
            print()
            ism = input("Ismi: ")
            file.write(f"Ismi: {ism}\n")
            yosh = int(input("Yosh: "))
            file.write(f"Yoshi: {yosh}\n")
            baholar = input("Baholar(, bilan kiriting): ")
            baholar_list = list(map(int, baholar.split(',')))
            file.write(f"Baholar: {baholar}\n")
            
            ortacha_baho = sum(baholar_list) / len(baholar_list)
            
            malumot = {
                "Ismi": ism,
                "Yoshi": yosh,
                "Boholar": baholar_list,
                "Ortacha baho": ortacha_baho
            }
            file.write(f"Ortacha baho: {ortacha_baho}\n")
            
            if ortacha_baho >= 70:
                file2.write(f"Ismi: {ism}\nYosh: {yosh}\nOrtacha baho: {ortacha_baho}\n\n")
