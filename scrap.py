import os
import requests
from lxml import html
from bs4 import BeautifulSoup

def scrapingImages(url):
    print("\n\tWEB SCRAPING")
    print("\nObteniendo imagenes de la url: "+ url)
    try:
        response = requests.get('http://'+url)  
        parsed_body = html.fromstring(response.text)
        # expresion regular para obtener imagenes
        images = parsed_body.xpath('//img/@src')
        print ('Imagenes %s encontradas' % len(images))
        #create directory for save images
        os.system("mkdir images")
        for image in images:
            if image.startswith("http") == False:
                download = url + image
            else:
                download = image
            print(download)
            # download images in images directory
            r = requests.get(download)
            f = open('images/%s' % download.split('/')[-1], 'wb')
            f.write(r.content)
            f.close()
        print("\nImagenes descargadas correctamente")
    except Exception as e:
            print(e)
            print ("Error conexion con " + url)
            pass
