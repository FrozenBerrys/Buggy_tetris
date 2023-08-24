import pygame, sys, random, math
from collections import deque

pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption('snake')
clock = pygame.time.Clock()

largefont = pygame.font.Font("pixel.ttf", 50)
font = pygame.font.Font("pixel.ttf", 35)
smallfont = pygame.font.Font("pixel.ttf", 20)
tinyfont = pygame.font.Font("pixel.ttf", 15)

pause_surface = pygame.Surface((500,500))
pause_text = largefont.render("GAME PAUSED", False, 'White')
pause_text_rect = pause_text.get_rect(center = (250,250))
gameover_surface = pygame.Surface((500,500))
gameover_surface.set_alpha(15)
gameover_text = largefont.render("GAME OVER", False, 'White')
gameover_text_rect = gameover_text.get_rect(center = (250,250))


def paused():
    global pausee
    while pausee:
        screen.blit(pause_text, pause_text_rect)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    pausee = False
        pygame.display.flip()
        clock.tick(10)  


def gameover():
    global lose, time
    lose = True
    time = 0
    while lose:
        screen.blit(gameover_surface, (0,0))
        screen.blit(gameover_text,gameover_text_rect)

        pygame.display.flip()
        clock.tick(10)  
        time += 1
        if time == 75:
            lose = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        


#####################################################################
def square_code():
    rect = [
        pygame.Rect(230,10,20,20),
        pygame.Rect(250,10,20,20),
        pygame.Rect(230,30,20,20),
        pygame.Rect(250,30,20,20)
    ]
    return rect

def tshirt_code():
    rect = [
        pygame.Rect(230,10,20,20),
        pygame.Rect(250,30,20,20),
        pygame.Rect(230,50,20,20),
        pygame.Rect(230,30,20,20)
    ]
    return rect

def leftHole_code():
    rect = [
        pygame.Rect(230,10,20,20),
        pygame.Rect(230,30,20,20),
        pygame.Rect(250,50,20,20),
        pygame.Rect(250,30,20,20)
    ]
    return rect

def rightHole_code():
    rect = [
        pygame.Rect(250,10,20,20),
        pygame.Rect(230,30,20,20),
        pygame.Rect(230,50,20,20),
        pygame.Rect(250,30,20,20)
    ]
    return rect

def leftL_code():
    rect = [
        pygame.Rect(230,10,20,20),
        pygame.Rect(250,10,20,20),
        pygame.Rect(230,50,20,20),
        pygame.Rect(230,30,20,20)
    ]
    return rect

def rightL_code():
    rect = [
        pygame.Rect(230,10,20,20),
        pygame.Rect(250,10,20,20),
        pygame.Rect(250,50,20,20),
        pygame.Rect(250,30,20,20)
    ]
    return rect

def tall_code():
    rect = [
        pygame.Rect(230,10,20,20),
        pygame.Rect(230,30,20,20),
        pygame.Rect(230,50,20,20),
        pygame.Rect(230,70,20,20)
    ]
    return rect

def blip(id, rect):
    if id == 0:
        for i in rect:
            screen.blit(square, i)
    if id == 1:
        for i in rect:
            screen.blit(leftHole, i)
    if id == 2:
        for i in rect:
            screen.blit(rightHole, i)
    if id == 3:
        for i in rect:
            screen.blit(leftL, i)
    if id == 4:
        for i in rect:
            screen.blit(rightL, i)
    if id == 5:
        for i in rect:
            screen.blit(tshirt, i)
    if id == 6:
        for i in rect:
            screen.blit(tall, i)

#####################################################################
def newblock(type):
    if type == 0:
        rect = square_code()
    if type == 1:
        rect = leftHole_code()
    if type == 2:
        rect = rightHole_code()
    if type == 3:
        rect = leftL_code()
    if type == 4:
        rect = rightL_code()
    if type == 5:
        rect = tshirt_code()
    if type == 6:
        rect = tall_code()
    return rect

