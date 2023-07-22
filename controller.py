#!/usr/bin/env python
# coding: utf-8

# # Controller

# This notebook is responsible for integrating all the notebooks present in this project
# 
# When executed, this notebook automaticall runs all other notebooks sequantially.

# In[ ]:


# Importing important libraries

import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.metrics import structural_similarity as ssim

#Resizing the Plots
plt.rcParams["figure.figsize"] = (12, 12)


# In[ ]:


get_ipython().run_line_magic('store', '-z  # Deleting all pre- stored variables')


# In[ ]:


# Running gui_1.ipynb

get_ipython().run_line_magic('run', './gui_1.ipynb')


# In[ ]:


# The GUI file produces and then stores the variables path and option
# Reading the stored variables

get_ipython().run_line_magic('store', '-r selectedImage')
get_ipython().run_line_magic('store', '-r path')
get_ipython().run_line_magic('store', '-r option')

print('Image selected: ', selectedImage)
print('Path: ', path)
print('Currency type: ', option)


# In[ ]:


if selectedImage == True:
    if option == 1:                        # For 500 currency note
        get_ipython().run_line_magic('run', './500_Testing.ipynb')
    elif option == 2:                      # For 2000 currency note
        get_ipython().run_line_magic('run', './2000_Testing.ipynb')


# In[ ]:


if selectedImage == True:
    # The above file produces and stores result_list variable
    # Reading the variable
    get_ipython().run_line_magic('store', '-r result_list')

    # Showing the results
    # The result list variable is a list of lists and each list conatins details about each feature
    for x in result_list:
        if x[0] is not None:            
            plt.imshow(x[0])   # Showing images
            plt.show()


# In[ ]:


if selectedImage == True:
# Show output in GUI

    get_ipython().run_line_magic('run', './gui_2.ipynb')


# In[ ]:


get_ipython().run_line_magic('store', '-z  # Deleting all pre- stored variables')


# In[ ]:




