import  configparser
configuracion = configparser.ConfigParser()

configuracion['Generar'] = {'chrome' : 'C:\\Users\\Luis\\Desktop\\Python_Selenium_Nicolas_Alvarez\\Drivers\\chromedriver.exe'}
configuracion['Paginas'] = {'page' : 'https://www.google.com'}

with open('configuracion.ini', 'w') as archivoconfig:
    configuracion.write(archivoconfig)
