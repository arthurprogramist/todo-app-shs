# Задание выполнял:Абильмансур

words = ["apple", "banana", "cherry", "banana","banana"]
counter = 0

for word in words:
    if word == "banana":
        counter += 1
        print("banana")
    else:
        print('no banana')

print(counter)
