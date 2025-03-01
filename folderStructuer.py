import logging.config
import os
from pathlib import Path
import logging


##Set up logging 
logging.basicConfig(level=logging.INFO , format='[%(asctime)s]: %(message)s:')


##List of the Folder/filee

list_of_file = [
    'src/__init__.py', ##Constructor Filee, It is used to initialize the package when it is imported
    'src/helper.py',
    'src/promt.py',
    'secretkey.py',
    'setup.py', # a module used to build and distribute Python packages. It typically contains information about the package, such as its name, version, and dependencies
    'app.py',
    'research/trials.ipynb',
    'templates/index.html'
]


##logic for folderStructuer

for filepath in list_of_file:
    filepath = Path(filepath) ##path detect os and according to thar transfom it into backword and forward slashhh
    filedir, filename = os.path.split(filepath) ##spliti into folder and filee ex src/ex.py


    if filedir != "": ##not empty it means there is filedir (above output)
        os.makedirs(filedir , exist_ok=True) #If the target directory already exists an OSError is raised if its value is False otherwise not
        logging.info(f"Creating Directory {filedir} for the file: {filename}")

    if(not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath , "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    
    else:
        logging.info(f"{filename} is already exitss")