import pygame as pg
import math


def sieve(n):
    prime = [1 for i in range(n+1)]
    p = 2
    while (p*p <= n):
        if prime[p]:
            for i in range(p*p, n+1, p):
                prime[i] = 0
        p += 1
    
    return [p for p in range(2, n+1) if prime[p]]


def coords(width, height, scale):
    max_r = math.floor(math.sqrt(width**2 + height**2) * scale)
    primes = sieve(max_r)
    
    cart_coords = [(p * math.cos(p) / scale + width//2, p * math.sin(p) / scale + height//2) for p in primes]
    return cart_coords


class Window:
    def __init__(self, width, height) -> None:
        pg.init()
        self.screen = pg.display.set_mode((width, height))
        self.clock = pg.time.Clock()
        
        self.width, self.height = width, height
        
    def run(self) -> None:
        scale = 1
        centres = coords(self.width, self.height, scale)
        
        ds = 0
        d2s = 0.3

        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    exit()
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_UP:
                        ds = -d2s
                        d2s *= 1.3
                    elif event.key == pg.K_DOWN:
                        ds = d2s
                        d2s /= 1.3
                elif event.type == pg.KEYUP:
                    ds = 0
                    
            scale += ds        
            centres = coords(self.width, self.height, scale)
            
            self.screen.fill("black")
            
            for x, y in centres:
                r = 5/scale if 5/scale >= 1 else 1
                pg.draw.circle(self.screen, "cyan", (x, y), r)
                
                                    
            pg.display.update()
            self.clock.tick(60)
            

if __name__ == "__main__":
    win = Window(1200, 900)
    win.run()
