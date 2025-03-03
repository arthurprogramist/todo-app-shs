import random as rand
def igra():
    while True:
        a = input("---Привет! Это игра камень ножницы бумага, ты готов сыграть? ")
        if a == "Да" or a == "да" or a == "ДА":
            print(f"Красавчик, начинаем игру\n")
            print(f"1 это камень")
            print(f"2 это бумага")
            print(f"3 это ножницы\n")

            b = int(input("Введите число от 1 до 3: "))

            options = {1: "камень", 2: "бумага", 3: "ножницы"}
            print(f"Ты выбрал {options[b]}\n")


            random = rand.randint(1,3)
            print(f"Компьютер выбрал: {options[random]}\n")
            print(f"{options[b]} против {options[random]}")
            if random == b:
                print("Ничья! Ну ниче, сыграй еще")
            if random == 1 and b == 2 or random == 2 and b == 3 or random == 3 and b == 1:
                print(f"\n Вы выиграли, поздравляем!!! Сыграйте еще, раз уж вам везет:) \n")
            if random == 1 and b == 3 or random == 2 and b == 1 or random == 2 and b == 1:
                print(f"\n Вы проиграли, но не расстаривайтесь:)\n"
                      f"Сыграйте еще, вам повезет!")

            iii = input("Ты хочешь сыграть еще? ")
            if iii == "Да" or iii == "да" or iii == "ДА":
                continue
            else:
                print("Пока")
                break
        else:
            print("Пока!")
            break

igra()
