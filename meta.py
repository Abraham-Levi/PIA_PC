import argparse
import os
import requests
from PIL.ExifTags import TAGS, GPSTAGS
from PIL import Image
from lxml import html
from bs4 import BeautifulSoup

def decode_gps_info(exif):
    gpsinfo = {}
    if 'GPSInfo' in exif:
        #Parse geo references.
        Nsec = exif['GPSInfo'][2][2] 
        Nmin = exif['GPSInfo'][2][1]
        Ndeg = exif['GPSInfo'][2][0]
        Wsec = exif['GPSInfo'][4][2]
        Wmin = exif['GPSInfo'][4][1]
        Wdeg = exif['GPSInfo'][4][0]
        if exif['GPSInfo'][1] == 'N':
            Nmult = 1
        else:
            Nmult = -1
        if exif['GPSInfo'][3] == 'E':
            Wmult = 1
        else:
            Wmult = -1
        Lat = Nmult * (Ndeg + (Nmin + Nsec/60.0)/60.0)
        Lng = Wmult * (Wdeg + (Wmin + Wsec/60.0)/60.0)
        exif['GPSInfo'] = {"Lat" : Lat, "Lng" : Lng}

def get_exif_metadata(image_path):
    ret = {}
    image = Image.open(image_path)
    if hasattr(image, '_getexif'):
        exifinfo = image._getexif()
        if exifinfo is not None:
            for tag, value in exifinfo.items():
                decoded = TAGS.get(tag, tag)
                ret[decoded] = value
    decode_gps_info(ret)
    print("\nMetadata obtenida exitosamente")
    return ret

def printMeta():
    print("\n\tOBTENCION DE METADATA")
    print("\nInspeccionando la carpeta con imagenes de web scraping")
    ruta = "C:.\images"
    os.chdir(ruta)
    for root, dirs, files in os.walk(".", topdown=False):
        for name in files:
            print(os.path.join(root, name))
            nombre = name+".txt"
            archivo = open(nombre, 'w')
            try:
                exifData = {}
                exif = get_exif_metadata(name)
                for metadata in exif:
                    archivo.write("Metadata: %s - Value: %s " %(metadata, exif[metadata]))
                    archivo.write("\n")
                    print ("\n")
            except:
                import sys, traceback
                traceback.print_exc(file=sys.stdout)
                archivo.close()
