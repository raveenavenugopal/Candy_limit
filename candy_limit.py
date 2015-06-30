import pygame,time,math
import sys
import random


pygame.mixer.init()
score=0
white=(255,255,255)
black=(0,0,0)
green=(0,255,0)
red=(255,0,0)
blue=(0,0,255)
gray=(128,128,128)
yellow=(255,204,0)
size=[650,600]
color=('red','blue','green','yellow')
xc=25
yc=125
chscr=0
count=0
flag=True
mouse=False
clock= pygame.time.Clock()
s=pygame.mixer.Sound("rav.wav")
no_of_moves=10
game_over=False

game=[ [0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0] ]


def event() :
        while True :
                for event in pygame.event.get() :
                        if event.type==pygame.QUIT :
                                sys.exit()
                                pygame.quit()
                        if event.type == pygame.KEYDOWN :
                                return True

def draw_screen() :
        screen.fill(black)
        i=0
        while i<(size[0]) :
                pygame.draw.line(screen,gray,(i,100),(i,size[1]))
                i+=50
        i=100
        while i<(size[1]) :
                pygame.draw.line(screen,gray,(0,i),(size[0],i))
                i+=50
	font=pygame.font.Font(None,80)
        scoreText = font.render("Rose", True, white)
        scoreRect = scoreText.get_rect()
        scoreRect.centerx=200
        scoreRect.centery=50
        screen.blit(scoreText,scoreRect)
	
	font=pygame.font.Font(None,40)
        scoreText = font.render("Score", True, white)
        scoreRect = scoreText.get_rect()
        scoreRect.centerx=450
        scoreRect.centery=20
        screen.blit(scoreText,scoreRect)

	font=pygame.font.Font(None,40)
        scoreText = font.render("Moves", True, white)
        scoreRect = scoreText.get_rect()
        scoreRect.centerx=550
        scoreRect.centery=20
        screen.blit(scoreText,scoreRect)

def display_score():
	font=pygame.font.Font(None,70)
        scoreText = font.render(str(score), True, white)
        scoreRect = scoreText.get_rect()
	pygame.draw.rect(screen,black,(400,35,200,50))
        scoreRect.centerx=450
        scoreRect.centery=60
        screen.blit(scoreText,scoreRect)
	pygame.display.update()

def display(string):
	font=pygame.font.Font(None,80)
        stri = font.render(str(string), True, white)
        sr = stri.get_rect()
	pygame.draw.rect(screen,black,(50,10,300,80))
        sr.centerx=200
        sr.centery=50
        screen.blit(stri,sr)
	pygame.display.update()

def display_moves(string):
	font=pygame.font.Font(None,70)
        stri = font.render( str(string), True, white)
        sr = stri.get_rect()
        sr.centerx=550
        sr.centery=60
        screen.blit(stri,sr)
	pygame.display.update()

        
def crush(x1,y1,x2,y2,x3,y3) :
	global score
	global chscr
	global flag
	y4=(x1+2)*50+25
	x4=(y1)*50+25
	y5=(x2+2)*50+25
	x5=(y2)*50+25
	y6=(x3+2)*50+25
	x6=y3*50+25
	pygame.draw.circle(screen,(255,110,180),(x4,y4),20)
	pygame.draw.circle(screen,(255,110,180),(x5,y5),20)
	pygame.draw.circle(screen,(255,110,180),(x6,y6),20)
	pygame.display.update()
	time.sleep(0.2)
	pygame.draw.circle(screen,black,(x4,y4),20)
	pygame.draw.circle(screen,black,(x5,y5),20)
	pygame.draw.circle(screen,black,(x6,y6),20)
	pygame.display.update()
	
	c=random.choice(color)
	if c=='red':
		color3=red
	if c=='green':
		color3=green
	if c=='blue':
		color3=blue
	if c=='yellow':
		color3=yellow
	pygame.draw.circle(screen,color3,(x4,y4),15)
	game[x1][y1]=c
	c=random.choice(color)
	if c=='red':
		color3=red
	if c=='green':
		color3=green
	if c=='blue':
		color3=blue
	if c=='yellow':
		color3=yellow

	pygame.draw.circle(screen,color3,(x5,y5),15)
	game[x2][y2]=c
	c=random.choice(color)
	if c=='red':
		color3=red
	if c=='green':
		color3=green
	if c=='blue':
		color3=blue
	if c=='yellow':
		color3=yellow

	pygame.draw.circle(screen,color3,(x6,y6),15)
	game[x3][y3]=c
	s.play()
	chscr+=1
	pygame.display.update()
#	score+=chscr
#	display_score()
	flag=True
	total_crush(flag)




def total_crush(f) :
	global flag
	global count
	global chscr,score
	i=0
	j=0
	while(f==True):
		for k in range(130):
			check_adj_init(i,j)
			i+=1
			if i==10:
				i=0
				j+=1
		if count==130:
			f=False
		else:
			count=0
			i=0
			j=0
		score+=chscr
		display_score()
		f=False
		flag=False
	if chscr==3 :
		display("Sweet")
	if chscr==2:
		display("Good")
	if chscr>=4:
		display("Fasty")
	chscr=0
	


def check_adj(cx,cy) :
	i=cx
	j=cy
	n=game[i][j]
	if i<8 and i>0:
		if (game[i+1][j]==n and game[i-1][j]==n):
			crush(i+1,j,i,j,i-1,j)
	if i<7 :
		if(game[i+1][j]==n and game[i+2][j]==n):
			crush(i,j,i+1,j,i+2,j)
	if i>1:
		if(game[i-2][j]==n and game[i-1][j]==n):
				crush(i-2,j,i-1,j,i,j)
	if j<11:
		if (game[i][j+1]==n and game[i][j+2]==n):
			crush(i,j,i,j+1,i,j+2)
	if j>1:
		if (game[i][j-1]==n and game[i][j-2]==n):
			crush(i,j-1,i,j,i,j-2)
	if j<12 and j>0:
		if (game[i][j-1]==n and game[i][j+1]==n):
			crush(i,j-1,i,j,i,j+1)


