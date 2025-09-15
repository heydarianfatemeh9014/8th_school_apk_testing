# import the mudols
from tkinter import *
from PIL import Image , ImageTk
from subprocess import *
import pygame
from tkinter import messagebox
import tkinter as tk
from tkinter import PhotoImage
from  bidi.algorithm import get_display
import arabic_reshaper
import tkinter
from tkinter import *
from random import*
import PIL
from PIL import*

def shedatt():
    
    def sound_play():
        pygame.mixer.init()  # مقداردهی اولیه میکسر pygame
        pygame.mixer.music.load("bib.mp3")  # بارگذاری فایل صوتی
        pygame.mixer.music.play()
        
    root = Toplevel()
    root.geometry('800x800')
    root.resizable(False,False)
    root.iconbitmap("icon.ico") 
    root.title('window to knowledge')
    #backgroun setting

    image = Image.open('imagess\\wall7.jpg')
    image = image.resize((800,800))
    bg_image = ImageTk.PhotoImage(image)


    bg_lbl = Label(root, image=bg_image)
    bg_lbl.place(relheight=1,relwidth=1)



    def ent_get():
        sound_play()
        global tt,qq,ii,result2 , result,s,w
        qq = q_ent.get()
        ii = I_ent.get()
        tt = t_ent.get()
        try:
            w.place_forget()
            s.place_forget()
        except:
            pass
        if ii=='' and qq!='' and tt!='':
            result = (int(qq))/(int(tt))
            w=Label(master = root,text=(convert(f'جواب :{result}')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red')
            w.place(x=0,y=500)
            result2 = f'I = Q ÷ t => \nI = {qq} ÷ {tt} => \nI = {result}'
            s=Label(master = root,text= result2 ,font=('Segoe Print',20,'bold'),bg='white',fg='black')
            s.place(x=0,y=550)

        elif ii!='' and qq=='' and tt!='':
            result = (int(tt))*(int(ii))
            w=Label(master = root,text=(convert(f'جواب :{result}')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red')
            w.place(x=0,y=500)
            result2 = f'Q = I x t => \nQ = {ii} x {tt} => \nQ = {result}'
            s=Label(master = root,text= result2 ,font=('Segoe Print',20,'bold'),bg='white',fg='black')
            s.place(x=0,y=550)

        elif ii!='' and qq!='' and tt=='':
            result = (int(qq))/(int(ii))
            w=Label(master = root,text=(convert(f'جواب :{result}')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red')
            w.place(x=0,y=500)
            result2 = f't = Q ÷ I => \nt = {qq} ÷ {ii} => \nt = {result}'
            s=Label(master = root,text= result2 ,font=('Segoe Print',20,'bold'),bg='white',fg='black')
            s.place(x=0,y=550)

        else:
            messagebox.showerror(message='اطلاعات نادرست یا ناکافی است!!!')
        


            





    Label(master = root,text=(convert(' مقدار هر یک را وارد کنید و مقدار خواسته شده را خالی بگذارید')) ,font=('Segoe Print',20,'bold'),bg='white',fg='green').place(x=80,y=0)
    Label(master = root,text=(('I : ( Q ÷ t )')) ,font=('Segoe Print',20,'bold'),bg='white',fg='blue').place(x=100,y=400)


    I= Label(master = root,text=(convert('شدت جریان الکتریکی:')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red').place(x=0,y=80)
    I_ent = Entry(master=root,font=('Segoe Print',20,'bold'))
    I_ent.place(x=400,y=80)
    q = Label(master = root,text=(convert('بار الکتریکی:')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red').place(x=0,y=160)
    q_ent = Entry(master=root,font=('Segoe Print',20,'bold'))
    q_ent.place(x=400,y=160)

    t = Label(master = root,text=(convert('زمان:')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red').place(x=0,y=240)
    t_ent = Entry(master=root,font=('Segoe Print',20,'bold'))
    t_ent.place(x=400,y=240)


    sub_btn = Button(master = root,text=(convert('تایید')),font=('Segoe Print',20,'bold'),bg='green',fg='white',activebackground='white',activeforeground='green',command = ent_get).place(x=0,y=400)



    root.mainloop()
def ohmm():

    def sound_play():
        pygame.mixer.init()  # مقداردهی اولیه میکسر pygame
        pygame.mixer.music.load("bib.mp3")  # بارگذاری فایل صوتی
        pygame.mixer.music.play()
    #root setting
    root = Toplevel()
    root.geometry('800x800')
    root.resizable(False,False)
    root.iconbitmap("icon.ico") 
    root.title('window to knowledge')
    #backgroun setting

    image = Image.open('imagess\\wall7.jpg')
    image = image.resize((800,800))
    bg_image = ImageTk.PhotoImage(image)


    bg_lbl = Label(root, image=bg_image)
    bg_lbl.place(relheight=1,relwidth=1)



    def ent_get():
        sound_play()
        global vv,rr,ii , result,result2,s,w
        vv = (V_ent.get())
        rr = (R_ent.get())
        ii = (I_ent.get())
        try:
            w.place_forget()
            s.place_forget()
        except:
            pass
        if vv=='' and ii!='' and rr!='':
            result = int(ii)*int(rr)
            w=Label(master = root,text=(convert(f'اختلاف پتانسیل :{result}')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red')
            w.place(x=0,y=400)
            result2 = f'V = I x R => \nV = {int(ii)} x {int(rr)} => \nV = {result}'
            s=Label(master = root,text= result2 ,font=('Segoe Print',20,'bold'),bg='white',fg='black')
            s.place(x=0,y=450)

        elif rr=='' and ii!='' and vv!='':
            result = int(vv)/int(ii)
            w=Label(master = root,text=(convert(f'مقاومت رسانا :{result}')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red')
            w.place(x=0,y=400)
            result2 = f'R = V ÷ I => \nR = {int(vv)} ÷ {int(ii)} => \nR = {result}'
            s=Label(master = root,text= result2 ,font=('Segoe Print',20,'bold'),bg='white',fg='black')
            s.place(x=0,y=450)

        elif ii=='' and vv!='' and rr!='':
            result = int(vv)/int(rr)
            w=Label(master = root,text=(convert(f'شدت جریان :{result}')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red')
            w.place(x=0,y=400)
            result2 = f'I = V ÷ R => \nI = {int(vv)} ÷ {int(rr)} => \nI = {result}'
            s=Label(master = root,text= result2 ,font=('Segoe Print',20,'bold'),bg='white',fg='black')
            s.place(x=0,y=450)

        else:
            messagebox.showerror(message='اطلاعات کم یا نادرست است!!!')


        
        
        
        


            






    Label(master = root,text=(convert(' مقدار هر یک را وارد کنید و مقدار خواسته شده را خالی بگذارید')) ,font=('Segoe Print',20,'bold'),bg='white',fg='green').place(x=80,y=0)

    V = Label(master = root,text=(convert('اختلاف پتانسیل:')) ,font=('Segoe Print',20,'bold'),bg='white',fg='black').place(x=0,y=80)
    V_ent = Entry(master=root,font=('Segoe Print',20,'bold'))
    V_ent.place(x=400,y=80)

    R = Label(master = root,text=(convert('مقاومت الکتریکی:')) ,font=('Segoe Print',20,'bold'),bg='white',fg='black').place(x=0,y=160)
    R_ent = Entry(master=root,font=('Segoe Print',20,'bold'))
    R_ent.place(x=400,y=160)

    I = Label(master = root,text=(convert('شدت جریان:')) ,font=('Segoe Print',20,'bold'),bg='white',fg='black').place(x=0,y=240)
    I_ent = Entry(master=root,font=('Segoe Print',20,'bold'))
    I_ent.place(x=400,y=240)

    sub_btn = Button(master = root,text=(convert('تایید')),font=('Segoe Print',20,'bold'),bg='green',fg='white',activebackground='white',activeforeground='green',command = ent_get).place(x=0,y=300)
    Label(master = root,text=(convert('قانون اهم:\nدر دمای ثابت نسبت اختلاف پتانسیل به شدت جریان\n همواره مقدار ثابتی میباشد\n که به آن مقاومت الکتریکی میگوییم')) ,font=('Segoe Print',20,'bold'),bg='white',fg='blue').place(x=300,y=360)



    root.mainloop()
def mvv():
    def sound_play():
        pygame.mixer.init()  # مقداردهی اولیه میکسر pygame
        pygame.mixer.music.load("bib.mp3")  # بارگذاری فایل صوتی
        pygame.mixer.music.play()
        
    #root setting
    root = Toplevel()
    root.geometry('800x800')
    root.resizable(False,False)
    root.iconbitmap("icon.ico") 
    root.title('window to knowledge')
    #backgroun setting

    image = Image.open('imagess\\wall7.jpg')
    image = image.resize((800,800))
    bg_image = ImageTk.PhotoImage(image)


    bg_lbl = Label(root, image=bg_image)
    bg_lbl.place(relheight=1,relwidth=1)



    def ent_get():

        sound_play()
        global vv,rr,ii , result,result2,w,s
        pp = P_ent.get()
        ll = L_ent.get()
        aa = A_ent.get()
        rr = R_ent.get()
        try:
            w.place_forget()
            s.place_forget()
        except:
            pass
        
        if rr=='' and ll!='' and aa!='' and pp!='':
            result = ((float(pp))*(float(ll)))/(float(aa))
            w=Label(master = root,text=(convert(f'.جواب حاصل مقاومت رسانا:{result}')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red')
            w.place(x=0,y=500)
            result2 = f'R = ( ρ x L ) ÷ A => \nR = ( {float(pp)} x {float(ll)} ) ÷ {float(aa)} => \nR = {result}'
            s=Label(master = root,text= result2 ,font=('Segoe Print',20,'bold'),bg='white',fg='black')
            s.place(x=0,y=550)

        elif rr!='' and ll!='' and aa!='' and pp=='':
            result = ((float(aa))*(float(rr)))/(float(ll))
            w=Label(master = root,text=(convert(f'جواب حاصل :{result}')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red')
            w.place(x=0,y=500)
            result2 = f'ρ = ( A x R ) ÷ L => \nρ = ( {float(aa)} x {float(rr)} ) ÷ {float(ll)} => \nρ = {result}'
            s=Label(master = root,text= result2 ,font=('Segoe Print',20,'bold'),bg='white',fg='black')
            s.place(x=0,y=550)

        elif rr!='' and ll=='' and aa!='' and pp!='':
            result = ((float(aa))*(float(rr)))/(float(pp))
            w=Label(master = root,text=(convert(f'جواب حاصل :{result}')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red')
            w.place(x=0,y=500)
            result2 = f'L = ( A x R ) ÷ ρ => \nL = ( {float(aa)} x {float(rr)} ) ÷ {float(pp)} => \nL = {result}'
            s=Label(master = root,text= result2 ,font=('Segoe Print',20,'bold'),bg='white',fg='black')
            s.place(x=0,y=550)

        elif rr!='' and ll!='' and aa=='' and pp!='':
            result = ((float(pp))*(float(ll)))/(float(rr))
            w=Label(master = root,text=(convert(f'جواب حاصل سطح مقطع:{result}')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red')
            w.place(x=0,y=500)
            result2 = f'A = ( P x L ) ÷ R => \nA = ( {float(pp)} x {float(ll)} ) ÷ {float(rr)} => \nA = {result}'
            s=Label(master = root,text= result2 ,font=('Segoe Print',20,'bold'),bg='white',fg='black')
            s.place(x=0,y=550)

        else:
            messagebox.showerror(message = 'اطلاعات کم یا نادرست است!!')
        
        
        
        


            





    Label(master = root,text=(convert(' مقدار هر یک را وارد کنید و مقدار خواسته شده را خالی بگذارید')) ,font=('Segoe Print',20,'bold'),bg='white',fg='green').place(x=80,y=0)


    P= Label(master = root,text=(convert('مقاومت ویژه:')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red').place(x=0,y=80)
    P_ent = Entry(master=root,font=('Segoe Print',20,'bold'))
    P_ent.place(x=400,y=80)
    L_l = Label(master = root,text=(convert('طول رسانا:')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red').place(x=0,y=160)
    L_ent = Entry(master=root,font=('Segoe Print',20,'bold'))
    L_ent.place(x=400,y=160)

    A_a = Label(master = root,text=(convert('سطح مقطع:')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red').place(x=0,y=240)
    A_ent = Entry(master=root,font=('Segoe Print',20,'bold'))
    A_ent.place(x=400,y=240)

    R_r = Label(master = root,text=(convert('مقاومت رسانا:')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red').place(x=0,y=320)
    R_ent = Entry(master=root,font=('Segoe Print',20,'bold'))
    R_ent.place(x=400,y=320)

    Label(master = root,text=(('R : ( L x ρ ) ÷ A')) ,font=('Segoe Print',20,'bold'),bg='white',fg='blue').place(x=100,y=400)

    sub_btn = Button(master = root,text=(convert('تایید')),font=('Segoe Print',20,'bold'),bg='green',fg='white',activebackground='white',activeforeground='green',command = ent_get).place(x=0,y=400)



    root.mainloop()
def movazenee():
    def sound_play():
        pygame.mixer.init()  # مقداردهی اولیه میکسر pygame
        pygame.mixer.music.load("bib.mp3")  # بارگذاری فایل صوتی
        pygame.mixer.music.play()
    #root setting
    root = Toplevel()
    root.geometry('800x800')
    root.resizable(False,False)
    root.iconbitmap("icon.ico") 
    root.title('window to knowledge')
    #backgroun setting

    image = Image.open('imagess\\wall1.jpg')
    image = image.resize((800,800))
    bg_image = ImageTk.PhotoImage(image)


    def ent_get():
        sound_play()
        global name_lbl, name_lbl2, result_lbl, result_lbl2, show_lbl, show_lbl2
        
        # try:
            # name_lbl.destroy()
            # name_lbl2.destroy()
            # result_lbl.destroy()
            # result_lbl2.destroy()
            # show_lbl.destroy()
            # show_lbl2.destroy()
            
        # except:
        #     pass
        
        
        megdar_va = va_dahande_ent.get()
        megdar_fara = int(faravarde_ent.get())

        
        


            







    va_dahande = Label(master = root,text=(convert('واکنش دهنده:')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red').place(x=0,y=0)

    va_dahande_ent = Entry(master=root,font=('Segoe Print',20,'bold'))
    va_dahande_ent.place(x=400,y=0)
    faravarde = Label(master = root,text=(convert('فراورده:')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red').place(x=0,y=150)
    faravarde_ent = Entry(master=root,font=('Segoe Print',20,'bold'))
    faravarde_ent.place(x=400,y=150)
    sub_btn = Button(master = root,text=(convert('تایید')),font=('Segoe Print',20,'bold'),bg='green',fg='white',activebackground='white',activeforeground='green',command = ent_get).place(x=0,y=550)


    root.mainloop()
def masraff():
    def sound_play():
        pygame.mixer.init()  # مقداردهی اولیه میکسر pygame
        pygame.mixer.music.load("bib.mp3")  # بارگذاری فایل صوتی
        pygame.mixer.music.play()

    root = Toplevel()
    root.geometry('800x800')
    root.resizable(False,False)
    root.iconbitmap("icon.ico") 
    root.title('window to knowledge')
    #backgroun setting

    image = Image.open('imagess\\wall7.jpg')
    image = image.resize((800,800))
    bg_image = ImageTk.PhotoImage(image)


    bg_lbl = Label(root, image=bg_image)
    bg_lbl.place(relheight=1,relwidth=1)



    def ent_get():
        sound_play()
        global result2 , result,w,s
        uu = u_ent.get()
        rr = R_ent.get()
        ii = I_ent.get()
        tt = t_ent.get()
        try:
            w.place_forget()
            s.place_forget()
        except:
            pass
        if uu=='' and rr!='' and ii!='' and tt!='':
            result = (int(rr))*(int(ii))*(int(ii))*(int(tt))
            w=Label(master = root,text=(convert(f'جواب:{result}')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red')
            w.place(x=0,y=500)
            result2 = f'u = R x I^2 x t => \nu = {rr} x {ii**2} x {tt} => \nu = {result}'
            s=Label(master = root,text= result2 ,font=('Segoe Print',20,'bold'),bg='white',fg='black')
            s.place(x=0,y=550)

        elif uu!='' and rr=='' and ii!='' and tt!='':
            result = (int(uu))/((int(ii))*(int(ii))*(int(tt)))
            w=Label(master = root,text=(convert(f'جواب:{result}')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red')
            w.place(x=0,y=500)
            result2 = f'R = u ÷ ( I^2 x t ) => \nR = {uu} ÷ ( {ii**2} x {tt} ) => \nR = {result}'
            s=Label(master = root,text= result2 ,font=('Segoe Print',20,'bold'),bg='white',fg='black')
            s.place(x=0,y=550)

        elif uu!='' and rr!='' and ii=='' and tt!='':
            result = ((int(uu))/((int(rr))*(int(tt))))**0.5
            w=Label(master = root,text=(convert(f'جواب:{result}')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red')
            w.place(x=0,y=500)
            result2 = f'I = √(u ÷ (R x t)) => \nI = √({uu} ÷ ( {rr} x {tt} )) => \nI = √{result**2} => \nI = {result}'
            s=Label(master = root,text= result2 ,font=('Segoe Print',20,'bold'),bg='white',fg='black')
            s.place(x=0,y=550)

        elif uu!='' and rr!='' and ii!='' and tt=='':
            result = (int(uu))/((int(ii))*(int(ii))*(int(rr)))
            w=Label(master = root,text=(convert(f'جواب:{result}')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red')
            w.place(x=0,y=500)
            result2 = f't = u ÷ ( I^2 x R ) => \nt = {uu} ÷ ( {ii} x {rr} ) => \nt = {result}'
            s=Label(master = root,text= result2 ,font=('Segoe Print',20,'bold'),bg='white',fg='black')
            s.place(x=0,y=550)

        else:
            messagebox.showerror(message='اطلاعات نادرست یا ناکافی است!!!')


            






    Label(master = root,text=(convert(' مقدار هر یک را وارد کنید و مقدار خواسته شده را خالی بگذارید')) ,font=('Segoe Print',20,'bold'),bg='white',fg='green').place(x=80,y=0)

    u = Label(master = root,text=(convert('انرژی الکتریکی مصرف شده:')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red').place(x=0,y=80)
    u_ent = Entry(master=root,font=('Segoe Print',20,'bold'))
    u_ent.place(x=400,y=80)
    R = Label(master = root,text=(convert('مقاومت الکتریکی:')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red').place(x=0,y=160)
    R_ent = Entry(master=root,font=('Segoe Print',20,'bold'))
    R_ent.place(x=400,y=160)

    I = Label(master = root,text=(convert('شدت جریان:')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red').place(x=0,y=240)
    I_ent = Entry(master=root,font=('Segoe Print',20,'bold'))
    I_ent.place(x=400,y=240)

    t = Label(master = root,text=(convert('مدت زمان رابطه:')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red').place(x=0,y=320)
    t_ent = Entry(master=root,font=('Segoe Print',20,'bold'))
    t_ent.place(x=400,y=320)

    Label(master = root,text=(('u : R x I^2 x t')) ,font=('Segoe Print',20,'bold'),bg='white',fg='blue').place(x=100,y=400)

    sub_btn = Button(master = root,text=(convert('تایید')),font=('Segoe Print',20,'bold'),bg='green',fg='white',activebackground='white',activeforeground='green',command = ent_get).place(x=0,y=400)


    root.mainloop()
# ---------------------------------------------------------------------------------
def ainee():
    def sound_play():
        pygame.mixer.init()  # مقداردهی اولیه میکسر pygame
        pygame.mixer.music.load("bib.mp3")  # بارگذاری فایل صوتی
        pygame.mixer.music.play()
        
    root = Toplevel()
    root.geometry('800x800')
    root.resizable(False,False)
    root.iconbitmap("icon.ico") 
    root.title('window to knowledge')
    #backgroun setting

    image = Image.open('imagess\\wall8.jpg')
    image = image.resize((800,800))
    bg_image = ImageTk.PhotoImage(image)


    bg_lbl = Label(root, image=bg_image)
    bg_lbl.place(relheight=1,relwidth=1)



    def ent_get():
        sound_play()
        global result,s,w,result2
        qq = q_ent.get()
        pp = p_ent.get()
        aabb = ab_ent.get()
        aabbb = abb_ent.get()
        ff = f_ent.get()
        rr = r_ent.get()
        mm = m_ent.get()

        try:
            w.place_forget()
            s.place_forget()
        except:
            pass

        if qq == '?' and pp != '' and (ff != '' or rr != ''):
            if ff != '':
                result1 = (1 / int(ff)) - (1 / int(pp))
                result2 = f'''
                    🔺 رابطه اصلی:
                        (1 ÷ f) = (1 ÷ q) + (1 ÷ p)

                    🔺 چون q را می‌خواهیم:
                        (1 ÷ q) = (1 ÷ f) - (1 ÷ p)

                    🔺 جایگذاری مقادیر:
                        (1 ÷ q) = (1 ÷ {int(ff)}) - (1 ÷ {int(pp)})

                    🔺 ساده‌سازی:
                        (1 ÷ q) = {1/int(ff)} - {1/int(pp)}

                    🔺 مقدار عددی:
                        (1 ÷ q) = {result1}

                    🔺 در نهایت:
                        q = {1 / result1}
                    '''

            else:
                ff = int(rr) / 2

                result1 = (1 / int(ff)) - (1 / int(pp))
                result2 = f'''
                            🔺 رابطه اصلی:
                                (1 ÷ f) = (1 ÷ q) + (1 ÷ p)

                            🔺 از آنجایی که ما f را نداریم:
                                f = r ÷ 2
                                r = {rr} 
                                f = {rr} ÷ 2 
                                f = {int(rr)/2}
                                                
                            🔺 چون q را می‌خواهیم:
                                (1 ÷ q) = (1 ÷ f) - (1 ÷ p)

                            🔺 جایگذاری مقادیر:
                                (1 ÷ q) = (1 ÷ {int(ff)}) - (1 ÷ {int(pp)})

                            🔺 ساده‌سازی:
                                (1 ÷ q) = {1/int(ff)} - {1/int(pp)}

                            🔺 مقدار عددی:
                                (1 ÷ q) = {result1}

                            🔺 در نهایت:
                                q = {1 / result1}
                            '''


            result = 1 / result1
            r2 = Tk()
            r2.geometry('900x900')
            
            r2.config(bg = 'white')
            
            result3 = Label(master=r2,
                            text=convert(result2),
                            font=('Segoe Print', 20, 'bold'),
                            bg='white',
                            fg='black',
                            justify='left',    # یا 'right' یا 'center'
                            anchor='center',       # بالا و چپ
                            )
            result3.pack()
            r2.mainloop()
            
            s=Label(master = root,text= result2 ,font=('Segoe Print',20,'bold'),bg='white',fg='black')
            s.place(x=0,y=450)

        elif qq != '' and pp == '?' and (ff != '' or rr != ''):
            if ff != '':
                result1 = (1 / int(ff)) - (1 / int(qq))

                result2 = f'''
                    🔺 رابطه اصلی:
                        (1 ÷ f) = (1 ÷ q) + (1 ÷ p)

                    🔺 چون p را می‌خواهیم:
                        (1 ÷ p) = (1 ÷ f) - (1 ÷ q)

                    🔺 جایگذاری مقادیر:
                        (1 ÷ p) = (1 ÷ {int(ff)}) - (1 ÷ {int(qq)})

                    🔺 ساده‌سازی:
                        (1 ÷ p) = {1/int(ff)} - {1/int(qq)}

                    🔺 مقدار عددی:
                        (1 ÷ p) = {result1}

                    🔺 در نهایت:
                        p = {1 / result1}
                    '''


            else:
                ff = float(rr) / 2
                result1 = (1 / float(ff)) - (1 / float(qq))

                result2 = f'''
                            🔺 رابطه اصلی:
                                (1 ÷ f) = (1 ÷ q) + (1 ÷ p)

                            🔺 از آنجایی که ما f را نداریم:
                                f = r ÷ 2
                                r = {rr} 
                                f = {rr} ÷ 2 
                                f = {int(rr)/2}
                                                
                            🔺 چون p را می‌خواهیم:
                                (1 ÷ p) = (1 ÷ f) - (1 ÷ q)

                            🔺 جایگذاری مقادیر:
                                (1 ÷ p) = (1 ÷ {int(ff)}) - (1 ÷ {int(qq)})

                            🔺 ساده‌سازی:
                                (1 ÷ p) = {1/int(ff)} - {1/int(qq)}

                            🔺 مقدار عددی:
                                (1 ÷ p) = {result1}

                            🔺 در نهایت:
                                p = {1 / result1}
                            '''

            result = 1 / result1
            w = Label(root, text=f'فاصله جسم تا آینه: {result:.2f}', font=('Segoe Print', 20, 'bold'), bg='white', fg='green')
            w.place(x=0, y=600)

            result = 1 / result1
            r2 = Tk()
            r2.geometry('900x900')
            
            r2.config(bg = 'white')
            
            result3 = Label(master=r2,
                            text=convert(result2),
                            font=('Segoe Print', 20, 'bold'),
                            bg='white',
                            fg='black',
                            justify='left',    # یا 'right' یا 'center'
                            anchor='center',       # بالا و چپ
                            )
            result3.pack()
            r2.mainloop()
            
            s=Label(master = root,text= result2 ,font=('Segoe Print',20,'bold'),bg='white',fg='black')
            s.place(x=0,y=450)


        elif qq != '' and pp != '' and aabb == '?' and aabbb != '':
            result1 = (int(aabbb) * abs(int(pp))) / abs(int(qq))
            w=Label(root, text=f'طول جسم: {result1:.2f}', font=('Segoe Print', 20, 'bold'), bg='white', fg='green')
            w.place(x=0, y=600)

        
            result2 = f'''
                        🔺 رابطه اصلی:
                            ( 'p| ÷ |q| ) = ( ab ÷ a'b| )

                        🔺 از آنجایی که ما ab را نداریم:
                            |ab = ( a'b' x |p| ) ÷ |q

                        🔺 جایگذاری مقادیر:
                            ab = ( {aabbb} x {abs(int(pp))} ) ÷ {abs(int(qq))}

                        🔺 ساده‌سازی:
                            ab = ({int(aabbb)*(abs(int(pp)))}) ÷ {abs(int(qq))}

                        🔺 در نهایت:
                            ab = {result1}
                        '''

            r2 = Tk()
            r2.geometry('900x900')
            
            r2.config(bg = 'white')
            
            result3 = Label(master=r2,
                            text=convert(result2),
                            font=('Segoe Print', 20, 'bold'),
                            bg='white',
                            fg='black',
                            justify='left',    # یا 'right' یا 'center'
                            anchor='center',       # بالا و چپ
                            )
            result3.pack()
            r2.mainloop()
            
            s=Label(master = root,text= result2 ,font=('Segoe Print',20,'bold'),bg='white',fg='black')
            s.place(x=0,y=450)

        elif qq != '' and pp != '' and aabb != '' and aabbb == '?':
            result1 = (int(aabb) * abs(int(qq))) / abs(int(pp))
            w = Label(root, text=f'طول تصویر: {result1:.2f}', font=('Segoe Print', 20, 'bold'), bg='white', fg='green')
            w.place(x=0, y=600)

            result2 = f'''
                        🔺 رابطه اصلی:
                            ( 'p| ÷ |q| ) = ( ab ÷ a'b| )

                        🔺 از آنجایی که ما a'b' را نداریم:
                            |a'b' = ( ab x |q| ) ÷ |p

                        🔺 جایگذاری مقادیر:
                            a'b' = ( {aabb} x {abs(int(qq))} ) ÷ {abs(int(pp))}

                        🔺 ساده‌سازی:
                            a'b' = ({int(aabb)*(abs(int(qq)))}) ÷ {abs(int(pp))}

                        🔺 در نهایت:
                            ab = {result1}
                        '''

            r2 = Tk()
            r2.geometry('900x900')
            
            r2.config(bg = 'white')
            
            result3 = Label(master=r2,
                            text=convert(result2),
                            font=('Segoe Print', 20, 'bold'),
                            bg='white',
                            fg='black',
                            justify='left',    # یا 'right' یا 'center'
                            anchor='center',       # بالا و چپ
                            )
            result3.pack()
            r2.mainloop()
            
            s=Label(master = root,text= result2 ,font=('Segoe Print',20,'bold'),bg='white',fg='black')
            s.place(x=0,y=450)

        
        elif ((qq != '' and pp != '') or rr != '') and ff == '?':
            if rr != '':
                result1 = int(rr) / 2

                result2 = f'''
                        🔺 رابطه اصلی:
                            R = 2f

                        🔺 از آنجایی که ما f را نداریم:
                            f = R ÷ 2

                        🔺 جایگذاری مقادیر:
                            f = {rr} ÷ 2

                        🔺 در نهایت:
                            f = {result1}
                        '''
            else:
                result1 = 1 / ((1 / int(qq)) + (1 / int(pp)))

                result2 = f'''
                        🔺 رابطه اصلی:
                            1 ÷ f = ( 1 ÷ p ) + ( 1 ÷ q )

                        🔺 جایگذاری مقادیر:
                            1 ÷ f = ( 1 ÷ {pp} ) + ( 1 ÷ {qq} )

                        🔺 ساده‌سازی:
                            1 ÷ f = ( {1/(int(pp))} ) + ( {1/(int(qq))} )

                        🔺 پس از آن:
                            1 ÷ f =  {(1/(int(pp))) + (1/(int(qq)))}

                        🔺 در نهایت:
                            f = {result1}
                        '''
            
            
            w=Label(root, text=f'فاصله کانونی: {result1:.2f}', font=('Segoe Print', 20, 'bold'), bg='white', fg='green')
            w.place(x=0, y=600)

            r2 = Tk()
            r2.geometry('900x900')
            
            r2.config(bg = 'white')
            
            result3 = Label(master=r2,
                            text=convert(result2),
                            font=('Segoe Print', 20, 'bold'),
                            bg='white',
                            fg='black',
                            justify='left',    # یا 'right' یا 'center'
                            anchor='center',       # بالا و چپ
                            )
            result3.pack()
            r2.mainloop()
            
            s=Label(master = root,text= result2 ,font=('Segoe Print',20,'bold'),bg='white',fg='black')
            s.place(x=0,y=450)

        elif ((qq != '' and pp != '') or ff != '') and rr == '?':
            if qq != '' and pp != '':
                result1 = (1 / ((1 / int(qq)) + (1 / int(pp)))) * 2

                result2 = f'''
                        🔺 رابطه اصلی:
                            1 ÷ f = ( 1 ÷ p ) + ( 1 ÷ q )
                            R = 2f

                        🔺 * نکته: اول فاصله کانونی را به دست می آوریم
                        
                        🔺 جایگذاری مقادیر:
                            1 ÷ f = ( 1 ÷ {pp} ) + ( 1 ÷ {qq} )

                        🔺 ساده‌سازی:
                            1 ÷ f = ( {1/(int(pp))} ) + ( {1/(int(qq))} )

                        🔺 پس از آن:
                            1 ÷ f =  {(1/(int(pp))) + (1/(int(qq)))}

                        🔺 در نهایت:
                            f = {1/((1/(int(pp))) + (1/(int(qq))))}
                            R = 2f
                            R = {result1}
                        '''
            
            else:
                result1 = int(ff) * 2

                result2 = f'''
                        🔺 رابطه اصلی:
                            R = 2f

                        🔺 جایگذاری مقادیر:
                            R = 2 x {ff}

                        🔺 در نهایت:
                            R = {2*(int(ff))}

                        
                        '''
            
            w=Label(root, text=f'شعاع: {result1:.2f}', font=('Segoe Print', 20, 'bold'), bg='white', fg='green')
            w.place(x=0, y=600)


            r2 = Tk()
            r2.geometry('900x900')
            
            r2.config(bg = 'white')
            
            result3 = Label(master=r2,
                            text=convert(result2),
                            font=('Segoe Print', 20, 'bold'),
                            bg='white',
                            fg='black',
                            justify='left',    # یا 'right' یا 'center'
                            anchor='center',       # بالا و چپ
                            )
            result3.pack()
            r2.mainloop()
            
            s=Label(master = root,text= result2 ,font=('Segoe Print',20,'bold'),bg='white',fg='black')
            s.place(x=0,y=450)

        elif ((qq != '' and pp != '') or (aabb != '' and aabbb != '')) and mm == '?':
            if qq != '' and pp != '':
                result1 = abs(int(qq)) / abs(int(pp))

                result2 = f'''
                        🔺 رابطه اصلی:
                            M = |q| ÷ |p| 
                            M = a'b' ÷ ab

                        🔺 از آنجایی که ما a'b' و ab  را نداریم:
                            M = |q| ÷ |p|

                        🔺 جایگذاری مقادیر:
                            M = |{qq}| ÷ |{pp}|

                        🔺 ساده‌سازی:
                            M = {abs(int(qq))} ÷ {abs(int(pp))}

                        🔺 در نهایت:
                            M = {result1}
                        '''

            else:
                result1 = float(aabbb) / float(aabb)
                result2 = f'''
                        🔺 رابطه اصلی:
                            M = |q| ÷ |p| 
                            M = a'b' ÷ ab

                        🔺 از آنجایی که ما p و q  را نداریم:
                            M = a'b ÷ ab

                        🔺 جایگذاری مقادیر:
                            M = {aabbb} ÷ {aabb}

                        🔺 در نهایت:
                            M = {result1}
                        '''

            w=Label(root, text=f'بزرگ نمایی: {result1:.2f}', font=('Segoe Print', 20, 'bold'), bg='white', fg='green')
            w.place(x=0, y=600)

            r2 = Tk()
            r2.geometry('900x900')
            
            r2.config(bg = 'white')
            
            result3 = Label(master=r2,
                            text=convert(result2),
                            font=('Segoe Print', 20, 'bold'),
                            bg='white',
                            fg='black',
                            justify='left',    # یا 'right' یا 'center'
                            anchor='center',       # بالا و چپ
                            )
            result3.pack()
            r2.mainloop()
            
            s=Label(master = root,text= result2 ,font=('Segoe Print',20,'bold'),bg='white',fg='black')
            s.place(x=0,y=450)

        else:
            messagebox.showwarning('هشدار', 'لطفاً مقدار درست وارد کن! حالت نامعتبره 😢')

        




    Label(master = root,text=(convert(' مقدار هر یک را که مربوط به مسئله است را وارد کنید و مقادیر خواسته شده را ? بگذارید')) ,font=('Segoe Print',20,'bold'),bg='white',fg='green').place(x=0,y=0)

    ab = Label(master = root,text=(convert('طول جسم:')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red').place(x=0,y=80)
    ab_ent = Entry(master=root,font=('Segoe Print',20,'bold'))
    ab_ent.place(x=400,y=80)
    abb = Label(master = root,text=(convert('طول تصویر:')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red').place(x=0,y=160)
    abb_ent = Entry(master=root,font=('Segoe Print',20,'bold'))
    abb_ent.place(x=400,y=160)

    p = Label(master = root,text=(convert('فاصله جسم تا آینه:')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red').place(x=0,y=240)
    p_ent = Entry(master=root,font=('Segoe Print',20,'bold'))
    p_ent.place(x=400,y=240)


    q = Label(master = root,text=(convert('فاصله تصویر تا آینه:')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red').place(x=0,y=320)
    q_ent = Entry(master=root,font=('Segoe Print',20,'bold'))
    q_ent.place(x=400,y=320)


    r = Label(master = root,text=(convert('شعاع:')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red').place(x=0,y=400)
    r_ent = Entry(master=root,font=('Segoe Print',20,'bold'))
    r_ent.place(x=400,y=400)

    f = Label(master = root,text=(convert('فاصله کانونی:')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red').place(x=0,y=480)
    f_ent = Entry(master=root,font=('Segoe Print',20,'bold'))
    f_ent.place(x=400,y=480)

    m= Label(master = root,text=(convert('بزرگ نمایی:')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red').place(x=0,y=560)
    m_ent = Entry(master=root,font=('Segoe Print',20,'bold'))
    m_ent.place(x=400,y=560)
    sub_btn = Button(master = root,text=(convert('تایید')),font=('Segoe Print',20,'bold'),bg='green',fg='white',activebackground='white',activeforeground='green',command = ent_get).place(x=0,y=660)


    root.mainloop()


#persian typing setting
def convert(text):
    rt = arabic_reshaper.reshape(text)
    converted = get_display(rt)
    return converted

def motegatee():
    def sound_play():
        pygame.mixer.init()  # مقداردهی اولیه میکسر pygame
        pygame.mixer.music.load("bib.mp3")  # بارگذاری فایل صوتی
        pygame.mixer.music.play()
        
    root = Toplevel()
    root.geometry('800x800')
    root.resizable(False,False)
    root.iconbitmap("icon.ico") 
    root.title('window to knowledge')
    #backgroun setting

    image = Image.open('imagess\\wall8.jpg')
    image = image.resize((800,800))
    bg_image = ImageTk.PhotoImage(image)


    bg_lbl = Label(root, image=bg_image)
    bg_lbl.place(relheight=1,relwidth=1)



    def ent_get():
        sound_play()
        global s,w , javab,result2
        try:
            w.place_forget()
            s.place_forget()
        except:
            pass
        aa = α_ent.get()
        nn = N_ent.get()
        if aa=='' and nn!='':
            javab = 360/(int(nn)+1)
            w=Label(master = root,text=((f'اندازه α:{javab}')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red')
            w.place(x=0,y=400)
            result2 = f'α = 360 ÷ (n+1) => \nα = 360 ÷ ( {nn} + 1 ) => \nα = 360 ÷ ( {int(nn)+1} ) => \nα = {javab}'
            s=Label(master = root,text= result2 ,font=('Segoe Print',20,'bold'),bg='white',fg='black')
            s.place(x=0,y=450)
        elif aa!='' and nn=='':
            javab = (360/(int(aa)))-1
            w=Label(master = root,text=((f'اندازه n:{javab}')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red')
            w.place(x=0,y=400)
            result2 = f'n = ( 360 ÷ α ) - 1 => \nn = ( 360 ÷ {aa} ) - 1 => \nn = ( {360 / int(aa)} ) + 1 => \nn = {javab}'
            s=Label(master = root,text= result2 ,font=('Segoe Print',20,'bold'),bg='white',fg='black')
            s.place(x=0,y=450)
        else:
            messagebox.showerror(message='اطلاعات ناکافی یا نادرست است!')
        
        
        


            






    Label(master = root,text=(convert(' مقدار هر یک را وارد کنید و مقدار خواسته شده را خالی بگذارید')) ,font=('Segoe Print',20,'bold'),bg='white',fg='green').place(x=80,y=0)

    N = Label(master = root,text=(convert('تعداد تصاویر:')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red').place(x=0,y=80)
    N_ent = Entry(master=root,font=('Segoe Print',20,'bold'))
    N_ent.place(x=400,y=80)
    α = Label(master = root,text=(convert('زاویه بین دو آینه:')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red').place(x=0,y=160)
    α_ent = Entry(master=root,font=('Segoe Print',20,'bold'))
    α_ent.place(x=400,y=160)

    Label(master = root,text=(convert('n = (360 ÷ α ) - 1')) ,font=('Segoe Print',20,'bold'),bg='white',fg='blue').place(x=150,y=300)

    sub_btn = Button(master = root,text=(convert('تایید')),font=('Segoe Print',20,'bold'),bg='green',fg='white',activebackground='white',activeforeground='green',command = ent_get).place(x=0,y=300)


    root.mainloop()
def elecc():
    def sound_play():
        pygame.mixer.init()  # مقداردهی اولیه میکسر pygame
        pygame.mixer.music.load("bib.mp3")  # بارگذاری فایل صوتی
        pygame.mixer.music.play()
        
    #root setting
    root = Toplevel()
    root.geometry('800x800')
    root.resizable(False,False)
    root.iconbitmap("icon.ico") 
    root.title('chemastry lesson')
    #backgroun setting

    image = Image.open('imagess\\wall6.jpg')
    image = image.resize((800,800))
    bg_image = ImageTk.PhotoImage(image)

    bg_lbl = Label(root, image=bg_image)
    bg_lbl.place(relheight=1,relwidth=1)

    
    def ohhm():

        sound_play()
        ohmm()

    def mmv():

        sound_play()
        mvv()

    def sshedat():

        sound_play()
        shedatt()

    def mmasraf():

        sound_play()
        masraff()
    oohm = Button(root,bg='#C1C8F5',activeforeground='#C1C8F5',fg='#656980',activebackground='#656980' ,command= ohhm , text=convert('قانون اهم'),font=('Segoe Print',20,'bold')).place(x=150,y=220)
    mogavematt_vige = Button(root,bg='#F5ACA6',activeforeground='#F5ACA6',fg='#80322D',activebackground='#80322D' ,command= mmv , text=convert('مقاومت رسانا'),font=('Segoe Print',20,'bold')).place(x=550,y=220)
    shedat_jjarian = Button(root,bg='#B0F4BC',activeforeground='#B0F4BC',fg='#5C8063',activebackground='#5C8063' ,command= sshedat , text=convert('شدت جریان الکتریکی'),font=('Segoe Print',20,'bold')).place(x=150,y=400)
    masraaf = Button(root,bg='#EAE88D',activeforeground='#EAE88D',fg='#767547',activebackground='#767547' ,command= mmasraf , text=convert('انرژی الکتریکی مصرف شده'),font=('Segoe Print',20,'bold')).place(x=450,y=400)


    root.mainloop()

def coll():
    def sound_play():
        pygame.mixer.init()  # مقداردهی اولیه میکسر pygame
        pygame.mixer.music.load("bib.mp3")  # بارگذاری فایل صوتی
        pygame.mixer.music.play()
        
    #root setting
    root = Toplevel()
    root.geometry('800x800')
    root.resizable(False,False)
    root.iconbitmap("icon.ico") 
    root.title('window to knowledge')
    #backgroun setting

    image = Image.open('imagess\\wall3.jpg')
    image = image.resize((800,800))
    bg_image = ImageTk.PhotoImage(image)


    bg_lbl = Label(root, image=bg_image)
    bg_lbl.place(relheight=1,relwidth=1)



    def ent_get():
        sound_play()
        global result2 , result,result3
        
        try:
            result.destroy()
            result2.destroy()
            
            
        except:
            pass
        qq1 = abs(int(q1_ent.get()))
        qqq1= int(q1_ent.get())
        qq2 = abs(int(q2_ent.get()))
        qqq2 = int(q2_ent.get())
        rr = int(r_ent.get())
        k = 9*(10**9)
        javab =(qq1*qq2*k)/(rr**2)

        a = 0
        b = ''
        for i in str(javab):
            if i == '0':
                a +=1
            else:
                b+= str(i)
        javab = b+'*10^'+str(a)

        result = Label(master = root,text=((f'اندازه نیرو:{javab}')) ,font=('Segoe Print',20,'bold'),bg='white',fg='black')
        result.place(x=0,y=330)
        if (qqq1>0 and qqq2>0) or (qqq1<0 and qqq2<2):
            noe_niro = 'رانشی'
        else:
            noe_niro = 'ربایشی'
        
        result2 = Label(master = root,text=(convert(f'نوع نیرو:{noe_niro}')) ,font=('Segoe Print',20,'bold'),bg='white',fg='black')
        result2.place(x=0,y=380)
        r2 = Tk()
        r2.geometry('900x900')
        r2.config(bg = 'white')

        real_result_3 = f'''
    🔹 ابتدا قدر مطلق هر دو بار را حساب می‌کنیم:
        {qqq1} => {qq1}
        {qqq2} => {qq2}

    🔹 مقادیر:
        q1 = {qqq1}
        q2 = {qqq2}
        r  = {rr}
        k  = 9 × (10 ^ 9)

    🔹 فرمول محاسبه نیرو:
        F = (q1 × q2 × k) ÷ (r ^ 2)

    🔹 جایگذاری اعداد:
        F = ({qq1} × {qq2} × 9 × (10 ^ 9)) ÷ ({rr} ^ 2)

    🔹 نتیجه نهایی:
        {javab}
    '''

        result3 = Label(master = r2,text=(convert(real_result_3)) ,font=('Segoe Print',20,'bold'),bg='white',fg='black')
        result3.pack()
        r2.mainloop()
        
        
        
        
        


            







    q1 = Label(master = root,text=(convert('q1(بار الکتریکی اول):')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red').place(x=0,y=0)
    q1_ent = Entry(master=root,font=('Segoe Print',20,'bold'))
    q1_ent.place(x=400,y=0)
    q2 = Label(master = root,text=(convert('q2(بار الکتریکی دوم):')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red').place(x=0,y=80)
    q2_ent = Entry(master=root,font=('Segoe Print',20,'bold'))
    q2_ent.place(x=400,y=80)

    r = Label(master = root,text=(convert('r(فاصله بین دو بار):')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red').place(x=0,y=160)
    r_ent = Entry(master=root,font=('Segoe Print',20,'bold'))
    r_ent.place(x=400,y=160)

    sub_btn = Button(master = root,text=(convert('تایید')),font=('Segoe Print',20,'bold'),bg='green',fg='white',activebackground='white',activeforeground='green',command = ent_get).place(x=0,y=220)




    root.mainloop()
def adasii():
    def sound_play():
        pygame.mixer.init()  # مقداردهی اولیه میکسر pygame
        pygame.mixer.music.load("bib.mp3")  # بارگذاری فایل صوتی
        pygame.mixer.music.play()
    root = Toplevel()
    root.geometry('800x800')
    root.resizable(False,False)(False,False)
    root.iconbitmap("icon.ico") 
    root.title('window to knowledge')
    #backgroun setting

    image = Image.open('imagess\\wall8.jpg')
    image = image.resize((800,800))
    bg_image = ImageTk.PhotoImage(image)


    bg_lbl = Label(root, image=bg_image)
    bg_lbl.place(relheight=1,relwidth=1)



    def ent_get():
        sound_play()
        global w,s,result,result1,result3 , result2
        qq = q_ent.get()
        pp = p_ent.get()
        aabb = ab_ent.get()
        aabbb = abb_ent.get()
        ff = f_ent.get()
        rr = r_ent.get()
        mm = m_ent.get()
        dd = d_ent.get()
        try:
            w.place_forget()
            s.place_forget()
        except:
            pass

        if qq == '?' and pp != '' and (ff != '' or rr != ''):
            if ff != '':
                result1 = (1 / int(ff)) - (1 / int(pp))
                result2 = f'''
                    🔺 رابطه اصلی:
                        (1 ÷ f) = (1 ÷ q) + (1 ÷ p)

                    🔺 چون q را می‌خواهیم:
                        (1 ÷ q) = (1 ÷ f) - (1 ÷ p)

                    🔺 جایگذاری مقادیر:
                        (1 ÷ q) = (1 ÷ {int(ff)}) - (1 ÷ {int(pp)})

                    🔺 ساده‌سازی:
                        (1 ÷ q) = {1/int(ff)} - {1/int(pp)}

                    🔺 مقدار عددی:
                        (1 ÷ q) = {result1}

                    🔺 در نهایت:
                        q = {1 / result1}
                    '''

            else:
                ff = int(rr) / 2

                result1 = (1 / int(ff)) - (1 / int(pp))
                result2 = f'''
                            🔺 رابطه اصلی:
                                (1 ÷ f) = (1 ÷ q) + (1 ÷ p)

                            🔺 از آنجایی که ما f را نداریم:
                                f = r ÷ 2
                                r = {rr} 
                                f = {rr} ÷ 2 
                                f = {int(rr)/2}
                                                
                            🔺 چون q را می‌خواهیم:
                                (1 ÷ q) = (1 ÷ f) - (1 ÷ p)

                            🔺 جایگذاری مقادیر:
                                (1 ÷ q) = (1 ÷ {int(ff)}) - (1 ÷ {int(pp)})

                            🔺 ساده‌سازی:
                                (1 ÷ q) = {1/int(ff)} - {1/int(pp)}

                            🔺 مقدار عددی:
                                (1 ÷ q) = {result1}

                            🔺 در نهایت:
                                q = {1 / result1}
                            '''

            result = 1 / result1
            w=Label(root, text=f'فاصله تصویر تا عدسی: {result:.2f}', font=('Segoe Print', 20, 'bold'), bg='white', fg='green')
            w.place(x=0, y=700)

            r2 = Tk()
            r2.geometry('900x900')
            
            r2.config(bg = 'white')
            
            result3 = Label(master=r2,
                            text=convert(result2),
                            font=('Segoe Print', 20, 'bold'),
                            bg='white',
                            fg='black',
                            justify='left',    # یا 'right' یا 'center'
                            anchor='center',       # بالا و چپ
                            )
            result3.pack()
            r2.mainloop()
            
            s=Label(master = root,text= result2 ,font=('Segoe Print',20,'bold'),bg='white',fg='black')
            s.place(x=0,y=450)

        elif qq != '' and pp == '?' and (ff != '' or rr != ''):
            if ff != '':
                result1 = (1 / int(ff)) - (1 / int(qq))

                result2 = f'''
                    🔺 رابطه اصلی:
                        (1 ÷ f) = (1 ÷ q) + (1 ÷ p)

                    🔺 چون p را می‌خواهیم:
                        (1 ÷ p) = (1 ÷ f) - (1 ÷ q)

                    🔺 جایگذاری مقادیر:
                        (1 ÷ p) = (1 ÷ {int(ff)}) - (1 ÷ {int(qq)})

                    🔺 ساده‌سازی:
                        (1 ÷ p) = {1/int(ff)} - {1/int(qq)}

                    🔺 مقدار عددی:
                        (1 ÷ p) = {result1}

                    🔺 در نهایت:
                        p = {1 / result1}
                    '''


            else:
                ff = int(rr) / 2
                result1 = (1 / int(ff)) - (1 / int(qq))

                result2 = f'''
                            🔺 رابطه اصلی:
                                (1 ÷ f) = (1 ÷ q) + (1 ÷ p)

                            🔺 از آنجایی که ما f را نداریم:
                                f = r ÷ 2
                                r = {rr} 
                                f = {rr} ÷ 2 
                                f = {int(rr)/2}
                                                
                            🔺 چون p را می‌خواهیم:
                                (1 ÷ p) = (1 ÷ f) - (1 ÷ q)

                            🔺 جایگذاری مقادیر:
                                (1 ÷ p) = (1 ÷ {int(ff)}) - (1 ÷ {int(qq)})

                            🔺 ساده‌سازی:
                                (1 ÷ p) = {1/int(ff)} - {1/int(qq)}

                            🔺 مقدار عددی:
                                (1 ÷ p) = {result1}

                            🔺 در نهایت:
                                p = {1 / result1}
                            '''
            result = 1 / result1
            w=Label(root, text=f'فاصله جسم تا عدسی: {result:.2f}', font=('Segoe Print', 20, 'bold'), bg='white', fg='green')
            w.place(x=0, y=700)
            r2 = Tk()
            r2.geometry('900x900')
            
            r2.config(bg = 'white')
            
            result3 = Label(master=r2,
                            text=convert(result2),
                            font=('Segoe Print', 20, 'bold'),
                            bg='white',
                            fg='black',
                            justify='left',    # یا 'right' یا 'center'
                            anchor='center',       # بالا و چپ
                            )
            result3.pack()
            r2.mainloop()
            
            s=Label(master = root,text= result2 ,font=('Segoe Print',20,'bold'),bg='white',fg='black')
            s.place(x=0,y=450)

        elif qq != '' and pp != '' and aabb == '?' and aabbb != '':
            result1 = (int(aabbb) * abs(int(pp))) / abs(int(qq))
            result2 = f'''
                        🔺 رابطه اصلی:
                            ( 'p| ÷ |q| ) = ( ab ÷ a'b| )

                        🔺 از آنجایی که ما ab را نداریم:
                            |ab = ( a'b' x |p| ) ÷ |q

                        🔺 جایگذاری مقادیر:
                            ab = ( {aabbb} x {abs(int(pp))} ) ÷ {abs(int(qq))}

                        🔺 ساده‌سازی:
                            ab = ({int(aabbb)*(abs(int(pp)))}) ÷ {abs(int(qq))}

                        🔺 در نهایت:
                            ab = {result1}
                        '''
            w=Label(root, text=f'طول جسم: {result1:.2f}', font=('Segoe Print', 20, 'bold'), bg='white', fg='green')
            w.place(x=0, y=700)
            r2 = Tk()
            r2.geometry('900x900')
            
            r2.config(bg = 'white')
            
            result3 = Label(master=r2,
                            text=convert(result2),
                            font=('Segoe Print', 20, 'bold'),
                            bg='white',
                            fg='black',
                            justify='left',    # یا 'right' یا 'center'
                            anchor='center',       # بالا و چپ
                            )
            result3.pack()
            r2.mainloop()
            
            s=Label(master = root,text= result2 ,font=('Segoe Print',20,'bold'),bg='white',fg='black')
            s.place(x=0,y=450)

        elif qq != '' and pp != '' and aabb != '' and aabbb == '?':
            result1 = (int(aabb) * abs(int(qq))) / abs(int(pp))
            result2 = f'''
                        🔺 رابطه اصلی:
                            ( 'p| ÷ |q| ) = ( ab ÷ a'b| )

                        🔺 از آنجایی که ما a'b' را نداریم:
                            |a'b' = ( ab x |q| ) ÷ |p

                        🔺 جایگذاری مقادیر:
                            a'b' = ( {aabb} x {abs(int(qq))} ) ÷ {abs(int(pp))}

                        🔺 ساده‌سازی:
                            a'b' = ({int(aabb)*(abs(int(qq)))}) ÷ {abs(int(pp))}

                        🔺 در نهایت:
                            ab = {result1}
                        '''


            w=Label(root, text=f'طول تصویر: {result1:.2f}', font=('Segoe Print', 20, 'bold'), bg='white', fg='green')
            w.place(x=0, y=700)
            r2 = Tk()
            r2.geometry('900x900')
            
            r2.config(bg = 'white')
            
            result3 = Label(master=r2,
                            text=convert(result2),
                            font=('Segoe Print', 20, 'bold'),
                            bg='white',
                            fg='black',
                            justify='left',    # یا 'right' یا 'center'
                            anchor='center',       # بالا و چپ
                            )
            result3.pack()
            r2.mainloop()
            
            s=Label(master = root,text= result2 ,font=('Segoe Print',20,'bold'),bg='white',fg='black')
            s.place(x=0,y=450)

        elif ((qq != '' and pp != '') or rr != '' or dd!='') and ff == '?':
            if rr != '':
                result1 = int(rr) / 2
                result2 = f'''
                        🔺 رابطه اصلی:
                            R = 2f

                        🔺 از آنجایی که ما f را نداریم:
                            f = R ÷ 2

                        🔺 جایگذاری مقادیر:
                            f = {rr} ÷ 2

                        🔺 در نهایت:
                            f = {result1}
                        '''
            elif dd!='':
                result1 = 1/int(dd)

                result2 = f'''
                        🔺 رابطه اصلی:
                            f = 1 ÷ d

                        🔺 جایگذاری مقادیر:
                            f = 1 ÷ {dd}

                        🔺 در نهایت:
                            f = {result1}
                        '''
            
            else:
                result1 = 1 / ((1 / int(qq)) + (1 / int(pp)))

                result2 = f'''
                        🔺 رابطه اصلی:
                            1 ÷ f = ( 1 ÷ p ) + ( 1 ÷ q )

                        🔺 جایگذاری مقادیر:
                            1 ÷ f = ( 1 ÷ {pp} ) + ( 1 ÷ {qq} )

                        🔺 ساده‌سازی:
                            1 ÷ f = ( {1/(int(pp))} ) + ( {1/(int(qq))} )

                        🔺 پس از آن:
                            1 ÷ f =  {(1/(int(pp))) + (1/(int(qq)))}

                        🔺 در نهایت:
                            f = {result1}
                        '''
            


            w=Label(root, text=f'فاصله کانونی: {result1:.2f}', font=('Segoe Print', 20, 'bold'), bg='white', fg='green')
            w.place(x=0, y=700)
            r2 = Tk()
            r2.geometry('900x900')
            
            r2.config(bg = 'white')
            
            result3 = Label(master=r2,
                            text=convert(result2),
                            font=('Segoe Print', 20, 'bold'),
                            bg='white',
                            fg='black',
                            justify='left',    # یا 'right' یا 'center'
                            anchor='center',       # بالا و چپ
                            )
            result3.pack()
            r2.mainloop()
            
            s=Label(master = root,text= result2 ,font=('Segoe Print',20,'bold'),bg='white',fg='black')
            s.place(x=0,y=450)

        elif ((qq != '' and pp != '') or ff != '') and rr == '?':
            if qq != '' and pp != '':
                result1 = (1 / ((1 / float(qq)) + (1 / float(pp)))) * 2
                result2 = f'''
                        🔺 رابطه اصلی:
                            1 ÷ f = ( 1 ÷ p ) + ( 1 ÷ q )
                            R = 2f

                        🔺 * نکته: اول فاصله کانونی را به دست می آوریم
                        
                        🔺 جایگذاری مقادیر:
                            1 ÷ f = ( 1 ÷ {pp} ) + ( 1 ÷ {qq} )

                        🔺 ساده‌سازی:
                            1 ÷ f = ( {1/(int(pp))} ) + ( {1/(int(qq))} )

                        🔺 پس از آن:
                            1 ÷ f =  {(1/(int(pp))) + (1/(int(qq)))}

                        🔺 در نهایت:
                            f = {1/((1/(int(pp))) + (1/(int(qq))))}
                            R = 2f
                            R = {result1}
                        '''
            else:
                result1 = int(ff) * 2
                result2 = f'''
                        🔺 رابطه اصلی:
                            R = 2f

                        🔺 جایگذاری مقادیر:
                            R = 2 x {ff}

                        🔺 در نهایت:
                            R = {2*(int(ff))}

                        
                        '''
            
            w=Label(root, text=f'شعاع: {result1:.2f}', font=('Segoe Print', 20, 'bold'), bg='white', fg='green')
            w.place(x=0, y=700)
            r2 = Tk()
            r2.geometry('900x900')
            
            r2.config(bg = 'white')
            
            result3 = Label(master=r2,
                            text=convert(result2),
                            font=('Segoe Print', 20, 'bold'),
                            bg='white',
                            fg='black',
                            justify='left',    # یا 'right' یا 'center'
                            anchor='center',       # بالا و چپ
                            )
            result3.pack()
            r2.mainloop()
            
            s=Label(master = root,text= result2 ,font=('Segoe Print',20,'bold'),bg='white',fg='black')
            s.place(x=0,y=450)

        elif ((qq != '' and pp != '') or (aabb != '' and aabbb != '')) and mm == '?':
            if qq != '' and pp != '':
                result1 = abs(int(qq)) / abs(int(pp))
            else:
                result1 = int(aabbb) / int(aabb)
            w=Label(root, text=f'بزرگ نمایی: {result1:.2f}', font=('Segoe Print', 20, 'bold'), bg='white', fg='green')
            w.place(x=0, y=700)

            r2 = Tk()
            r2.geometry('900x900')
            
            r2.config(bg = 'white')
            
            result3 = Label(master=r2,
                            text=convert(result2),
                            font=('Segoe Print', 20, 'bold'),
                            bg='white',
                            fg='black',
                            justify='left',    # یا 'right' یا 'center'
                            anchor='center',       # بالا و چپ
                            )
            result3.pack()
            r2.mainloop()
            
            s=Label(master = root,text= result2 ,font=('Segoe Print',20,'bold'),bg='white',fg='black')
            s.place(x=0,y=450)
        elif dd=='?' and ff!='':
            result1 = 1/int(ff)
            result2 = f'''
                        🔺 رابطه اصلی:
                            d = 1 ÷ f

                        🔺 جایگذاری مقادیر:
                            d = 1 ÷ {ff}

                        🔺 در نهایت:
                            d = {result1}
                        '''
            
            w=Label(root, text=f'توان عدسی: {result1:.2f}', font=('Segoe Print', 20, 'bold'), bg='white', fg='green')
            w.place(x=0, y=700)
            r2 = Tk()
            r2.geometry('900x900')
            
            r2.config(bg = 'white')
            
            result3 = Label(master=r2,
                            text=convert(result2),
                            font=('Segoe Print', 20, 'bold'),
                            bg='white',
                            fg='black',
                            justify='left',    # یا 'right' یا 'center'
                            anchor='center',       # بالا و چپ
                            )
            result3.pack()
            r2.mainloop()
            
            s=Label(master = root,text= result2 ,font=('Segoe Print',20,'bold'),bg='white',fg='black')
            s.place(x=0,y=450)

        else:
            messagebox.showwarning('هشدار', 'لطفاً مقدار درست وارد کن! حالت نامعتبره 😢')

        




    Label(master = root,text=(convert(' مقدار هر یک را که مربوط به مسئله است را وارد کنید و مقادیر خواسته شده را ? بگذارید')) ,font=('Segoe Print',20,'bold'),bg='white',fg='green').place(x=0,y=0)


    ab = Label(master = root,text=(convert('طول جسم:')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red').place(x=0,y=80)
    ab_ent = Entry(master=root,font=('Segoe Print',20,'bold'))
    ab_ent.place(x=400,y=80)
    abb = Label(master = root,text=(convert('طول تصویر:')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red').place(x=0,y=160)
    abb_ent = Entry(master=root,font=('Segoe Print',20,'bold'))
    abb_ent.place(x=400,y=160)

    p = Label(master = root,text=(convert('فاصله جسم تا عدسی:')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red').place(x=0,y=240)
    p_ent = Entry(master=root,font=('Segoe Print',20,'bold'))
    p_ent.place(x=400,y=240)


    q = Label(master = root,text=(convert('فاصله تصویر تا عدسی:')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red').place(x=0,y=320)
    q_ent = Entry(master=root,font=('Segoe Print',20,'bold'))
    q_ent.place(x=400,y=320)


    r = Label(master = root,text=(convert('شعاع:')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red').place(x=0,y=400)
    r_ent = Entry(master=root,font=('Segoe Print',20,'bold'))
    r_ent.place(x=400,y=400)

    f = Label(master = root,text=(convert('فاصله کانونی:')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red').place(x=0,y=480)
    f_ent = Entry(master=root,font=('Segoe Print',20,'bold'))
    f_ent.place(x=400,y=480)

    m= Label(master = root,text=(convert('بزرگ نمایی:')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red').place(x=0,y=560)
    m_ent = Entry(master=root,font=('Segoe Print',20,'bold'))
    m_ent.place(x=400,y=560)
    d= Label(master = root,text=(convert('توان عدسی')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red').place(x=0,y=640)
    d_ent = Entry(master=root,font=('Segoe Print',20,'bold'))
    d_ent.place(x=400,y=640)
    sub_btn = Button(master = root,text=(convert('تایید')),font=('Segoe Print',20,'bold'),bg='green',fg='white',activebackground='white',activeforeground='green',command = ent_get).place(x=300,y=700)


    root.mainloop()


def nogte_ii():
    def sound_play():
        pygame.mixer.init()  # مقداردهی اولیه میکسر pygame
        pygame.mixer.music.load("bib.mp3")  # بارگذاری فایل صوتی
        pygame.mixer.music.play()
        
    #root setting
    root = Toplevel()
    root.geometry('800x800')
    root.resizable(False,False)
    root.iconbitmap("icon.ico") 
    root.title('window to knowledge')
    #backgroun setting

    image = Image.open('imagess\\yellow.jpg')
    image = image.resize((800,800))

    bg_image = ImageTk.PhotoImage(image)

    bg_lbl = Label(root, image=bg_image)
    bg_lbl.place(relheight=1,relwidth=1)

    def ent_get():
        sound_play()
        global name_lbl, name_lbl2, result_lbl, result_lbl2, show_lbl, show_lbl2
        
        try:
            name_lbl.destroy()
            name_lbl2.destroy()
            result_lbl.destroy()
            result_lbl2.destroy()
            show_lbl.destroy()
            show_lbl2.destroy()
            
        except:
            pass
        
        
        name_atom = at_name_ent.get()
        number_electrom = int(electron_ent.get())
        name_atom2 = at_name_ent2.get()
        number_electrom2 = int(electron_ent2.get())
        
        

        num_num1 = number_electrom
        num_num2 = number_electrom2
        n1 = 1
        n2 = 1
        y = False


        if number_electrom in [1,2,3]: num1 = True 
        else: num1 = False


        if number_electrom2 in [1,2,3]:num2 = True
        else:num2 = False

        if num1==True and num2==True:
            y=True
            messagebox.showerror(message=(('هر دو فلز نمیشود! یک فلز و یک نافلز')))
        if num1==False and num2==False:
            y = True
            messagebox.showerror(message=(('هردو نافلز نمیشود! یک فلز و یک نافلز')))
        if number_electrom == 4 or number_electrom2==4:
            y = True
            messagebox.showinfo(message=(('خنثی ترکیب نمیسازد!')))
        if number_electrom>8 or number_electrom2>8:
            y = True
            messagebox.showinfo(message=(('درست نیست.بیشتر از 8 نمیتونه باشه')))
        if number_electrom==8 or number_electrom2==8:
            y = True
            messagebox.showinfo(message=(('یکیشون پایداره نمیخواد بگیره.')))

        


        
        # تا زمانی که وای ترو نیست اگر اولی ترو(فلز) و دومی فالس(نافلز) باشد تا زمانی که  اولی صفر و دومی هشت(پایدار نشده باشه ادامه داره
        #خوب از فلز کم میشه میره به نافلز اما اگر اولی پایدار و دومی نشده بود قدار اولی رو دووباره برابر اولش میکنیم انگار یک عنصر جدید اضافه کردیم
        #و نام یک +1 میشه چون تعداد رو نشون میده.اگر اولی صفر نشده دومی هشت هم به همین صورت و اگر اولی صفر دومی هشت وای برابر ترو و حلقه تمام
        if y==False:
            while y==False:
                if num1==True and num2 ==False:
                    while num_num1>0 and num_num2<8:
                        num_num1-=1
                        num_num2+=1
                        if num_num1==0 and num_num2!=8:
                            num_num1 = number_electrom
                            n1+=1
                        if num_num1!=0 and num_num2==8:
                            num_num2= number_electrom2
                            n2+=1
                        if num_num1==0 and num_num2==8:
                            y=True

                if num2==True and num1 ==False:
                    while num_num2>0 and num_num1<8:
                        num_num2-=1
                        num_num1+=1
                        if num_num2==0 and num_num1!=8:
                            num_num2 = number_electrom2
                            n2+=1
                        if num_num2!=0 and num_num1==8:
                            num_num1= number_electrom
                            n1+=1
                        if num_num2==0 and num_num1==8:
                            y=True
        name_lbl = Label(master = root,text=(f'{name_atom}:'),font=('Segoe Print',30,'bold'),bg='white',fg='black')
        name_lbl.place(x=200,y=550)
        num_el_2 = number_electrom-(number_electrom//2)
        num_el_3 = number_electrom//2
        dots = '.' * num_el_3
        dots2 = '.' * num_el_2
        result = dots + name_atom + dots2+'   '
        result_lbl = Label(master = root,text=(n1*result),font=('Segoe Print',30,'bold'),bg='white',fg='black')
        result_lbl.place(x=200,y=550)

        name_lbl2 = Label(master = root,text=(f'{name_atom2}:'),font=('Segoe Print',30,'bold'),bg='white',fg='black')
        name_lbl2.place(x=200,y=650)
        num_el_22 = number_electrom2-(number_electrom2//2)
        num_el_32 = number_electrom2//2
        dots2 = '.' * num_el_32
        dots22 = '.' * num_el_22
        result2 = dots2 + name_atom2 + dots22+'   '
        result_lbl2 = Label(master = root,text=(n2*result2),font=('Segoe Print',30,'bold'),bg='white',fg='black')
        result_lbl2.place(x=200,y=650)

        show_lbl = Label(master = root,text=(convert(f' {name_atom} : {n1}')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red')
        show_lbl.place(x=0,y=650)
        show_lbl2 = Label(master = root,text=(convert(f' {name_atom2} : {n2}')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red')
        show_lbl2.place(x=0,y=750)
        a=3
        


            







    at_name = Label(master = root,text=(convert('نام اتم اول را وارد کنید:')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red').place(x=0,y=0)

    at_name_ent = Entry(master=root,font=('Segoe Print',20,'bold'))
    at_name_ent.place(x=400,y=0)
    electron = Label(master = root,text=(convert(' تعداد الکترون های آخرین لایه اتم اول:')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red').place(x=0,y=150)
    electron_ent = Entry(master=root,font=('Segoe Print',20,'bold'))
    electron_ent.place(x=400,y=150)

    at_name2 = Label(master = root,text=(convert('نام اتم دوم را وارد کنید:')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red').place(x=0,y=300)
    at_name_ent2 = Entry(master=root,font=('Segoe Print',20,'bold'))
    at_name_ent2.place(x=400,y=300)
    electron2 = Label(master = root,text=(convert(' تعداد الکترون های آخرین لایه اتم دوم:')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red').place(x=0,y=450)
    electron_ent2 = Entry(master=root,font=('Segoe Print',20,'bold'))
    electron_ent2.place(x=400,y=450)
    sub_btn = Button(master = root,text=(convert('تایید')),font=('Segoe Print',20,'bold'),bg='green',fg='white',activebackground='white',activeforeground='green',command = ent_get).place(x=0,y=550)



    root.mainloop()
def arayeshh():
    def sound_play():
        
        pygame.mixer.init()  # مقداردهی اولیه میکسر pygame
        pygame.mixer.music.load("bib.mp3")  # بارگذاری فایل صوتی
        pygame.mixer.music.play()
    root = Toplevel()
    root.geometry('800x800')
    root.resizable(False,False)
    root.iconbitmap("icon.ico") 
    root.title('chemastry lesson')
    #backgroun setting

    image = Image.open('imagess\\wall2.jpg')
    image = image.resize((800,800))
    bg_image = ImageTk.PhotoImage(image)

    bg_lbl = Label(root, image=bg_image)
    bg_lbl.place(relheight=1,relwidth=1)

    def ent_get():
        sound_play()
        global num_list,name_lbl,bohr_lbl
        try:
            name_lbl.destroy()
        except:
            pass

        try:
            bohr_lbl.destroy()
        except:
            pass

        name_atom = at_name_ent.get()
        number_electrom = int(electron_ent.get())
        
        name_lbl = Label(master = root,text=(f'{name_atom}:'),font=('Segoe Print',30,'bold'),bg='white',fg='black')
        name_lbl.place(x=20,y=450)
        number2 = number_electrom
        dor = 1
        num_list = []
        while number2>0:
            new_num = (dor**2)*2
            if number2-new_num<0:
                new_num=number2
            number2-= new_num
            
            num_list.append(int(new_num))
            dor+=1
        num_list.append(number2)
        num_list.pop()

        num_unlist = ')'.join(str(x) for x in num_list)

        bohr_lbl =Label(master = root,text=(f'{num_unlist}'),font=('Segoe Print',30,'bold'),bg='white',fg='black')
        bohr_lbl.place(x=100,y=450)
        root2 = Tk()
        if (new_num in [1,2,3]):
            f_no_f = convert('فلز')
        elif (new_num in [5,6,7,8]):
            f_no_f = convert('نافلز')
        elif (new_num in [4]):
            f_no_f = convert('خنثی')
        else:
            f_no_f = convert('تعریف نشده')
        
        f_no_f_lbl = Label(master = root2,text=convert((f'فلز یا نافلز بودن عنصر:{convert(f_no_f)}')),font=('Segoe Print',20,'bold'),bg='white',fg='black')
        f_no_f_lbl.pack()
        e_zarfiat = Label(master = root2,text=convert((f'الکترون ظرفیت:{(new_num)}')),font=('Segoe Print',20,'bold'),bg='white',fg='black')
        e_zarfiat.pack()
        if (new_num in [1,2,3]):
            zarf_atom = new_num
        else:
            zarf_atom = 8-new_num
        atom_zarfiat = Label(master = root2,text=convert((f' اتم ظرفیت:{(zarf_atom)}')),font=('Segoe Print',20,'bold'),bg='white',fg='black')
        atom_zarfiat.pack()


        root2.mainloop()



    at_name = Label(master = root,text=(convert('نام اتم را وارد کنید:')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red').place(x=0,y=0)
    at_name_ent = Entry(master=root,font=('Segoe Print',20,'bold'))
    at_name_ent.place(x=400,y=0)
    electron = Label(master = root,text=(convert('تعداد الکترون ها را وارد کنید:')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red').place(x=0,y=150)
    electron_ent = Entry(master=root,font=('Segoe Print',20,'bold'))
    electron_ent.place(x=400,y=150)
    sub_btn = Button(master = root,text=(convert('تایید')),font=('Segoe Print',20,'bold'),bg='green',fg='white',activebackground='white',activeforeground='green',command = ent_get).place(x=250,y=350)



    name_atom = Entry(master= root,)
    root.mainloop()
def atomm():
    def sound_play():
        pygame.mixer.init()  # مقداردهی اولیه میکسر pygame
        pygame.mixer.music.load("bib.mp3")  # بارگذاری فایل صوتی
        pygame.mixer.music.play()
    global icon_label,backgr,icon_image_original,angle
        
    # root setting
    root = Toplevel()
    root.geometry('800x800')
    root.resizable(False, False)
    root.iconbitmap("icon.ico") 
    root.title('Chemistry Lesson')

    icon_image_original = Image.open('imagess\\atom.png').resize((300, 300))  # اندازه‌ش کوچیکه
    icon_photo = None  # عکس چرخیده‌ش
    icon_label = None  # لیبل اون عکس
    angle = 0  # زاویه برای چرخش


    # background image list
    photo_list = ['imagess\\atom1.jpg', 'imagess\\atom2.jpg','imagess\\atom3.png']
    backgr = 0  # global index for image

    # Load initial background
    image = Image.open(photo_list[backgr])
    image = image.resize((800, 800))
    bg_image = ImageTk.PhotoImage(image)

    bg_lbl = Label(root, image=bg_image)
    bg_lbl.place(relheight=1, relwidth=1)

    # Define navigation buttons first (but don't place them yet)
    next_btn = Button(root, text=">>", font=('Segoe Print', 20, 'bold'), bg='pink', fg='red', command=lambda: change_bg(1))
    pr_btn = Button(root, text="<<", font=('Segoe Print', 20, 'bold'), bg='pink', fg='red', command=lambda: change_bg(-1))

    # Function to update the background
    def update_background():
        global bg_image, icon_photo, icon_label, angle

        # عکس اصلی پس‌زمینه
        img = Image.open(photo_list[backgr])
        img = img.resize((800, 800))
        bg_image = ImageTk.PhotoImage(img)
        bg_lbl.config(image=bg_image)
        bg_lbl.image = bg_image

        # دکمه‌ها
        if backgr > 0:
            pr_btn.place(x=15, y=230, height=40, width=50)
        else:
            pr_btn.place_forget()

        if backgr < len(photo_list) - 1:
            next_btn.place(x=735, y=230, height=40, width=50)
        else:
            next_btn.place_forget()

        # 🔁 اگه عکس دوم بود، آیکن بچرخه بیاد
        if backgr == 2:
            if not icon_label:
                icon_label = Label(root, bg='white')
                icon_label.place(x=350, y=450)  # جای دلخواه
            rotate_icon()
        else:
            if icon_label:
                icon_label.destroy()
                icon_label = None

    def rotate_icon():
        global icon_image_original, icon_photo, icon_label, angle
        if backgr == 2 and icon_label:
            rotated = icon_image_original.rotate(angle)
            icon_photo = ImageTk.PhotoImage(rotated)
            icon_label.config(image=icon_photo)
            icon_label.image = icon_photo
            angle = (angle + 10) % 360
            root.after(100, rotate_icon)  # هر ۰.۱ ثانیه یک دور


    # Function to change image index
    def change_bg(step):
        sound_play()
        global backgr
        backgr += step
        backgr = max(0, min(backgr, len(photo_list) - 1))
        update_background()

    # Initial button setup
    update_background()

    # Start the main loop
    root.mainloop()

def fisaa():
    def sound_play():
        pygame.mixer.init()  # مقداردهی اولیه میکسر pygame
        pygame.mixer.music.load("bib.mp3")  # بارگذاری فایل صوتی
        pygame.mixer.music.play()
        
    #root setting
    root = Toplevel()
    root.geometry('800x800')
    root.resizable(False,False)
    root.iconbitmap("icon.ico") 
    root.title('window to knowledge')
    #backgroun setting

    image = Image.open('imagess\\wall7.jpg')
    image = image.resize((800,800))
    bg_image = ImageTk.PhotoImage(image)


    bg_lbl = Label(root, image=bg_image)
    bg_lbl.place(relheight=1,relwidth=1)



    def ent_get():
        sound_play()
        global result1,result2,result3,s,w
        cc = c_ent.get()
        aa = a_ent.get()
        bb = b_ent.get()
        try:
            w.place_forget()
            s.place_forget()
        except:
            pass
        if cc=='' and aa!='' and bb!='':
            result1 = ((int(aa)**2)+(int(bb)**2))**0.5
            w = Label(root, text=f'وتر مثلث: {result1}', font=('Segoe Print', 20, 'bold'), bg='white', fg='green')
            w.place(x=0, y=400)
            result2 = f'''
                        🔺 رابطه اصلی:
                            c^2 = a^2 + b^2
                        
                        🔺 از آنجایی که ما c را میخواهیم:
                            c = √(a^2 + b^2)

                        🔺 جایگذاری مقادیر:
                            c = √({aa}^2 + {bb}^2)

                        🔺 سپس:
                            c = √({int(aa)**2} + {int(bb)**2})

                        🔺در نهایت:
                            c = √({(int(aa)**2)+(int(bb)**2)})

                        🔺جواب پایانی:
                            c = {result1}
                        '''

            r2 = Tk()
            r2.geometry('900x900')
            
            r2.config(bg = 'white')
            
            result3 = Label(master=r2,
                            text=convert(result2),
                            font=('Segoe Print', 20, 'bold'),
                            bg='white',
                            fg='black',
                            justify='left',    # یا 'right' یا 'center'
                            anchor='center',       # بالا و چپ
                            )
            result3.pack()
            r2.mainloop()
            
            s=Label(master = r2,text= result2 ,font=('Segoe Print',20,'bold'),bg='white',fg='black')
            s.place(x=0,y=450)
            r2.mainloop()


        elif cc!='' and aa=='' and bb!='':
            result1 = ((int(cc)**2)-(int(bb)**2)) ** 0.5
            w = Label(root, text=f'ضلع غیر وتر اول : {result1}', font=('Segoe Print', 20, 'bold'), bg='white', fg='green')
            w.place(x=0, y=400)

            result2 = f'''
                        🔺 رابطه اصلی:
                            c^2 = a^2 + b^2
                            
                        🔺 از آنجا که ما a را میخواهیم:
                            a = √(c^2 - b^2)

                        🔺 جایگذاری مقادیر:
                            a = √({cc}^2 - {bb}^2)

                        🔺 سپس:
                            a = √({int(cc)**2} - {int(bb)**2})

                        🔺در نهایت:
                            a = √({(int(cc)**2)-(int(bb)**2)})

                        🔺جواب پایانی:
                            a = {result1}
                        '''

            r2 = Tk()
            r2.geometry('900x900')
            
            r2.config(bg = 'white')
            
            result3 = Label(master=r2,
                            text=convert(result2),
                            font=('Segoe Print', 20, 'bold'),
                            bg='white',
                            fg='black',
                            justify='left',    # یا 'right' یا 'center'
                            anchor='center',       # بالا و چپ
                            )
            result3.pack()
            
            s=Label(master = r2,text= result2 ,font=('Segoe Print',20,'bold'),bg='white',fg='black')
            s.place(x=0,y=450)
            r2.mainloop()


        elif cc!='' and aa!='' and bb=='':
            result1 = ((int(cc)**2)-(int(aa)**2))**0.5
            w = Label(root, text=f'ضلع غیر وتر دوم : {result1}', font=('Segoe Print', 20, 'bold'), bg='white', fg='green')
            w.place(x=0, y=400)

            result2 = f'''
                        🔺 رابطه اصلی:
                            c^2 = a^2 + b^2
                            
                        🔺 از آنجا که ما a را میخواهیم:
                            b = √(c^2 - a^2)

                        🔺 جایگذاری مقادیر:
                            b = √({cc}^2 - {aa}^2)

                        🔺 سپس:
                            b = √({int(cc)**2} - {int(aa)**2})

                        🔺در نهایت:
                            b = √({(int(cc)**2)-(int(aa)**2)})

                        🔺جواب پایانی:
                            b = {result1}
                        '''

            r2 = Tk()
            r2.geometry('900x900')
            
            r2.config(bg = 'white')
            
            result3 = Label(master=r2,
                            text=convert(result2),
                            font=('Segoe Print', 20, 'bold'),
                            bg='white',
                            fg='black',
                            justify='left',    # یا 'right' یا 'center'
                            anchor='center',       # بالا و چپ
                            )
            result3.pack()
            r2.mainloop()
            
            s=Label(master = r2,text= result2 ,font=('Segoe Print',20,'bold'),bg='white',fg='black')
            s.place(x=0,y=450)
            r2.mainloop()
        else:
            messagebox.showerror(message='اطلاعات نادرست یا ناکافی است!!!')




    Label(master = root,text=(convert(' مقدار هر یک را وارد کنید و مقدار خواسته شده را خالی بگذارید')) ,font=('Segoe Print',20,'bold'),bg='white',fg='green').place(x=0,y=0)

    c = Label(master = root,text=(convert('طول وتر:')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red').place(x=0,y=80)
    c_ent = Entry(master=root,font=('Segoe Print',20,'bold'))
    c_ent.place(x=400,y=80)
    a = Label(master = root,text=(convert(' طول ضلع غیر وتر اول:')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red').place(x=0,y=160)
    a_ent = Entry(master=root,font=('Segoe Print',20,'bold'))
    a_ent.place(x=400,y=160)

    b = Label(master = root,text=(convert('طول ضلع غیر وتر دوم:')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red').place(x=0,y=240)
    b_ent = Entry(master=root,font=('Segoe Print',20,'bold'))
    b_ent.place(x=400,y=240)


    sub_btn = Button(master = root,text=(convert('تایید')),font=('Segoe Print',20,'bold'),bg='green',fg='white',activebackground='white',activeforeground='green',command = ent_get).place(x=0,y=320)

    root.mainloop()
def jazrr():
    def sound_play():
        pygame.mixer.init()  # مقداردهی اولیه میکسر pygame
        pygame.mixer.music.load("bib.mp3")  # بارگذاری فایل صوتی
        pygame.mixer.music.play()
    #root setting
    root = Toplevel()
    root.geometry('800x800')
    root.resizable(False,False)
    root.iconbitmap("icon.ico") 
    root.title('window to knowledge')
    #backgroun setting

    image = Image.open('imagess\\wall7.jpg')
    image = image.resize((800,800))
    bg_image = ImageTk.PhotoImage(image)


    bg_lbl = Label(root, image=bg_image)
    bg_lbl.place(relheight=1,relwidth=1)



    def ent_get():
        sound_play()
        global lbl 
        try:
            lbl.place_forget()
        except:
            pass
        
        
            
        try:
            aa = int(ad_ent.get())
            tt = int(tav_ent.get())
            lbl = Label(root, text=f'جواب:{aa**(1/tt)}', font=('Segoe Print', 20, 'bold'), bg='white', fg='green')
            lbl.place(x=0, y=300)
        except:
            messagebox.showerror(message='اطلاعات ناکافی یا نادرست میباشد!!')
        
        


            







    ad = Label(master = root,text=(convert('عدد:')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red').place(x=0,y=0)
    ad_ent = Entry(master=root,font=('Segoe Print',20,'bold'))
    ad_ent.place(x=400,y=0)
    tav = Label(master = root,text=(convert('فرجه:')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red').place(x=0,y=80)
    tav_ent = Entry(master=root,font=('Segoe Print',20,'bold'))
    tav_ent.place(x=400,y=80)


    sub_btn = Button(master = root,text=(convert('تایید')),font=('Segoe Print',20,'bold'),bg='green',fg='white',activebackground='white',activeforeground='green',command = ent_get).place(x=0,y=160)


    root.mainloop()  # ایمپورت کتابخانه pygame برای پخش موسیقی
def tavann():
    def sound_play():
        pygame.mixer.init()  # مقداردهی اولیه میکسر pygame
        pygame.mixer.music.load("bib.mp3")  # بارگذاری فایل صوتی
        pygame.mixer.music.play()
        
    root = Toplevel()
    root.geometry('800x800')
    root.resizable(False,False)
    root.iconbitmap("icon.ico") 
    root.title('window to knowledge')
    #backgroun setting

    image = Image.open('imagess\\wall7.jpg')
    image = image.resize((800,800))
    bg_image = ImageTk.PhotoImage(image)


    bg_lbl = Label(root, image=bg_image)
    bg_lbl.place(relheight=1,relwidth=1)



    def ent_get():
        sound_play()
        global lbl
        try:
            lbl.place_forget()
        except:
            pass 
        
        
            
        try:
            aa = int(ad_ent.get())
            tt = int(tav_ent.get())
            lbl = Label(root, text=f'جواب:{aa**tt}', font=('Segoe Print', 20, 'bold'), bg='white', fg='green')
            lbl.place(x=0, y=300)
        except:
            messagebox.showerror(message='اطلاعات ناکافی یا نادرست میباشد!!')
        
        


            







    ad = Label(master = root,text=(convert('عدد:')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red').place(x=0,y=0)
    ad_ent = Entry(master=root,font=('Segoe Print',20,'bold'))
    ad_ent.place(x=400,y=0)
    tav = Label(master = root,text=(convert('به توان:')) ,font=('Segoe Print',20,'bold'),bg='white',fg='red').place(x=0,y=80)
    tav_ent = Entry(master=root,font=('Segoe Print',20,'bold'))
    tav_ent.place(x=400,y=80)


    sub_btn = Button(master = root,text=(convert('تایید')),font=('Segoe Print',20,'bold'),bg='green',fg='white',activebackground='white',activeforeground='green',command = ent_get).place(x=0,y=160)


    root.mainloop()




# ---------------------------------------------------------------------------------
def riazii():
    def sound_play():
        pygame.mixer.init()  # مقداردهی اولیه میکسر pygame
        pygame.mixer.music.load("bib.mp3")  # بارگذاری فایل صوتی
        pygame.mixer.music.play()
        
    root = Toplevel()
    root.geometry('800x800')
    root.resizable(False,False)
    root.title('Math lesson')
    root.iconbitmap("icon.ico") 
    #backgroun setting

    image = Image.open('imagess\\yellow.jpg')
    image = image.resize((800,800))
    bg_image = ImageTk.PhotoImage(image)

    bg_lbl = Label(root, image=bg_image)
    bg_lbl.place(relheight=1,relwidth=1)


    def tavv():
        
        sound_play()
        tavann()

    def jazr():

        sound_play()
        jazrr()

    def fisa():

        sound_play()
        fisaa()
    # moadele = Button(root,bg='#C1C8F5',activeforeground='#C1C8F5',fg='#656980',activebackground='#656980' ,command= chimi , text=convert('معادله'),font=('Segoe Print',20,'bold')).place(x=250,y=20)
    tavan = Button(root,bg='#F5ACA6',activeforeground='#F5ACA6',fg='#80322D',activebackground='#80322D' ,command= tavv , text=convert('توان  '),font=('Segoe Print',20,'bold')).place(x=250,y=20)
    jazzr = Button(root,bg='#B0F4BC',activeforeground='#B0F4BC',fg='#5C8063',activebackground='#5C8063' ,command= jazr , text=convert('جذر'),font=('Segoe Print',20,'bold')).place(x=250,y=170)
    fisagores = Button(root,bg='#A4EBD6',activeforeground='#A4EBD6',fg='#3E5850',activebackground='#3E5850' ,command= fisa , text=convert('فیثاغورس'),font=('Segoe Print',20,'bold')).place(x=250,y=320)
    # dayere = Button(root,bg='#EAE88D',activeforeground='#EAE88D',fg='#767547',activebackground='#767547' ,command= chimi , text=convert('دایره ها'),font=('Segoe Print',20,'bold')).place(x=250,y=470)


    root.mainloop()
def chemm():
    def sound_play():
        
        pygame.mixer.init()  # مقداردهی اولیه میکسر pygame
        pygame.mixer.music.load("bib.mp3")  # بارگذاری فایل صوتی
        pygame.mixer.music.play()
        
    #root setting
    root = Toplevel()
    root.geometry('800x800')
    root.resizable(False,False)
    root.iconbitmap("icon.ico") 
    root.title('chemastry lesson')
    #backgroun setting

    image = Image.open('imagess\\wall2.jpg')
    image = image.resize((800,800))
    bg_image = ImageTk.PhotoImage(image)

    bg_lbl = Label(root, image=bg_image)
    bg_lbl.place(relheight=1,relwidth=1)

    def atom():

        sound_play()
        atomm()

    def arayesh():

        sound_play()
        arayeshh()
   
    def nogte_i():

        sound_play()
        nogte_ii()
    

    atom = Button(root,bg='#C1C8F5',activeforeground='#C1C8F5',fg='#656980',activebackground='#656980' ,command= atom , text=convert('ریز ترین ذرات تشکیل دهنده مواد'),font=('Segoe Print',20,'bold')).place(x=250,y=20)
    arayesh = Button(root,bg='#F5ACA6',activeforeground='#F5ACA6',fg='#80322D',activebackground='#80322D' ,command= arayesh , text=convert('  آرایش الکترونی به روش بور  '),font=('Segoe Print',20,'bold')).place(x=250,y=170)
    electro_dot = Button(root,bg='#B0F4BC',activeforeground='#B0F4BC',fg='#5C8063',activebackground='#5C8063' ,command= nogte_i , text=convert('  مدل الکترو نقطه ای اتم ها    '),font=('Segoe Print',20,'bold')).place(x=250,y=320)
    # vaconesh = Button(root,bg='#A4EBD6',activeforeground='#A4EBD6',fg='#3E5850',activebackground='#3E5850' ,command= movazene , text=convert('       موازنه ی واکنش ها     '),font=('Segoe Print',20,'bold')).place(x=250,y=470)

    root.mainloop()

# import the mudols

def fizikk():
    def sound_play():
        pygame.mixer.init()  # مقداردهی اولیه میکسر pygame
        pygame.mixer.music.load("bib.mp3")  # بارگذاری فایل صوتی
        pygame.mixer.music.play()
        
    #root setting
    root = Toplevel()
    root.geometry('800x800')
    root.resizable(False,False)
    root.iconbitmap("icon.ico") 
    root.title('lesson')
    #backgroun setting

    image = Image.open('imagess\\wall4.jpg')
    image = image.resize((800,800))
    bg_image = ImageTk.PhotoImage(image)

    bg_lbl = Label(root, image=bg_image)
    bg_lbl.place(relheight=1,relwidth=1)

    def adasi():

        sound_play()
        adasii()

    def cool():

        sound_play()
        coll()

    def eleec():

        sound_play()
        elecc()

    def motegatte():

        sound_play()
        motegatee()

    def aiine():

        sound_play()
        ainee()
    colon = Button(root,bg='#C1C8F5',activeforeground='#C1C8F5',fg='#656980',activebackground='#656980' ,command= cool , text=convert('مسائل کولن'),font=('Segoe Print',20,'bold')).place(x=150,y=220)
    elecctric = Button(root,bg='#F5ACA6',activeforeground='#F5ACA6',fg='#80322D',activebackground='#80322D' ,command= eleec , text=convert('جریان الکتریکی'),font=('Segoe Print',20,'bold')).place(x=550,y=220)
    moteggate = Button(root,bg='#B0F4BC',activeforeground='#B0F4BC',fg='#5C8063',activebackground='#5C8063' ,command= motegatte , text=convert('آینه های متقاطع'),font=('Segoe Print',20,'bold')).place(x=150,y=400)
    ainne = Button(root,bg='#A4EBD6',activeforeground='#A4EBD6',fg='#3E5850',activebackground='#3E5850' ,command= aiine , text=convert('آینه ها'),font=('Segoe Print',20,'bold')).place(x=550,y=400)
    adasiii = Button(root,bg='#EAE88D',activeforeground='#EAE88D',fg='#767547',activebackground='#767547' ,command= adasi , text=convert('عدسی ها'),font=('Segoe Print',20,'bold')).place(x=350,y=580)


    root.mainloop()
#root setting
def mainn():
    root = Tk()
    root.geometry('800x800')
    root.resizable(False,False)
    root.iconbitmap("icon.ico") 
    root.title('window to knowledge')
    def sound_play():
        pygame.mixer.init()  # مقداردهی اولیه میکسر pygame
        pygame.mixer.music.load("bib.mp3")  # بارگذاری فایل صوتی
        pygame.mixer.music.play()
    #backgroun setting

    image = Image.open('imagess\\wall1.jpg')
    image = image.resize((800,800))
    bg_image = ImageTk.PhotoImage(image)

    bg_lbl = Label(root, image=bg_image)
    bg_lbl.place(relheight=1,relwidth=1)

    def chimi():
        sound_play()
        chemm()

    def fizik():

        sound_play()
        fizikk()

    def riazi():

        sound_play()
        riazii()
    chimi_btn = Button(root,bg='#C1C8F5',activeforeground='#C1C8F5',fg='#656980',activebackground='#656980' ,command= chimi , text='                                شیمی                                  ',font=('Segoe Print',20,'bold')).place(x=1,y=20)
    fizik_btn = Button(root,bg='#F5ACA6',activeforeground='#F5ACA6',fg='#80322D',activebackground='#80322D' ,command= fizik , text='                                فیزیک                                 ',font=('Segoe Print',20,'bold')).place(x=1,y=120)
    riaz_btn = Button(root,bg='#B0F4BC',activeforeground='#B0F4BC',fg='#5C8063',activebackground='#5C8063' ,command= riazi , text='                                 ریاضی                                ',font=('Segoe Print',20,'bold')).place(x=1,y=220)


    root.mainloop()
if __name__ == "__main__":
    mainn()