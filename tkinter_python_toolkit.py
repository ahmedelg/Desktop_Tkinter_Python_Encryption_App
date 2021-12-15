# ########################
# # TKINTER DESKTOP APPs #
# ########################
# from tkinter import messagebox
# import tkinter as tk
# # print(dir(tk))
# # print(tkinter)
# # main_window=Tk()
# # app_name=Tk()
# # zagazig_computer_science_encrypts=Tk()
# # zcse=tk.Tk()
# # Main Widget
# # top level widget
# # top level Frame
# zcse = tk.Tk()
# # zcse.title = "Zagazing's Computer Science"
# zcse.title = "Computer Science"
# # print(dir(zcse))
# # print(dir(zcse))
# # Containment Tree شجرة الاحتواء
# # print('children' in dir(zcse))
# # print('master' in dir(zcse))
# # print(zcse.master) # None
# # print('_tclCommands' in dir(zcse))
# # create `FRAME`
# # define the `MASTER`/`PARENT`
# # F = Frame(zcse,relief='sunken',border=5,padx=10,pady=10)
# # F = Frame(zcse,relief='raised',border=5,padx=10,pady=10)
# F = tk.Frame(zcse, relief='groove', border=3, padx=5, pady=5)
# # F = Frame(zcse,relief='ridge',border=5,padx=10,pady=10)
# # F = Frame(zcse,relief='flat',border=5,padx=10,pady=10)
# # F1 = Frame(zcse)
# # print(F.master) # .
# # print(F.master)
# # print(F.master)  # .
# # print(zcse.children)
# # {'!frame': <tkinter.Frame object .!frame>}
# # {'!frame': <tkinter.Frame object .!frame>, '!frame2': <tkinter.Frame object .!frame2>}
# # display FRAME in the window
# # F.pack()
# # F.pack(fill='x')
# # F.pack(fill='y')
# F.pack(fill='both')
# # F.pack(side='left')
# # F.pack(side='right')
# # F.pack(side='center') # Error "center": must be top, bottom, left, or right
# #####################################
# #           address of app          #
# #####################################
# F_encr = tk.Frame(F, relief='sunken', border=2, pady=5)
# path_file_label = tk.Label(F_encr, text=' !ما اسمك', foreground='blue')
# path_file_label.pack(side='right')
# path_file_entery = tk.Entry(F_encr)
# def evKey(event):
#     messagebox.showinfo('Copy acction?', 'Entry has been copied.')
#     clear_enc_input()
# path_file_entery.bind("<Control-x>", evKey)
# path_file_entery.pack(side='right')
# lHistory = tk.Label(F_encr, foreground='steelblue')
# lHistory.pack(side='right', fill='x')
# pass_file_label = tk.Label(F_encr, text=' !ما الرقم السري', foreground='blue')
# pass_file_label.pack(side='right')
# pass_file_entery = tk.Entry(F_encr)
# pass_file_entery.pack(side='right')
# F_encr.pack(fill='both', side='top')
# #####################################
# # change `PROPs` at once
# # app_name_lbl.configure(text='Zagazig Packages')
# # app_name_lbl['text'] = 'Zagazig Packages'
# # change title of window
# # F.master.title = "Zagazing's Computer Science"
# # path_file_input = path_file_label(F)
# # path_file_input.pack(pady=5)
# # path_file_input = Text(F)
# # path_file_input.pack(pady=5)
# #####################################
# #           app-buttons             #
# #####################################
# F_app_btns = tk.Frame(F, relief='sunken', border=1, pady=5)
# zcse_encr_btn = tk.Button(F_app_btns, relief='raised', text='ماذا تنتظر!')
# zcse_encr_btn.pack(padx=5, side='right')
# def clear_enc_input():
#     lHistory['text'] = path_file_entery.get()
#     path_file_entery.delete(0, tk.END)
#     # From index: 0 -> END
# zcse_encr_clear = tk.Button(
#     F_app_btns, relief='raised', text='تفريغ', command=clear_enc_input)
# def warn_quit_app():
#     # Yes/No Box
#     # Warn Box
#     # Ok/Cancel
#     quite_sure = messagebox.askyesno('تأكيد خروج', 'هل حقا تريد ان تخرج؟')
#     print(quite_sure)
#     if quite_sure == True:
#         print('quit')
#         zcse.quit
# zcse_encr_clear.pack(padx=5, side='right')
# zcse_quit_btn = tk.Button(F_app_btns, relief='raised',
#                           text='خروج', command=warn_quit_app)
# zcse_quit_btn.pack(padx=5, side='right')
# F_app_btns.pack(fill='both', side='top')
# #####################################
# # file_path_input=Message(F,text='message here....')
# # file_path_input.pack(side='righ')
# # run `event-loop`
# zcse.mainloop()
#############################################
import tkinter as tk
from tkinter import Label, PhotoImage, font
from typing import Collection