#####################################################################
def rotate(rect, id, turn, data):
    if id == 0:
       pass
    elif id == 1:
       if turn == 0:
           rect[0][0] += 40; rect[1][0] += 20; rect[1][1] -= 20; rect[2][0] -= 20; rect[2][1] -= 20
           if checkrightbound(rect) or checkleftbound(rect) or collisioncheck(rect, data):
               rect[0][0] -= 40; rect[1][0] -= 20; rect[1][1] += 20; rect[2][0] += 20; rect[2][1] += 20
           else : turn += 1
           
       elif turn == 1:
           rect[0][1] += 40; rect[1][0] += 20; rect[1][1] += 20; rect[2][0] += 20; rect[2][1] -= 20
           if checkrightbound(rect) or checkleftbound(rect) or collisioncheck(rect, data):
               rect[0][1] -= 40; rect[1][0] -= 20; rect[1][1] -= 20; rect[2][0] -= 20; rect[2][1] += 20
           else : turn += 1
           
       elif turn == 2:
           rect[0][0] -= 40; rect[1][0] -= 20; rect[1][1] += 20; rect[2][0] += 20; rect[2][1] += 20
           if checkrightbound(rect) or checkleftbound(rect) or collisioncheck(rect, data):
               rect[0][0] += 40; rect[1][0] += 20; rect[1][1] -= 20; rect[2][0] -= 20; rect[2][1] -= 20
           else : turn += 1
           
       elif turn == 3:
           rect[0][1] -= 40; rect[1][0] -= 20; rect[1][1] -= 20; rect[2][0] -= 20; rect[2][1] += 20
           if checkrightbound(rect) or checkleftbound(rect) or collisioncheck(rect, data):
               rect[0][1] += 40; rect[1][0] += 20; rect[1][1] += 20; rect[2][0] += 20; rect[2][1] -= 20
           else : turn += 1
           
           
    elif id == 2: 
       if turn == 0:
           rect[2][1] -= 40; rect[1][0] += 20; rect[1][1] -= 20; rect[0][0] += 20; rect[0][1] += 20
           if checkrightbound(rect) or checkleftbound(rect) or collisioncheck(rect, data):
               rect[2][1] += 40; rect[1][0] -= 20; rect[1][1] += 20; rect[0][0] -= 20; rect[0][1] -= 20
           else : turn += 1
       elif turn == 1:
           rect[2][0] += 40; rect[1][0] += 20; rect[1][1] += 20; rect[0][0] -= 20; rect[0][1] += 20
           if checkrightbound(rect) or checkleftbound(rect) or collisioncheck(rect, data):
               rect[2][0] -= 40; rect[1][0] -= 20; rect[1][1] -= 20; rect[0][0] += 20; rect[0][1] -= 20
           else : turn += 1
           
       elif turn == 2:
           rect[2][1] += 40; rect[1][0] -= 20; rect[1][1] += 20; rect[0][0] -= 20; rect[0][1] -= 20
           if checkrightbound(rect) or checkleftbound(rect) or collisioncheck(rect, data):
               rect[2][1] -= 40; rect[1][0] += 20; rect[1][1] -= 20; rect[0][0] += 20; rect[0][1] += 20
           else : turn += 1
           
       elif turn == 3:
           rect[2][0] -= 40; rect[1][0] -= 20; rect[1][1] -= 20; rect[0][0] += 20; rect[0][1] -= 20
           if checkrightbound(rect) or checkleftbound(rect) or collisioncheck(rect, data):
               rect[2][0] += 40; rect[1][0] += 20; rect[1][1] += 20; rect[0][0] -= 20; rect[0][1] += 20
           else : turn += 1
           
    elif id == 3:
       if turn == 0:
           rect[1][1] += 40; rect[0][0] += 20; rect[0][1] += 20; rect[2][0] -= 20; rect[2][1] -= 20
           if checkrightbound(rect) or checkleftbound(rect) or collisioncheck(rect, data):
               rect[1][1] -= 40; rect[0][0] -= 20; rect[0][1] -= 20; rect[2][0] += 20; rect[2][1] += 20
           else : turn += 1
       elif turn == 1:
           rect[1][0] -= 40; rect[0][0] -= 20; rect[0][1] += 20; rect[2][0] += 20; rect[2][1] -= 20
           if checkrightbound(rect) or checkleftbound(rect) or collisioncheck(rect, data):
               rect[1][0] += 40; rect[0][0] += 20; rect[0][1] -= 20; rect[2][0] -= 20; rect[2][1] += 20
           else : turn += 1
       elif turn == 2:
           rect[1][1] -= 40; rect[0][0] -= 20; rect[0][1] -= 20; rect[2][0] += 20; rect[2][1] += 20
           if checkrightbound(rect) or checkleftbound(rect) or collisioncheck(rect, data):
               rect[1][1] += 40; rect[0][0] += 20; rect[0][1] += 20; rect[2][0] -= 20; rect[2][1] -= 20
           else : turn += 1
       elif turn == 3:
           rect[1][0] += 40; rect[0][0] += 20; rect[0][1] -= 20; rect[2][0] -= 20; rect[2][1] += 20
           if checkrightbound(rect) or checkleftbound(rect) or collisioncheck(rect, data):
               rect[1][0] -= 40; rect[0][0] -= 20; rect[0][1] += 20; rect[2][0] += 20; rect[2][1] -= 20
           else : turn += 1
           
    elif id == 4:
       if turn == 0: 
           rect[0][0] += 40; rect[1][0] += 20; rect[1][1] += 20; rect[2][0] -= 20; rect[2][1] -= 20
           if checkrightbound(rect) or checkleftbound(rect) or collisioncheck(rect, data):
               rect[0][0] -= 40; rect[1][0] -= 20; rect[1][1] -= 20; rect[2][0] += 20; rect[2][1] += 20
           else : turn += 1
       elif turn == 1:
           rect[0][1] += 40; rect[1][0] -= 20; rect[1][1] += 20; rect[2][0] += 20; rect[2][1] -= 20
           if checkrightbound(rect) or checkleftbound(rect) or collisioncheck(rect, data):
               rect[0][1] -= 40; rect[1][0] += 20; rect[1][1] -= 20; rect[2][0] -= 20; rect[2][1] += 20
           else : turn += 1
       elif turn == 2:
           rect[0][0] -= 40; rect[1][0] -= 20; rect[1][1] -= 20; rect[2][0] += 20; rect[2][1] += 20
           if checkrightbound(rect) or checkleftbound(rect) or collisioncheck(rect, data):
               rect[0][0] += 40; rect[1][0] += 20; rect[1][1] += 20; rect[2][0] -= 20; rect[2][1] -= 20
           else : turn += 1
       elif turn == 3:
           rect[0][1] -= 40; rect[1][0] += 20; rect[1][1] -= 20; rect[2][0] -= 20; rect[2][1] += 20
           if checkrightbound(rect) or checkleftbound(rect) or collisioncheck(rect, data):
               rect[0][1] += 40; rect[1][0] -= 20; rect[1][1] += 20; rect[2][0] += 20; rect[2][1] -= 20
           else : turn += 1
           
    elif id == 5:
       if turn == 0:
           rect[0][0] += 20; rect[0][1] += 20; rect[2][0] -= 20; rect[2][1] -= 20; rect[1][0] -= 20; rect[1][1] += 20
           if checkrightbound(rect) or checkleftbound(rect) or collisioncheck(rect, data):
               rect[0][0] -= 20; rect[0][1] -= 20; rect[2][0] += 20; rect[2][1] += 20; rect[1][0] += 20; rect[1][1] -= 20
           else : turn += 1
       elif turn == 1:
           rect[0][0] -= 20; rect[0][1] += 20; rect[2][0] += 20; rect[2][1] -= 20; rect[1][0] -= 20; rect[1][1] -= 20
           if checkrightbound(rect) or checkleftbound(rect) or collisioncheck(rect, data):
               rect[0][0] += 20; rect[0][1] -= 20; rect[2][0] -= 20; rect[2][1] += 20; rect[1][0] += 20; rect[1][1] += 20
           else : turn += 1
       elif turn == 2:
           rect[0][0] -= 20; rect[0][1] -= 20; rect[2][0] += 20; rect[2][1] += 20; rect[1][0] += 20; rect[1][1] -= 20
           if checkrightbound(rect) or checkleftbound(rect) or collisioncheck(rect, data):
               rect[0][0] += 20; rect[0][1] += 20; rect[2][0] -= 20; rect[2][1] -= 20; rect[1][0] -= 20; rect[1][1] += 20
           else : turn += 1
       elif turn == 3:
           rect[0][0] += 20; rect[0][1] -= 20; rect[2][0] -= 20; rect[2][1] += 20; rect[1][0] += 20; rect[1][1] += 20
           if checkrightbound(rect) or checkleftbound(rect) or collisioncheck(rect, data):
               rect[0][0] -= 20; rect[0][1] += 20; rect[2][0] += 20; rect[2][1] -= 20; rect[1][0] -= 20; rect[1][1] -= 20
           else : turn += 1
           
        
    elif id == 6:
       if turn == 0:
           rect[0][0] += 40; rect[0][1] += 20; rect[1][0] += 20; rect[2][1] -= 20; rect[3][0] -= 20; rect[3][1] -= 40
           if checkrightbound(rect) or checkleftbound(rect) or collisioncheck(rect, data):
               rect[0][0] -= 40; rect[0][1] -= 20; rect[1][0] -= 20; rect[2][1] += 20; rect[3][0] += 20; rect[3][1] += 40
           else :
            turn += 1
       elif turn == 1:
           rect[0][0] -= 20; rect[0][1] += 40; rect[1][1] += 20; rect[2][0] += 20; rect[3][0] += 40; rect[3][1] -= 20
           if checkrightbound(rect) or checkleftbound(rect) or collisioncheck(rect, data):
               rect[0][0] += 20; rect[0][1] -= 40; rect[1][1] -= 20; rect[2][0] -= 20; rect[3][0] -= 40; rect[3][1] += 20
           else : 
               turn += 1
           
       elif turn == 2:
           rect[0][0] -= 40; rect[0][1] -= 20; rect[1][0] -= 20; rect[2][1] += 20; rect[3][0] += 20; rect[3][1] += 40
           if checkrightbound(rect) or checkleftbound(rect) or collisioncheck(rect, data):
               rect[0][0] += 40; rect[0][1] += 20; rect[1][0] += 20; rect[2][1] -= 20; rect[3][0] -= 20; rect[3][1] -= 40
           else :
               turn += 1
       elif turn == 3:
           rect[0][0] += 20; rect[0][1] -= 40; rect[1][1] -= 20; rect[2][0] -= 20; rect[3][0] -= 40; rect[3][1] += 20
           if checkrightbound(rect) or checkleftbound(rect) or collisioncheck(rect, data):
               rect[0][0] -= 20; rect[0][1] += 40; rect[1][0] += 20; rect[2][1] += 20; rect[3][0] += 40; rect[3][1] -= 20
           else : 
               turn += 1
               


    return rect, turn
