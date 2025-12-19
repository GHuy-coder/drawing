from guizero import *
from PIL import Image
import os

current_img_path = None

def upd_meme():
    global lst
    chon_anh(lst.value)
    draw.text(
        0,0, chu.value, color= mau.value, font= phong.value, size= co.value
    )
    if meme.value == 'square':
        draw.rectangle(50,50,120,120,color=mau.value)
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
    size = (450, 450)
    resized_image = image.resize(size)
    resized_image.save(current_img_path)
    draw.image(0,0,resized_image)

def dchuyen():
    global x, y
    x = S_x.value
    y = S_y.value
    draw.clear()
    chon_anh(lst.value)
    draw.text(
        x,y, chu.value, color= mau.value, font= phong.value, size= co.value
    )
    if meme.value == 'square':
        draw.rectangle(50,50,120,120,color=mau.value)

    
    

app = App(title="APP", width=900, height=900)
box = Box(app, layout="grid", width=450, height=250, border=True)
box.bg = "#F0FFFF"
Text(box, text="Enter text: ", size =15, grid=[0,0])
chu = TextBox(box, width=25, grid=[1,0])
chu.text_size = 15
Text(box, text="Select text color: ", size =15, grid=[0,1])
mau = Combo(box, options=["black", "Crimson", "blue"], grid=[1,1])
mau.text_size = 15
mau.bg = "#28C2FF"
Text(box, text="Select font: ", size =15, grid=[0,2])
phong = ButtonGroup(box, options=["Arial", "Times New Roman", "Courier"], grid=[1,2])
phong.text_size = 15
phong.bg = "#F2CD5D"
Text(box, text="Text Size: ", size =15, grid=[0,3])
co = Slider(box, start=10,end= 100, width=250, grid=[1,3])
ano_box = Box(app, width=450, height=130, layout="grid")
Text(ano_box, text="Select meme sticker: ", grid=[0,0])
Text(ano_box, text="X", grid=[0,1])
Text(ano_box, text="Y", grid=[0,2])
meme = Combo(ano_box, options=["star", "square", "triangle"], grid=[1,0])
meme.text_size= 13
S_x = Slider(ano_box, start=0, end=430, width=200, grid=[1,1], command=dchuyen)
S_y = Slider(ano_box, start=0, end=430, width=200, grid=[1,2], command=dchuyen)

push = PushButton(app, text="Update", width=6, command=upd_meme)
push.text_size = 15
push.bg="#FF00FF"

box1 = Box(app, layout="grid", width=700, height=600)
lst = ListBox(box1, items=load_img(), grid=[0,0], command=chon_anh)
lst.text_size=15
lst.bg= "#4169E1"
draw = Drawing(box1, grid=[1, 0], width=450, height=450)


app.display()