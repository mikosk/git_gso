#Mikolaj Oskar Chojecki
#27.01.2017
#GSÖ verkefni git

file = open("gsogit.txt","w")

file.write("Hola evado una servesa por favor?")

file.close()

file = open("text.txt" , "r")

file.write("ég elska pizzu")
file.write("ég hata vakna snemma í skólann")
file.write("gsö er skemmtilegt")

file.close()

file = open("text.txt" , "r")

print(file.readline())

file.close()

