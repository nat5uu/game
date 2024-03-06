import pandas as pd
import pygame

#Dataframe
df = pd.read_csv("./recepies.csv", header = 'infer', sep =";")

#Pygame Grundvariablen
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
hitbox = 20

# neue_zeile = {"Input_1": "none","Input_2": "none","Aktiviert":1,"Item":"luft","Position":(screen.get_width() / 4, screen.get_height() / 4),"Bewegt":False,"Gemalt":1}
# df.loc[len(df)] = neue_zeile
# df.to_csv("./recepies.csv",sep=";",index=False)

def distanz(point1,point2):
     return ((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2) ** 0.5

class Object():
    def __init__(self,input_1,input_2,aktiviert,item,position,bewegt,gemalt) -> None:
        self.input_1 = input_1
        self.input_2 = input_2
        self.aktiviert = aktiviert
        self.item = item
        self.position = eval(position)
        self.bewegt = bewegt
        self.gemalt = gemalt
    def info(self):
        return print(f"{self.input_1},{self.input_2},{self.aktiviert},{self.item},{self.position},{self.bewegt},{self.gemalt}")

objects = []
for i in range(0,len(df)):
    objects.append(Object(df.at[i,"Input_1"],df.at[i,"Input_2"],df.at[i,"Aktiviert"],df.at[i,"Item"],df.at[i,"Position"],df.at[i,"Bewegt"],df.at[i,"Gemalt"],))
print("check1")
for obj in objects:
    obj.info()
while running:
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    for item in objects:
        if item.gemalt and item.item == "feuer":
            pygame.draw.circle(screen, "red", pygame.Vector2(item.position), hitbox)
        elif item.gemalt and item.item == "wasser":
            pygame.draw.circle(screen, "blue", pygame.Vector2(item.position), hitbox)
        elif item.gemalt and item.item == "luft":
            pygame.draw.circle(screen, "white", pygame.Vector2(item.position), hitbox)
        elif item.gemalt and item.item == "erde":
            pygame.draw.circle(screen, "brown", pygame.Vector2(item.position), hitbox)
        elif item.gemalt:
            pygame.draw.circle(screen, "yellow", pygame.Vector2(item.position), hitbox)
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for item in objects:
                if distanz(item.position, event.pos) <= hitbox:
                    item.bewegt = 1
                    
        elif event.type == pygame.MOUSEBUTTONUP:
            for item in objects:
                item.bewegt = 0
    
        elif event.type == pygame.MOUSEMOTION:
            for item in objects:
                if item.bewegt:
                # Aktualisiere die Position des Kreises entsprechend der Mausbewegung
                    item.position = event.pos

        for item1 in objects:
            if item1.aktiviert:
                for item2 in objects:
                    if not item1 == item2 and item2.aktiviert:
                        if distanz(item1.position, item2.position) <= hitbox and not item1.bewegt and not item2.bewegt:
                            for item in objects:
                                if (item.input_1 == item1.item and item.input_2 == item2.item) or (item.input_2 == item1.item and item.input_1 == item2.item):
                                    item.activiert = 1
                                    item.gemalt = 1
                                    item.position = item1.position
                                    objects.remove(item1)
                                    objects.remove(item2)                       

        
    keys = pygame.key.get_pressed()
    if keys[pygame.K_c] and keys[pygame.K_LCTRL]:
        running = False

    

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()


