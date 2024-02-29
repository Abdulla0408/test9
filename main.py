# Fayllar bilan ishlash

# ----------------------------------------------------------------

# Faylni ochish

file = open("navoiy.txt", encoding = "utf-8")

content = file.read()
print(content)
file.close()

# ----------------------------------------------------------------

# r - read() - O'qish
# w - write() - Yozish
# a - append() - Qo'shish
# rb - readytes() - O'qish
# wb - writebytes() - Yozish

# ----------------------------------------------------------------

# Fayllarga yozish

file = open("test.txt", mode = "w",encoding = "utf-8")
file.write("\nHello, World!")
print(file)
file.close()

# ----------------------------------------------------------------

file = open("bobur.txt", mode = "r", encoding = "utf-8")
content = file.read()

bobur_copy = open("Bobur_copy.txt", mode = "w", encoding = "utf-8")
bobur_copy.write(content)
print(bobur_copy)

file.close()
bobur_copy.close()

# ----------------------------------------------------------------

file = open("navoiy.txt", mode = "r", encoding = "utf-8")
content  =  file.read()

navoiy_copy = open("navoiy_copy.txt", mode = "w", encoding = "utf-8")
navoiy_copy.write(content)
print(navoiy_copy)

file.close()
navoiy_copy.close()

# ----------------------------------------------------------------

i = 1
while True:
    first_name = input("Ism: ")
    if first_name == "stop":
        break

    last_name = input("Familiya: ")
    age = int(input("Yosh: "))
    addres = input("Manzil: ")

    text = f"""{i}. Ism: {first_name}
Familiya: {last_name}
Yosh: {age}
Manzil: {addres}\n\n"""
    print(text)

    file = open("info.txt", mode = "a", encoding = "utf-8")
    file.write(text)

    i+=1
    
    print(file)
    file.close()

# # ----------------------------------------------------------------

file = open("tong.jpg", mode = "rb")
content = file.read()

morning_copy = open("morning_copy.gif", mode = "wb")
morning_copy.write(content)

file.close()
morning_copy.close()

# # ----------------------------------------------------------------

import csv
with open("user_info.csv",mode = "w") as file:
    writer = csv.writer(file, delimiter = ";")
    writer.writerow("NAME", "USERNAME", "AGE", "ADDRESS")
    
with open("user_info.csv",mode = "a") as file:
    writer = csv.writer(file, delimiter = ";")
    writer.writerow("Sobir", "Sobirov", 45, "Ferghana")

l = []
with open("bobur.txt") as file:
    content = file.readlines()
    print(content)

with open("color_srgb.csv",mode = "r") as csv_file:
    print(list(csv_file))



def find_word(file_name, word):
    file = open(file_name, "r")
    text =file.read()
    file.close()

    words = text.split()
    count = word.count(word)
    return count

print(find_word("text.txt", "yoruglik"))

def find_word(file_name, word):
    file = open(file_name, "r")
    text = file.read()
    file.close()
    words = text.split()
    count = words.count(word)
    return count
print(find_word("test.txt", "Abdulla Hayitboyev"))
4

