import pygame
import random
from random import randint

print()
print()
print()
print("Together we'll build a busy city full of traffic today!")
screenx = int(input("Choose the horizontal resolution of the game: "))
screeny = int(input("Choose the vertical resolution of the game: "))
pygame.init()                     # Prepare pygame
clock = pygame.time.Clock()       # To set game speed
screen = pygame.display.set_mode((screenx, screeny))
carwidth = int(input("Choose how large you want your car to be (square side): "))

car = pygame.image.load('car_sprites.png')
car = pygame.transform.scale(car, (8 * carwidth, carwidth))

typecarfw = [0, carwidth*2, carwidth*4, carwidth*6] #backwards
typecarbw = [carwidth, carwidth*3, carwidth*5, carwidth*7] #forwards
streets = int(input("How many streets do you want? "))
rows = streets * 2

print("I'll do the hard work of selecting how large are the rivers between the streets!")
clock.tick(1)
ok = input("Is that ok for you? Y/N: ")
if ok == 'y' or ok == 'Y' :
    
    rivers = []
    for street in range(streets):
        rivers.append(random.randint(0, 9))

else:
    rivers = []
    print("This is your list of how large you want the rivers to be, yet..", rivers)
    clock.tick(1)
    print("This is your mission: insert how large you want every river to be")
    print("0 means no river; 1 means that the river is large as the cars; 2 means the river is twice the cars")
    print("And so on...")
    for street in range(streets):
        rivers.append(int(input("Choose how large do you want the river " + str(street + 1) + " to be: ")))
    print("Well done!")
    
print("Now see it in action!")

carrow = []


for row in range(rows):
                
    if row == 0:
        carrow.append(carwidth)
    else:
        if row%2 ==1:
            carrow.append(carrow[row-1] + carwidth + carwidth // 8)
        if row%2 == 0:
            if rivers[row//2] == 0:
                carrow.append(carrow[row-1] + carwidth * (rivers[row//2] + 1) + carwidth // 8)
            else:
                carrow.append(carrow[row-1] + carwidth * (rivers[row//2] + 1))




#cars = [7, 5, 2, 3] numero di macchine per corsia, la lunghezza della lista corrisponde al numero di corsie
cars = []
for k in range(rows):
    cars.append(randint(1, 9))
distance = []
for r in range(rows):
    distance.append((screenx + carwidth) // cars [r])
carinrowbw=[]
carinrowfw=[]


for k in range(9):
    carinrowbw.append(random.choice(typecarbw))
for k in range(9):
    carinrowfw.append(random.choice(typecarfw))


    




playing = True
while playing:
    for e in pygame.event.get():  # Handle events: mouse, keyb etc.
        if e.type == pygame.QUIT: playing = False
    
    for mov in range(screenx + carwidth):
        
        screen.fill((255, 255, 255))
        for r in range(rows):
            pygame.draw.rect(screen, (40,43,42), (0, carrow[r], screenx, carwidth))
            
        x = 0
        for a in range(screenx + carwidth // carwidth):
            for r in range(0, rows, 2):
                
                pygame.draw.rect(screen, (40, 43, 42), (x, carrow[r] + carwidth, carwidth, carwidth // 8))
 
            x += carwidth*2
        for row in range(rows):
            if row%2 == 0:
                x = -mov
                for i in range(cars[row]):
                    if -carwidth <= x < 0:
                        screen.blit(car, (x, carrow[row]), area=(carinrowbw[i], 0, carwidth, carwidth))
                        x += distance[row]
                    else:
                        screen.blit(car, (x % (screenx + carwidth), carrow[row]), area=(carinrowbw[i], 0, carwidth, carwidth))
                        x += distance[row]
            elif row%2 == 1:
                x = mov
                for i in range(cars[row]):
                    if screenx <= x < (screenx + carwidth):
                        screen.blit(car, (x - (screenx + carwidth), carrow[row]), area=(carinrowfw[i], 0, carwidth, carwidth))
                        x += distance[row]
                    else:
                        
                        screen.blit(car, (x % (screenx + carwidth), carrow[row]), area=(carinrowfw[i], 0, carwidth, carwidth))
                        x += distance[row]
        
 
    
        
        pygame.display.flip()

   
pygame.quit()                     
quit()
