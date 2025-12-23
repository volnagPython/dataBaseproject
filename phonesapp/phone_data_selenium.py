import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
###############################################################

from selenium.webdriver.common.keys import Keys
from selenium.common import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

##############################################################
# def main():
service = Service(executable_path = ChromeDriverManager().install())
driver = webdriver.Chrome(service = service)
##########################################################
# driver.get("https://example.com")
driver.get("https://brain.com.ua/ukr/Mobilniy_telefon_Apple_iPhone_15_128GB_Black-p1044347.html")
print(50*"-")
######################################################
# try:
#     el = driver.find_element(By.ID, "does-not-exist")
#     print("Found:", el.text)
# except NoSuchElementException as e:
#     print(f"--Caught NoSuchElementException — element not found:--, {e}")
# except Exception as e:
#     print(f"--Other exception-- :, {e}, {type(e)}")
#####################################################


################### Кіл-сть відгуків ###############
try:
    xpath ='//a[@class ="forbid-click"]/span'
    link = driver.find_element(By.XPATH, xpath); print(50*"-")
    print( "Кіл-сть відгуків: ",link.get_attribute("textContent"))
except NoSuchElementException as e:
    print(f"--This element was not found--: {e}")
except Exception as e:
    print(f"--- The information was not found --- :{e}")
finally:
    pass
######################### Колір ########################################
try:
    xpath ='//a[@title="Колір чорний"]'
    link = driver.find_element(By.XPATH, xpath)
    time.sleep(2)
    print(50 * "-")
    print( "Колір телефону:",link.get_attribute("textContent"))
except NoSuchElementException as e:
    print(f"--This element was not found--: {e}")
except Exception as e:
    print(f"--- The information was not found --- :{e}")
finally:
    pass
###########################  Полное название товара информация о товаре ###########################
try:
    # Locate the  element with a specific ID using XPath
    WebDriverWait(driver, 3).until(EC.presence_of_all_elements_located(
        (By.XPATH, '//*[@id="br-pr-1"]/h1')))
    element = driver.find_element(By.XPATH, '//*[@id="br-pr-1"]/h1')
    name= element.text
    print(f"Назва вашого продукту: {name}")
except NoSuchElementException as e:
    print(f"-This element was not found-: {e}")
except Exception as e:
    print(f"--- The information was not found --- :{e}")
finally:
    pass
######################## Имя продукта ####################
try:
    # Locate the  element with a specific ID using XPath
    element = driver.find_element(By.XPATH, '//*[@id="br-pr-1"]/h1')
    name = element.text
    print(f"Назва продукту: {name}")
except NoSuchElementException as e:
    print(f"-This element was not found-: {e}")
except Exception as e:
    print(f"--- The information was not found --- :{e}")
finally:
    pass
################ Виробник #######################
try:
    xpath = '//*[@id="br-pr-7"]/div/div/div[11]/div/div[1]/span[2]'
    manufacturer = driver.find_element(By.XPATH,xpath)
    res = manufacturer.get_attribute("textContent")
    print("Виробник :", res.strip())
except NoSuchElementException as e:
    print(f"-This element was not found-: {e}")
except Exception as e:
    print(f"--- The information was not found --- :{e}")
finally:
    pass
############# Код ######################################
try:
    element = driver.find_element(By.XPATH,"/html/body/header/div[3]/div/div[2]/div/div/span[2]")
    kod = element.get_attribute("textContent")
    print("Код товару:", kod)
except NoSuchElementException as e:
    print(f"-This element was not found-: {e}")
except Exception as e:
    print(f"--- The information was not found --- :{e}")
finally:
    pass
####################### Память ###########
try:
    xpath1 = '//*[@class="br-pr-chr"]/div[4]/div/div/span[1]'
    xpath2 ='//*[@class="br-pr-chr"]/div[4]/div/div/span[2]'
    link1 = driver.find_element(By.XPATH,xpath1)
    link2 = driver.find_element(By.XPATH,xpath2)

    k = link1.get_attribute("textContent")
    v = link2.get_attribute("textContent")
    print(k,":",v.strip())
except NoSuchElementException as e:
    print(f"-This element was not found-: {e}")
except Exception as e:
    print(f"--- The information was not found --- :{e}")
finally:
    pass
#################### OS #####################
try:
    xpath1 = '//*[@class="br-pr-chr"]/div[6]/div/div/span[1]'
    xpath2 ='//*[@class="br-pr-chr"]/div[6]/div/div/span[2]'
    link1 = driver.find_element(By.XPATH, xpath1)
    link2 = driver.find_element(By.XPATH, xpath2)
    k = link1.get_attribute("textContent")
    v = link2.get_attribute("textContent")
    m = v.split()
    z = " ".join(m)
    print(k, ":", z)
except NoSuchElementException as e:
    print(f"-This element was not found-: {e}")
except Exception as e:
    print(f"--- The information was not found --- :{e}")
