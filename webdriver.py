from selenium import webdriver
from bs4 import BeautifulSoup
import time, re


def main():
    driver = ''
    try:
        driver = webdriver.Firefox()
    except:
        print('No hay driver de firefox en el directorio')
    if not driver:
        try:
            driver = webdriver.Chrome()
        except:
            print('No hay driver de chrome en el directorio')
    try:
        f = open('.login', 'r')
        usuario = f.readline().replace('\n', '')
        password = f.readline().replace('\n', '')
        
    except:
        print('No hay ningun archivo .login con usuario y contraseña')

    login(usuario, password, driver)


def ObtenerDatosGrupoGoogleCSV(html):
    soup = BeautifulSoup(html, 'html.parser')
    posicion = soup.select('h1.KdPHLc')[0].string
    
    members = soup.select("div[role='gridcell'] a[href^='mailto:']")
    s = "First Name,Last Name,Email,Position\n"
    for m in members:
        if '@alu' not in m.string and '@fp' not in m.string:
            continue

        nombre = re.sub('@.*', '', m.string)
        s += nombre + ",," + m.string + ',' + posicion + '\n'
    print(s)
    if s != "First Name,Last Name,Email,Position\n":
        nombreFichero = str(posicion).replace(' ', '').replace('/','-') + '.csv'
        fs = open(nombreFichero, 'w')
        fs.write(s)
    pass

def login(usuario, password, driver):
    driver.get('https://groups.google.com/u/1/all-groups')
    time.sleep(1)
    dEmail = driver.find_element_by_css_selector('[type="email"]')
    if dEmail:
        dEmail.clear()
        dEmail.send_keys(usuario)

        driver.find_element_by_css_selector('button.VfPpkd-LgbsSe').click()

    time.sleep(1)
    dPass = driver.find_element_by_css_selector('[type="password"]')
    if dPass:
        dPass.clear()
        dPass.send_keys(password)
        driver.find_element_by_css_selector('button.VfPpkd-LgbsSe').click()

    time.sleep(4)

    hipervinculos = driver.find_elements_by_css_selector('a.eRnJIb')
    links = []

    for a in hipervinculos:
        links.append(a.get_attribute('href'))

    for link in links:
        driver.get(link+'/members')
        html = driver.page_source
        ObtenerDatosGrupoGoogleCSV(html)


    pass

if __name__ == "__main__":
    main()
