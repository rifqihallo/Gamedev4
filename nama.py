import pygame#mengimport modul pygame dan sys
import time#mengimport modul time

BLACK = (0,0,0)
RED = (255,0,0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


pygame.init()#menginisialisasi setiap submodules di pygame paket, yang dapat memuat driver dan permintaan pygame hardware sehingga siap untuk menggunakan semua perangkat pada komputer
screen = pygame.display.set_mode((640,240))#mengatur lebar dan tinggi window
pygame.display.set_caption('NAMA')#mengeset judul window

text = "RIFQI ACHMAD FADHILLA"
font = pygame.font.SysFont(None, 48)
img = font.render(text, True, RED)

rect = img.get_rect()
rect.topleft = (20,20)
cursor = Rect(rect.topright, (3, rect.height))

running = True
baground = GREEN

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        if event.type == KEYDOWN:
            if event.key == K_BACKSPACE:
                if len(text)>0:
                    text = text[:-1]

            else:
                text += event.unicode
            img = font.render(text, True, RED)
            rect.size = img.get_size()
            cursor.topleft = rect.topright

    screen.fill(baground)#Untuk Menampilkan background
    screen.blit(img,rect)#Untuk Menampilkan IMG
    if time.time() % 1 > 0.5:
        pygame.draw.rect(screen, RED, cursor)
    pygame.display.update()

pygame.quit()
