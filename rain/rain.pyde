nighttop = color(0, 0, 51)
nightbottom = color(0, 51, 102)
rainc = color(96, 96, 96)
#linesize = 40
def setup():
    size(800, 500)
    frameRate(20)
    
def draw():
    setgradient(0, 0, width, height, nighttop, nightbottom)
    
    rain(width, height)
    
def setgradient(x, y, w, h, c1, c2):
    for i in range(y, y + h + 1):
        inter = map(i, y, y + h, 0, 1)
        c = lerpColor(c1, c2, inter)
        stroke(c)
        line(x, i, x + w, i)
        
def rain(w, h):
    for x in range(0, w, 4):
        y = random(0, h)
        linesize = random(10, 70)
        stroke(rainc)
        line(x, y, x+2, y+linesize)
        
    
