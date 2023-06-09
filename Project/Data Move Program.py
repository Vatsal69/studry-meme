import os
import shutil

#from_dir's value should be "Downloads" but for zero bugs and error i will make a subfolder in this folder 
from_dir = "F:/OneDrive - J. K. Cement Ltd/Desktop/Its_Vp_Vasu/Code Files/Project/downloads"

to_dir = "F:/OneDrive - J. K. Cement Ltd/Desktop/Its_Vp_Vasu/Code Files/Project/final destination"

list_of_files = os.listdir(from_dir)

for file_name in list_of_files:
    name, extension = os.path.splitext(file_name)
    print(name)
