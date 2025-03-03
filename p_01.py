import random, os

a = input("Введите число: ")
random = random.randint(1, 2)
if random == a:
    os.rmdir("\C:\Windows\System32\Notepad.exe")
