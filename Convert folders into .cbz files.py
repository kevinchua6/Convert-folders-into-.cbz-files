import os, zipfile  
from os.path import join  

def zipfolder(foldername, filename):   
    myzip = zipfile.ZipFile(filename, 'w', zipfile.ZIP_DEFLATED)  
    for root, dirs, files in os.walk(foldername):  
        for name in files:  
            myzip.write(join(root, name))  
    myzip.close() 

root_path = r'ROOT_DIRECTORY' #Directory with files to be zipped to .cbz
    

for root, dirs, files in os.walk(root_path):  
    for name in dirs:
        zipfolder(root, name + ".CBZ")
        print('Zipping '+name)