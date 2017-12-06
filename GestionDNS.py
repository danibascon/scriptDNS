#!/usr/bin/python
# -+- coding: utf-8 .*.

import os
import commands


print "Bienvenidos al script en python sobre Gestion de DNS"
os.system("sleep 2s")
os.system("clear")

print "¿Que quieres hacer?"
print ""
print "     -a: añadir un nuevo nombre"
print "     -b: eliminar un nombre"
print ""
var= raw_input()

lista1=["a","b"]
lista2=["dir","alias"]
os.system("clear")

while var not in lista1:
    print "Error"
    print "Las opciones disponibles son -a y -b "
    print "     -a: añadir un nuevo nombre"
    print "     -b: eliminar un nombre"
    var=raw_input("¿Que opcion quieres hacer?  ")
    os.system("clear")



if var in lista1:
    if var == "a":
        print "Vamos a añadir un nuevo nombre"
        print "¿Que quieres hacer?"
        print ""
        print "     -dir: crear un registro tipo A"
        print "     -alias: crear un registro tipo CNAME"
        print ""
        var= raw_input()
        os.system("clear")
        while var not in lista2:
            print "Error"
            print "Las opciones disponibles son -dir y -alias "
            print "     -dir: crear un registro tipo A"
            print "     -alias: crear un registro tipo CNAME"
            var=raw_input("¿Que opcion quieres hacer?  ")
            os.system("clear")

        nombre=raw_input('Nombre de la maquina: ')
        f=open("db.mickey.txt","a")
        g=open("db.inverso","a")

        if var == "alias":            
            print "Vamos a crear un registro tipo CNAME"
            alias=raw_input('Dime el alias: ')
            f.writelines(nombre+"\t"+"IN"+"\t"+"CNAME"+"\t"+alias+"\n")

        else:
            print "Vamos a crear un registro tipo A"
            ip=raw_input('Dime la ip: ')
            while ip[:7] != '172.22.' and ip[:7] != '10.0.0.':
                ip=raw_input("dime una ip valida: ")

            f.writelines(nombre+"\t"+"IN"+"\t"+"A"+"\t"+ip+"\n")
            if ip[:7] == '172.22.':
                ip= ip[7:].split(".")[1]+"."+ip[7:].split(".")[0]
            else:
                ip=ip[7:]

            g.writelines(ip+"\t"+"IN"+"\t"+"PTR"+"\t"+nombre+".bascon.gonzalonazareno.org."+"\n")
            g.close

        f.close

    else:
        print "¿Que quieres hacer?"
        print ""
        print "     -dir: eliminar un registro tipo A"
        print "     -alias: eliminar un registro tipo CNAME"
        print ""
        var= raw_input()
        os.system("clear")
        while var not in lista2:
            print "Error"
            print "Las opciones disponibles son -dir y -alias "
            print "     -dir: eliminar un registro tipo A"
            print "     -alias: eliminar un registro tipo CNAME"
            var=raw_input("¿Que opcion quieres hacer?  ")
            os.system("clear")


        if var == "alias":            
            print "Vamos a eliminar un registro tipo CNAME"
            alias=raw_input('Dime el alias: ')
            commands.getoutput('sed -i /'+alias+'/d db.mickey.txt')

        else:
            print "Vamos a eliminar un registro tipo A"
            ip=raw_input('ip de la maquina que deseas eliminar: ')
            commands.getoutput('sed -i /'+ip+'/d db.mickey.txt')
            if ip[:7] == '172.22.':
                ip= ip[7:].split(".")[1]+"."+ip[7:].split(".")[0]
            else:
                ip=ip[7:]
            commands.getoutput('sed -i /'+ip+'/d db.inverso')
            
commands.getoutput('service bind9 restart')
