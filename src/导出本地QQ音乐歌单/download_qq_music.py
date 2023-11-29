import os

# --------------------------------------��ȡ�赥----------------------------------


# ����ļ�Ŀ¼������everything���ң��ҵ�  QQMusicCache\QQMusicLyricNew����Ŀ¼copy�������ŵ�file_path��
file_path= "E:\QQMusicCache\QQMusicLyricNew" # ��Ŀ¼�´����������ֵ�����
save_file_path = r"�赥����ĵط�" # ������д��ַ

# file_path Ŀ¼�µ��ļ���ʽ��ÿ�����ʹ�� - �ָ�
# ǰ��Ϊ����������ȻҲ����ΪһȺ���֣�һȺ���ֵ�����£�ÿ��������_���зָ�
# Ȼ���Ǹ�������
# 330 ����֪����ϸ���壬Ҳ���Ǹ����б���ı�ţ�
# Ȼ����ר������
# Aimer (����) - �礵�� (Ϧ��) - 330 - �礵��_everlasting snow (Ϧ��_everlasting snow)_qmRoma.qrc


with open(save_file_path, "w",encoding="utf-8") as f:
    lists = os.listdir(file_path)
    for i in lists:
        # file_path Ŀ¼���м��ֽ�β��׺������ǰ������ݶ���࣬����ʹ��_qm.qrc����Ϊ�����������׺�Ƕ��е�
        if i.endswith("_qm.qrc"):
            items = i.split("-")
            author = items[0] 
            song_name = items[1] 
            f.write(song_name + " | " + author + "\n")



# --------------------------------------���ظ���----------------------------------
# ������ҳ�Զ����ķ�ʽ����
from selenium import webdriver  
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
import pyperclip
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests


def download(name,url):
    save_path = r"���������·��"
    html = requests.get(url)
    file_path = save_path + "\\" + name + ".mp3"
    if os.path.exists(file_path):
        pass
    else:
        with open(file_path,"wb") as f:
            f.write(html.content)
        
        
        
with open(save_file_path,'r',encoding="utf-8") as f:
    contents = f.readlines()

options = Options()
options.add_experimental_option("detach",True)

wait_timeout = 10 # ������ȴ�ʱ��

driver = webdriver.Chrome(options=options)


for content in contents:
    song = content.split("|")[0]
    print(song)
    try:
        driver.get(f'https://www.myfreemp3.com.cn/?page=audioPage&type=netease&name={song}')
        
        try:
            close_button = WebDriverWait(driver, wait_timeout).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "a.layui-layer-ico.layui-layer-close.layui-layer-close2")))
            close_button.click()
        except:
            pass
        download_button = WebDriverWait(driver, wait_timeout).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "span.aplayer-list-download.iconfont.icon-xiazai")))
        download_button.click()
        copy_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#m-download > div > div > div.modal-body > div:nth-child(3) > div.input-group-append > a.btn.btn-outline-secondary.copy > i")))
        copy_button.click()
        content = pyperclip.paste()
        download(song,content)
    except:
        pass
    

driver.quit()