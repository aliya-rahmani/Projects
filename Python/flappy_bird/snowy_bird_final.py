import pygame ,sys ,random
def draw_floor():
    screen.blit(floor_surface,(floor_x_pos,250))
    screen.blit(floor_surface,(floor_x_pos + 400,250))

def create_pipe():
    random_pipe_pos = random.choice(pipe_height) #create random heighted pipes from  defined list
    new_pipe = pipe_surface.get_rect(midtop =(400,random_pipe_pos))#half coordinates of our display screen
    
    return new_pipe

def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    return pipes

def draw_pipes(pipes):
    for pipe in pipes:
        screen.blit(pipe_surface,pipe)
        
def check_collision(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe): #checking for coliisions of bird and pipe rectangles
            death_sound.play()
            return False
            
    if bird_rect.top <= -300 or bird_rect.bottom >= 1000:
        print ("boom")
        death_sound.play()
        return False
         
    return True    

def rotate_bird(bird):
    new_bird = pygame.transform.rotozoom(bird,-bird_movement *3 ,1)
    return new_bird

def score_display(game_state):
    if game_state == 'main_game':
        
       score_surface = game_font.render(str(int(score)),True,(255,255,255))#255 255 255 are red green blue tupples and gives font colour
       score_rect = score_surface.get_rect(center = (200,50))
       screen.blit(score_surface,score_rect)
    
    if game_state == 'game_over':
        score_surface = game_font.render(f'Score: {int(score)}',True,(255,255,255))
        score_rect = score_surface.get_rect(center = (200,50))
        screen.blit(score_surface,score_rect)
        
        high_score_surface = game_font.render(f'High Score: {int(high_score)}',True,(255,255,255))
        high_score_rect = high_score_surface.get_rect(center = (200,80))
        screen.blit(high_score_surface,high_score_rect)
        
def update_score(score,high_score):
    if score > high_score:
        high_score = score
    return high_score        
        
        
        
#pygame.mixer.pre_init(frequency = 44100,size 16 ,channels =1, buffer = 512)    
pygame.init()
screen = pygame.display.set_mode((400,330))#pixels for display screen
clock = pygame.time.Clock() #this clock is used for limiting our FPS
game_font = pygame.font.Font('./KelsonSans-Bold.ttf',30)


#Game variables
gravity = 0.32
bird_movement = 0
game_active = True
score = 0
high_score = 0


bg_surface = pygame.image.load('./background.jpg').convert()
bg_surface = pygame.transform.scale2x(bg_surface)

floor_surface = pygame.image.load('./base.png').convert()
floor_surface = pygame.transform.scale2x(floor_surface)
floor_x_pos = 0

bird_surface = pygame.image.load('./bird.png').convert_alpha()
#bird_surface = pygame.transform.scale2x(bird_surface)
bird_rect = bird_surface.get_rect(center=(30,115))

pipe_surface = pygame.image.load('./bpipe.png').convert()
#pipe_surface = pygame.transform.scale2x(pipe_surface)
pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE,1200)#timer for pipes in ms
pipe_height = [100,120,150,250,20,50,300,405]

game_over_surface =( pygame.image.load('./game over.png').convert_alpha())
game_over_rect = game_over_surface.get_rect(center =( 200,165))

#SOUNDS
flap_sound = pygame.mixer.Sound('./swoosh.wav')
death_sound = pygame.mixer.Sound('./hit.wav')
score_sound = pygame.mixer.Sound('./point.wav')
score_sound_countdown = 100
    


while True:
    #image of player 1
    #background image
    #EVENT LOOP
    for event in pygame.event.get():  #cmd look for any events occuring
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN: #this checks if any key is pressed
            if event.key == pygame.K_SPACE and game_active: #this checks which key is pressed
                bird_movement=0
                bird_movement -= 11
                flap_sound.play()
            if event.key == pygame.K_SPACE and game_active == False:
                game_active =True 
                pipe_list.clear()              
                bird_rect.center = (30,115)
        
                bird_movement=0
                
                score = 0
                
        if event.type == SPAWNPIPE:
            pipe_list.append(create_pipe())
            
            
            
    screen.blit(bg_surface,(0,0))
    
    #GAME LOOP
    
    
    if game_active:
        
        
        
        
    
        #BIRDS
        bird_movement += 0.8*gravity # for making bird fall
        rotated_bird = rotate_bird(bird_surface)
        bird_rect.centery += bird_movement #this allows bird to fall continously
        screen.blit(rotated_bird,bird_rect)
    
        game_active = check_collision(pipe_list)
    
        #PIPES
        pipe_list = move_pipes(pipe_list)
        draw_pipes(pipe_list)
        
        score += 0.03
        score_display('main_game')
        score_sound_countdown -=1
        if score_sound_countdown <=0:
            score_sound.play()
            score_sound_countdown = 80
        
    else:
        screen.blit(game_over_surface,game_over_rect)
        high_score = update_score(score,high_score)
        score_display('game_over')
        
    
    #FLOOR
    floor_x_pos -=3
    draw_floor()
    if floor_x_pos<= -400:
        floor_x_pos = 0
    
            
    
    pygame.display.update()
    clock.tick(120)
    
