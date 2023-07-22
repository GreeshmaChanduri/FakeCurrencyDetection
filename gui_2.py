#!/usr/bin/env python
# coding: utf-8

# # GUI - ENDING

# This is the ending GUI of the project
# 
# This GUI will show the complete result analysis of each feature and the status (Pass/ Fail) of each feature

# In[ ]:


# Importing necessary packages to be used

from tkinter import *
from PIL import Image as PIL_Image
from PIL import ImageTk
import tkinter.filedialog as tkFileDialog
import cv2
from tkinter import messagebox
import matplotlib.pyplot as plt


# In[ ]:


# Retrieving the data stored by the previously running notebooks 

# Result list: contains complete result analysis of each feaature
#get_ipython().run_line_magic('store', '-r result_list')

# Path of input image
#get_ipython().run_line_magic('store', '-r path')


# In[ ]:



# Display the output
def display_output():
    # Creating 4 sub frames inside the master_frame
    sub_frame1 = Frame(master_frame, bg='black', pady=5)
    sub_frame2 = Frame(master_frame, bg='brown', pady=5, padx = 5)
    sub_frame3 = Frame(master_frame, pady=5, padx = 5)
    sub_frame4 = Frame(master_frame, pady=5, padx = 5)
    
    # Packing them in a grid layout
    sub_frame1.grid(row = 1, column = 1, padx = 5, pady = 5)
    sub_frame2.grid(row = 2, column = 1, padx = 5, pady = 5)
    sub_frame3.grid(row = 3, column = 1, padx = 5, pady = 5)
    sub_frame4.grid(row = 4, column = 1, padx = 5, pady = 5)
    
    # Title label in sub_frame1
    title = Label(master=sub_frame1, text="FAKE CURRENCY DETECTION SYSTEM", fg = 'dark blue', font = "Verdana 28 bold")
    title.pack() # Put the label into the window
    
    # Displaying input image in sub_frame2
    canvas_input = Canvas(master=sub_frame2, width = 675, height = 300)  
    canvas_input.pack()
    
    # Ensuring that file path is valid
    if len(path) > 0 and path[-4:] == '.jpg':
        # load the image from disk
        image = cv2.imread(path)
        original_image = image.copy()

        #  represents images in BGR order; however PIL represents
        # images in RGB order, so we need to swap the channels
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = cv2.resize(image, (675, 300))

        # convert the images to PIL format...
        image = PIL_Image.fromarray(image)

        # ...and then to ImageTk format
        image = ImageTk.PhotoImage(image)

        canvas_input.image = image
        canvas_input.create_image(0, 0, anchor=NW, image=image) 
    
    pass_count = 0
    
    # Displaying analysis of each feature in sub_frame4
    # Looping over result_list and displaying the data for each feature
    for i in range(4):
        for j in range(3):
            feature_num = 3*i+j      # This can vary from 0 to 9
            
            if feature_num < 10:     # There are 10 features
                sub_frame4.grid_rowconfigure(i, weight=1)
                sub_frame4.grid_columnconfigure(j, weight=1)
                
                # Creating a frame to display each image
                feature_frame = Frame(master = sub_frame4, relief = RAISED, borderwidth = 1, bg='light blue')
                feature_frame.grid(row = i, column = j, padx = 20, pady = 20, sticky="nsew")
                
                # Creating frames inside the feature_frame to display the details of a feature
                frame1 = Frame(feature_frame, padx=3, pady=3)
                frame2 = Frame(feature_frame, bg='brown', pady=5, padx = 5)
                frame3 = Frame(feature_frame)
                frame4 = Frame(feature_frame)
                frame5 = Frame(feature_frame)
                
                # Assigning a grid layout
                frame1.grid(row = 1, column = 1, padx = 5, pady = 5, ipadx = 100)
                frame2.grid(row = 2, column = 1, padx = 5, pady = 5)
                frame3.grid(row = 3, column = 1, padx = 5, pady = 5)
                frame4.grid(row = 4, column = 1, padx = 5, pady = 5)
                frame5.grid(row = 5, column = 1, padx = 5, pady = 5)
                
                # Displaying the feature number through a label in frame1 ------------
                label1 = Label(master = frame1, text = f"Feature {feature_num +1}", fg = 'black', font = "Verdana 12 bold")
                label1.pack()

                # Creating a canvas to display the image in frame2 ------------
                canvas = Canvas(master=frame2, width = 200, height = 200)  
                canvas.pack()

                image = result_list[feature_num][0].copy()

                h, w = image.shape[:2]
                aspect_ratio = w/h

                resize_height = 0
                resize_width = 0
                img_x = 0
                img_y = 0
                
                if h > w:
                    resize_height = 200
                    resize_width = aspect_ratio * resize_height
                    img_x = (200 - resize_width)/2
                elif h < w:
                    resize_width = 200
                    resize_height = resize_width / aspect_ratio
                    img_y = (200 - resize_height)/2
                else:
                    resize_height = 200
                    resize_width = 200
                
                resize_height = int(resize_height)
                resize_width = int(resize_width)
                img_x = int(img_x)
                img_y = int(img_y)

                # Resizing the image while maintaining the aspect ratio
                image = cv2.resize(image, (resize_width, resize_height))

                # convert the images to PIL format...
                image = PIL_Image.fromarray(image)

                # ...and then to ImageTk format
                image = ImageTk.PhotoImage(image)

                # Show the image in canvas
                canvas.image = image
                canvas.create_image(img_x, img_y, anchor=NW, image=image) 
                
                # 2nd label in frame3 ------------
                if feature_num < 7:
                    avg_score = result_list[feature_num][1]
                    avg_score = "{:.3f}".format(avg_score)
                    text2 = "Avg. SSIM Score: " + avg_score
                elif feature_num < 9:
                    line_count = result_list[feature_num][1]
                    line_count = "{:.3f}".format(line_count)
                    text2 = "Avg. Number of lines: " + line_count
                else:
                    status = result_list[feature_num][1]
                    if status == True:
                        text2 = "9 characters detected!"
                    else:
                        text2 = "Less than 9 characters detected!"
                label2 = Label(master = frame3, text = text2, fg = 'dark blue', font = "Verdana 11", bg='light blue')
                label2.pack()
                
                # 3rd label in frame4 ------------
                if feature_num < 7:
                    max_score = result_list[feature_num][2]
                    max_score = "{:.3f}".format(max_score)
                    text3 = "Max. SSIM Score: " + max_score
                elif feature_num < 9:
                    text3 = ""
                else:
                    text3 = ""
                label3 = Label(master = frame4, text = text3, fg = 'dark blue', font = "Verdana 11", bg='light blue')
                label3.pack()
                
                # 4th label in frame5 ------------
                if feature_num < 7:
                    status = result_list[feature_num][3]
                elif feature_num < 9:
                    status = result_list[feature_num][2]
                else:
                    status = result_list[feature_num][1]
                
                if status == True:
                    pass_count += 1
                    label4 = Label(master = frame5, text = "Status: PASS!", fg = 'green', font = "Verdana 11 bold", bg='light blue')
                    label4.pack()
                else:
                    label4 = Label(master = frame5, text = "Status: FAIL!", fg = 'red', font = "Verdana 11 bold", bg='light blue')
                    label4.pack()
    
    # Result label in sub_frame3
    result = Label(master=sub_frame3, text= f"RESULT: {pass_count} / 10 features PASSED!", fg = 'green', font = "Verdana 24 bold")
    result.pack()
    
    
# Configuring the scroll bar widget and canvas widget
def scrollbar_function(event):
    canvas.configure(scrollregion=canvas.bbox("all"),width=1050,height=550)

    
# Main Function
# Declaring root window and specifying its attributes
root=Tk()
root.title('Fake Currency Detection - Result Analysis')

# Defining attributes of root window
root.resizable(False, False)  # This code helps to disable windows from resizing

window_height = 600
window_width = 1100

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

# Creating a main frame inside the root window
main_frame=Frame(root,relief=GROOVE, bd=1)
main_frame.place(x=10,y=10) # Placing the frame at (10, 10)

# Creating a canvas inside main_frame
canvas=Canvas(main_frame)
master_frame=Frame(canvas)  # Creating master_frame inside the canvas

# Inserting  and configuringscrollbar widget
myscrollbar=Scrollbar(main_frame,orient="vertical",command=canvas.yview)
canvas.configure(yscrollcommand=myscrollbar.set)

myscrollbar.pack(side="right",fill="y")
canvas.pack(side="left")
canvas.create_window((0,0),window=master_frame,anchor='nw')
master_frame.bind("<Configure>",scrollbar_function)

# Displaying output
display_output()

# Open the root window and loop
root.mainloop()