root_bg=''

bg = '#001f3f'
fg='#ffffff'
fg1='red'
quit_bg='red'
quit_fg='#ffffff'
root_font=14



app_name='Encryption Algorithms'
class EncryptionApp:
    def __init__(self, parent):
        # main window
        self.mainwindow = tk.Frame(parent, bg=bg)
        # LOGO
        self.logo_img=PhotoImage(file='enc.gif')
        img_lab=Label(self.mainwindow, image=self.logo_img,pady=10)
        # img_lab.pack()
        img_lab.grid()
	
        # elements
        # self.eHellow = tk.Entry(self.mainwindow)
        # self.eHellow.insert(0, 'hello world')
        self.e_path_file_title=tk.Label(self.mainwindow, text="What is the path of the file:", fg=fg, bg=bg, font='android 14 bold')
        # self.e_path_file_title.pack(fill='x',padx=10,pady=10)
        self.e_path_file_title.grid(column=0,row=1)
        
        # self.eHellow.pack(fill='x', padx=5, pady=5)
        # self.eHellow.bind("<Control-x>", self.evHotKey)

        # buttons
        fButtons = tk.Frame(self.mainwindow,bg=bg)
        self.bClear = tk.Button(fButtons, text='clear',
                                width=12, height=1, command=self.evClear)
        self.bQuit = tk.Button(fButtons, text='خروج',
                               width=25, height=1, bg=quit_bg,fg=quit_fg,font='none 12 bold',command=self.mainwindow.quit)
        # self.bClear.pack(padx=1, pady=1)
        self.bClear.grid(column=0,row=2)
        # self.bQuit.pack(padx=1, pady=1)
        self.bQuit.grid(column=0,row=3)
        # fButtons.pack(fill='x', pady=4)
        fButtons.grid(column=0,row=2)

				# handle settings of mainwindow
        self.mainwindow.pack(fill='x')
        self.mainwindow.master.title(app_name)

    def evClear(self):
        self.eHellow.delete(0, tk.END)

    def evHotKey(self, event):
        self.evClear()


# `empty-application`
root = tk.Tk()


root.config(bg=bg)

root.geometry('350x400')
root.iconbitmap('enc.ico')

# application menu
app_menu=tk.Menu(root)
# file menu
file_menu=tk.Menu(app_menu)
file_menu.add_command(label='New')
file_menu.add_command(label='save')
file_menu.add_command(label='Save All')
file_menu.add_command(label='Exit')
app_menu.add_cascade(label="File", menu=file_menu)
# settings Menu
settings_menu=tk.Menu(app_menu)
settings_menu.add_command(label='Help')
settings_menu.add_command(label='About')
# view menu
view_menu=tk.Menu(app_menu)
view_menu.add_command(label='Full Screen')
themes_menu=tk.Menu(view_menu)
themes_menu.add_command(label='Dark mode')
themes_menu.add_command(label='Light mode')
view_menu.add_cascade(label='Theme',menu=themes_menu)
app_menu.add_cascade(label='View', menu=view_menu)
app_menu.add_cascade(label='Settings?', menu=settings_menu)
root.config(menu=app_menu)





app = EncryptionApp(root)
root.mainloop()
##########################################################
# How to make the `width` & `height` of mainwindow fixed!

##########################################################