finally:
    pass

####################### Display size ################
try:
    xpath='//*[@id="br-pr-7"]/div/div/div[2]/div/div[2]/span[2]'
    disp = driver.find_element(By.XPATH,xpath)
    screen = disp.get_attribute("textContent")
    print(f"Диагональ экрана': {screen.strip()}")
except NoSuchElementException as e:
    print(f"-This element was not found-: {e}")
except Exception as e:
    print(f"--- The information was not found --- :{e}")
finally:
    pass

################### Ціна ################
try:
    xpath ='//*[@class="br-pr-np"]/div/span'
    slovo = driver.find_element(By.XPATH, xpath)
    price = slovo.get_attribute("textContent")
    print( "Ціна:",price.strip(), "грн.")
except NoSuchElementException as e:
    print(f"-This element was not found-: {e}")
except Exception as e:
    print(f"--- The information was not found --- :{e}")
finally:
    pass
################### Акційна ціна ################
try:
    xpath ='//div[@class ="title-action-promo-price"]'
    aprice = driver.find_element(By.XPATH,xpath)
    print("Акційна ціна:", end = "")
    if aprice.text == "":
        print(" - ")
    else:
        print(aprice.get_attribute("textContent"))
except NoSuchElementException as e:
        print(f"-This element was not found-: {e}")
except Exception as e:
    print(f"--- The information was not found --- :{e}")
finally:
    pass
########## Роздільна здатність экрану ###########################
try:
    xpath='//a[@title ="Роздільна здатність екрану 1179 х 2556"]'
    link = driver.find_element(By.XPATH,xpath)
    print( "Роздільна здатність экрану : ",link.get_attribute("textContent"))
except NoSuchElementException as e:
    print(f"-This element was not found-: {e}")
except Exception as e:
    print(f"--- The information was not found --- :{e}")
finally:
    pass
####################### Кількість SIM-карт #############
try:
    xpath1 = '//*[@class="br-pr-chr"]/div[1]/div[1]/div[2]/span[1]'
    xpath2 ='//*[@class="br-pr-chr"]/div[1]/div[1]/div[2]/span[2]'
    link1 = driver.find_element(By.XPATH,xpath1)
    link2 = driver.find_element(By.XPATH,xpath2)
    k = link1.get_attribute("textContent")
    v = link2.get_attribute("textContent")
    m = v.split()
    z = " ".join(m)
    print(k, ":", z)
except NoSuchElementException as e:
    print(f"-This element was not found-: {e}")
except Exception as e:
    print(f"--- The information was not found --- :{e}")
finally:
    pass
################## Формат SIM-карти ##############################
try:
    xpath1 = '//*[@class="br-pr-chr"]/div[1]/div[1]/div[3]/span[1]'
    xpath2 ='//*[@class="br-pr-chr"]/div[1]/div[1]/div[3]/span[2]'
    link1 = driver.find_element(By.XPATH, xpath1)
    link2 = driver.find_element(By.XPATH, xpath2)
    k = link1.get_attribute("textContent")
    v = link2.get_attribute("textContent")
    m = v.split()
    z = " ".join(m)
    print(k, ":", z)
except NoSuchElementException as e:
    print(f"-This element was not found-: {e}")
except Exception as e:
    print(f"--- The information was not found --- :{e}")
finally:
    pass
############### Фото  телефону #####################
try:
    images = driver.find_elements(By.XPATH, "//*[@class='slick-track']//img")
    photo_links = [img.get_attribute("src") for img in images]
    if photo_links == []:
        raise NoSuchElementException
    else:
        print("****************************** Фото телефону ********************************")
        for src in photo_links:
            print(src)
        print(70*"-")
except NoSuchElementException as e:
    print(f"--This element was not found--: {e}")
except Exception as e:
    print(f"--- The information was not found --- :{e}")
finally:
    pass
###################### Printing all characteristics in dictionary ####################
try:
    link1 = driver.find_elements(By.XPATH,'//*[@class="br-pr-tblock br-pr-chr-wrap"]//span[1]')
    link2 = driver.find_elements(By.XPATH,'//*[@class="br-pr-tblock br-pr-chr-wrap"]//span[2]')
    size1 = len(link1);size2 = len(link2); k=[]; v=[]; size = 0
    print(70*"-")
    if size1 >= size2 :
        size = size2
    else: size = size1
    for i in range(size):
        o = link1[i].get_attribute("textContent").strip()
        p = link2[i].get_attribute("textContent").strip()
        m = p.split()
        z = " ".join(m)
        k.append(o)
        v.append(z)
    zippo = zip(k,v)
    phone_characteristics= dict(zippo)
    if phone_characteristics != {}:
        print(phone_characteristics)
    else:
        raise NoSuchElementException
except NoSuchElementException as e:
    print(f"-This element was not found-: {e}")
except Exception as e:
    print(f"--- The information was not found --- :{e}")
finally:
    pass
driver.quit()
