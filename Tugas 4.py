import pygame, sys #mengimport modul pygame dan sys
from pygame import rect #Mengimpor Model Persegi
from pygame.locals import * #Mengimpor file local pygame
import time #Mengimpor waktu

WIDTH, HEIGHT = 600, 480 #mengatur Resolusi Window
pygame.display.set_caption('Smooth Movement') #memberi judul window

pygame.init() #menginisialisasi setiap submodules di pygame paket, yang dapat memuat driver dan permintaan pygame hardware sehingga siap untuk menggunakan semua perangkat pada komputer
win = pygame.display.set_mode((WIDTH, HEIGHT))#mengeset ukuran lebar dan tinggi window
clock = pygame.time.Clock()#membuat objek untuk membantu melacak waktu

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#membuat kelas player

class Player:
    def __init__(self, x, y):#membuat fungsi constructor dengan memasukan objek self dan parameter x,y
        self.x = int(x)#memberikan tipe data variabel x integer
        self.y = int(y)#memberikan tipe data variabel y integer
        self.rect = pygame.Rect(self.x, self.y, 32, 32)#membuat bangun rectangle dengan ukuran 32 x 32
        self.color = (250, 120, 60)#memberikan warna orange
        self.velX = 0#kecepatan awal x 0
        self.velY = 0#kecepatan awal y 0
        self.left_pressed = False#ketika ditekan tombol kiri posisinya awal/default adalah false
        self.right_pressed = False#ketika ditekan tombol kanan posisinya awal/default adalah false
        self.up_pressed = False#ketika ditekan tombol atas posisinya awal/default adalah false
        self.down_pressed = False#ketika ditekan tombol bawah posisinya awal/default adalah false
        self.speed = 4#kecepatan objectnya adalah 4
    
    def draw(self, win):#fungsi untuk menggambar object dari rectangle dengan warna orange serta ukuran layar yang sudah ditentukan
        pygame.draw.rect(win, self.color, self.rect)
    
    def update(self):#fungsi update dari objek self, agar bisa bergerak setiap kita tekan tombol, mengikuti titik koordinat dan kecepatan yang telah ditentukan
        self.velX = 0
        self.velY = 0
        if self.left_pressed and not self.right_pressed:
            self.velX = -self.speed
        if self.right_pressed and not self.left_pressed:
            self.velX = self.speed
        if self.up_pressed and not self.down_pressed:
            self.velY = -self.speed
        if self.down_pressed and not self.up_pressed:
            self.velY = self.speed
        
        self.x += self.velX
        self.y += self.velY

        self.rect = pygame.Rect(int(self.x), int(self.y), 32, 32)


player = Player(WIDTH/2, HEIGHT/2)

font_color = (BLACK)
font_obj = pygame.font.Font("C:\Windows\Fonts\RAVIE.TTF",25)
text = "RIFQI ACHMAD F"
img = font_obj.render(text, True, (BLACK))

rect = img.get_rect()
rect.topleft = (20,20)
cursor = Rect(rect.topright, (3, rect.height))

while True:#akan menjalankan jika perulangannya True, dan akan menyusun logic-logic pemrogramannya ketika tombol ditekan maka harus menggerakan kondisi apa

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.left_pressed = True
            if event.key == pygame.K_RIGHT:
                player.right_pressed = True
            if event.key == pygame.K_UP:
                player.up_pressed = True
            if event.key == pygame.K_DOWN:
                player.down_pressed = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.left_pressed = False
            if event.key == pygame.K_RIGHT:
                player.right_pressed = False
            if event.key == pygame.K_UP:
                player.up_pressed = False
            if event.key == pygame.K_DOWN:
                player.down_pressed = False
    


    
            if event.type == QUIT:
                    running = False

            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    if len(text)>0:
                        text = text[:-1]

                else:
                    text += event.unicode
                    img = font_obj.render(text, True, PINK)
                    rect.size = img.get_size()
                    cursor.topleft = rect.topright


#Menggambar warna background
    win.fill((GREEN))
    pygame.draw.rect(win, (RED), player)

    win.blit(img,rect)
    if time.time() % 1 > 0.5:
        pygame.draw.rect(win, BLUE, cursor)
    pygame.display.update()

    player.update()
    pygame.display.flip()

    clock.tick(120)#program tidak akan pernah berjalan lebih dari 120 frame per detik.
    pygame.display.update()
    
pygame.quit()
