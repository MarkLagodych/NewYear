import webbrowser as wb
import winsound as ws
import time
def gingle():
    x_16 = 200
    x_8 = 400
    x_4 = 800
    x_8_16 = 600
    x_2 = 800
    c = 523
    d = 587
    e = 659
    f = 699
    g = 784
    ws.Beep(e, x_8)
    ws.Beep(e, x_8)
    ws.Beep(e, x_4)
    
    ws.Beep(e, x_8)
    ws.Beep(e, x_8)
    ws.Beep(e, x_4)
    
    ws.Beep(e, x_8)
    ws.Beep(g, x_8)
    ws.Beep(c, x_8_16)
    ws.Beep(d, x_16)
    ws.Beep(e, x_2)
    
    ws.Beep(f, x_8)
    ws.Beep(f, x_8)
    ws.Beep(f, x_8_16)
    
    ws.Beep(f, x_16)
    ws.Beep(f, x_8)
    ws.Beep(e, x_8)
    ws.Beep(e, x_8)
    ws.Beep(e, x_16)
    ws.Beep(e, x_16)
    
    ws.Beep(g, x_8)
    ws.Beep(g, x_8)
    ws.Beep(f, x_8)
    ws.Beep(e, x_8)
    ws.Beep(c, x_4)
    
print("Happy New Year!")
wb.open('https://img.7dach.ru/image/600/00/00/71/2013/12/23/9968ed.jpg')
gingle()
time.sleep(60)
