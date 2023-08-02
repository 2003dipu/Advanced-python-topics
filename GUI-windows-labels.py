from tkinter import *
from PIL import Image, ImageTk

window = Tk()
window.title("Dipu Singha's first GUI program")
window.config(background="#5cfcff")

# Load the image using Pillow
image = Image.open('C:\\Users\\t\\Downloads\\aiart.jpg')

# Resize the image to a smaller size
image = image.resize((300, 300), Image.LANCZOS)  # Use Image.LANCZOS for high-quality resizing

# Convert the image to a format compatible with PhotoImage
photo = ImageTk.PhotoImage(image)

# Create a label for the image
image_label = Label(window, image=photo)
image_label.pack()

# Create a label for the text
text_label = Label(window,
                   text="Do you even code, Dipu Singha?",
                   font=('Arial', 20, 'bold'),
                   fg='#00FF00',
                   bg='black',
                   padx=20,
                   pady=10)
text_label.pack()

window.mainloop()
