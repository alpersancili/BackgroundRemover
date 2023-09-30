import tkinter
from tkinter import filedialog
from rembg import remove

newimage_file = "C:/Users/alper/OneDrive/Masaüstü/newimage.jpeq."

def open_file_dialog():
    file_path = filedialog.askopenfilename(title="Select a Image")
    if file_path:
        with open(file_path, "rb") as i:
            with open(newimage_file, "wb") as o:
                input_file = i.read()
                output_file = remove(input_file)
                o.write(output_file)

window = tkinter.Tk()
window.title("PDF CONVERTER")
window.minsize(width=400, height=400)

btn = tkinter.Button(text="Select a Image", command=open_file_dialog, bg="red")
btn.config(height=3, width=10)
btn.place(x=170, y=150)

window.mainloop()