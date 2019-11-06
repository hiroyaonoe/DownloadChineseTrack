import os
import glob
import shutil
import zipfile
from download import download



os.makedirs('contents/honbun', exist_ok=True)
url = "http://hanyujiaocai.jinkan.kyoto-u.ac.jp/2017beijing/2017CALL/download/"

for i in range(1,23):


    zip_name = "L" + str(i) + ".zip"
    zip_url = url + zip_name
    download(zip_url,'./contents/'+zip_name)

    with zipfile.ZipFile('contents/'+zip_name) as existing_zip:
        existing_zip.extractall('contents/')


    folder_name = 'L' + str(i)
    for path in sorted(glob.glob('contents/L'+str(i)+'/honbun/[A-Z]*')):
        shutil.move(path, 'contents/honbun/')



    j = 1
    for path in sorted(glob.glob('contents/L'+str(i)+'/bunpou/*/[0-9]*')):

        if(j<10):
            new_file_path = path[:-6] + '000' + str(j) + '.mp3'
        elif(j<100):
            new_file_path = path[:-6] + '00'  + str(j) + '.mp3'
        else:
            new_file_path = path[:-6] + '0'   + str(j) + '.mp3'


        os.rename(path,new_file_path)
        shutil.move(new_file_path,'contents/L'+str(i)+'/')
        j = j + 1







#delete folders
for i in range(1,23):
    zip_name = "L" + str(i) + ".zip"
    zip_url = url + zip_name
    os.remove('contents/'+zip_name)
    folder_name = 'L' + str(i)
    shutil.rmtree('contents/'+folder_name+'/mondai')
    shutil.rmtree('contents/'+folder_name+'/tango')
    shutil.rmtree('contents/L'+str(i)+'/honbun')
    shutil.rmtree('contents/L'+str(i)+'/bunpou/')