def check_adj_init(cx,cy) :
	global count
	i=cx
	j=cy
	n=game[i][j]
	if i<8 and i>0:
		if (game[i+1][j]==n and game[i-1][j]==n):
			crush(i+1,j,i,j,i-1,j)
	if i<7 :
		if(game[i+1][j]==n and game[i+2][j]==n):
			crush(i,j,i+1,j,i+2,j)
	if i>1:
		if(game[i-2][j]==n and game[i-1][j]==n):
				crush(i-2,j,i-1,j,i,j)
	if j<11:
		if (game[i][j+1]==n and game[i][j+2]==n):
			crush(i,j,i,j+1,i,j+2)
	if j>1:
		if (game[i][j-1]==n and game[i][j-2]==n):
			crush(i,j-1,i,j,i,j-2)
	if j<12 and j>0:
		if (game[i][j-1]==n and game[i][j+1]==n):
			crush(i,j-1,i,j,i,j+1)
	else:
		count+=1
	


def round_down(num, divisor):
	result= num - (num%divisor)
	if result%10==0:
		result+=25
	return result



def game1():
	global mouse,game_over,no_of_moves
	global score
	global chscr
	while game_over==False:
		if mouse==False:
			for event in pygame.event.get():
				
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

				if event.type == pygame.MOUSEBUTTONDOWN:
					display("Rose")
					mx1,my1 = pygame.mouse.get_pos()
					nx1=round_down(mx1,25)
					ny1=round_down(my1,25)
					i=(ny1/50)-2
					j=(nx1/50)
					c=game[i][j]
					if c=='red':
						color1=red
					if c=='green':
						color1=green
					if c=='blue':
						color1=blue
					if c=='yellow':
						color1=yellow
					pygame.draw.circle(screen,color1,(nx1,ny1),20)
					pygame.display.update()
					mouse=True
		if mouse==True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
					
				if event.type==pygame.MOUSEBUTTONDOWN:
					mx2,my2=pygame.mouse.get_pos()
					nx2=round_down(mx2,25)
					ny2=round_down(my2,25)
					k=(ny2/50)-2
					l=(nx2/50)
					c1=game[k][l]
					if c1=='red':
						color2=red
					if c1=='green':
						color2=green
					if c1=='blue':
						color2=blue
					if c1=='yellow':
						color2=yellow
					pygame.draw.circle(screen,color2,(nx2,ny2),20)
					pygame.display.update()
					time.sleep(0.1)
					pygame.draw.circle(screen,black,(nx1,ny1),21)
					pygame.draw.circle(screen,black,(nx2,ny2),21)
					pygame.display.update
					d=math.sqrt((nx2-nx1)*(nx2-nx1)+(ny2-ny1)*(ny2-ny1))
					if d==50:
						game[i][j]=c1
						game[k][l]=c
						pygame.draw.circle(screen,color2,(nx1,ny1),15)
						pygame.draw.circle(screen,color1,(nx2,ny2),15)
						check_adj(i,j)
						check_adj(k,l)
					
					else:
						pygame.draw.circle(screen,color1,(nx1,ny1),15)
						pygame.draw.circle(screen,color2,(nx2,ny2),15)
					pygame.display.update()
					score+=chscr
					display_score()
					if chscr==3 :
						display("Sweet")
					if chscr==2:
						display("Good")
					if chscr>=4:
						display("Fasty")
					chscr=0
					no_of_moves-=1
					display_moves(no_of_moves)
					if(no_of_moves==0):
						game_over=True
					mouse=False
	if game_over==True:
		display("Game over")

																	


pygame.init()
screen=pygame.display.set_mode(size,0,32)
pygame.display.set_caption("Candy Crush")
screen.fill(white)
font=pygame.font.Font(None,120)
Text1 = font.render('Candy Crush', True, (208,32,143))
Text2 = font.render('Game', True, (196,0,10))
Text3 = font.render("RAVEENA", True, (75,0,130))
Rect3 = Text3.get_rect()
Rect1 = Text1.get_rect()
Rect2 = Text2.get_rect()
Rect3.centerx=(size[0]/2)
Rect3.centery=(size[1]/2)+150
Rect1.centerx=(size[0]/2)
Rect1.centery=(size[1]/2)-150
Rect2.centerx=(size[0]/2)
Rect2.centery=(size[1]/2)
screen.blit(Text1, Rect1)
screen.blit(Text2, Rect2)
screen.blit(Text3, Rect3)
font=pygame.font.Font(None,30)
text = font.render("Press any key to continue", True, black)
rect = text.get_rect()
rect.centerx=size[0]-150
rect.centery=size[1]-50
screen.blit(text, rect)
pygame.display.update()

while True :
        if event() :
                break


while 1:
	
	draw_screen()
	for i in range(10):
		for j in range(13):
			c=random.choice(color)
			if c=='red':
				color1=red
			if c=='green':
				color1=green
			if c=='blue':
				color1=blue
			if c=='yellow':
				color1=yellow

			pygame.draw.circle(screen,color1,(xc,yc),15)
			game[i][j]=c
			xc+=50
		xc=25
		yc=yc+50
	xc=25
	yc=125
	pygame.display.update()
	time.sleep(1)
	total_crush(flag)
	display("Play game")
	display_moves(no_of_moves)
	game1()
	event()


