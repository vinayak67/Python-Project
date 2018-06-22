import pygame
import time
import random                                            #to generate food randomly for snake.

pygame.init()		                                 #Initialising all pygame modules and return a tuple (no. of success,no.of failure).	
x=500						         #Screen Dimension.
y=500
snake_width=10			                         #thickness of snake  
screen=pygame.display.set_mode((x,y))			 #Since function needs necessary a tuple or a list ((width,height),flags,depth).
pygame.display.set_caption('Mamba')

white=(255,255,255)				         #assigning variable their respective to their name, RGB values. 					
black=(0,0,0)
blue=(0,0,50)
red=(255,0,0)
green=(0,102,0)
border=(64,64,64)
dull=(224,224,224)

font=pygame.font.SysFont("comicsansms",25)		 #creating object font by assigning its font style and text size.
font1=pygame.font.SysFont("comicsansms",18)
clock=pygame.time.Clock()
oops=pygame.image.load('startscreen.jpg')						
screen.blit(oops,(0,0))
pos_msg=font.render("Vinayak Gupta",True,black)	         #Displaying Personal Info
screen.blit(pos_msg,[180,330])
pos_msg=font.render("151448",True,black)
screen.blit(pos_msg,[220,370])
pygame.display.update()                                  #Image won't be displayed untile the screen is refreshed after pasting and image.
time.sleep(3)

head=pygame.image.load('head.png')		         #Image of head of snake.
direction="right"                                        #Snake's head position, up, down, left, right.

def pause():	                                         #Function that pause game when invoked
	paused=True
	while paused:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				pygame.quit()
				quit()
			if event.type==pygame.KEYDOWN:   #If any key is pressed during this loop.
				if event.key==pygame.K_SPACE:  #If pressed then which one?
					paused=False
				elif event.key==pygame.K_q:
					pygame.quit()
					quit()
		pos=pygame.image.load('pause.png')	#Displaying proper Image and message on screen.
		screen.blit(pos,(100,80))
		pos_msg=font.render("Press Space to play and Q to quit!",True,black)
		screen.blit(pos_msg,[50,390])
		pygame.display.update()
		
def score_board(score):				        #For Score and Function.
	text=font.render("Score: "+str(score),True,black)
	screen.blit(text,[10,5])
	text=font1.render("Press Space to Pause!",True,black)
	screen.blit(text,[300,12])
	
def rand_food():					#Function generatin food randomly and returning values as tuple
	food_x=round(random.randrange(4,x-snake_width-4)/10.0)*10.0	#random coordinate of Snake's food.	(3 is width of boundaries)
	food_y=round(random.randrange(44,y-snake_width-4)/10.0)*10.0	#rounded off to snake's thickness to make snake overlap food completely.
	return food_x,food_y
	
def mamba(snake_width,snakelist):			 #Function responsible for rotating snake's head according to 4 directions.
	if direction=="right":			         #Rotation works anti-clockwise.
		nhead=pygame.transform.rotate(head,270)
	if direction=="left":
		nhead=pygame.transform.rotate(head,90)
	if direction=="up":			         #Since image don't need to be rotated as in image head face upwards by default.
		nhead=head
	if direction=="down":
		nhead=pygame.transform.rotate(head,180)
	
	screen.blit(nhead,(snakelist[-1][0],snakelist[-1][1]))	#Displaying head of Snake
	for xny in snakelist[:-1]:				#Displaying snake's body till its max. length.
		pygame.draw.rect(screen,black,[xny[0],xny[1],snake_width,snake_width])	#Body blocks of Snake.
	
'''def message(mseg):														#function responsible to display message when you loose.
	loose=font.render(mseg,True,red)
	screen.blit(loose,[5,y/2])'''
	
	
