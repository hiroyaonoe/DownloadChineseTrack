import os
import glob
import shutil
import zipfile
from download import download



os.makedirs('contents/1stCheckTest', exist_ok=True)
url = "http://hanyujiaocai.jinkan.kyoto-u.ac.jp/2017beijing/2017CALL/download/"


for i in range(11,16):


    zip_name = "L" + str(i) + ".zip"
    zip_url = url + zip_name
    download(zip_url,'./contents/1stCheckTest/'+zip_name)

    with zipfile.ZipFile('contents/1stCheckTest/'+zip_name) as existing_zip:
        existing_zip.extractall('contents/1stCheckTest/')





Q1_list  = glob.glob('contents/1stCheckTest/L11/honbun/01.mp3')
Q2_list  = glob.glob('contents/1stCheckTest/L11/bunpou/4/06.mp3')
Q3_list  = glob.glob('contents/1stCheckTest/L12/bunpou/2/05.mp3')
Q4_list  = glob.glob('contents/1stCheckTest/L12/bunpou/4/03.mp3')
Q5_list  = glob.glob('contents/1stCheckTest/L13/honbun/07.mp3')
Q6_list  = glob.glob('contents/1stCheckTest/L13/bunpou/4/04.mp3')
Q7_list  = glob.glob('contents/1stCheckTest/L14/bunpou/3/04.mp3')
Q8_list  = glob.glob('contents/1stCheckTest/L15/bunpou/2/01.mp3')
Q9_list  = glob.glob('contents/1stCheckTest/L15/bunpou/3/02.mp3')
Q10_list = glob.glob('contents/1stCheckTest/L15/bunpou/4/03.mp3')

Q3_ans_list  = glob.glob('contents/1stCheckTest/L12/bunpou/2/06.mp3')
Q6_ans_list  = glob.glob('contents/1stCheckTest/L13/bunpou/4/05.mp3')



new_Q1_path  = Q1_list[0][:-6]  + '001_A.mp3'
new_Q2_path  = Q2_list[0][:-6]  + '002_A.mp3'
new_Q3_path  = Q3_list[0][:-6]  + '003_A.mp3'
new_Q4_path  = Q4_list[0][:-6]  + '004_A.mp3'
new_Q5_path  = Q5_list[0][:-6]  + '005_A.mp3'
new_Q6_path  = Q6_list[0][:-6]  + '006_A.mp3'
new_Q7_path  = Q7_list[0][:-6]  + '007_A.mp3'
new_Q8_path  = Q8_list[0][:-6]  + '008_A.mp3'
new_Q9_path  = Q9_list[0][:-6]  + '009_A.mp3'
new_Q10_path = Q10_list[0][:-6] + '010_A.mp3'

new_Q3_ans_path = Q3_ans_list[0][:-6] + '003_B.mp3'
new_Q6_ans_path = Q6_ans_list[0][:-6] + '006_B.mp3'


os.rename(Q1_list[0],new_Q1_path)
os.rename(Q2_list[0],new_Q2_path)
os.rename(Q3_list[0],new_Q3_path)
os.rename(Q4_list[0],new_Q4_path)
os.rename(Q5_list[0],new_Q5_path)
os.rename(Q6_list[0],new_Q6_path)
os.rename(Q7_list[0],new_Q7_path)
os.rename(Q8_list[0],new_Q8_path)
os.rename(Q9_list[0],new_Q9_path)
os.rename(Q10_list[0],new_Q10_path)

os.rename(Q3_ans_list[0],new_Q3_ans_path)
os.rename(Q6_ans_list[0],new_Q6_ans_path)



shutil.move(new_Q1_path,'contents/1stCheckTest/')
shutil.move(new_Q2_path,'contents/1stCheckTest/')
shutil.move(new_Q3_path,'contents/1stCheckTest/')
shutil.move(new_Q4_path,'contents/1stCheckTest/')
shutil.move(new_Q5_path,'contents/1stCheckTest/')
shutil.move(new_Q6_path,'contents/1stCheckTest/')
shutil.move(new_Q7_path,'contents/1stCheckTest/')
shutil.move(new_Q8_path,'contents/1stCheckTest/')
shutil.move(new_Q9_path,'contents/1stCheckTest/')
shutil.move(new_Q10_path,'contents/1stCheckTest/')


shutil.move(new_Q3_ans_path,'contents/1stCheckTest/')
shutil.move(new_Q6_ans_path,'contents/1stCheckTest/')



for i in range(11,16):

    zip_name = "L" + str(i) + ".zip"
    zip_url = url + zip_name
    os.remove('contents/1stCheckTest/'+zip_name)

    shutil.rmtree('contents/1stCheckTest/L' + str(i))
