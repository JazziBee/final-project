import pygame,os

os.system('clear')

try:
    color1 = int(input("color 1  > "))
    if color1 not in range(0,256):
        raise ValueError
except:
    print("please enter a number between (0-255)")
    color1 = int(input("color 1  > "))
color2 = int(input(f"({color1},X,X)  > "))
color3 = int(input(f"({color1},{color2},X)  > "))
print(f"({color1},{color2},{color3})")
color4 = int(input("color 2  > "))
color5 = int(input(f"({color4},X,X)  > "))
color6 = int(input(f"({color4},{color5},X)  > "))
print(f"({color4},{color5},{color6})")

screen = pygame.display.set_mode((500,500))

run = True
while run:

    rgb = ((color1+color4)//2,(color2+color5)//2,(color3+color6)//2)

    screen.fill(color=rgb)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()


pygame.quit()