#####################################################################
def checklowerbound(rect):
    x = 0
    for i in rect:
        if i[1] > x:
            x = i[1]
    if x >= 490:
        return True
    return False

def checkrightbound(rect):
    x = 0
    for i in rect:
        if i[0] > x:
            x = i[0]
    if x > 330:
        return True
    return False

def checkleftbound(rect):
    x = 500
    for i in rect:
        if i[0] < x:
            x = i[0]
    if x < 150:
        return True
    return False

def collisioncheck(rect, data):
    for i in range(20):
        for j in range(10):
            if data[i][j] and rect[0][0] == 150 + j * 20 and rect[0][1] == 90 + i * 20:
                return True
            if data[i][j] and rect[1][0] == 150 + j * 20 and rect[1][1] == 90 + i * 20:
                return True
            if data[i][j] and rect[2][0] == 150 + j * 20 and rect[2][1] == 90 + i * 20:
                return True
            if data[i][j] and rect[3][0] == 150 + j * 20 and rect[3][1] == 90 + i * 20:
                return True

    return False

def match(saved, i, lower):
    for j in saved:
        for k in j[1]:
            if k[1] == i * 20 + 90:
                k[1] = 1000
            elif k[1] < i * 20 + 90:
                k[1] += 20 * lower[int((k[0]-150)/20)]
    return saved

