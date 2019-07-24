from setting import *

def Prince(player):
	pygame.init()
	x = SCREEN_WIDTH - 50
	walkCount = 0
	images = [pygame.image.load(enemy_path + 'slime/slime-move-0.png'),pygame.image.load(enemy_path + 'slime/slime-move-1.png'),pygame.image.load(enemy_path + 'slime/slime-move-2.png'),pygame.image.load(enemy_path + 'slime/slime-move-3.png')]

	pygame.mixer.init()
	pygame.mixer.music.load('assets/sounds/clear.mp3')
	pygame.mixer.music.play(-1)

	prince_name = Font(20).render("PRINCE",True,WHITE)
	prince_name_rect = prince_name.get_rect()

	run = True
	while run:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
		screen.fill((30, 30, 30))
		screen.blit(pygame.image.load("assets/images/items/prince_bg.jpg"), (0,0))

		# draw player
		player.draw()
		player.x += 1

		# draw prince
		if walkCount + 1 >= 12:
			walkCount = 0
		screen.blit(images[walkCount//3], (x, SCREEN_HEIGHT - 50))
		walkCount += 1
		# prince name
		prince_name_rect.center = (x + 20,SCREEN_HEIGHT - 70)
		screen.blit(prince_name,prince_name_rect)
		x -= 1

		if(x<SCREEN_WIDTH/2):
			run = False
		pygame.display.flip()
		clock.tick(30)
	
def EndScreen():
	# title_font = Font(25)
	LEFT_CLICK = (1,0,0)
	RIGHT_CLICK = (0,0,1)
	title_y = -40

	# music
	pygame.mixer.init()
	pygame.mixer.music.load('assets/sounds/title.mp3')
	pygame.mixer.music.play(-1)

	# objects
	Title = Font(25).render("Python Monsters",True,WHITE)
	TitleRect = Title.get_rect()

	Coder = Font(15).render("by Group B",True,GREY)
	CoderRect = Coder.get_rect()

	Credit = Font(15).render("Credit",True,GREY)
	CreditRect = Credit.get_rect()
	Music = Font(15).render("Music: Wingless-seraph, DragonQuest",True,GREY)
	MusicRect = Music.get_rect()
	Image = Font(15).render("Image: RPGtkool",True,GREY)
	ImageRect = Image.get_rect()

	StartButton = Font(30).render("END",True,WHITE)
	StartRect = StartButton.get_rect()
	StartRect.center = (SCREEN_WIDTH/2,(SCREEN_HEIGHT/2) + CoderRect.height + CoderRect.height*5)

	Move = True
	while Move:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
		screen.fill(BLACK)
		TitleRect.center = (SCREEN_WIDTH/2, title_y - TitleRect.height)
		screen.blit(Title,TitleRect)
		CoderRect.center = (SCREEN_WIDTH/2,title_y)
		screen.blit(Coder,CoderRect)
		CreditRect.center = (SCREEN_WIDTH/2,title_y + CoderRect.height*2)
		screen.blit(Credit,CreditRect)
		MusicRect.center = (SCREEN_WIDTH/2,title_y + CoderRect.height*3)
		screen.blit(Music,MusicRect)
		ImageRect.center = (SCREEN_WIDTH/2,title_y + CoderRect.height*4)
		screen.blit(Image,ImageRect)

		pygame.display.flip()
		pygame.time.Clock().tick(30)
		title_y += 1
		if (title_y > (SCREEN_HEIGHT/2)):
			screen.blit(StartButton,StartRect)
			pygame.display.flip()
			Move = False

	PreviousClick = (0,0,0)
	Start = True
	while Start:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == KEYDOWN:
				if (event.key == K_RETURN):
					Start = False
			elif event.type == MOUSEBUTTONDOWN:
				PreviousClick = pygame.mouse.get_pressed()						
			elif event.type == MOUSEBUTTONUP:
				if (PreviousClick == LEFT_CLICK):
					if(pygame.mouse.get_pos()[0] > StartRect.x and\
						pygame.mouse.get_pos()[0] < StartRect.x + StartRect.width and\
						pygame.mouse.get_pos()[1] > StartRect.y and\
						pygame.mouse.get_pos()[1] < StartRect.y + StartRect.height):
							Start = False

def StartScreen():
	# title_font = Font(25)
	LEFT_CLICK = (1,0,0)
	RIGHT_CLICK = (0,0,1)
	title_y = -40

	# music
	pygame.mixer.init()
	pygame.mixer.music.load('assets/sounds/title.mp3')
	pygame.mixer.music.play(-1)

	# objects
	Title = Font(25).render("Python Monsters",True,WHITE)
	TitleRect = Title.get_rect()

	Coder = Font(15).render("by GroupB",True,GREY)
	CoderRect = Coder.get_rect()

	StartButton = Font(30).render("START",True,WHITE)
	StartRect = StartButton.get_rect()
	StartRect.center = (SCREEN_WIDTH/2,(SCREEN_HEIGHT/2) + CoderRect.height + StartRect.height)

	Move = True
	while Move:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
		screen.fill(BLACK)
		TitleRect.center = (SCREEN_WIDTH/2, title_y - TitleRect.height)
		screen.blit(Title,TitleRect)
		CoderRect.center = (SCREEN_WIDTH/2,title_y)
		screen.blit(Coder,CoderRect)
		pygame.display.flip()
		pygame.time.Clock().tick(30)
		title_y += 1
		if (title_y > (SCREEN_HEIGHT/2)):
			screen.blit(StartButton,StartRect)
			pygame.display.flip()
			Move = False

	PreviousClick = (0,0,0)
	Start = True
	while Start:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == KEYDOWN:
				if (event.key == K_RETURN):
					Start = False
			elif event.type == MOUSEBUTTONDOWN:
				PreviousClick = pygame.mouse.get_pressed()						
			elif event.type == MOUSEBUTTONUP:
				if (PreviousClick == LEFT_CLICK):
					if(pygame.mouse.get_pos()[0] > StartRect.x and\
						pygame.mouse.get_pos()[0] < StartRect.x + StartRect.width and\
						pygame.mouse.get_pos()[1] > StartRect.y and\
						pygame.mouse.get_pos()[1] < StartRect.y + StartRect.height):
							Start = False