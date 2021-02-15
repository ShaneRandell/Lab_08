from guizero import App, Slider,TextBox
from gpiozero import AngularServo
import time 

maxPW = 2/1000
minPW = 1/1000


def slider_read(slider_value):
    textbox.value = slider_value
    print(slider_value)
    servo1 = AngularServo(17, min_pulse_width = minPW, max_pulse_width = maxPW, initial_angle = 0, min_angle = -90, max_angle = 90)
    servo1.angle = int(slider_value)    
    time.sleep(0.5)    

app = App()
slider1 = Slider(app, start=-90, end=90, width="fill",command = slider_read)
textbox = TextBox(app)

print(textbox.value)

app.display()



                       
