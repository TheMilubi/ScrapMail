from bs4 import BeautifulSoup
import sys
import re

def main():
    docs = sys.argv[1:]
    for doc in docs:
        try:
            fileContent = open(doc, 'r').read()
            ObtenerDatosGrupoGoogleCSV(fileContent)
        except:
            print('Ruta a ficheros no válida')
    pass


def ObtenerDatosGrupoGoogleCSV(html):
    soup = BeautifulSoup(html,'html.parser')
    posicion = soup.select('h1.KdPHLc')[0].string
    nombreFichero = str(posicion).replace(' ', '') + '.csv'
    fs = open(nombreFichero, 'w')
    members = soup.select("div[role='gridcell'] a[href^='mailto:']")
    s = ""
    for m in members:
        if 'alu' not in m.string and 'fp' not in m.string: 
            continue
        
        nombre = re.sub('@.*','',m.string)
        s += nombre + ',,'+m.string+','+posicion+'\n'
    print(s)
    fs.write(s)
    pass

if __name__ == "__main__":
    main()