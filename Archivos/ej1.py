'''1. Listar todos los modos de apertura de un archivo y extraer conclusiones
de cada uno'''



try: 
    file = open("..//file.txt")
    print("Archivo abierto de forma: '..//file.txt'")
   

    file = open("Archivos//file.txt","r")
    print("Archivo abierto de forma: 'D:\Documents\Work\dhs\Archivos/file.txt','r'")
    

    file = open("file.txt",mode = "r", encoding = "utf-8")
    print("Archivo abierto de forma: 'file.txt',mode = 'r', encoding = 'utf-8'")
    file.close()
    
except:
    "No se pudo abrir el archivo"
