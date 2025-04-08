import os 
from pathlib import Path
import logging


# Setting up logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

list_of_files = [
    "src/__init__.py", #to construct modularity
    "src/helper.py", #to write all functionality
    "src/prompt.py", #to specified system prompt
    ".env",
    #"requirements.txt",
    "setup.py", #because we want to use src as our local package
    "app.py", 
    "research/trials.ipynb" # all the code first implemented in this file then we add modularity
]



for file_path in list_of_files:
    filepath = Path(file_path)
    filedir,filename = os.path.split(filepath)

    #folder creation
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file : {filename}")
    #file creation    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file : {filepath}")
    
    else:
        logging.info(f"{filename} is already exists")