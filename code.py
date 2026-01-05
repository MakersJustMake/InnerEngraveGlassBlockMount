import board
import digitalio
import neopixel

from time import sleep


class ColorSwitch:


    def __init__(self):
        """
        Class for cycling through NeoPixel colors with a switch.
        Used for the Inner Engraving Glass Block Display Mounts.
        """
        self.color = 0
        
        self.pixels = neopixel.NeoPixel(board.GP28, 12)
        self.pixels.brightness = 1
        self.sw = digitalio.DigitalInOut(board.GP16)
        
        self.sw.direction = digitalio.Direction.INPUT
        self.sw.pull = digitalio.Pull.UP

        
    def amber(self):
        self.pixels.fill((255,100,0))

    def blue(self):
        self.pixels.fill((0,0,255))

    def cyan(self):
        self.pixels.fill((0,255,255))
        
    def green(self):
        self.pixels.fill((0,255,0))
            
    def orange(self):
        self.pixels.fill((255,68,0))

    def purple(self):
        self.pixels.fill((255,0,255))
    
    def red(self):
        self.pixels.fill((255,0,0))
                
    def yellow(self):
        self.pixels.fill((255,255,0))
    
    def white(self):
        self.pixels.fill((255,255,255))

    def select(self):
        """
        Set color by cycling through
        """
        
        if self.color == 0:
            self.white()
        elif self.color == 1:
            self.yellow()
        elif self.color == 2:
            self.amber()
        elif self.color == 3:
            self.orange()
        elif self.color == 4:
            self.red()
        elif self.color == 5:
            self.purple()
        elif self.color == 6:
            self.blue()
        elif self.color == 7:
            self.cyan()
        elif self.color == 8:
            self.green()
        else:
            self.color = 0
            self.white()
        

def mainFn():
    """
    Main function. This sets the initial color when powered on
    to white.
    """
    
    neo = ColorSwitch()
    neo.white()
    
    while True:
        if not neo.sw.value:
            print(neo.sw.value)
            neo.color += 1
            neo.select()
        sleep(0.5)
    
mainFn()
