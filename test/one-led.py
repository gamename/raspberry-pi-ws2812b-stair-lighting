import board
import neopixel
pixels = neopixel.NeoPixel(board.D18, 1)
pixels[0] = (255, 0, 0)
