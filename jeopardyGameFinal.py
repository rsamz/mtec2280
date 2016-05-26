import time, sys, os, serial
##----python jeopardy game v.6-----##
#------rsamz spring 2016-------
#import serial
#data = serial.Serial('/dev/cu.usbmodem1441' , 9600)		#macintosh serial/com port to arduino
serial.Serial('COM4' , 9600)										#windows ver. serial/com port to arduino
x=0

#-------------------to declare variables and dictionaries to hold data-----------------------------

cat1='sports'
level = '300'
clue ={'100':{'super name':"superman secret id",'music albums':"reasonable doubt was the first",'sport':'jack johnson was first black champ of this sport'},
			'200':{'super name':"batman secret id",'music albums':'canadian rapper wants to be thanked later','sport':'tiger plays this sport at pebble beach'},
			'300':{'super name':"spiderman secret id",'music albums':'known as college dropout','sport':'pete rose bet on games of this sport'},
			'400':{'super name':"deadpool secret id",'music albums':'self titled record included song about jam-master jay and walk this way','sport':'air Jordan shoes are for playing this sport'}}

ans ={'100':{'super name':"clark kent",'music albums':'jay-z','sport':'boxing'},
			'200':{'super name':"bruce wayne",'music albums':'drake','sport':'golf'},
			'300':{'super name':"peter parker",'music albums':'kanye west','sport':'baseball'},
			'400':{'super name':"wade wilson",'music albums':'run dmc','sport':'basketball'}}			

score = {'100':{'super name':100,'music albums':100,'sport':100},
			'200':{'super name':200,'music albums':200,'sport':200},
			'300':{'super name':300,'music albums':300,'sport':300},
			'400':{'super name':400,'music albums':400,'sport':400}}			

myScore = 0
myPoint = 0
reps = 0
writeData = '97'
category = ["super name","music albums","sport"]
#def disPick(pick, category):#------pick=user input category is title name---------
while(reps < 3):															#----to ask for clue/ ans 3 times then send string to arduino------------
	print("\n\n//-------------------cagegories----------------\n")

	print(score['100'])
	print(score['200'])
	print(score['300'])
	cat1 = raw_input("pick a category?  ")					#----for keyboard input category/ points--------------
	level = raw_input("choose point amount?  ") 
	myPoint = 	score[level][cat1]
	while(myPoint == 0):									#---------dont allow user to choose same clue/points twice-----------------------
		print("//-----previously used, pick another ---------------")
		cat1 = raw_input("pick a category:  ")
		level = raw_input("choose point amount:  ") 
		myPoint = 	score[level][cat1]

	sys.stdout.write("\n")
	print('category = '+cat1 +'\t' +'points = ' + level)
	print('\nthe clue:   '+clue[level][cat1])
	storedAns = ans[level][cat1]
	time.sleep(3)
	myAns = raw_input("\n your answer:  ") 
	if(myAns == storedAns):										#--------to compare user answer to correct ans-------------
		print('\nwhat is,  '+storedAns)
		print("CORRECT !\n")
		myScore = myScore + myPoint
		score[level][cat1] = 0
		time.sleep(1)
	else:
		print('\nno the correct answer is '+storedAns)
		myScore -= myPoint
		score[level][cat1] = 0
	print('total points so far = ',myScore) 					#---------- to keep score add / subtract--------------
            
	reps += 1
	time.sleep(3)

	if(myScore == 100):											# ------to send score to arduino for dispalay 7-segment led as char-----------------
		writeData = 'a'
	if(myScore == 200):
		writeData = 'b'
	if(myScore == 300):
		writeData = 'c'
	if(myScore == 400):
		writeData = 'd'
	if(myScore == 500):
		writeData = 'e'
	if(myScore == 600):
		writeData = 'f'
	if(myScore == 700):
		writeData = 'g'
	if(myScore == 800):
		writeData = 'h'
	if(myScore == 900):
		writeData = 'i'	
	
	data.write(writeData)     					#!!!!!send score as string to arduino data converted as ASCII.
										#---use ASCII table to convert data into int inside arduino -------------