#####################################################################
highscoreint = 0
scoreint = 0
score = smallfont.render(str(scoreint), False, 'White')
score_rect = score.get_rect(bottomleft = (150, 85))
highscore = smallfont.render(str(highscoreint), False, 'White')
highscore_rect = highscore.get_rect(topleft = (390,90))
trophy = pygame.transform.scale(pygame.image.load("trophy.png"), (30,30))
trophy_rect = trophy.get_rect(topleft = (355,90))
pause = tinyfont.render("'P' to pause", False, 'White')
pause_rect = pause.get_rect(bottomright = (490,490))
start = tinyfont.render("'C' to continue", False, 'White')
start_rect = start.get_rect(bottomleft = (10,490))


background2 = pygame.transform.scale(pygame.image.load("background2.gif"), (500,500))
game_surface = pygame.Surface((200,400))
game_surface.set_alpha(100)
background = pygame.Surface((500,500))

#####################################################################
rightL = pygame.transform.scale(pygame.image.load("block/rightL.png"), (20,20))
leftL = pygame.transform.scale(pygame.image.load("block/leftL.png"), (20,20))
tshirt = pygame.transform.scale(pygame.image.load("block/tshirt.png"), (20,20))
square = pygame.transform.scale(pygame.image.load("block/square.png"), (20,20))
tall = pygame.transform.scale(pygame.image.load("block/tall.png"), (20,20))
rightHole = pygame.transform.scale(pygame.image.load("block/rightHole.png"), (20,20))
leftHole = pygame.transform.scale(pygame.image.load("block/leftHole.png"), (20,20))

