import sys
print("\n\nPython Jeopardy\nCategories")

clue = {"Super Man" : "Clark Kent","Bruce Whayne":"Batman"}
#display categories
category = ["science  ","math  ","sports  "]
points = ["10","20","30","40","50"]

first = ["a\t","b\t","c\t"]
sec = ["1","2","3"]
third = ["a","b","c"]
fourth = ["1","2","3"]

def dispScreen(first):
	for i in range(0,3):
		sys.stdout.write(first[i])
	sys.stdout.write("\n")
#pick clues
#piCategory = input("Pick a cagegory")
#piPoints = input("Pick points")
#display clue
dispScreen(category)
dispScreen(first)
'''
print(state1[2])
#answer with question format
pick = input("points")

#compare answer with clue
if()



#score
print(state2[2])
'''

