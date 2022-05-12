def resizer(e,bg):
    global bg1, resize_bg, new_bg
    #Se abre la imagen a modificar
    bg1= bg
    #Se hace el cambio de tamaño de la imagen
    resize_bg=bg1.resize((e.width, e.height), Image.ANTIALIAS)
    #Se redefine la imagen del fondo
    new_bg = ImageTk.PhotoImage(resize_bg)
    #Se añade un canvas que se usara para establecer el nuevo fondo
    my_canvas.create_image(0,0, image=new_bg, anchor="nw")



root.bind('<Configure>',resizer())