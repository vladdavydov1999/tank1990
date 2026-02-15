import pygame


class Tank():
    def __init__(self, window):
        self.field = window
        self.field_rect = self.field.get_rect()
        # self.x self.y #coordinates of the origin
        self.image = pygame.image.load("tanki_1990/image/tank.png") # tank image
        self.image_rect = self.image.get_rect()  # logical rectangel
        self.image_rect.midbottom = self.field_rect.midbottom
        self.speed = 3

    def blitme(self):
    # drawing a tank in each frame 
        self.field.blit(self.image, self.image_rect)


    def move(self, keys):
    # method on moving Tank
        if keys[pygame.K_UP]:
        # move on Y up
            self.image_rect.y -= self.speed

        if keys[pygame.K_DOWN]:
            self.image_rect.y += self.speed
        #move on Y down

        if keys[pygame.K_LEFT]:
            self.image_rect.x -= self.speed
        #move on X left

        if keys[pygame.K_RIGHT]:
            self.image_rect.x += self.speed 