def m_g_loop():
	global direction
	gameloop=True						    #main game loop (basically for holding the game screen).
	gameover=False
	head_x=x/2						    #Fresh or Updated location of Snake.
	head_y=y/2
	food_x,food_y=rand_food()				    #Calling function to generate food randomly.
	snakelist=[]
	snakelength=1                                               #Length of snake as it eats food.
	continous_x=0
	continous_y=0
	dim=1
	while gameloop:
		while gameover==True:
			while dim:
				if dim%2==0:
					go=pygame.image.load('gm.jpg')	#Game Over Message.						
					screen.blit(go,(0,0))
					pygame.display.update()
					time.sleep(0.4)
				elif dim%2!=0:
					go=pygame.image.load('gm1.jpg')	#Game Over Message.						
					screen.blit(go,(0,0))
					pygame.display.update()
					time.sleep(0.6)
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						quit()
					if event.type==pygame.KEYDOWN:						
						if event.key==pygame.K_q: #If user click close button instead of Q or closes game in Middle.
							quit()
						if event.key==pygame.K_p:
							m_g_loop()
				dim+=1
		                                     
					
		for event in pygame.event.get():			#built-in event handing.
			if event.type == pygame.QUIT:
				gameloop = False
			
			if event.type==pygame.KEYDOWN:		        #when key is pressed
				if event.key==pygame.K_LEFT:
					direction="left"
					continous_x =-snake_width
					continous_y =0			#To avoid diagonal movement problem
				elif event.key==pygame.K_RIGHT:
					direction="right"
					continous_x =snake_width
					continous_y =0		        #To avoid diagonal movement problem
				elif event.key==pygame.K_UP:
					direction="up"
					continous_y =-snake_width
					continous_x =0		        #To avoid diagonal movement problem
				elif event.key==pygame.K_DOWN:
					direction="down"
					continous_y =snake_width
					continous_x =0			#To avoid diagonal movement problem
				elif event.key==pygame.K_SPACE:		#If User wants to pause game.
					pause()
			'''if event.type==pygame.KEYUP:								#when key is released (If u want to move until key is pressed and then stop)
					if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:	
						continous_x=0'''
		
		if head_x>=x-3 or head_x<=3 or head_y>=y-3 or head_y<=43:      #Collision Detection. (last one is 43 due to score boundary)
			gameover=True
			time.sleep(2)	
			oops=pygame.image.load('oops.jpg')						
			screen.blit(oops,(0,0))
			pygame.display.update()
			time.sleep(1)					       #Holding Screen for 2 seconds
			pygame.display.update()
				
		head_x +=continous_x
		head_y +=continous_y
		
		screen.fill(white)					       #changing background color of screen.
		pygame.draw.rect(screen,black,[0,0,x,3])		       #North Boundry
		pygame.draw.rect(screen,black,[0,497,x,3])		       #South Boundry
		pygame.draw.rect(screen,black,[0,0,3,y])		       #West Boundry
		pygame.draw.rect(screen,black,[497,0,3,y])		       #East Boundary
		pygame.draw.rect(screen,black,[0,40,x,3])		       #Boundary below Score
		food=pygame.image.load('food.png')			       #loading image and then passing its object in next line.
		screen.blit(food,(food_x,food_y))
		
		snakehead=[]
		snakehead.append(head_x)
		snakehead.append(head_y)
		snakelist.append(snakehead)
		if len(snakelist) >snakelength:	
			del snakelist[0]                                        #To prevent continous stretching problem from the initial position of snake.
		
		for eachblock in snakelist[:-1]:
			if eachblock==snakehead:				#If head of snake is equal to any other segment of his body i.e. if snake eats himself
				gameover=True
				time.sleep(1)
				oops=pygame.image.load('oops.jpg')						
				screen.blit(oops,(0,0))
				pygame.display.update()
				time.sleep(2)					
			
		mamba(snake_width,snakelist)
		#screen.fill(white,[500,350,20,10])			        #alternative of constructing a rectangle.
		
		score_board(snakelength-1)                                      #by default length of snake is 1 due to its head therefore passing snakelength-1
		
		if head_x==food_x and head_y==food_y:	
			food_x,food_y=rand_food()				#To generate another food as soon as previous gets eaten.
			snakelength+=1					        #increasing length after eating food.
		pygame.display.update()						#Just like a flipbook that is changing frame to make it look like motion.		
	
	
		clock.tick(15)							#Value passed is frames per second (i.e. speed of snake)
	quit()
	
m_g_loop()

'''for generating .exe the setup.py file is coded and passed through cx_Freeze(stimulator to convrt .py to .exe by opening command Prompt in same directory
and writing "python Setup.py build" threby creating build folder containing .exe'''
