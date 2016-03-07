#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lxml import etree

arbol = etree.parse("via-publica.xml")
lista = arbol.getroot()

lista_incidencias = lista.xpath('////tipoincidencia')
incidencias=[]
for i in lista_incidencias:
	if not i.find("title") in incidencias:
		incidencias.append(i)
for x in incidencias:
	print x.tag
