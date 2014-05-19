#This program will take an input of a Hearthstone pack and do various
#things with that (e.g., determine # of legendaries, other fun ratios, etc.)

import csv
import re

SAVEDPACKS = "savedpacks.csv" #global for the saved packs file
CARDLIST = "cardlist.csv" #list of hearthstone cards
carddict = {}

def MainMenu():
	PrintStars(20)
	print "Main Menu"
	PrintStars(20)
	print """
	Here are your options:
	1. Enter a new pack.
	2. View card list.
	3. Import card list.
	4. View statistics.
	T. Choose a card!
	Q. Quit
	"""
	choice  = raw_input("Choose an option: ")
	
	if choice == "1":
		EnterNewPack()
		MainMenu()
	elif choice == "2":
		PrintCardList()
		MainMenu()
	elif choice == "3":
		ImportList()
		MainMenu()
	elif choice.lower() == "t":
		SelectCard()
		MainMenu()
	elif choice.lower() == "q":
		exit()
	else:
		print "That isn't a valid option."
	
def ImportList():
	with open(CARDLIST,"r") as csvfile:
		cards = csv.reader(csvfile, delimiter = ',')
		for row in cards:
			currentcard = ' '.join(row)
			currentcard = currentcard.split()
						
			#combining the card title into the first item in the list
			currentcard[0] = currentcard[0:(len(currentcard)-1)] #combines them, excluding rarity (the last value)
			cardname = " ".join(currentcard[0]) #joins those values together, using a space as the separator
			cardname = cardname.lower() #make it lowercase
			
			rarity = currentcard[len(currentcard)-1]
			
			carddict[cardname] = rarity
			currentcard[1] = rarity


def PrintCardList():
	for name, rarity in carddict.items():
		print "%r, (%r)" % (name, rarity)
	
def SelectCard():
	selection = raw_input("Enter the name of the card: ")
	selection = selection.lower()
	current = ""
	found = 0
	
	PrintStars(5)
	
	with open(CARDLIST,"r") as csvfile:
		cards = csv.reader(csvfile, delimiter = ",")
		
		
		
		for row in cards:
			currentcard = ' '.join(row)
			currentcard = currentcard.split()
			
			currentcard[0] = currentcard[0:(len(currentcard)-1)]
			
			rarity = currentcard[len(currentcard)-1]
			
			cardname = " ".join(currentcard[0])
			cardname = cardname.lower()
					
			if cardname == selection:
				print "Aha! We found the card!"
				print "It's %r." % rarity
				found = 1 #indicates we found the card
				break
	
	if found == 0:
		print "That isn't a valid card." #if it's still 0 at this point, the card isn't there!
		
	PrintStars(5)

def EnterNewPack():
	#take entry of five cards, store them in a file
	#need to add option to specify golden cards
	print "Hi! You can enter your five cards in sequence."
	
	newpack = []
	
	while len(newpack) < 5:
		print "You need to enter %d more card(s). Type 'q' to quit." % (5 - len(newpack))
		entry = raw_input("Card: ")
		entry = entry.lower()

		if entry == "q":
			print "No pack added. Returning to Main Menu."
			MainMenu()
		elif CheckForCard(entry) == 1:
			newpack.append(entry)
			print "Added %r." % entry
			if len(newpack) == 5:
				print "You've added five cards!"
				print "Here's the pack:"
				for y in newpack:
					print y
		else:
			print "That isn't a valid card"
	
	
	
	
	
def CheckForCard(entry):
	#returns 1 if the card is in the list
	selection = entry
	selection = selection.lower()
	current = ""
	found = 0
	
	PrintStars(5)
	
	with open(CARDLIST,"r") as csvfile:
		cards = csv.reader(csvfile, delimiter = ",")
		
		
		
		for row in cards:
			currentcard = ' '.join(row)
			currentcard = currentcard.split()
			
			currentcard[0] = currentcard[0:(len(currentcard)-1)]
			
			rarity = currentcard[len(currentcard)-1]
			
			cardname = " ".join(currentcard[0])
			cardname = cardname.lower()
					
			if cardname == selection:
				found = 1 #indicates we found the card
				return 1
				break
	
	if found == 0:
		return 0 #returns 0 if no card is found
		
	PrintStars(5)
	
def PrintStars(n):
	print "*" * n
	
	
#Let's get it started!
ImportList()
MainMenu()

