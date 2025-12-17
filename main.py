from guizero import *
from PIL import Image
import os

current_img_path = None

def upd_meme():
    

    draw.text(
        0,0, textbox.value, color= combo.value, font= group.value, size= slide.value
    )

def load_img():
    
    img_file = []
    for f in os.listdir("birds"):
        if f.endswith(('.png')):
            img_file.append(f)
    return img_file
def chon_anh(selected_img):
    draw.clear()

    global current_img_path
    current_img_path =f"birds/{selected_img}"

    image = Image.open(current_img_path)
    size = (500, 500)
    resized_image = image.resize(size)
    resized_image.save(current_img_path)
    draw.image(0,0,resized_image)

app = App(title="APP", width=900, height=820)
box = Box(app, layout="grid", width=450, height=250, border=True)
Text(box, text="Enter text: ", size =15, grid=[0,0])
textbox = TextBox(box, width=25, grid=[1,0])
textbox.text_size = 15
Text(box, text="Select text color: ", size =15, grid=[0,1])
combo = Combo(box, options=["black", "Crimson", "blue"], grid=[1,1])
combo.text_size = 15
combo.bg = "#28C2FF"
Text(box, text="Select font: ", size =15, grid=[0,2])
group = ButtonGroup(box, options=["Arial", "Times New Roman", "Courier"], grid=[1,2])
group.text_size = 15
group.bg = "#F2CD5D"
Text(box, text="Text Size: ", size =15, grid=[0,3])
slide = Slider(box, start=10,end= 100, width=250, grid=[1,3])

push = PushButton(app, text="Update", width=6, command=upd_meme)
push.text_size = 15
push.bg="#FF00FF"

box1 = Box(app, layout="grid", width=750, height=600)
lst = ListBox(box1, items=load_img(), grid=[0,0], command=chon_anh)
lst.text_size=15
lst.bg= "#4169E1"
draw = Drawing(box1, grid=[1, 0], width=500, height=500)


app.display()