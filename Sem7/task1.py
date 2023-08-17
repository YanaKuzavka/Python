#Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках
#не настолько просто, насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух считает, что 
#ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может 
#состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от 
#друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, 
#если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке
#*Пример:*
#**Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
#   **Вывод:** Парам пам-пам 
def countSounds(s):
    sounds = "уеыаоэяиюe"
    soundss=sounds+sounds.upper()
    cc=0
    for j in soundss :
        cc+= s.count(j)
    return cc
str1 = "пара-ра-рам рам-пам-папам па-ра-па-да"
s = str1.split()
print(s)
for w in s :
    print(w," :гласных:", countSounds(w))
ss = list(map(lambda x: countSounds(x), str1.split()))
print(ss)
if max(ss)==min(ss) :
    print("Парам пам-пам")
else :
    print("Пам парам")