#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lxml import etree

arbol = etree.parse("via-publica.xml")
lista = arbol.getroot()

lista_incidencia = lista.xpath("////tipoincidencia")
tipos_incidencia=[]
for incidencia in lista_incidencia:
	if not incidencia.find("id").text in tipos_incidencia:
		tipos_incidencia.append(incidencia.find("id").text)
	
print tipos_incidencia
