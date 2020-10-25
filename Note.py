import os
while True:
	a = int(input("\n[0] Exit\n[1] Edit notes\n[2] New notes folder\n[3] Read notes \n[4] Replace new notes\n[5] Note folder names\n[6] https://t.me/PowerBot_TM\nEnter a number >>>> "))
	if a == 1:
		listread = open("list.txt","r")
		print(listread.readline())
		for line in listread:
			print(line)
		listread.close()
		wea = input("Select the name of the note folder to edit the note! ")
		f = input(f"Write your note to edit and add to the {wea} note folder ")
		k = open(f"{wea}.txt","a")
		k.write(f"\n{f}\n")
		k.close()
		print("Edited successfully!\n")
	
	elif a == 2:
		h = input("Enter the name of the note folder! ")
		ed = input("Enter your text to add to the notes folder ;) ")
		w = open(f"{h}.txt","a")
		w.write(f"\n{ed}\n")
		w.close()
		list = open("list.txt","a")
		list.write(f"{h}\n")
		list.close()
		print("Successfully built!\n")
	elif a == 3:
		listread = open("list.txt","r")
		print(listread.readline())
		for line in listread:
			print(line)
		listread.close()
		fg = input("Enter the name of the note folder to read :) ")
		kd = open(f"{fg}.txt","r")
		print(kd.readline())
		for line in kd:
			print(line)
		kd.close()
		
	elif a == 4:
		listread = open("list.txt","r")
		print(listread.readline())
		for line in listread:
			print(line)
		listread.close()
		omid = input("Enter the name of the note folder! ")
		kl = input(f"Enter your text to replace in the note in the {omid} folder! ")
		des = open(f"{omid}.txt","w")
		des.write(f"\n{kl}")
		des.close()
		print("Successfully replaced!\n")
	
	elif a == 5:
		print("The name of your note folder:\n")
		listread = open("list.txt","r")
		print(listread.readline())
		for line in listread:
			print(line)
		listread.close()
		
	elif a == 6:
		print("\ntelegram chanell :\n@PowerBot_TM")
	elif a == 0:
		print("\nGood Time ;)")
		break