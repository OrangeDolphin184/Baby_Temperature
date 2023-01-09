from guizero import *
from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
babies = []
babyname = None
recordt = None
all_temps = None


def open_window1():
    global recordt, all_temps
    recordt = Window(app, title="Third Window", height=1920, width=1400, bg="#3e2f5b")
    new_name = Text(recordt, font="Secular One", size=30, color="#e0ca3c", text="Baby's name:")
    name_box = Text(recordt, font="Secular One", size=30, color="#e0ca3c", text=babies)
    temp = Text(recordt, font="Secular One", size=30, color="#e0ca3c", text="Temperature recording")
    record = PushButton(recordt, text="Press to start recording temps", command=save_time)
    all_temps = ListBox(recordt, items=babies)
    app.repeat(15000, save_time)

def save_time():
    global all_temps, recordt
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    temps = recordt.\
        question(current_time, "It is: " + current_time + " Record babies temperature")
    if temps != "":
        temps = float(temps)
        babies.append(temps)
        all_temps.append(temps)
        print(babies)
        if temps < 36.0:
            recordt.warn("LOW TEMP", "Please call the nurse the temperature is too low")
        elif temps > 37.5:
            recordt.warn("HIGH TEMP", "Please call the nurse the temperature is too high")
        else:
            print(temps)
        recordt.update()





def open_window():
    global babyname
    life = Window(app, title="Second Window", height=1920, width=1400, bg="#3e2f5b")
    nothing = Box(life, width=1400, height=550, align="bottom")
    box1 = Box(life, height=50, width=200, align="left")
    box1.bg = "#e0ca3c"
    text = Text(box1, font="Secular One", text="Enter baby's name:", size=20, color="#3e2f5b")
    nothing1 = Box(life, height=56, width=150, align="left")
    babyname = TextBox(nothing1, height="fill", width="fill")
    babyname.bg = "#e0ca3c"
    babyname.text_color = "#3e2f5b"
    babyname.text_size = 20
    save = PushButton(life, text = "Save", align="left", command=save_baby)
    save.font = "Secular One"
    save.text_color = "#3e2f5b"
    save.text_size = 20
    life.show(wait=True)
    record = PushButton(life, text="Record baby's temperature", align="bottom", command=open_window1)
    record.font = "Secular One"
    record.text_color = "#3e2f5b"
    record.text_size = 20



def save_baby():
    baby = [babyname.value]
    babies.append(baby)
    print(babies)





app = App(title="Baby's Temperatures", height=1920, width=1400, bg="#3e2f5b")
empty = Box(app, width=1400, height=550, align="bottom")
box = Box(app, height=50, width=150, align="left", )
box.bg = "#e0ca3c"
text = Text(box, font="Secular One", text="New Baby:", size=20, color="#3e2f5b")
empty1 = Box(app, height=56, width=150, align="left")
newbaby = PushButton(empty1, height="fill", width="fill", text="Click here:", command=open_window)
newbaby.font = "Secular One"
newbaby.text_color = "#3e2f5b"
newbaby.text_size = 20



app.display()

