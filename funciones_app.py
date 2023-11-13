import pickle
from deep_translator import GoogleTranslator
#from selenium import webdriver
#from selenium.webdriver.chrome.options import Options
#from selenium.webdriver import Keys
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.support.wait import WebDriverWait
#from bs4 import BeautifulSoup
import time

#Traducir texto
def traducir(texto):
    traducidos=[]
    for text in texto:
        traducidos.append(GoogleTranslator(source='spanish', target='russian').translate(text))
    return traducidos

#Transformar la data para la red neuronal
def procesar_data(vectorizer,data):
    lista=vectorizer.transform(data)
    lista=lista.toarray()
    return lista

#Obtener una estructura
def obtener(nombre):
    with open(nombre+'.pkl', 'rb') as file:
        return pickle.load(file)

#Obtener tweets de usuario
def obtener_tweets(usuarios):
    #Configurando selenium
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    prefs = {"credentials_enable_service": False,
         "profile.password_manager_enabled": False}
    options.add_experimental_option("prefs", prefs)
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    driver = webdriver.Chrome(options=options)
    #Log Twitter
    driver.get("https://twitter.com/i/flow/login")
    username = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[autocomplete="username"]')))
    username.send_keys("u59645381@gmail.com")
    username.send_keys(Keys.ENTER)
    username = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[data-testid="ocfEnterTextTextInput"]')))
    username.send_keys("YOU683493514748")
    username.send_keys(Keys.ENTER)
    password = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[name="password"]')))
    password.send_keys("unmsm2023")
    password.send_keys(Keys.ENTER)
    #Obteniendo tweets
    time.sleep(10)
    lista_usuarios=[]
    for us in usuarios:
        driver.get("https://twitter.com/search?q=from%3A%40"+us+"&src=recent_search_click&f=live")
        lista_tweets=[]
        lista_fechas=[]
        lista=[]
        last_height= driver.execute_script("return document.body.scrollHeight")
        const=last_height
        time.sleep(10)
        while 1:
            time.sleep(1)
            html = driver.page_source
            bs=BeautifulSoup(html,'html.parser')
            all_tweets = bs.find_all('article')
            for j in all_tweets:
                for i in j.select("time"):
                    fecha=i.text
                    #print(i)
                fecha=str(fecha)
                for i in j.select('div[data-testid="tweetText"]'):
                    tweet=i.text
                    #print(i)
                tweet=str(tweet)
                if fecha not in lista_fechas:
                    lista_tweets.append(tweet)
                    lista_fechas.append(fecha)
            print(last_height)
            print(len(lista_fechas))
            if len(lista_fechas)>20 or last_height>30000:
                break
            driver.execute_script("window.scrollTo(0,"+str(last_height)+")")
            last_height = const+last_height
        lista_usuarios.append([us,lista_fechas,lista_tweets])
    driver.quit()
    return lista_usuarios