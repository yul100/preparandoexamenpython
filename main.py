bandas=[]  # lista



#construyendo la interfaz

print("****Altavoz  es tu VOZ****")
print("**************************")

option= 100
while(option != 5):

    print("1.registrar banda")
    print("2.buscar informacion de una banda")
    print("3.agenda del evento ")
    print("4.modificar una banda ")
    print("5.salir ")


    option=int(input("dijita una opcion:  "))



    if option==1:
        banda={}   #objeto
        #creando bandas de diccionario
        banda["id"]=int(input("dijita el id  "))
        banda["nombre"]=input("nombre de la banda  ")
        banda["genero"]=input("el genero de la banda  ")
        banda["clasificacion"]=input("cual es la calificacion ")
        banda["timepo"]=int(input("tiempo:   "))
        banda["costo"]=int(input("costo: $ "))
        
        #agregando un diccionario a una lista 
        bandas.append(banda)

    elif option==2:
        
        bandaBuscada=input("digita  el nombre de la banda que estas buscando")

        for bandAuxiliar in bandas:
            if bandAuxiliar["nombre"]==bandaBuscada:
                #como lo encontre muestro los datos de bandAuxiliar
                print(f"id: {bandAuxiliar["id"]}----nombre: {bandAuxiliar["nombre"]}")
            else:
                print("parce siga buscando....")


    elif option==3:

        print(bandas)
        
    elif option==4:
        pass
    elif option==5:
        pass
    else:
        pass







