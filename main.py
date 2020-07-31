print("THIS IS NOAH BUCHANAN'S CODE, YOU CAN GET INSPIRATION FROM THIS BUT PLEASE DON'T Copy")

#IMPORTS
from termcolor import colored,cprint
import math
import time



#VARIABLE
twenty = (colored("~~~~~~~~~~~~~~~~~~~~", "yellow"))
twenty2 = (colored("~~~~~~~~~~~~~~~~~~~~\n{}", "yellow").format(twenty))



please = colored("SOMETHING ELSE WENT WRONG PLEASE TELL NOAH.","green")

#FUNCTIONS

#FUTURE PERSON, THIS IS MADE FOR THE line_lengths function and helps clean the code for all of the possible ax,ay,bx,by options, type the print thing as opposed to this 4 times.
def options(ab,xy,strab):
	print(colored("EDGE {}:","red").format(strab))
	return(colored("(LENGTH ON {} AXIS: {})\n{}","red").format(xy,ab,twenty))


#calculates ROC based on the arguments, simple, math book formula already has it, made this a long time ago but made it better through colors and exception handling, making it so that the code runs no matter what.
def midpoint(x1,y1,x2,y2):
	try:
		midx=x1+x2
		midy=y1+y2
		midx = midx/2
		midy = midy/2
		print(colored("MIDPOINT IS: ({},{})","red","on_white").format(midx,midy))
	except:
		print(colored("SOMETHING WENT WRONG, TRY AGAIN...THIS ISN\'T NORMAL\n           - NOAH.","green"))
def line_distance(x1,y1,x2,y2):
	try:
		xsqr1 = (x2-x1)
		xsqr = xsqr1**xsqr1
		print("x square is: {} then: {}".format(xsqr1,xsqr1))
		ysqr1 = (y2-y1)
		ysqr = ysqr1**ysqr1
		print("y square is: {} then: {}".format(ysqr,ysqr1))
		add = (xsqr + ysqr)
		print(add)
		distance = math.sqrt(add)
		print(twenty)
		print(colored("THE DISTANCE OF POINT ({},{}) TO POINT ({},{}) IS:","red").format(x1,y1,x2,y2))
		print(twenty)
		print(distance)
		return(twenty)
	except:
		print(colored("SOMETHING WENT WRONG, TRY AGAIN...THIS ISN\'T NORMAL\n           - NOAH.","green"))

def ROC(x1,x2,y1,y2):
	try:
		y = y2-y1
		x = x2-x1 
		print(colored("ROC IS:","yellow"))
		print(twenty)
		yx = y/x
		return(colored("{} / {} : {}","red","on_white").format(y,x,yx))
	except ZeroDivisionError:
		print(twenty2)
		return(colored("CANNOT DIVIDE BY 0(or something else)\nTRY AGAIN","green"))
	



def line_lengths(x1,x2,y1,y2):
	try:
		global ay
		global ax
		global bx
		global by
		if bool == True:
			print(colored("\n!!!!\nTHERE ARE 2 POSSIBLE OPTIONS FOR EACH(a and b) LINE, IF YOU CHOOSE THE FIRST FOR ONE CHOOSE THE SECOND FOR THE OTHER\nDEFAULT IS (AX,BY)\n!!!!!","green","on_red").format(twenty,twenty,twenty,twenty))
		elif bool == False:
			pass
		ay = abs(y2 - y1)
		ax = abs(x2 - x1)
		by = abs(y2 - y1)
		bx = abs(x2 - x1)
		print("\n")
		print(options(ax,"X","AX"))
		print(options(by,"Y","BY"))
		print(twenty2)
		print(colored("THE OTHER TWO OPTIONS (AY,BX) ARE:","yellow"))
		print(options(ay,"Y","AY"))
		return(options(bx,"X","BX"))
		bool == False
	except :
		print(colored("SOMETHING WENT WRONG, TRY AGAIN...THIS ISN\'T NORMAL\n- NOAH.","green"))
	


def triangle(ax, by):
	try:
		a2 = ax*ax
		b2 = by*by
		c2 = a2+b2
		text = (colored("({a})^2 + {b}^2 = {c2}","red").format(a=ax,b=by,c2=c2))
		print(text)
		print(twenty2)
		print(twenty)
		print(colored("C^ =","red","on_white"))
		print(colored(c2,"red"))
		print(twenty2)
		print(colored("SQUARE ROOT OF C/LENGTH OF POINT ({},{}) TO POINT ({},{}) =\n","red").format(x1,y1,x2,y2))
		sqrtc = math.sqrt(c2)
		return(sqrtc)
	except :
		print(colored("SOMETHING WENT WRONG, TRY AGAIN...THIS ISN\'T NORMAL\n- NOAH.","green"))





def calc(word):
	try:
		for i in range(0,5):
			print(colored("CALCULATING {}","green").format(word))
			print(twenty)
			time.sleep(.2)
	except AttributeError:
		print("no")




#RUNNING
print(twenty2)
print(twenty2)
print(twenty2)
print(colored("CODED BY NOAH. IF YOU KNOW ME YOU DO.\nIF YOU DON\'T YOU DON\'T","green"))
print(twenty2)
print(twenty2)
print(twenty2)
print("\n\n\n\n")
print(colored("THIS CALCULATOR WILL SOLVE THE PYTHAGOREAN THEOREM, SLOPE/ROC, TELL ALL POINTS AND THEIR LINE LENGTH, AND MIDPOINTS(update 3-17-2020)\nENTER TWO POINTS IN THIS FORMAT:\n(x1,y1)\n(x2,y2)","red"))
while True:
	try:
		print(colored("------------------------------------------------","red","on_blue"))
		print(twenty)
		x1 = float(input(colored("ENTER X1:","yellow")))
		print(twenty)
		y1 = float(input(colored("ENTER Y1:","yellow")))
		print(twenty)
		x2 = float(input(colored("ENTER X2:","yellow")))
		print(twenty)
		y2 = float(input(colored("ENTER Y2:","yellow")))
		print(twenty)
		print(twenty)
		print(ROC(y2,y1,x2,x1))
		#print(calc("PLATAGOREAM_MEAURES"))
		print(line_lengths(x1,x2,y1,y2))
		#print(twenty2)
	  #print(line_distance(x1,y1,x2,y2)) # causing a problem that i can\'t figure out - mathbook saiys that the formula is the same as a^ b^ = c^ stuff
		print(twenty2)
		print(triangle(ax,by))
		print(twenty2)
		print(midpoint(x1,y1,x2,y2))
	except ValueError:
		print(twenty)
		print(colored("INPUT A VALID NUMBER(NOT LETTERS OR SYMBOLS, ONLY NUMBERS WITH ONE DECIMAL OR NONE AT ALL)","green"))