#####################################################################
Menu = True
Game = False

while True:
    while Menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    Menu = False
                    Game = True

        screen.blit(background2, (0,0))
        screen.blit(game_surface, (150,90))
        highscore = smallfont.render(str(highscoreint), False, 'White')
        screen.blit(highscore, highscore_rect)
        score = smallfont.render(str(scoreint), False, 'White')
        screen.blit(score, score_rect)
        screen.blit(trophy,trophy_rect)
        screen.blit(start, start_rect)
        screen.blit(pause, pause_rect)

        clock.tick(10)  
        pygame.display.flip()

#####################################################################
    block = False
    saved = deque([])
    saved.clear
    id = math.floor(random.randrange(-1,6))
    data = []
    for i in range(20):
        row = []
        for j in range(10):
            row.append(0)
        data.append(row)
    delay = 300
    scoreint = 0

    while Game:
        if block == False:
            id += 1
            if id > 6:
                id = 0
            rect = newblock(id)
            block = True
            turn = 0

        for i in rect:
            i[1] += 20
        if checklowerbound(rect) or collisioncheck(rect, data):
            for i in rect:
                i[1] -= 20
                if i[1] < 90:
                    print("GAME OVER")
                    gameover()
                    Game = False
                    Menu = True
                    break

            saved.appendleft([id, rect])
            block = False

            for i in rect:
                data[int((i[1] - 90)/20)][int((i[0] - 150)/20)] = 1
                        
            #CHECK FOR COMPLETED ROWS
            for i in range(20):
                if Game == False:
                    break

                if data[i] == [1,1,1,1,1,1,1,1,1,1]:
                    lower = [1,1,1,1,1,1,1,1,1,1]
                    scoreint += 10
                    for j in range(10):
                        for k in range(i+1, 20):
                            if data[k][j] == 0:
                                lower[j] += 1
                            else : break
                    saved = match(saved, i, lower)
                    for j in range(20):
                        for k in range(10):
                            data[j][k] = 0
                    for j in saved:
                        for k in j[1]:
                                if k[1] != 1000:
                                    data[int((k[1] - 90)/20)][int((k[0] - 150)/20)] = 1

        screen.blit(background2, (0,0))
        screen.blit(game_surface, (150,90))
        highscore = smallfont.render(str(highscoreint), False, 'White')
        screen.blit(highscore, highscore_rect)
        score = smallfont.render(str(scoreint), False, 'White')
        screen.blit(score, score_rect)
        screen.blit(trophy,trophy_rect)
        screen.blit(start, start_rect)
        screen.blit(pause, pause_rect)
        for i in saved:
            blip(i[0], i[1])        
        blip(id, rect)
        pygame.display.flip()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pausee = True
                    paused()
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    pp = rotate(rect, id, turn, data)
                    rect = pp[0]
                    turn = pp[1]
                    if turn == 4:
                        turn = 0

                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    for i in rect:
                        i[1] += 20
                    if checklowerbound(rect) or collisioncheck(rect, data):
                        for i in rect:
                            i[1] -= 20
                            if i[1] < 90:
                                if scoreint > highscoreint:
                                    highscoreint = scoreint
                                print("GAME OVER")
                                gameover()
                                Game = False
                                Menu = True
                                break

                        saved.appendleft([id, rect])
                        block = False

                        for i in rect:
                            if i[1] != 1000:
                                data[int((i[1] - 90)/20)][int((i[0] - 150)/20)] = 1
                        
                        #CHECK FOR COMPLETED ROWS
                        for i in range(20):
                            if Game == False:
                                break

                            if data[i] == [1,1,1,1,1,1,1,1,1,1]:
                                lower = [1,1,1,1,1,1,1,1,1,1]
                                scoreint += 10
                                for j in range(10):
                                    for k in range(i+1, 20):
                                        if data[k][j] == 0:
                                            lower[j] += 1
                                        else : break
                                saved = match(saved, i, lower)
                                for j in range(20):
                                    for k in range(10):
                                        data[j][k] = 0
                                for j in saved:
                                    for k in j[1]:
                                        if k[1] != 1000:
                                            data[int((k[1] - 90)/20)][int((k[0] - 150)/20)] = 1

                    screen.blit(background2, (0,0))
                    screen.blit(game_surface, (150,90))
                    highscore = smallfont.render(str(highscoreint), False, 'White')
                    screen.blit(highscore, highscore_rect)
                    score = smallfont.render(str(scoreint), False, 'White')
                    screen.blit(score, score_rect)
                    screen.blit(trophy,trophy_rect)
                    screen.blit(start, start_rect)
                    screen.blit(pause, pause_rect)
                    for i in saved:
                        blip(i[0], i[1])
                    
                    blip(id, rect)
                    pygame.display.flip()

                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    for i in rect:
                            i[0] += 20
                    if checkrightbound(rect) or collisioncheck(rect, data):
                        for i in rect:
                            i[0] -= 20
                    elif Game == False:
                        pass
                    else:
                        screen.blit(background2, (0,0))
                        screen.blit(game_surface, (150,90))
                        highscore = smallfont.render(str(highscoreint), False, 'White')
                        screen.blit(highscore, highscore_rect)
                        score = smallfont.render(str(scoreint), False, 'White')
                        screen.blit(score, score_rect)
                        screen.blit(trophy,trophy_rect)
                        screen.blit(start, start_rect)
                        screen.blit(pause, pause_rect)
                        for i in saved:
                            blip(i[0], i[1])
                    blip(id, rect)
                    pygame.display.flip()

                if event.key == pygame.K_LEFT or event.key == pygame.K_a: 
                    for i in rect:
                            i[0] -= 20
                    if checkleftbound(rect) or collisioncheck(rect, data):
                        for i in rect:
                            i[0] += 20
                    elif Game == False:
                        pass
                    else:
                        screen.blit(background2, (0,0))
                        screen.blit(game_surface, (150,90))
                        highscore = smallfont.render(str(highscoreint), False, 'White')
                        screen.blit(highscore, highscore_rect)
                        score = smallfont.render(str(scoreint), False, 'White')
                        screen.blit(score, score_rect)
                        screen.blit(trophy,trophy_rect)
                        screen.blit(start, start_rect)
                        screen.blit(pause, pause_rect)
                        for i in saved:
                            blip(i[0], i[1])
                    blip(id, rect)
                    pygame.display.flip()

        if Game == True:
            screen.blit(background2, (0,0))
            screen.blit(game_surface, (150,90))
            highscore = smallfont.render(str(highscoreint), False, 'White')
            screen.blit(highscore, highscore_rect)
            score = smallfont.render(str(scoreint), False, 'White')
            screen.blit(score, score_rect)
            screen.blit(trophy,trophy_rect)
            screen.blit(start, start_rect)
            screen.blit(pause, pause_rect)
            for i in saved:
                blip(i[0], i[1])
            blip(id, rect)
        pygame.display.flip()
        pygame.time.wait(400)
        clock.tick(10)  
