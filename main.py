#When I compile the game there are viruses in it for some reason. I don't know why. So I'll just give you the code from the game. 

from random import randint
from time import sleep

print("Выберите язык. Choise language. 1) Русский. 2) English. Просто напишите число | Just type a number")
languagechoise = int(input()) # Выбор языка

allpassword = ["aghjk", "123gh", "lqpwe"]  #Список паролей

playermoney = 200

if languagechoise == 1:
	playername = input("Напишите ваше имя: ")
	print(f"Итак {playername}, вы решились взломать очень известную компанию, что-бы ваше имя осталось в потоках интернета на долгие времена.")

	tutorial1 = 0
	if tutorial1 == 0:
		print("Обучение")
		print("Что-бы начать изучать сюжетные вещи. Например язык программирование, ддос и т.д, напишите *Изучение*")
		playerchoose = input()
		if playerchoose == "Изучение" or playerchoose == 'изучение':
			print("Отлично вы во вкладке изучение. Здесь вы сможете изучать сюжетные вещи.")
			print(f"Изначально у вас есть {playermoney} долларов. Сейчас вы можете изучить основы C++. Просто напишите c++")
			playerchoose = input()
			if playerchoose == "c++" or playerchoose == "C++":
				print("Во время курсов вы научились, создавать простые программы, циклы условие. Для базового уровня сойдет.")

elif languagechoise == 2:
	playername = input("Write your name: ")
	print(f"So {playername}, you've decided to hack into a very famous company so that your name remains in the streams of the internet for a long time to come.")

	tutorial1 = 0
	if tutorial1 == 0:
		print("Tutorial")
		print("To start learning story things. For example programming language, ddos, etc., write *study*")
		playerchoose = input()
		if playerchoose == "study" or playerchoose == "Study":
			print("Great, you're in the explore tab. This is where you can explore story items.")
			print(f"Initially, you have {playermoney} dollars. You can now learn the basics of C++. Just write c++")
			playerchoose = input()
			if playerchoose == "c++" or playerchoose == "C++":
				print("During the course you learned how to create simple programmes, loop a condition. That's good for a basic level.")



input()
