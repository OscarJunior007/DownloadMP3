import tkinter
from customtkinter  import *
from pytube import YouTube
from tkinter import messagebox
from PIL import Image

ventana = CTk()
ventana.title('Descargar MP3 YT')
ventana.geometry('800x400')
def descargar():
    url = link.get()
    if not url:
        messagebox.showinfo(title='Informacion',message='Debes pegar un link')
    else:
        yt = YouTube(url)
        audio = yt.streams.filter(only_audio=True).first()
        nombre_cancion = yt.title
        try:
            if salsa.get() == 'on':
                audio.download(output_path='C:\\Musica\\Salsa', filename=f'{nombre_cancion}.mp3')
                messagebox.showinfo(title='infomacion',message=f'{nombre_cancion}, se descargo exitosamente!, en la carpeta "Salsa" ')
            elif vallenato.get() == 'on':
                audio.download(output_path='C:\\Musica\\Vallenato',filename=f'{nombre_cancion}.mp3')
                messagebox.showinfo(title='infomacion',message=f'{nombre_cancion}, se descargo exitosamente!, en la carpeta "Vallenato" ')
            elif champeta.get() == 'on':
                audio.download(output_path='C:\\Musica\\Champeta', filename=f'{nombre_cancion}.mp3')
                messagebox.showinfo(title='infomacion', message=f'{nombre_cancion}, se descargo exitosamente!, en la carpeta "Champeta" ')
            elif reggeton.get() == 'on':
                audio.download(output_path='C:\\Musica\\reggeton', filename=f'{nombre_cancion}.mp3')
                messagebox.showinfo(title='infomacion',message=f'{nombre_cancion}, se descargo exitosamente!, en la carpeta "Reggeton" ')
            else:
                audio.download(output_path='C:\\Musica\\Musica sin carpeta', filename=f'{nombre_cancion}.mp3')
                messagebox.showinfo(title='infomacion', message=f'{nombre_cancion}, se descargo exitosamente!')
        except:
            messagebox.showinfo(title='infomacion',message=f'{nombre_cancion}, no se pudo descargar, intentalo nuevamenta :c')

is_light = True
def mode():
    global is_light
    #print(is_light)
    if is_light:
        boton_descargar.configure(text="Descargar",fg_color= "#000000",text_color='#FFFFFF')
        boton_mode.configure(text="Mode Dark",fg_color= "#000000",text_color='#FFFFFF')
        set_appearance_mode('light')
    else:
        boton_descargar.configure(text="Descargar",text_color='#000000',fg_color= "#FFFFFF")
        boton_mode.configure(text="Mode Light",text_color='#000000',fg_color= "#FFFFFF")
        set_appearance_mode('dark')
    is_light = not is_light

def selected_check():
   if vallenato.get() =='on':
        boton_descargar.configure(text="Descargar Vallenato")
        salsa_check.deselect()
        champeta_check.deselect()
        reggeton_check.deselect()
   if salsa.get() == 'on':
       boton_descargar.configure(text="Descargar Salsa")
       champeta_check.deselect()
       vallenato_check.deselect()
       reggeton_check.deselect()
   if champeta.get() == 'on':
       boton_descargar.configure(text="Descargar Champeta")
       vallenato_check.deselect()
       salsa_check.deselect()
       reggeton_check.deselect()
   if reggeton.get() == 'on':
       boton_descargar.configure(text="Descargar Reggeton")
       vallenato_check.deselect()
       salsa_check.deselect()
       champeta_check.deselect()

vallenato = tkinter.StringVar(value='off')
vallenato_check = CTkCheckBox(master=ventana,text='Crear carpeta Vallenato',variable=vallenato,onvalue='on',offvalue='off',command=selected_check)
vallenato_check.place(relx='0.11',rely='0.17',anchor='center')

salsa = tkinter.StringVar(value='off')
salsa_check = CTkCheckBox(master=ventana,text='Crear carpeta Salsa',variable=salsa,onvalue='on',offvalue='off',command=selected_check)
salsa_check.place(relx='0.10',rely='0.26',anchor='center')

champeta = tkinter.StringVar(value='off')
champeta_check = CTkCheckBox(master=ventana,text='Crear carpeta Champeta',variable=champeta,onvalue='on',offvalue='off',command=selected_check)
champeta_check.place(relx='0.12',rely='0.35',anchor='center')

reggeton = tkinter.StringVar(value='off')
reggeton_check = CTkCheckBox(master=ventana,text='Crear carpeta reggeton',variable=reggeton,onvalue='on',offvalue='off',command=selected_check)
reggeton_check.place(relx='0.12',rely='0.45',anchor='center')

boton_descargar = CTkButton(master=ventana,text='Descargar',text_color='#000000',font=('Lucida Console',20), fg_color= "#FFFFFF",command=descargar,corner_radius=10,hover=True,hover_color="#FF0000",border_color='#FFFFFF')
boton_descargar.place(relx='0.5',rely='0.6',anchor='center')

boton_mode:CTkButton = CTkButton(master=ventana,text='Chose Mode', fg_color= "#3b8cc6",command=mode,corner_radius=10,hover=True,hover_color="#FF0000",border_color='#FFFFFF')
boton_mode.place(relx='0.9',rely='0.9',anchor='center')

message = CTkLabel(master=ventana, text='La descarga puede durar entre 10-20 seugndos')
message.place(relx='0.5',rely='0.7',anchor='center')

message2 = CTkLabel(master=ventana,font=('arial',15), text='Las canciones se guardaran "Disco local C:" en un carpeta llamada (musica) \n y se creara una carpeta extra dependiendo el genero elegido.')
message2.place(relx='0.5',rely='0.8',anchor='center')

message3 = CTkLabel(master=ventana, text='Desarollado por Oscar Mejia.',text_color='#FF0000',font=('Magneto',15))
message3.place(relx='0.8',rely='0.10',anchor='center')

message4 = CTkLabel(master=ventana, text='Elegir genero:',text_color='#FF0000',font=('arial',18))
message4.place(relx='0.12',rely='0.10',anchor='center')

mode = set_appearance_mode('Dark')

link =  CTkEntry(master=ventana,placeholder_text='Pega el link aqui')
link.place(relx='0.5',rely='0.5',anchor='center')

ventana.mainloop()