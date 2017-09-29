#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'JaviBautista'

from bs4 import BeautifulSoup
import requests

URL_BASE = "http://espinillo.org/foros/foroppp.php?foro=6&pagina=1"
MAX_PAGES = 3
counter = 0

for i in range(1, MAX_PAGES):

    # Construyo la URL
    if i > 1:
        url = "http://espinillo.org/foros/foroppp.php?foro=6&pagina=%d/" % (i)
    else:
        url = URL_BASE

    # Realizamos la petición a la web
    req = requests.get(url)
    # Comprobamos que la petición nos devuelve un Status Code = 200
    statusCode = req.status_code
    if statusCode == 200:

        # Pasamos el contenido HTML de la web a un objeto BeautifulSoup()
        html = BeautifulSoup(req.text, "html.parser")

        # Obtenemos todos los divs donde estan las entradas
        entradas = html.find_all('td')
        # Recorremos todas las entradas para extraer el título, autor y fecha
        
        
        
        for entrada in entradas:
            counter += 1
            #print(entrada.prettify())
            titulo = entrada.find('span', {'class': 'TituloTema'})
            fecha = entrada.find('span',{'class': 'fecha'})
            texto = entrada.find('span',{'class': 'textotema'})
            #mail= entrada.find('a')['href']

            if ( fecha != None ):
                print(fecha.getText())
            if ( titulo != None ):
                print(titulo.getText())
            if ( texto != None ):
                print(texto.getText())


            # Imprimo el Título, Autor y Fecha de las entradas
           # print "%d - %s  |  %s  |  %s" %(counter, titulo, autor, fecha)
    else:
        # Si ya no existe la página y me da un 400
        break
