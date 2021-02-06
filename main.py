from tkinter import *
import requests

#e0eda8193a6a3795b8e4fe4b8594262f
#api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}

def mostras_repuesta(clima):
	try:
		nombre_ciudad=clima['name']
		desc=clima['weather'][0]['description']
		temp=clima['main']['temp']

		ciudad['text']=nombre_ciudad
		description['text']=desc
		temperatura['text']=str(int(temp))+'ºC'
	except:
		ciudad['text']='No se ha encontrado resultados'

def clima(ciudad):
	try:
		API_KEY='e0eda8193a6a3795b8e4fe4b8594262f'
		URL='https://api.openweathermap.org/data/2.5/weather'
		parametros={'APPID':API_KEY, 'q':ciudad, 'units':'metric', 'lang':'es'}
		response=requests.get(URL, params=parametros)
		clima=response.json()
		mostras_repuesta(clima)
	except KeyError:
		print('Error')

ventana=Tk()
ventana.title('App Clima')

ventana.iconbitmap('img/icono.ico')

ventana.geometry('450x550')
texto_ciudad=Entry(ventana, font=('Courier', 18, 'normal'), justify='center')
texto_ciudad.pack(padx=30, pady=30)
obtener_clima=Button(ventana, text='Obtener Clima', command=lambda:clima(texto_ciudad.get()))
obtener_clima.pack()
	
ciudad = Label(font=('Courier', 18, 'normal'))
ciudad.pack(padx=10, pady=10)

temperatura = Label(font=('Courier', 18, 'normal'))
temperatura.pack(padx=10, pady=10)

description = Label(font=('Courier', 18, 'normal'))
description.pack(padx=10, pady=10)
ventana.mainloop()