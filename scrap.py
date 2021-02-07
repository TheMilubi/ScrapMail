from bs4 import BeautifulSoup
import sys

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
    members = soup.select("div[role='gridcell'] a[href^='mailto:']")
    for m in members:
        print(',,'+m.string+',')
    pass

if __name__ == "__main__":
    main()