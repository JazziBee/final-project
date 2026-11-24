import pygame

color1 = int(input("color 1  > "))
color2 = int(input(f"({color1},X,X)  > "))
color3 = int(input(f"({color1},{color2},X)  > "))
print(f"({color1},{color2},{color3})")
screen = pygame.display.set_mode((500,500))

run = True
while run:

    rgb = (color1,color2,color3)

    screen.fill(color=rgb)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()


pygame.quit()