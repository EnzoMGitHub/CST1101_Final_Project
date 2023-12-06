import os
from dotenv import load_dotenv

load_dotenv() 

file = os.getenv("file")
file = open(file,'r')
    
file.close()