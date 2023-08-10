import time
from win10toast import ToastNotifier
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bardapi import Bard
import keyboard
def readtxt(txt):
    try:
        with open(txt,'r') as file:
            isi_file = file.read()
        return isi_file
    except FileNotFoundError:
        print(f"file'{txt}' tidak ditemukan.")
        return None
    except Exception as e:
        print("terjadi kesalahan: {e}")
        return None
def end():
    print("program terhenti")
    browser.quit()

def triger():
    alert=ToastNotifier()
    alert.show_toast("generate",icon_path="bang.ico",duration=2)
    soal = WebDriverWait(browser, 60).until(
    EC.presence_of_element_located((By.XPATH,"//*[@id='checkans']/div[1]"))
    )
    pila = WebDriverWait(browser, 60).until(
    EC.presence_of_element_located((By.XPATH,"//*[@id='checkans']/div[3]/div[1]"))
    )
    pilb = WebDriverWait(browser, 60).until(
    EC.presence_of_element_located((By.XPATH,"//*[@id='checkans']/div[3]/div[3]"))
    )
    pilc = WebDriverWait(browser, 60).until(
     EC.presence_of_element_located((By.XPATH,"//*[@id='checkans']/div[3]/div[5]"))
    )
    pild = WebDriverWait(browser, 60).until(
    EC.presence_of_element_located((By.XPATH,"//*[@id='checkans']/div[3]/div[7]"))
        )

    a=pila.text
    b=pilb.text
    c=pilc.text
    d=pild.text
    time.sleep(5)
    ask=" soal : "+soal.text+'.Pilihan ganda : A. '+a+' B. '+b+' C. '+c+' D. '+d+' . pilihlah jawaban yang paling sesuai dan tolong jawab dengan singkat + konsisten'
    answer=bard.get_answer(ask)['content']   
    print('validation---proses')
    answerl= answer.lower()
    pilal = "jawaban adalah adalah: **a. a. "+a.lower()+'**'+" **"+a.lower()+"**"+" **"+a.lower()+"**."
    pilbl = "jawaban adalah adalah: **b. b. "+b.lower()+'**'+" **"+b.lower()+"**"+" **"+b.lower()+"**."
    pilcl = "jawaban adalah adalah: **c. c. "+c.lower()+'**'+" **"+c.lower()+"**"+" **"+c.lower()+"**."
    pildl = "jawaban adalah adalah: **d. d. "+d.lower()+'**'+" **"+d.lower()+"**"+" **"+d.lower()+"**."

    answers = set(answerl.split())
    pilas = set(pilal.split())
    pilbs = set(pilbl.split())
    pilcs = set(pilcl.split())
    pilds = set(pildl.split())

    kataA = answers.symmetric_difference(pilas)
    kataB = answers.symmetric_difference(pilbs)
    kataC = answers.symmetric_difference(pilcs)
    kataD = answers.symmetric_difference(pilds)

    print(answer)
    if len(kataA) < len(kataB) and len(kataA) < len(kataC) and len(kataA) < len(kataD)   :       
        pila.click()
    elif len(kataB) < len(kataA) and len(kataB) < len(kataC) and len(kataB) < len(kataD)   :       
        pilb.click()
    elif len(kataC) < len(kataA) and len(kataC) < len(kataB) and len(kataC) < len(kataD)   :     
        pilc.click()
    elif len(kataD) < len(kataA) and len(kataD) < len(kataB) and len(kataD) < len(kataC)  :
        pild.click()
    else:
        alert.show_toast("Failed Generate",icon_path="bang.ico",duration=2)

cookie_txt="cookies.txt"
url_txt="url.txt"
token = readtxt(cookie_txt)
bard = Bard(token=token)
options = webdriver.EdgeOptions()
options.add_experimental_option("detach", True )
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches", ['enable-automation'])
browser = webdriver.Edge(options=options,service=None )
browser.get(readtxt(url_txt))
keyboard.add_hotkey('esc', end)
keyboard.add_hotkey('`', triger)
o=input('PRESS ESC TO EXIT  ')
       
keyboard.remove_hotkey(triger)
keyboard.remove_hotkey(end)
