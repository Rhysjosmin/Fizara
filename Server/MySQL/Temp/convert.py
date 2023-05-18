from PIL import Image as _Image
from werkzeug.utils import secure_filename
import os
import random
PharmacyDB=[]
path='Server/MySQL/Temp/DELETEMEFOLDER/'
count=0
def Convert(filepath,Name,Price):
    global count
    
    # filename = secure_filename(Image.filename)
    # filepath = path+'Images'+'/'+filename
    # Image.save(filepath)
    print(f'{count} : {filepath}')
    im = _Image.open(filepath)
    resized = im.resize((500, 500))
    resized.save(filepath)

    # with open(filepath, 'rb') as f:
    #     Image = 'f.read()'
    item = {

        'Image': './Server/DB/Images/'+filepath,
        'Name': Name.capitalize(),
        'Price': str(Price)
    }
    PharmacyDB.append(item)
    count+=1

os.chdir('Server/MySQL/Temp/DELETEMEFOLDER')
Files=os.listdir()
path='Server/MySQL/Temp/DELETEMEFOLDER/'
for File in Files:
    Convert(File,File,random.randrange(20,2000))
    
print(PharmacyDB)

