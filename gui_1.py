#!/usr/bin/env python
# coding: utf-8

# # GUI- Starting

# This file will be used as the starting GUI of our project. 
# 
# When this script is run, a tkinter window appears which allows the user to choose an image,  select the currency type and then submit the image for processing. The user can put the test currency image in his/her system and then through this GUI, the user can browse his/her system and find the test image

# In[ ]:


# Importing necessary packages to be used

from tkinter import *
from PIL import Image
from PIL import ImageTk
import tkinter.filedialog as tkFileDialog
import cv2
from tkinter import messagebox
from IPython import get_ipython

# In[ ]:


# This func is called whenever a radio button is clicked
def currency_type():
    global option
    option = int(var.get())

# This func is called whenever the 'Select an image' button is clicked
def select_image():
    # grab a reference to the image canvas and the path variable
    global canvas
    global path
    
    canvas.delete("all")
    # open a file chooser dialog and allow the user to select an input
    # image
    path = tkFileDialog.askopenfilename()

    # ensure a file path was selected
    if len(path) > 0 and path[-4:] == '.jpg':
        # load the image from disk
        image = cv2.imread(path)
        original_image = image.copy()

        #  represents images in BGR order; however PIL represents
        # images in RGB order, so we need to swap the channels
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = cv2.resize(image, (675, 300))

        # convert the images to PIL format...
        image = Image.fromarray(image)

        # ...and then to ImageTk format
        image = ImageTk.PhotoImage(image)

        canvas.image = image
        canvas.create_image(0, 0, anchor=NW, image=image) 
    else:
        messagebox.showinfo("Warning","Please choose an image! (It should be a .jpg file)")
                
# Submit the image for preprocessing if the image path is valid and the currency type is chosen
# Currently, this GUI is just a prototype. So the image is not being sent anywhere. 
# 
def submit():
    global option
    global path
    global selectedImage
    if len(path) <= 0:
        messagebox.showinfo("Warning","Please choose an image!")
    elif option == -1:
        messagebox.showinfo("Warning","Please choose the currency type!")
    else:
        print(path)
        print(option)
        selectedImage = True
        messagebox.showinfo("Info","Image sent for processing!")
        root.destroy()

# Exit window
def exit_window():
    root.destroy()

    
# Main function
# Declaring root window
root = Tk() 
root.title("Fake Currency Detection System")

# Declaring the attributes of the GUI window
root.resizable(False, False)  # This code helps to disable windows from resizing

window_height = 600
window_width = 1100

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

# Declaring variables
path = ""                      # Stores path of image selected
option = -1                    # Stores option number. -1 ---> No option selected
selectedImage = False          #                        1 ---> 500 currency type selected
                               #                        2 ---> 1000 currency type selected

# create all of the main containers
top_frame = Frame(root, bg='black', width=1090, height=50, pady=3)
frame1 = Frame(root, bg='cyan', width=1090, height=80, padx=3, pady=3)
frame2 = Frame(root, bg='brown', width=1090, height=400, pady=5, padx = 5)
frame3 = Frame(root, width=1090, height=50, pady=3)
frame4 = Frame(root, width=1090, height=50, pady=3)
frame5 = Frame(root, bg='white', width=1090, height=20, pady=3)

# Assigning all frames in a grid layout on the root window
top_frame.grid(row = 1, column = 1, padx = 5, pady = 5)
frame1.grid(row = 2, column = 1, padx = 5, pady = 5)
frame2.grid(row = 3, column = 1, padx = 5, pady = 5)
frame3.grid(row = 4, column = 1, padx = 5, pady = 5)
frame4.grid(row = 5, column = 1, padx = 5, pady = 5)
frame5.grid(row = 6, column = 1, padx = 5, pady = 5)

# Title label
title = Label(master=top_frame, text="FAKE CURRENCY DETECTION SYSTEM", fg = 'dark blue', font = "Verdana 28 bold")
title.pack() # Put the label into the window

# Text label
text1 = Label(master=frame1, text="This is a fake currency detection sytem. Select the currency type, browse your image file and get started!", fg = 'blue', font = "Verdana 10")
text1.pack() 

# Creating a canvas to display the image
canvas = Canvas(master=frame2, width = 675, height = 300)  
canvas.pack()  

# Text label
text1 = Label(master=frame3, text="Select currency type: ", fg = 'black', font = "Verdana 12")
text1.pack(side = 'left') 

# Creating radio button to choose between 500 or 2000 currency notes
var = IntVar()
R1 = Radiobutton(master=frame3, text="500", variable=var, value=1, command=currency_type, font = "Verdana 15")
R1.pack(anchor =  W)

R2 = Radiobutton(master=frame3, text="2000", variable=var, value=2,command=currency_type, font = "Verdana 15")
R2.pack(anchor =  W)

# Button to browse the image
btn = Button(master = frame4, text="Select an image", command=select_image, font = "Verdana 15 bold", fg='blue')
btn.pack(side = 'left', padx=10, pady=10)

# Button to submit the image
btn = Button(master = frame4, text="Submit", command=submit, font = "Verdana 15 bold", fg='green')
btn.pack(side = 'left', padx=10, pady=10)

# Button to exit window
btn = Button(master = frame4, text="Exit", command=exit_window, font = "Verdana 15 bold", fg='red')
btn.pack(side = 'left', padx=10, pady=10)

# Open the root window
root.mainloop() 


# In[ ]:


# When an image is selected, currency type is chosen and submit button is clicked
# Then the path of the image and the currency type is stored using Ipython magic commands
get_ipython().run_line_magic('store', 'selectedImage')

if selectedImage == True:
    get_ipython().run_line_magic('store', 'path')
    get_ipython().run_line_magic('store', 'option')


# In[ ]:




