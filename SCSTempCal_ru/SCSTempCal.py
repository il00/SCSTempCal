# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import messagebox
from tkinter import filedialog as fd
from sys import exit
import numpy as np
import os
import glob
import matplotlib.pyplot as plt


class Option_Menu():
    dict_menu = {'-': '-', 'Окислитель (Ox)': 'Ox', 'Топливо (F)': 'F', 'Целевой продукт (Ob)': 'Ob'}

    def __init__(self, master, value=('-', 'Окислитель (Ox)', 'Топливо (F)'), name='example', default=0, **kw):
        self.master = master
        self.value = value
        self.default = default
        self.max = len(value)
        self.name = name
        self.lab = Label(master, text=str(value[default]), **kw)
        self.menu = Menu(tearoff=0)
        for i, txt in enumerate(value):
            self.menu.add_command(label=txt, command=lambda num=int(i), value=value: self.remap_default(num, value))
        self.relief()
        self.lab['text'] = '-'

    def func(self, event):
        self.menu.post(event.x_root, event.y_root)

    def remap_default(self, num, value):
        def root_geometry_remap():
            s = root.geometry().split('+')
            root_g = s[0].split('x')
            if (3 in fi_list) or (4 in fi_list):
                root.geometry('910x{}'.format(root_g[1]))
            else:
                if (1 in fi_list) or (2 in fi_list):
                    root.geometry('700x{}'.format(root_g[1]))
                else:
                    root.geometry('500x{}'.format(root_g[1]))

        def checkbutton_move():
            global cbtn_log, cbtn_1, cbtn_2
            if cbtn_log:
                cbtn_1.destroy()
                cbtn_2.destroy()
                cbtn_log = False
            if len(fi_list) > 0:
                if 3 in fi_list or 4 in fi_list:
                    d1 = 615
                else:
                    d1 = 510
                if 2 in fi_list or 4 in fi_list:
                    d2 = 490
                else:
                    d2 = 240
                cbtn_1 = Checkbutton(text="Показать график", font="Arial 12", variable=cbtnvar_1, onvalue=1, offvalue=0)
                cbtn_1.place(x=d1, y=d2)
                cbtn_2 = Checkbutton(text="Показать таблицу", font="Arial 12", variable=cbtnvar_2, onvalue=1, offvalue=0)
                cbtn_2.place(x=d1, y=d2 + 20)
                cbtn_log = True

        def add_fi(i):
            if i == 1:
                xi, yi = 0, 0
            elif i == 2:
                xi, yi = 0, 1
            elif i == 3:
                xi, yi = 1, 0
            elif i == 4:
                xi, yi = 1, 1
            root_geometry_remap()
            checkbutton_move()

            globals()['fi_{}'.format(i)] = Entry(width=12, font="Arial 12")
            globals()['fi_{}'.format(i)].place(x=580+210*xi, y=39+250*yi)
            globals()['fi_{}'.format(i)].insert(0, 1)

            globals()['label{}_fi'.format(i)] = Label(text='φ{}'.format(i), font="Arial 12", justify=LEFT)
            globals()['label{}_fi'.format(i)].place(x=510+210*xi, y=36+250*yi)
            globals()['label{}_ra'.format(i)] = Label(text='Серия расчетов:', font="Arial 12", justify=LEFT)
            globals()['label{}_ra'.format(i)].place(x=530+210*xi, y=95+250*yi)
            globals()['label{}_st'.format(i)] = Label(text='φ{}(нач.)'.format(i), font="Arial 12", justify=LEFT)
            globals()['label{}_st'.format(i)].place(x=510+210*xi, y=120+250*yi)
            globals()['label{}_fn'.format(i)] = Label(text='φ{}(кон.)'.format(i), font="Arial 12", justify=LEFT)
            globals()['label{}_fn'.format(i)].place(x=510+210*xi, y=146+250*yi)
            globals()['label{}_sp'.format(i)] = Label(text='шаг', font="Arial 12", justify=LEFT)
            globals()['label{}_sp'.format(i)].place(x=510+210*xi, y=172+250*yi)

            globals()['entry{}_st'.format(i)] = Entry(width=12, font="Arial 12")
            globals()['entry{}_st'.format(i)].place(x=580+210*xi, y=123+250*yi)
            globals()['entry{}_st'.format(i)].insert(0, 0.5)
            globals()['entry{}_fn'.format(i)] = Entry(width=12, font="Arial 12")
            globals()['entry{}_fn'.format(i)].place(x=580+210*xi, y=148+250*yi)
            globals()['entry{}_fn'.format(i)].insert(0, 1.5)
            globals()['entry{}_sp'.format(i)] = Entry(width=12, font="Arial 12")
            globals()['entry{}_sp'.format(i)].place(x=580+210*xi, y=174+250*yi)
            globals()['entry{}_sp'.format(i)].insert(0, 0.1)

            globals()['btn_mem_{}'.format(i)] = Button(text="Запомнить φ{}".format(i), background="#555",
                                                       foreground="#ccc", padx="20", pady="8", font="7",
                                                       command=lambda: click_button_mem(i))
            globals()['btn_mem_{}'.format(i)].place(x=580 + 210 * xi, y=20 + 250 * yi, anchor="c", height=30, width=135,
                                                    bordermode=OUTSIDE)
            globals()['btn_ref_{}'.format(i)] = Button(text="Обновить F{}".format(i), background="#555",
                                                       foreground="#ccc", padx="20", pady="8", font="7",
                                                       command=lambda: click_button_fi(i))
            globals()['btn_ref_{}'.format(i)].place(x=580 + 210 * xi, y=80 + 250 * yi, anchor="c", height=30, width=135,
                                                    bordermode=OUTSIDE)
            globals()['btn_ra_{}'.format(i)] = Button(text="Диапазон φ{}".format(i), background="#555",
                                                      foreground="#ccc", padx="20", pady="8", font="7",
                                                      command=lambda: click_button_range(i))
            globals()['btn_ra_{}'.format(i)].place(x=580 + 210 * xi, y=215 + 250 * yi, anchor="c", height=30, width=135,
                                                   bordermode=OUTSIDE)

        def del_fi(i):
            globals()['fi_{}'.format(i)].destroy()
            globals()['label{}_fi'.format(i)].destroy()
            globals()['label{}_ra'.format(i)].destroy()
            globals()['label{}_st'.format(i)].destroy()
            globals()['label{}_fn'.format(i)].destroy()
            globals()['label{}_sp'.format(i)].destroy()
            globals()['entry{}_st'.format(i)].destroy()
            globals()['entry{}_fn'.format(i)].destroy()
            globals()['entry{}_sp'.format(i)].destroy()
            globals()['btn_mem_{}'.format(i)].destroy()
            globals()['btn_ref_{}'.format(i)].destroy()
            globals()['btn_ra_{}'.format(i)].destroy()
            root_geometry_remap()
            checkbutton_move()

        self.default = num
        if value[num] == '-':
            if self.name[0] == 'r':
                if self.lab['text'][0] == 'F':
                    fi_list.remove(int(self.lab['text'][1:]))
                    del_fi(int(self.lab['text'][1:]))
                globals()['reag_{}'.format(self.opt_num)].config(background="#FFFFFF")
            else:
                globals()['prod_{}'.format(self.opt_num)].config(background="#FFFFFF")
            self.lab['text'] = '-'
        elif value[num] == 'Окислитель (Ox)':
            if self.lab['text'][0] == 'F':
                fi_list.remove(int(self.lab['text'][1:]))
                del_fi(int(self.lab['text'][1:]))
            self.lab['text'] = 'Ox'
            globals()['reag_{}'.format(self.opt_num)].config(background="#F0F8FF")
        elif value[num] == 'Топливо (F)':
            if self.lab['text'][0] != 'F':
                i = 1
                while i in fi_list:
                    i += 1
                if i < 5:
                    fi_list.append(i)
                    self.lab["text"] = 'F{}'.format(i)
                    globals()['reag_{}'.format(self.opt_num)].config(background="#FFF0F5")
                    add_fi(i)
                else:
                    messagebox.showwarning('Внимание!', 'Превышено максимальное количество различных видов топлива')
        elif value[num] == 'Целевой продукт (Ob)':
            self.lab['text'] = 'Ob'
            globals()['prod_{}'.format(self.opt_num)].config(background="#F0FFF0")
        print(fi_list)

    def relief(self, rel1=FLAT, rel2=RIDGE):
        self.lab.bind("<Leave>", lambda event: self.config(relief=rel1))
        self.lab.bind("<Enter>", lambda event: self.config(relief=rel2))
        self.lab.bind("<ButtonPress>", lambda event: self.config(relief=SUNKEN))
        self.lab.bind("<ButtonRelease>", self.func)

    def pack(self, cnf={}, **kw):
        self.lab.pack(cnf, **kw)

    def place(self, cnf={}, **kw):
        self.lab.place(cnf, **kw)

    def config(self, cnf=None, **kw):
        self.lab.config(cnf, **kw)

    def destroy(self):
        self.lab.destroy()

    configure = config


def isnotfloat(value):
    try:
        float(value)
        return False
    except ValueError:
        return True


def ch_dist():
    '''пересчет координат y объектов при добавлении/удалении полей ввода'''
    global num_str
    dist = 25 * (num_str - 5)
    btn_p.place(y=167 + dist)
    btn_m.place(y=167 + dist)
    btn_u.place(y=177 + dist)
    btn_ns.place(y=177 + dist)
    label5.place(y=205 + dist)
    label6.place(y=230 + dist)
    label7.place(y=255 + dist)
    label8.place(y=280 + dist)
    label9.place(y=305 + dist)
    label10.place(y=410 + dist)
    label11.place(y=435 + dist)
    label12.place(y=460 + dist)
    label13.place(y=485 + dist)
    label14.place(y=510 + dist)
    label15.place(y=535 + dist)
    label16.place(y=560 + dist)
    label17.place(y=585 + dist)
    label18.place(y=610 + dist)
    label19.place(y=635 + dist)
    label20.place(y=660 + dist)
    label21.place(y=685 + dist)
    ltemp.place(y=330 + dist)
    mass.place(y=205 + dist)
    area.place(y=230 + dist)
    ftime.place(y=255 + dist)
    tig.place(y=280 + dist)
    nh2o.place(y=305 + dist)
    etemp.place(y=330 + dist)
    btn_1.place(y=380 + dist)
    btn_2.place(y=380 + dist)
    btn_3.place(y=380 + dist)


def click_button_p():
    '''добавление полей ввода реагентов'''
    global num_str
    dist = 25 * (num_str - 4)
    num_str += 1
    globals()['reag_{}o'.format(num_str)] = Option_Menu(root, cursor='hand2', relief=RIDGE, name='reag_{}o'.format(num_str))
    globals()['reag_{}o'.format(num_str)].opt_num = num_str
    globals()['reag_{}o'.format(num_str)].relief(RIDGE, RAISED)
    globals()['reag_{}o'.format(num_str)].place(x=10, y=35 + 25 * (num_str - 1))
    globals()['reag_{}'.format(num_str)] = Entry(width=15, font="Arial 12")
    globals()['reag_{}'.format(num_str)].place(x=32, y=35 + 25 * (num_str - 1))
    globals()['reag_{}k'.format(num_str)] = Entry(width=5, font="Arial 12")
    globals()['reag_{}k'.format(num_str)].place(x=180, y=35 + 25 * (num_str - 1))
    globals()['prod_{}'.format(num_str)] = Entry(width=15, font="Arial 12")
    globals()['prod_{}o'.format(num_str)] = Option_Menu(root, cursor='hand2', relief=RIDGE, name='prod_{}o'.format(num_str), value=('-', 'Целевой продукт (Ob)'))
    globals()['prod_{}o'.format(num_str)].opt_num = num_str
    globals()['prod_{}o'.format(num_str)].relief(RIDGE, RAISED)
    globals()['prod_{}o'.format(num_str)].place(x=260, y=35 + 25 * (num_str - 1))
    globals()['prod_{}'.format(num_str)] = Entry(width=15, font="Arial 12")
    globals()['prod_{}'.format(num_str)].place(x=282, y=35 + 25 * (num_str - 1))
    globals()['prod_{}k'.format(num_str)] = Entry(width=5, font="Arial 12")
    globals()['prod_{}k'.format(num_str)].place(x=430, y=35 + 25 * (num_str - 1))
    ch_dist()
    s = root.geometry().split('+')
    root_g = s[0].split('x')
    root.geometry('{}x{}'.format(root_g[0], 720 + dist))


def click_button_m():
    '''удаление полей ввода реагентов'''
    global num_str, fi_list, cbtn_log, cbtn_1, cbtn_2
    if num_str > 3:
        dist = 25 * (num_str - 6)
        if globals()['reag_{}o'.format(num_str)].lab['text'][0] == 'F':
            ii = int(globals()['reag_{}o'.format(num_str)].lab['text'][1:])
            fi_list.remove(ii)
            globals()['fi_{}'.format(ii)].destroy()
            globals()['label{}_fi'.format(ii)].destroy()
            globals()['label{}_ra'.format(ii)].destroy()
            globals()['label{}_st'.format(ii)].destroy()
            globals()['label{}_fn'.format(ii)].destroy()
            globals()['label{}_sp'.format(ii)].destroy()
            globals()['entry{}_st'.format(ii)].destroy()
            globals()['entry{}_fn'.format(ii)].destroy()
            globals()['entry{}_sp'.format(ii)].destroy()
            globals()['btn_mem_{}'.format(ii)].destroy()
            globals()['btn_ref_{}'.format(ii)].destroy()
            globals()['btn_ra_{}'.format(ii)].destroy()
            if (3 in fi_list) or (4 in fi_list):
                root.geometry('910x{}'.format(720 + dist))
                print('910')
            else:
                if (1 in fi_list) or (2 in fi_list):
                    root.geometry('700x{}'.format(720 + dist))
                    print('700')
                else:
                    root.geometry('500x{}'.format(720 + dist))
                    print('500')
            if cbtn_log:
                cbtn_1.destroy()
                cbtn_2.destroy()
                cbtn_log = False
            if len(fi_list) > 0:
                if 3 in fi_list or 4 in fi_list:
                    d1 = 615
                else:
                    d1 = 510
                if 2 in fi_list or 4 in fi_list:
                    d2 = 490
                else:
                    d2 = 240
                cbtn_1 = Checkbutton(text="Показать график", font="Arial 12", variable=cbtnvar_1, onvalue=1, offvalue=0)
                cbtn_1.place(x=d1, y=d2)
                cbtn_2 = Checkbutton(text="Показать таблицу", font="Arial 12", variable=cbtnvar_2, onvalue=1,
                                     offvalue=0)
                cbtn_2.place(x=d1, y=d2 + 20)
                cbtn_log = True
        else:
            s = root.geometry().split('+')
            root_g = s[0].split('x')
            root.geometry('{}x{}'.format(root_g[0], 720 + dist))
        globals()['reag_{}o'.format(num_str)].destroy()
        globals()['reag_{}'.format(num_str)].destroy()
        globals()['reag_{}k'.format(num_str)].destroy()
        globals()['prod_{}o'.format(num_str)].destroy()
        globals()['prod_{}'.format(num_str)].destroy()
        globals()['prod_{}k'.format(num_str)].destroy()
        num_str -= 1
        ch_dist()


def click_button_3(q=5):
    '''считывание данных и алгоритм подсчета T'''
    global num_str, range_temp, etemp, log_range
    all_right = True
    string = 'Максимальная температура горения:'
    label11.config(text=string)
    label14.config(text=string)
    label17.config(text=string)
    label20.config(text=string)
    string = 'Температурный эффект:'
    label12.config(text=string)
    label15.config(text=string)
    label18.config(text=string)
    label21.config(text=string)
    i = 1
    reag_list = []
    prod_list = []
    while i <= num_str:
        if globals()['reag_{}'.format(i)].get() != '':
            if isnotfloat(globals()['reag_{}k'.format(i)].get()) is False:
                reag_list.append([globals()['reag_{}'.format(i)].get(),
                                  float(globals()['reag_{}k'.format(i)].get()), globals()['reag_{}o'.format(i)].lab['text']])
            else:
                messagebox.showerror('Ошибка', 'Коэффициент реагента {} указан некорректно'.format(i))
                all_right = False

        elif (globals()['reag_{}'.format(i)].get() == '') and (globals()['reag_{}k'.format(i)].get() != ''):
            messagebox.showerror('Ошибка', 'Реагент {} отсутствует'.format(i))
            all_right = False

        if globals()['prod_{}'.format(i)].get() != '':
            if isnotfloat(globals()['prod_{}k'.format(i)].get()) is False:
                prod_list.append([globals()['prod_{}'.format(i)].get(),
                                  float(globals()['prod_{}k'.format(i)].get()), globals()['prod_{}o'.format(i)].lab['text']])
            else:
                messagebox.showerror('Ошибка', 'Коэффициент продукта {} указан некорректно'.format(i))
                all_right = False
        elif (globals()['prod_{}'.format(i)].get() == '') and (globals()['prod_{}k'.format(i)].get() != ''):
            messagebox.showerror('Ошибка', 'Продукт {} отсутствует'.format(i))
            all_right = False
        i += 1

    try:
        klib = open("substance_library.txt", "r")
    except FileNotFoundError:
        messagebox.showerror("Ошибка", "Файл substance_library.txt отсутствует")
        all_right = False
    else:
        klib.close()
        reag_lib = []
        prod_lib = []
        for elem in reag_list:
            klib = open("substance_library.txt", "r")
            for line in klib:
                if line[0] != '#':
                    spl_string = line.split()
                    if len(spl_string) == 0:
                        continue
                    if spl_string[0] == elem[0]:
                        reag_lib.append([spl_string[0], spl_string[1], spl_string[2], float(spl_string[3]),
                                         float(spl_string[4]), spl_string[5], spl_string[6], spl_string[7], elem[1], 298])
                        elem.append(True)
                        break
            klib.close()
            if len(elem) == 3:
                messagebox.showerror("Ошибка", "Реагент {} не найден в базе substance_library.txt".format(elem[0]))
                all_right = False
        for elem in prod_list:
            klib = open("substance_library.txt", "r")
            for line in klib:
                if line[0] != '#':
                    spl_string = line.split()
                    if len(spl_string) == 0:
                        continue
                    if spl_string[0] == elem[0]:
                        prod_lib.append([spl_string[0], spl_string[1], spl_string[2], float(spl_string[3]),
                                         float(spl_string[4]), spl_string[5], spl_string[6], spl_string[7], elem[1], 298])
                        elem.append(True)
                        break
            klib.close()
            if len(elem) == 3:
                messagebox.showerror("Ошибка", "Реагент {} не найден в базе substance_library.txt".format(elem[0]))
                all_right = False

    if isnotfloat(mass.get()):
        messagebox.showerror("Ошибка", "Значение массы целевого продукта введено некорректно")
        all_right = False
    if isnotfloat(area.get()):
        messagebox.showerror("Ошибка", "Значение площади введено некорректно")
        all_right = False
    if isnotfloat(ftime.get()):
        messagebox.showerror("Ошибка", "Значение времени горения введено некорректно")
        all_right = False
    if isnotfloat(tig.get()):
        messagebox.showerror("Ошибка", "Значение температуры возгорания введено некорректно")
        all_right = False
    if isnotfloat(nh2o.get()):
        messagebox.showerror("Ошибка", "Значение количества кристаллогидратной воды введено некорректно")
        all_right = False
    if isnotfloat(etemp.get()):
        messagebox.showerror("Ошибка", "Верхняя граница температурного интервала дожна быть числом")
        all_right = False
    elif float(etemp.get()) < 298:
        messagebox.showerror("Ошибка", "Верхняя граница температурного интервала не может быть меньше 298 K")
        all_right = False
    ob_list = []
    for elem in prod_list:
        if elem[2] == 'Ob':
            ob_list.append(elem)
    if len(ob_list) == 0:
        messagebox.showerror("Ошибка", "Не задано ни одного целевого продукта. Определение количества вещества невозможно.")
        all_right = False

    if all_right:
        if log_range:
            out_file = open("output_{}_{}.txt".format(q, globals()['fi_{}'.format(q)].get()), "w")
        else:
            for f in glob.glob('output*.txt'):
                os.remove(f)
            out_file = open("output.txt", "w")
        out_file.write('Введенные данные\n')
        out_file.write('Реагенты:\n')
        out_cp = open('out_cp.txt', 'w')                   # файл для записи Cp = f(T) компонентов
        out_dh = open('out_dh.txt', 'w')                   # файл для записи dH = f(T) компонентов
        out_cp.write('Температурные зависимости теплоемкостей\n')
        out_dh.write('Температурные зависимости энтальпий\n')
        string_2 = '  T       '
        for elem in reag_list:
            string = str(elem[0]) + ' ' + str(elem[1]) + '\n'
            out_file.write(string)
            string_2 = string_2 + '{:<17}'.format(elem[0])
        out_file.write('Продукты:\n')
        for elem in prod_list:
            string = str(elem[0]) + ' ' + str(elem[1]) + '\n'
            out_file.write(string)
            string_2 = string_2 + '{:<17}'.format(elem[0])
        string_2 = string_2 + '\n'
        out_cp.write(string_2)
        out_dh.write(string_2)
        string = 'Масса целевого продукта, г: ' + mass.get() + '\n'
        out_file.write(string)
        string = 'Площадь излучающей поверхности, м^2: ' + area.get() + '\n'
        out_file.write(string)
        string = 'Время горения, с: ' + ftime.get() + '\n'
        out_file.write(string)
        string = 'Температура возгорания, K: ' + tig.get() + '\n'
        out_file.write(string)
        string = 'Количество воды в кристаллогидрате: ' + nh2o.get() + '\n'
        out_file.write(string)
        out_file.write('Запуск расчетов\n')
        out_file.write('  T, K    Cp(реаг)   Cp(прод)    dH(реаг)     dH(прод)        Q          Cp*dT       A          delta       delta*n      rad       Итог \n')
        delta_3 = 1
        delta_4 = 1
        delta_5 = 1

        mol_v = 0  # молярная масса продукта
        for el in ob_list:
            mol_el = 0
            klib = open("substance_library.txt", "r")
            for line in klib:
                if line[0] != '#':
                    spl_string = line.split()
                    if len(spl_string) == 0:
                        continue
                    if spl_string[0] == el[0]:
                        ind_k = 0
                        while ind_k < (len(spl_string) - 8) / 2:
                            mol_el = mol_el + molar_mass.get(spl_string[2 * ind_k + 8]) * float(spl_string[2 * ind_k + 9])
                            ind_k += 1
                        mol_v = mol_v + mol_el * el[1]
                        break
            klib.close()
            print('M_tot ', mol_v, 'M_el', mol_el)  # del

        max_temp_2, max_temp_3, max_temp_4 = 'не определено', 'не определено', 'не определено'
        max_dtemp_2, max_dtemp_3, max_dtemp_4 = 'не определено', 'не определено', 'не определено'
        temp = 298
        maxima_temp = float(etemp.get())
        while temp < maxima_temp:
            cp_p = 0
            cp_r = 0
            dh_p = 0
            dh_r = 0
            n_r = 0
            n_p = 0
            cp_dt = 0
            string_2 = '{:<10}'.format(temp)
            string_3 = '{:<10}'.format(temp)
            for elem in reag_lib:
                cp_ri = float(elem[5]) + float(elem[6]) * temp / 1000 - float(elem[7]) * 10**5 / (temp**2)
                if elem[3] < cp_ri:
                    cp_ri = elem[3]
                    if temp < float(tig.get()):
                        dh_ri = elem[4] * 1000 + float(elem[5]) * (elem[-1] - 298) + float(elem[6]) * (elem[-1] ** 2 - 298 ** 2) / 2000 + float(elem[7]) * 10**5 * (1 / elem[-1] - 1 / 298)
                        dh_ri = dh_ri + elem[3] * (temp - elem[-1])
                    else:
                        if elem[-1] <= float(tig.get()):
                            dh_ri = elem[4] * 1000 + float(elem[5]) * (elem[-1] - 298) + float(elem[6]) * (elem[-1] ** 2 - 298 ** 2) / 2000 + float(elem[7]) * 10 ** 5 * (1 / elem[-1] - 1 / 298)
                            dh_ri = dh_ri + elem[3] * (float(tig.get()) - elem[-1])
                        else:
                            dh_ri = elem[4] * 1000 + float(elem[5]) * (float(tig.get()) - 298) + float(elem[6]) * (float(tig.get()) ** 2 - 298 ** 2) / 2000 + float(elem[7]) * 10 ** 5 * (1 / float(tig.get()) - 1 / 298)
                else:
                    elem[-1] = temp
                    if temp < float(tig.get()):
                        dh_ri = elem[4] * 1000 + float(elem[5]) * (temp - 298) + float(elem[6]) * (temp ** 2 - 298 ** 2) / 2000 + float(elem[7]) * 10**5 * (1 / temp - 1 / 298)
                    else:
                        dh_ri = elem[4] * 1000 + float(elem[5]) * (float(tig.get()) - 298) + float(elem[6]) * (float(tig.get()) ** 2 - 298 ** 2) / 2000 + float(elem[7]) * 10 ** 5 * (1 / float(tig.get()) - 1 / 298)
                if elem[2] == 'g':
                    n_r = n_r + elem[8]
                cp_r = cp_r + cp_ri * elem[8]
                dh_r = dh_r + dh_ri * elem[8]
                string_2 = string_2 + '{0:<17.6f}'.format(cp_ri)
                string_3 = string_3 + '{0:<17.6f}'.format(dh_ri)
                if temp == 298:
                    dh_rs = dh_r
            for elem in prod_lib:
                cp_pi = float(elem[5]) + float(elem[6]) * temp / 1000 - float(elem[7]) * 10**5 / (temp**2)
                if elem[3] < cp_pi:
                    cp_pi = elem[3]
                    dh_pi = elem[4] * 1000 + float(elem[5]) * (elem[-1] - 298) + float(elem[6]) * (elem[-1] ** 2 - 298 ** 2) / 2000 + float(elem[7]) * 10 ** 5 * (1 / elem[-1] - 1 / 298)
                    dh_pi = dh_pi + elem[3] * (temp - elem[-1])
                    cp_dti = float(elem[5]) * (elem[-1] - float(tig.get())) + float(elem[6]) * (elem[-1] ** 2 - float(tig.get()) ** 2) / 2000 + float(elem[7]) * 10 ** 5 * (1 / elem[-1] - 1 / float(tig.get()))
                    cp_dti = cp_dti + elem[3] * (temp - elem[-1])
                else:
                    elem[-1] = temp
                    dh_pi = elem[4] * 1000 + float(elem[5]) * (temp - 298) + float(elem[6]) * (temp ** 2 - 298 ** 2) / 2000 + float(elem[7]) * 10 ** 5 * (1 / temp - 1 / 298)
                    cp_dti = float(elem[5]) * (temp - float(tig.get())) + float(elem[6]) * (temp ** 2 - float(tig.get()) ** 2) / 2000 + float(elem[7]) * 10 ** 5 * (1 / temp - 1 / float(tig.get()))
                if elem[2] == 'g':
                    n_p = n_p + elem[8]
                cp_p = cp_p + cp_pi * elem[8]
                dh_p = dh_p + dh_pi * elem[8]
                cp_dt = cp_dt + cp_dti * elem[8]
                if temp == 298:
                    dh_ps = dh_p
                    cp_ps = cp_p
                string_2 = string_2 + '{0:<17.6f}'.format(cp_pi)
                string_3 = string_3 + '{0:<17.6f}'.format(dh_pi)

            string_2 = string_2 + '\n'
            string_3 = string_3 + '\n'
            out_cp.write(string_2)
            out_dh.write(string_3)
            dq = dh_r - dh_p
            gas_work = (n_p - n_r) * 8.314456 * (temp - float(tig.get())) / 4.1868
            delta = dq - cp_dt - gas_work - 9716 * float(nh2o.get())
            delta_n = delta * float(mass.get()) / mol_v
            radiation = 5.670367 * float(ftime.get()) * float(area.get()) * (temp ** 4) * (10 ** (-8)) / 4.1868
            delta_2 = delta_n - radiation
            if delta_2 > 0 > delta_3 or delta_3 > 0 > delta_2:
                max_dtemp_4 = temp - int(tig.get())
                max_temp_4 = temp
            delta_3 = delta_2
            if delta > 0 > delta_4 or delta_4 > 0 > delta:
                max_temp_3 = temp
                max_dtemp_3 = temp - int(tig.get())
            delta_4 = delta
            delta_6 = dq - cp_dt
            if delta_5 > 0 > delta_6 or delta_6 > 0 > delta_5:
                max_temp_2 = temp
                max_dtemp_2 = temp - int(tig.get())
            delta_5 = delta_6
            string = '{0:6.0f}'.format(temp) + '{0:11.4f}'.format(cp_r) + '{0:11.4f}'.format(cp_p) + '{0:13.1f}'.format(dh_r) + \
                         '{0:13.1f}'.format(dh_p) + '{0:13.1f}'.format(dq) + '{0:12.1f}'.format(cp_dt) + '{0:10.1f}'.format(gas_work) +\
                     '{0:13.1f}'.format(delta) + '{0:12.1f}'.format(delta_n) + '{0:9.1f}'.format(radiation) + '{0:12.1f}'.format(delta_2) + '\n'
            ttt = float(tig.get())
            if temp == ttt:
                string = '##' + '{0:4.0f}'.format(temp) + '##' + '{0:9.4f}'.format(cp_r) + '{0:11.4f}'.format(
                    cp_p) + '{0:13.1f}'.format(dh_r) + \
                         '{0:13.1f}'.format(dh_p) + '{0:13.1f}'.format(dq) + '{0:12.1f}'.format(
                    cp_dt) + '{0:10.1f}'.format(gas_work) + \
                         '{0:13.1f}'.format(delta) + '{0:12.1f}'.format(delta_n) + '{0:9.1f}'.format(
                    radiation) + '{0:12.1f}'.format(delta_2) + '\n'
            out_file.write(string)
            if dh_p > 0:
                messagebox.showwarning('Внимание!', 'Суммарная энтльпия продуктов превысила ноль при температуре {} K. Расчет был прерван.'.format(temp))
                string = '\nСуммарная энтльпия продуктов превысила ноль при температуре {} K. Расчет был прерван.\n'.format(temp)
                out_file.write(string)
                break
            temp += 1
        max_dtemp_1 = (dh_rs - dh_ps)/cp_ps
        max_temp_1 = round(max_dtemp_1 + 298)
        string = '\nРезультаты:\n1) Адиабатическое приближение при стандартных значениях dH и Cp\n'
        out_file.write(string)
        string = 'Максимальная температура горения            ' + str(int(max_temp_1)) + '\n'
        out_file.write(string)
        label11.config(text=string)
        string = 'Температурный эффект                        ' + str(int(max_dtemp_1)) + '\n'
        out_file.write(string)
        string = 'Температурный эффект                                   ' + str(int(max_dtemp_1)) + '\n'
        label12.config(text=string)
        string = '2) Адиабатическое приближение с учетом температурных зависимостей dH и Cp\n'
        out_file.write(string)
        string = 'Максимальная температура горения            ' + str(max_temp_2) + '\n'
        out_file.write(string)
        label14.config(text=string)
        string = 'Температурный эффект                        ' + str(max_dtemp_2) + '\n'
        out_file.write(string)
        string = 'Температурный эффект                                   ' + str(max_dtemp_2) + '\n'
        label15.config(text=string)
        string = '3) Адиабатическое приближение с учетом температурных зависимостей dH и Cp и потерь теплоты на расширение газов\n'
        out_file.write(string)
        string = 'Максимальная температура горения            ' + str(max_temp_3) + '\n'
        out_file.write(string)
        label17.config(text=string)
        string = 'Температурный эффект                        ' + str(max_dtemp_3) + '\n'
        out_file.write(string)
        string = 'Температурный эффект                                   ' + str(max_dtemp_3) + '\n'
        label18.config(text=string)
        string = '4) Адиабатическое приближение с учетом температурных зависимостей dH и Cp, потерь теплоты на расширение газов и излучение\n'
        out_file.write(string)
        string = 'Максимальная температура горения            ' + str(max_temp_4) + '\n'
        out_file.write(string)
        label20.config(text=string)
        string = 'Температурный эффект                        ' + str(max_dtemp_4) + '\n'
        out_file.write(string)
        string = 'Температурный эффект                                   ' + str(max_dtemp_4) + '\n'
        label21.config(text=string)
        out_file.close()
        out_cp.close()
        out_dh.close()
        if max_temp_2 == 'не определено' or max_temp_3 == 'не определено' or max_temp_4 == 'не определено':
            messagebox.showwarning('Внимание!', 'Обнаружены неопределенные значения. Возможно, стоит повысить верхнуюю границу температурного интервала.')
    else:
        out_file = open("output.txt", "w")
        out_file.write('Нет сохраненных результатов')
        out_file.close()
        string = 'Максимальная температура горения:'
        label11.config(text=string)
        label14.config(text=string)
        label17.config(text=string)
        label20.config(text=string)
        string = 'Температурный эффект:'
        label12.config(text=string)
        label15.config(text=string)
        label18.config(text=string)
        label21.config(text=string)
    if log_range:
        file = open("output_temp.txt", "a")
        string = '{0:<9}'.format(globals()['fi_{}'.format(q)].get()) + '{0:>6}'.format(max_temp_1) + '{0:>6}'.format(max_temp_2) + '{0:>6}'.format(max_temp_3) + '\n'
        file.write(string)
        file.close()


def click_button_del_reag():
    '''функция очистки полей коэффициентов реагентов'''
    i = 1
    global num_str
    while i <= num_str:
        globals()['reag_{}k'.format(i)].delete(0, END)
        i += 1


def click_button_del_prod():
    '''функция очистки полей коэффициентов продуктов'''
    i = 1
    global num_str
    while i <= num_str:
        globals()['prod_{}k'.format(i)].delete(0, END)
        i += 1


def click_button_1():
    '''функция очистки всех полей ввода'''
    i = 1
    global num_str
    while i <= num_str:
        globals()['reag_{}'.format(i)].delete(0, END)
        globals()['reag_{}k'.format(i)].delete(0, END)
        globals()['prod_{}'.format(i)].delete(0, END)
        globals()['prod_{}k'.format(i)].delete(0, END)
        i += 1
    mass.delete(0, END)
    area.delete(0, END)
    ftime.delete(0, END)
    tig.delete(0, END)
    nh2o.delete(0, END)


def click_button_2():
    '''заполнения полей данными из файла в папке программы'''
    global num_str
    tc_input = False             # определение стандарта записи (УХК или Tcalc)
    try:
        inpf = open("input.txt", "r")
    except FileNotFoundError:
        messagebox.showerror("Ошибка", "Файл input.txt отсутствует")
    else:
        i = 1
        while i <= num_str:
            globals()['reag_{}'.format(i)].delete(0, END)
            globals()['reag_{}k'.format(i)].delete(0, END)
            globals()['prod_{}'.format(i)].delete(0, END)
            globals()['prod_{}k'.format(i)].delete(0, END)
            i += 1
        dash_line_n = 0
        string = inpf.readline()
        if string == 'Tcalc input file\n':
            tc_input = True
        if string[0] == '-':
            dash_line_n = 1
        while dash_line_n < 2:
            string = inpf.readline()
            if string[0] == '-':
                dash_line_n += 1
        i = 1
        while dash_line_n < 3:
            string = inpf.readline()
            if string[0] == '-':
                dash_line_n += 1
            else:
                if i > num_str:
                    click_button_p()
                string_el = string.split()
                if string_el[1] != 'non':
                    globals()['reag_{}'.format(i)].insert(0, string_el[1])
                if string_el[0] != 'non':
                    globals()['reag_{}k'.format(i)].insert(0, string_el[0])
                i += 1
        i = 1
        while dash_line_n < 4:
            string = inpf.readline()
            if string[0] == '-':
                dash_line_n += 1
            else:
                if i > num_str:
                    click_button_p()
                string_el = string.split()
                if string_el[1] != 'non':
                    globals()['prod_{}'.format(i)].insert(0, string_el[1])
                if string_el[0] != 'non':
                    globals()['prod_{}k'.format(i)].insert(0, string_el[0])
                i += 1
        if tc_input:
            mass.delete(0, END)
            area.delete(0, END)
            ftime.delete(0, END)
            tig.delete(0, END)
            nh2o.delete(0, END)
            string = inpf.readline()
            string_el = string.split()
            mass.insert(0, string_el[-1])
            string = inpf.readline()
            string_el = string.split()
            area.insert(0, string_el[-1])
            string = inpf.readline()
            string_el = string.split()
            ftime.insert(0, string_el[-1])
            string = inpf.readline()
            string_el = string.split()
            tig.insert(0, string_el[-1])
            string = inpf.readline()
            string_el = string.split()
            nh2o.insert(0, string_el[-1])
        inpf.close()


def click_button_open():
    '''аналог предыдущей функции, только с загрузкой из выбранного файла'''
    global num_str
    tc_input = False
    file_name = fd.askopenfilename()
    inpf = open(file_name)
    i = 1
    while i <= num_str:
        globals()['reag_{}'.format(i)].delete(0, END)
        globals()['reag_{}k'.format(i)].delete(0, END)
        globals()['prod_{}'.format(i)].delete(0, END)
        globals()['prod_{}k'.format(i)].delete(0, END)
        i += 1
    dash_line_n = 0
    string = inpf.readline()
    if string == 'Tcalc input file\n':
        tc_input = True
    if string[0] == '-':
        dash_line_n = 1
    while dash_line_n < 2:
        string = inpf.readline()
        if string[0] == '-':
            dash_line_n += 1
    i = 1
    while dash_line_n < 3:
        string = inpf.readline()
        if string[0] == '-':
            dash_line_n += 1
        else:
            if i > num_str:
                click_button_p()
            string_el = string.split()
            if string_el[1] != 'non':
                globals()['reag_{}'.format(i)].insert(0, string_el[1])
            if string_el[0] != 'non':
                globals()['reag_{}k'.format(i)].insert(0, string_el[0])
            i += 1
    i = 1
    while dash_line_n < 4:
        string = inpf.readline()
        if string[0] == '-':
            dash_line_n += 1
        else:
            if i > num_str:
                click_button_p()
            string_el = string.split()
            if string_el[1] != 'non':
                globals()['prod_{}'.format(i)].insert(0, string_el[1])
            if string_el[1] != 'non':
                globals()['prod_{}k'.format(i)].insert(0, string_el[0])
            i += 1
    if tc_input:
        mass.delete(0, END)
        area.delete(0, END)
        ftime.delete(0, END)
        tig.delete(0, END)
        nh2o.delete(0, END)
        string = inpf.readline()
        string_el = string.split()
        mass.insert(0, string_el[-1])
        string = inpf.readline()
        string_el = string.split()
        area.insert(0, string_el[-1])
        string = inpf.readline()
        string_el = string.split()
        ftime.insert(0, string_el[-1])
        string = inpf.readline()
        string_el = string.split()
        tig.insert(0, string_el[-1])
        string = inpf.readline()
        string_el = string.split()
        nh2o.insert(0, string_el[-1])
    inpf.close()


def click_button_u():
    '''функция расчета коэффициентов химического уравнения'''
    all_right = True
    i = 1
    k_list = []
    while i <= num_str:
        if globals()['reag_{}'.format(i)].get() != '':
            if isnotfloat(globals()['reag_{}k'.format(i)].get()) is False:
                k_list.append([globals()['reag_{}'.format(i)].get(), float(globals()['reag_{}k'.format(i)].get()), 'r'])
            else:
                k_list.append([globals()['reag_{}'.format(i)].get(), 'N', 'r'])
        i += 1
    i = 1
    while i <= num_str:
        if globals()['prod_{}'.format(i)].get() != '':
            if isnotfloat(globals()['prod_{}k'.format(i)].get()) is False:
                k_list.append([globals()['prod_{}'.format(i)].get(), float(globals()['prod_{}k'.format(i)].get()), 'p'])
            else:
                k_list.append([globals()['prod_{}'.format(i)].get(), 'N', 'p'])
        i += 1
    inp_num = 0
    for elem in k_list:
        if elem[1] != 'N':
            inp_num += 1

    try:
        klib = open("substance_library.txt", "r")
    except FileNotFoundError:
        messagebox.showerror("Ошибка", "Файл substance_library.txt отсутствует")
        all_right = False
    else:
        klib.close()
        elem_list = []
        for elem in k_list:
            klib = open("substance_library.txt", "r")
            for line in klib:
                if line[0] != '#':
                    spl_string = line.split()
                    if len(spl_string) == 0:
                        continue
                    if spl_string[0] == elem[0]:
                        j = 0
                        while len(spl_string) - 8 > j:
                            elem.append([spl_string[j+8], float(spl_string[j+9])])
                            add_elem = True
                            for lem in elem_list:
                                if spl_string[j+8] == lem:
                                    add_elem = False
                            if add_elem:
                                elem_list.append(spl_string[j+8])
                            j += 2
                        break
            klib.close()
            if len(elem) == 3:
                messagebox.showerror("Ошибка", "Реагент {} не найден в базе substance_library.txt".format(elem[0]))
                all_right = False
    if len(elem_list) < len(k_list) - inp_num:
        complit_num = len(k_list) - inp_num - len(elem_list)
        messagebox.showerror('Ошибка', 'Необходимо указать на {} больше коэффициентов'.format(complit_num))
        all_right = False
    if len(elem_list) > len(k_list) - inp_num:
        complit_num = len(elem_list) - len(k_list) + inp_num
        messagebox.showerror('Ошибка', 'Необходимо указать на {} меньше коэффициентов'.format(complit_num))
        all_right = False

    if all_right:
        coef_array = np.zeros((len(elem_list), len(elem_list)))
        rez_array = np.zeros((len(elem_list), 1))
        k = 0
        for elem in k_list:
            if elem[1] == 'N':
                i = 3
                while i < len(elem):
                    j = 0
                    while j < len(elem_list):
                        if elem[i][0] == elem_list[j]:
                            if elem[2] == 'r':
                                coef_array[j][k] = elem[i][1]
                            else:
                                coef_array[j][k] = elem[i][1] * (-1)
                        j += 1
                    i += 1
            else:
                i = 3
                while i < len(elem):
                    j = 0
                    while j < len(elem_list):
                        if elem[i][0] == elem_list[j]:
                            if elem[2] == 'p':
                                rez_array[j][0] = rez_array[j][0] + elem[i][1] * elem[1]
                            else:
                                rez_array[j][0] = rez_array[j][0] + elem[i][1] * elem[1] * (-1)
                        j += 1
                    i += 1
                k -= 1
            k += 1
        try:
            answer_array = np.linalg.solve(coef_array, rez_array).round(6)
            i = 1
            j = 0
            while i <= num_str:
                if globals()['reag_{}'.format(i)].get() != '':
                    if isnotfloat(globals()['reag_{}k'.format(i)].get()):
                        globals()['reag_{}k'.format(i)].insert(0, answer_array[j][0])
                        j += 1
                i += 1
            i = 1
            while i <= num_str:
                if globals()['prod_{}'.format(i)].get() != '':
                    if isnotfloat(globals()['prod_{}k'.format(i)].get()):
                        globals()['prod_{}k'.format(i)].insert(0, answer_array[j][0])
                        j += 1
                i += 1
        except:
            messagebox.showerror("Ошибка", "Получена вырожденная матрица коэффициентов. Попробуйте задать коэффициенты для других веществ")


def click_button_exit():
    exit()


def click_button_info():
    '''программе'''
    infow = Toplevel(root)
    infow.title('О программе')
    infow.geometry('400x160')
    infow.resizable(width=False, height=False)
    #infow.resizable(width=False, height=False)
    mycolor = '#%02x%02x%02x' % (240, 240, 240)
    label01 = Text(infow, font="Arial 11", wrap=WORD, width=50, bg=mycolor)
    label01.insert(1.0, 'Программа расчета температур горения в реакциях SCS (SCSTempCal) предназначена для расчета максимальной '
                        'температуры в реакции горения из растворов (SCS).\nВерсия программы 1.0\n\n'
                        'Автор алгоритма: Халиуллин Ш.М.\nemail: shamil58@rambler.ru\n'
                        'Программная реализация: Попов И.С.\nemail: popov@ihim.uran.ru')
    label01.config(state=DISABLED)
    label01.place(x=0, y=0)


def click_button_help():
    '''справка'''
    global help_index
    help_index = 1

    def help_list(help_index):
        if help_index == 1:
            return('   Ниже приведена справка для быстрого начала работы. Более подробная информация о программе и '
                   'примеры ее использования можно найти в файле manual.\n\n   Алгоритм проведения одиночного расчета.'
                   '\n   1) Запустить программу. На стартовом окне представлена версия программы и ее авторы. '
                   'Нажмите кнопку «Начать работу», чтобы перейти к рабочему окну.\n   2) Ввести уравнение химической '
                   'реакции горения. В верхней части рабочего окна представлены поля для ввода химических соединений, '
                   'участвующих в реакции. В левой части необходимо указать исходные реагенты, а в правой – продукты '
                   'химической реакции. В соседних полях справа указываются соответствующие соединениям коэффициенты '
                   'уравнения химической реакции. Кнопка «Уравнять» позволяет расставить коэффициенты автоматически. '
                   'Кнопки «+» и «-» изменяют количество полей. Назначение меток «-», «Ox», «F» и «Ob» будет пояснено '
                   'позже.\n   В программе присутствует возможность загрузки уравнения реакции из файла input.txt в '
                   'папке программы при помощи кнопки «Загрузить данные». Можно загрузить из меню > Файл > Загрузить '
                   'с возможностью выбора ранее сохраненных файлов, которые рекомендуется сохранять в виде '
                   'input_xxx.txt.')
        elif help_index == 2:
            return('   3) Указать условия протекания реакции. Отредактировать поля масса целевого продукта, площадь '
                   'излучающей поверхности, время горения, температура возгорания, количество оставшейся воды в '
                   'кристаллогидрате к моменту возгорания, верхняя граница температурного диапазона расчета. '
                   'Последняя используется в качестве критерия останова расчета. В качестве целевого продукта '
                   'принимается то вещество, около которого стоит метка «Ob». Именно его массу необходимо указать в '
                   'графе масса целевого продукта. Можно указать более одного целевого продукта и ввести их суммарную '
                   'массу. Площадь излучающей поверхности характеризуется площадью реактора. Большая площадь приводит '
                   'к более быстрому охлаждению и снижению температуры. Время горения и температура возгорания '
                   'характеризуют продолжительность реакции и температуру ее начала. При горении в закрытом реакторе '
                   'необходимо ввести ноль в графе площадь излучающей поверхности. Если к началу реакции один из '
                   'реагентов существует в форме кристаллогидрата, в графе количество воды в кристаллогидрате '
                   'указывают число молей воды на один моль соответствующего нитрата, умноженное на коэффициент '
                   'химического уравнения перед кристаллогидратом. При этом в качестве окислителя необходимо ввести '
                   'его формулу в виде кристаллогидрата с соответствующим количеством молей воды.')
        elif help_index == 3:
            return('   4) Запустить расчет. Для запуска расчета нажмите кнопку «Пуск». Если все необходимые '
                   'параметры расчета были введены, в нижней части окна появятся значения максимальных температур '
                   'горения в различных приближениях, а в папке программы будут созданы или перезаписаны файлы '
                   'output.txt, out_cp.txt и out_dh.txt. В файлы out_cp.txt и out_dh.txt программа записывает '
                   'соответственно теплоемкости при постоянном давлении и изменения энтальпий реагентов и продуктов '
                   'реакции в зависимости от температуры. Файл output.txt содержит более подробную информацию о '
                   'результатах расчета.\n\n   Структура файл output.txt.\n   В начале файла перечислены введенные '
                   'пользователем данные – уравнение химической реакции и параметры ее протекания. Далее выписываются '
                   'промежуточные результаты расчетов при различных температурах. В конце файла перечислены '
                   'вычисленные максимальные температуры горения и температурные эффекты (разность максимальной '
                   'температуры и температуры возгорания) в различных приближениях с последовательным улучшением '
                   'качества модели.')
        elif help_index == 4:
            return('   Ошибка: Реагент X не найден в базе substance_library.txt – необходимо ввести информацию о '
                   'соединении X в базу данных substance_library.txt. Для этого нажмите на кнопку «Новое соединение» '
                   'или воспользуйтесь опцией меню База данных > Новое соединение. Затем введите требуемую информацию '
                   'и нажмите кнопку «Записать». В графу соединение необходимо внести название соединения или его '
                   'химическую формулу. Далее указывается агрегатное состояние соединения при температуре возгорания '
                   'и его стандартная энтальпия (в ккал/моль). Коэффициенты a, b и c (в кал/(моль·К)) уравнения '
                   '(a + b·T/1000 – c·10^5/T^2) описывают температурную зависимость теплоемкости Cp. Если эти '
                   'коэффициенты неизвестны, то вместо коэффициентов b и c указываются 0, а вместо коэффициента a '
                   'записывается Сp при 298 K. В графе Cp предельное указывается предельное значение Cp '
                   '(в кал/(моль·К)). Для твердых веществ оно равно 3RN, где N – количество атомов в формульной '
                   'единице, R – универсальная газовая постоянная, R = 1.98586357 кал/(моль·К). В графе комментарий '
                   'можно внести короткое пояснение. Для расчета молярной массы соединения необходимо указать список '
                   'всех элементов, входящих в соединение, и их количество.\n   Проверить наличие записи о соединении '
                   'X в базе данных можно с помощью опции меню База данных > Найти соединение. Найденная запись может '
                   'быть удалена или перезаписана с помощью кнопок «Удалить» и «Перезаписать» соответственно. Также '
                   'возможно непосредственное редактирование файла substance_library.txt.')
        elif help_index == 5:
            return('   Использование переменной φ.\n   Величина φ характеризует отношение топливо/окислитель. Значение '
                   'φ = 1 в том случае, если в уравнении реакции отсутствует O2, φ > 1, когда O2 входит в список '
                   'реагентов и φ < 1, когда O2 входит в список продуктов. Чтобы использовать φ, необходимо расставить '
                   'метки реагентов. Напротив топлива в списке реагентов нужно выставить метку «F», а напротив '
                   'окислителя метку «Ox». Если в списке реагентов присутствует кислород, то напротив него должна '
                   'стоять метка «-». Кнопка «Запомнить φi» позволяет программе запомнить значение коэффициента '
                   'топлива с меткой «Fi», где i – это порядковый номер от 1 до 4. Используя данную кнопку, '
                   'пользователь должен самостоятельно убедиться, что уравнение реакции соответствует φ = 1, а в поле '
                   'под этой кнопкой указано значение 1. Далее, варьируя значение φ в поле под кнопкой «Запомнить φi», '
                   'можно автоматически пересчитать коэффициенты уравнения реакции при помощи кнопки «Обновить Fi».')
        elif help_index == 6:
            return('   Проведение серийных расчетов с φ.\n   Кнопка «Диапазон φi» позволяет провести серию расчетов с '
                   'различными значениями φ. Перед ее использованием необходимо применить кнопку «Запомнить φi» и '
                   'указать начальное и конечное значение φ, а также шаг, с которым эта переменная будет '
                   'варьироваться в процессе расчетов. Программа будет автоматически пересчитывать коэффициенты '
                   'уравнения химической реакции и запускать расчет. Результаты каждого отдельного расчета серии '
                   'сохранятся в файл output_i_φ.txt, где φ – численное значение φ, а i – порядковый номер переменной '
                   'φ. Также будет создан файл output_temp.txt, в котором представлены максимальные температуры в '
                   'зависимости от φ. Опционально пользователь может запросить автоматическое открытие этого файла или '
                   'построение графика на его основе.\n\n   Более подробную информацию о программе SCSTempCal '
                   ' и примеры ее использования можно найти в файле manual.')

    def click_button_next():
        global help_index
        if help_index < 6:
            help_index += 1
        label01.config(state=NORMAL)
        label01.delete(1.0, END)
        label01.insert(1.0, help_list(help_index))
        label01.config(state=DISABLED)

    def click_button_prev():
        global help_index
        if help_index > 1:
            help_index -= 1
        label01.config(state=NORMAL)
        label01.delete(1.0, END)
        label01.insert(1.0, help_list(help_index))
        label01.config(state=DISABLED)

    helpw = Toplevel(root)
    helpw.title('Помощь')
    #helpw.geometry('500x450')
    helpw.geometry('500x465')
    helpw.resizable(width=False, height=False)
    mycolor = '#%02x%02x%02x' % (240, 240, 240)
    label01 = Text(helpw, font="Arial 11", wrap=WORD, width=62, height=24, bg=mycolor)
    label01.insert(1.0, help_list(help_index))
    label01.config(state=DISABLED)
    label01.place(x=0, y=0)
    btn_next = Button(helpw, text="Далее >", background="#555", foreground="#ccc",
                   padx="20", pady="8", font="16", command=click_button_next)
    btn_next.place(x=280, y=437, anchor="c", height=30, width=80, bordermode=OUTSIDE)
    btn_next = Button(helpw, text="< Назад", background="#555", foreground="#ccc",
                      padx="20", pady="8", font="16", command=click_button_prev)
    btn_next.place(x=190, y=437, anchor="c", height=30, width=80, bordermode=OUTSIDE)


def click_button_ns():
    '''создания окна для введения данных о новом соединении'''
    def click_button_b():
        '''запись нового соединения в бд'''
        all_right = True
        try:
            libr = open("substance_library.txt", "r")
        except FileNotFoundError:
            messagebox.showerror("Ошибка", "Файл substance_library.txt отсутствует")
            all_right = False
        else:
            str_sub_name = entry_s1.get()
            str_sub_name = str_sub_name.replace(' ', '_')
            if str_sub_name == '':
                messagebox.showerror("Ошибка", "Отсутствует название соединения")
                all_right = False
            elif len(str_sub_name) > 15:
                messagebox.showerror("Ошибка", "Максимально допустимая длина названия составляет 15 символов")
                all_right = False
            else:
                for line in libr:
                    if line[0] != '#':
                        spl_string = line.split()
                        if len(spl_string) == 0:
                            continue
                        if spl_string[0] == str_sub_name:
                            messagebox.showerror("Ошибка", "Соединение с такой формулой уже записано")
                            all_right = False
                            break
        if all_right:
            libr.close()
            libr = open("substance_library.txt", "a")
            if agr_state.get() == 0:
                agr_val = 's'              # solid
            elif agr_state.get() == 1:
                agr_val = 'g'              # gas
            if entry_s7.get() != '':
                str_comm = entry_s7.get()
                str_comm = str_comm.replace(' ', '_')
                if len(str_comm) > 12:
                    messagebox.showerror("Ошибка", "Превышено допустимое количество символов комментария")
                    all_right = False
            else:
                str_comm = '-'
            str_cp = entry_s6.get()
            if str_cp != '':
                str_cp = str_cp.replace(',', '.')
                if isnotfloat(str_cp):
                    messagebox.showerror("Ошибка", "Введенное значение Cp пред. не является числом")
                    all_right = False
                else:
                    str_cp = '{:9.3f}'.format(float(str_cp))
                    if len(str_cp) > 9:
                        messagebox.showerror("Ошибка", "Превышено допустимое количество символов Cp пред.")
                        all_right = False
            else:
                messagebox.showerror("Ошибка", "Значение Cp пред. не указано")
                all_right = False
            str_dh = entry_s2.get()
            if str_dh != '':
                str_dh = str_dh.replace(',', '.')
                if isnotfloat(str_dh):
                    messagebox.showerror("Ошибка", "Введенное значение dH(298) не является числом")
                    all_right = False
                else:
                    str_dh = '{:9.3f}'.format(float(str_dh))
                    if len(str_dh) > 9:
                        messagebox.showerror("Ошибка", "Превышено допустимое количество символов dH(298)")
                        all_right = False
            else:
                messagebox.showerror("Ошибка", "Значение dH(298) не указано")
                all_right = False

            str_a = entry_s3.get()
            if str_a != '':
                str_a = str_a.replace(',', '.')
                if isnotfloat(str_a):
                    messagebox.showerror("Ошибка", "Введенное значение коэффициента a не является числом")
                    all_right = False
                else:
                    str_a = '{:7.3f}'.format(float(str_a))
                    if len(str_a) > 7:
                        messagebox.showerror("Ошибка", "Превышено допустимое количество символов коэффициента a")
                        all_right = False
            else:
                messagebox.showerror("Ошибка", "Значение коэффициента a не указано")
                all_right = False
            str_b = entry_s4.get()
            if str_b != '':
                str_b = str_b.replace(',', '.')
                if isnotfloat(str_b):
                    messagebox.showerror("Ошибка", "Введенное значение коэффициента b не является числом")
                    all_right = False
                else:
                    str_b = '{:7.3f}'.format(float(str_b))
                    if len(str_b) > 7:
                        messagebox.showerror("Ошибка", "Превышено допустимое количество символов коэффициента b")
                        all_right = False
            else:
                messagebox.showerror("Ошибка", "Значение коэффициента b не указано")
                all_right = False
            str_c = entry_s5.get()
            if str_c != '':
                str_c = str_c.replace(',', '.')
                if isnotfloat(str_c):
                    messagebox.showerror("Ошибка", "Введенное значение коэффициента c не является числом")
                    all_right = False
                else:
                    str_c = '{:7.3f}'.format(float(str_c))
                    if len(str_c) > 7:
                        messagebox.showerror("Ошибка", "Превышено допустимое количество символов коэффициента c")
                        all_right = False
            else:
                messagebox.showerror("Ошибка", "Значение коэффициента c не указано")
                all_right = False

            str_elem_co = ''
            i = 1
            elem_not_found = True
            while i < num_let + 1:
                str_elem = globals()['entry_el_{}'.format(i)].get()
                str_elem = str_elem.capitalize()
                str_co = globals()['entry_ko_{}'.format(i)].get()
                if len(str_co) > 6:
                    messagebox.showerror("Ошибка", "Превышено допустимое количество символов (6) для коэффициента элемента {}".format(str_elem))
                    all_right = False
                if str_elem != '' and str_co != '':
                    if str_elem in molar_mass:
                        str_co = str_co.replace(',', '.')
                        if isnotfloat(str_co) == False:
                            str_elem_co = str_elem_co + '{:<2}'.format(str_elem) + ' ' + '{:<6}'.format(str_co) + ' '
                            elem_not_found = False
                        else:
                            messagebox.showerror("Ошибка", "Введенное значение коэффициента для элемента {} не является числом".format(str_elem))
                            all_right = False
                    else:
                        messagebox.showerror("Ошибка", "Элемент {} отсутствует в списке элементов программы".format(str_elem))
                        all_right = False
                elif str_elem != '' and str_co == '':
                    messagebox.showerror("Ошибка", "Отсутствует коэффициент для элемента {}".format(str_elem))
                    all_right = False
                elif str_elem == '' and str_co != '':
                    messagebox.showerror("Ошибка", "Отсутствует химический элемента в строке № {}".format(i))
                    all_right = False
                i += 1
            if elem_not_found:
                messagebox.showerror("Ошибка", "Отсутствуют химические элементы, входяшие в соединение")
                all_right = False

        if all_right:
            string_0 = '\n' + '{:<15}'.format(str_sub_name) + ' ' + '{:<12}'.format(str_comm) +\
                       '{:^3}'.format(agr_val) + '{:9.3f}'.format(float(str_cp)) + ' ' + \
                       '{:9.3f}'.format(float(str_dh)) + ' ' + '{:7.3f}'.format(float(str_a)) + ' ' + \
                       '{:7.3f}'.format(float(str_b)) + ' ' + '{:7.3f}'.format(float(str_c)) + ' ' + str_elem_co
            libr.write(string_0)
            libr.close()
            messagebox.showinfo("Запись", "Соединение {} занесено в базу данных".format(str_sub_name))
            subinp.destroy()

    def click_button_sp():
        global num_let
        num_let += 1
        globals()['entry_el_{}'.format(num_let)] = Entry(subinp, width=3, font="Arial 12")
        globals()['entry_el_{}'.format(num_let)].place(x=10, y=260 + 25 * (num_let - 1))
        globals()['entry_ko_{}'.format(num_let)] = Entry(subinp, width=6, font="Arial 12")
        globals()['entry_ko_{}'.format(num_let)].place(x=100, y=260 + 25 * (num_let - 1))
        dist = 25 * (num_let - 5)
        btn_sp.place(y=393 + dist)
        btn_sm.place(y=393 + dist)
        b.place(y=400 + dist)
        subinp.geometry('380x{}'.format(430 + dist))

    def click_button_sm():
        global num_let
        if num_let > 1:
            globals()['entry_el_{}'.format(num_let)].destroy()
            globals()['entry_ko_{}'.format(num_let)].destroy()
            num_let -= 1
            dist = 25 * (num_let - 5)
            btn_sp.place(y=393 + dist)
            btn_sm.place(y=393 + dist)
            b.place(y=400 + dist)
            subinp.geometry('380x{}'.format(430 + dist))

    '''Разложение введенной химической формулы на компоненты'''
    def click_button_recognize():
        global num_let

        def delete_end_item(el_list):
            if el_list[-1] == '*' or el_list[-1] == '(':
                el_list.pop(-1)
                el_list = delete_end_item(el_list)
            return el_list

        '''Первичное разложение формулы'''
        one_sign = ''      # строка составления названия элемента
        one_num = ''       # строка составления коэффициента
        el_str = entry_s1.get()
        el_str = el_str.replace(' ', '')
        el_str = el_str.replace(',', '.')
        el_str = el_str.replace('[', '(')
        el_str = el_str.replace(']', ')')
        el_str = el_str.replace('{', '(')
        el_str = el_str.replace('}', ')')
        el_list = []      # список элементов и их коэффициентов
        for elem in el_str:
            if elem.isalpha():
                if one_num != '':
                    el_list.append(float(one_num))
                    one_num = ''
                if elem == elem.upper():
                    if one_sign != '':
                        el_list.append(one_sign)
                        el_list.append(1)
                        one_sign = ''
                one_sign = one_sign + elem
            elif elem.isnumeric() or elem == '.':
                if one_sign != '':
                    el_list.append(one_sign)
                    one_sign = ''
                one_num = one_num + elem
            elif elem == '(' or elem == ')' or elem == '*':
                if one_sign != '':
                    el_list.append(one_sign)
                    one_sign = ''
                    el_list.append(1)
                if one_num != '':
                    el_list.append(float(one_num))
                    one_num = ''
                el_list.append(elem)
        if one_sign != '':
            el_list.append(one_sign)
            el_list.append(1)
        if one_num != '':
            el_list.append(float(one_num))
        el_list = delete_end_item(el_list)

        '''преобразование звездочек в скобки'''
        cycle_counter_1 = 0
        while '*' in el_list:
            if cycle_counter_1 == 30:
                break
            cycle_counter_1 += 1
            i = 0
            cycle_counter_2 = 0
            while i < len(el_list):
                if cycle_counter_2 == 30:
                    break
                cycle_counter_2 += 1
                if el_list[i] == '*':
                    if i + 1 < len(el_list):
                        j = i + 1
                        bra_count = 0
                        while j < len(el_list):
                            if el_list[j] == '(':
                                bra_count += 1
                            if (el_list[j] == ')' or el_list[j] == '*') and bra_count == 0:
                                k2 = j
                                break
                            elif j == len(el_list) - 1:
                                k2 = j + 1
                            if el_list[j] == ')':
                                bra_count -= 1
                            j += 1
                        koef_2 = 1
                        if isnotfloat(el_list[i + 1]) is False:
                            koef_2 = el_list[i + 1]
                    if i > 0:
                        j = i - 1
                        bra_count = 0
                        while j >= 0:
                            if el_list[j] == ')':
                                bra_count += 1
                            if el_list[j] == '(' and bra_count == 0:
                                k1 = j + 1
                                break
                            elif j == 0:
                                k1 = 0
                            if el_list[j] == '(':
                                bra_count -= 1
                            j -= 1
                        koef_1 = 1
                        if isnotfloat(el_list[j + 1]) is False:
                            koef_1 = el_list[j + 1]
                    el_list.insert(k2, koef_2)
                    el_list.insert(k2, ')')
                    if isnotfloat(el_list[i + 1]) is False:
                        el_list.pop(i+1)
                    el_list.insert(i + 1, '(')
                    el_list.pop(i)
                    el_list.insert(i, koef_1)
                    el_list.insert(i, ')')
                    if isnotfloat(el_list[j + 1]) is False:
                        el_list.pop(j+1)
                    el_list.insert(k1, '(')
                i += 1

        ''' цикл раскрытия скобок '''
        cycle_counter_1 = 0
        while ('(' in el_list) and (')' in el_list):
            if cycle_counter_1 == 30:
                break
            cycle_counter_1 += 1
            i = 0
            while i < len(el_list):
                if el_list[i] == ')':
                    j = i
                    while j >= 0:
                        if el_list[j] == '(':
                            if len(el_list) > (i + 1) and isnotfloat(el_list[i+1]) is False:
                                mult = el_list.pop(i+1)
                            else:
                                mult = 1
                            for k in range(j+1, i):
                                if isnotfloat(el_list[k]) is False:
                                    el_list[k] = el_list[k] * mult
                                    if int(el_list[k]) == el_list[k]:
                                        el_list[k] = int(el_list[k])
                            el_list.pop(i)
                            el_list.pop(j)
                            break
                        j -= 1
                i += 1
        for i in range(0, len(el_list)):
            el_list[i] = str(el_list[i])

        '''проверка результатов разложения'''
        all_ok = True
        if '*' in el_list or '(' in el_list or ')' in el_list:
            all_ok = False
            messagebox.showerror('Ошибка', 'Не удалось раскрыть скобки')
        if isnotfloat(el_list[0]) is False:
            all_ok = False
            messagebox.showerror('Ошибка', 'Обнаружен лишний коэффициент перед формулой')
        if len(el_list) % 2 != 0 and all_ok:
            all_ok = False
            messagebox.showerror('Ошибка', 'Не удалось раскрыть скобки')
        i = 0
        for elem in el_list:
            i += 1
            if isnotfloat(elem) and elem.isalpha():
                if elem not in molar_mass and all_ok:
                    all_ok = False
                    messagebox.showerror('Ошибка', '{} отсутсвует в списке химических элементов'.format(elem))
                if i % 2 == 0 and all_ok:
                    all_ok = False
                    messagebox.showerror('Ошибка', 'Элемент занимает позицию коэффициента'.format(elem))
            elif isnotfloat(elem) and elem.isalpha() is False and (elem != '(' and elem != ')' and elem != '*') and all_ok:
                all_ok = False
                messagebox.showerror('Ошибка', '{} отсутсвует в списке химических элементов'.format(elem))
            elif isnotfloat(elem) is False and i % 2 != 0 and all_ok:
                all_ok = False
                messagebox.showerror('Ошибка', 'Коэффициент занимает позицию химического элемента'.format(elem))

        '''объединение одинаковых элементов'''
        if all_ok:
            i, j = 0, 2
            while i < len(el_list):
                while j < len(el_list):
                    if el_list[i] == el_list[j]:
                        el_list[i + 1] = str(float(el_list[i + 1]) + float(el_list[j + 1]))
                        el_list.pop(j + 1)
                        el_list.pop(j)
                        j -= 2
                    j += 2
                i += 2
                j = i + 2
            for i in range(0, len(el_list)):
                if isnotfloat(el_list[i]) is False and int(float(el_list[i])) == float(el_list[i]):
                    el_list[i] = int(float(el_list[i]))

        '''выгрузка результатов в поля окна'''
        i = 1
        while i <= num_let:
            globals()['entry_el_{}'.format(i)].delete(0, END)
            globals()['entry_ko_{}'.format(i)].delete(0, END)
            i += 1
        if all_ok:
            i = 1
            while i < len(el_list)/2 + 1:
                if i > num_let:
                    click_button_sp()
                globals()['entry_el_{}'.format(i)].insert(0, el_list[2 * i - 2])
                globals()['entry_ko_{}'.format(i)].insert(0, el_list[2 * i - 1])
                i += 1

    subinp = Toplevel(root)
    subinp.title('Запись нового соединения в базу данных')
    subinp.geometry('380x430')
    global num_let                          # счетчик количества полей для элементов
    num_let = 0
    agr_state = IntVar()
    agr_state.set(0)
    labels01 = Label(subinp, text='Название соединение', font="Arial 12", justify=LEFT)
    labels01.place(x=10, y=10)
    labels02 = Label(subinp, text='Агрегатное состояние в реакции', font="Arial 12", justify=LEFT)
    labels02.place(x=10, y=35)
    labels03 = Label(subinp, text='dH(298)', font="Arial 12", justify=LEFT)
    labels03.place(x=10, y=85)
    labels04 = Label(subinp, text='Коэффициенты температурной зависимости Cp:', font="Arial 12", justify=LEFT)
    labels04.place(x=10, y=110)
    labels05 = Label(subinp, text='a', font="Arial 12", justify=LEFT)
    labels05.place(x=10, y=135)
    labels06 = Label(subinp, text='b', font="Arial 12", justify=LEFT)
    labels06.place(x=120, y=135)
    labels07 = Label(subinp, text='c', font="Arial 12", justify=LEFT)
    labels07.place(x=230, y=135)
    labels08 = Label(subinp, text='Сp предельное', font="Arial 12", justify=LEFT)
    labels08.place(x=10, y=160)
    labels09 = Label(subinp, text='Комментарий', font="Arial 12", justify=LEFT)
    labels09.place(x=10, y=185)
    labels10 = Label(subinp, text='Элементный состав:', font="Arial 12", justify=LEFT)
    labels10.place(x=10, y=210)
    labels11 = Label(subinp, text='элемент', font="Arial 12", justify=LEFT)
    labels11.place(x=10, y=235)
    labels12 = Label(subinp, text='количество', font="Arial 12", justify=LEFT)
    labels12.place(x=100, y=235)

    entry_s1 = Entry(subinp, width=18, font="Arial 12")  # формула нового соединения
    entry_s1.place(x=200, y=10)
    entry_s2 = Entry(subinp, width=18, font="Arial 12")  # dH(298)
    entry_s2.place(x=200, y=85)
    entry_s3 = Entry(subinp, width=8, font="Arial 12")  # a
    entry_s3.place(x=30, y=135)
    entry_s4 = Entry(subinp, width=8, font="Arial 12")  # b
    entry_s4.place(x=140, y=135)
    entry_s5 = Entry(subinp, width=8, font="Arial 12")  # c
    entry_s5.place(x=250, y=135)
    entry_s6 = Entry(subinp, width=18, font="Arial 12")  # Cp пред.
    entry_s6.place(x=200, y=160)
    entry_s7 = Entry(subinp, width=18, font="Arial 12")  # комментарий.
    entry_s7.place(x=200, y=185)
    while num_let < 5:
        globals()['entry_el_{}'.format(num_let + 1)] = Entry(subinp, width=3, font="Arial 12")
        globals()['entry_el_{}'.format(num_let + 1)].place(x=10, y=260 + 25 * num_let)
        globals()['entry_ko_{}'.format(num_let + 1)] = Entry(subinp, width=6, font="Arial 12")
        globals()['entry_ko_{}'.format(num_let + 1)].place(x=100, y=260 + 25 * num_let)
        num_let += 1

    radiobutton_g = Radiobutton(subinp, text="газообразное", variable=agr_state, value=1, font="Arial 12", justify=LEFT)
    radiobutton_g.place(x=200, y=55)
    radiobutton_s = Radiobutton(subinp, text="твердое или жидкое", variable=agr_state, value=0, font="Arial 12", justify=LEFT)
    radiobutton_s.place(x=200, y=35)

    b = Button(subinp, text="Записать", background="#555", foreground="#ccc",
                   padx="20", pady="8", font="16", command=click_button_b)
    b.place(x=300, y=400, anchor="c", height=30, width=135, bordermode=OUTSIDE)
    btn_recognize = Button(subinp, text="Автораспознавание", background="#555", foreground="#ccc",
                padx="20", pady="8", font="Arial 10", command=click_button_recognize)
    btn_recognize.place(x=300, y=260, anchor="c", height=30, width=140, bordermode=OUTSIDE)
    btn_sp = Button(subinp, text="+", background="#555", foreground="#ccc",
                   padx="20", pady="8", font="7", command=click_button_sp)
    btn_sp.place(x=150, y=393, anchor="c", height=12, width=12, bordermode=OUTSIDE)
    btn_sm = Button(subinp, text="-", background="#555", foreground="#ccc",
                   padx="20", pady="8", font="7", command=click_button_sm)
    btn_sm.place(x=133, y=393, anchor="c", height=12, width=12, bordermode=OUTSIDE)


def click_button_fs():
    '''поиск соединения в бд'''
    global true_e
    true_e = False

    def click_button_sp():
        global num_e
        num_e += 1
        globals()['entry_el_{}'.format(num_e)] = Entry(subfin, width=3, font="Arial 12")
        globals()['entry_el_{}'.format(num_e)].place(x=10, y=260 + 25 * (num_e - 1))
        globals()['entry_ko_{}'.format(num_e)] = Entry(subfin, width=6, font="Arial 12")
        globals()['entry_ko_{}'.format(num_e)].place(x=100, y=260 + 25 * (num_e - 1))
        dist = 25 * (num_e - 5)
        btn_sp.place(y=393 + dist)
        btn_sm.place(y=393 + dist)
        btn_search.place(y=400 + dist)
        btn_del.place(y=365 + dist)
        btn_rw.place(y=330 + dist)
        subfin.geometry('380x{}'.format(430 + dist))

    def click_button_sm():
        global num_e
        if num_e > 1:
            globals()['entry_el_{}'.format(num_e)].destroy()
            globals()['entry_ko_{}'.format(num_e)].destroy()
            num_e -= 1
            dist = 25 * (num_e - 5)
            btn_sp.place(y=393 + dist)
            btn_sm.place(y=393 + dist)
            btn_search.place(y=400 + dist)
            btn_del.place(y=365 + dist)
            btn_rw.place(y=330 + dist)
            subfin.geometry('380x{}'.format(430 + dist))

    def click_button_search():
        global true_e, num_e, str_sub_name, entry_s2, entry_s3, entry_s4, entry_s5, entry_s6, entry_s7, agr_state_2

        def click_button_1():    # без этих двух функций не работают переключатели агрегатного состояния
            agr_state_2.set(1)

        def click_button_0():
            agr_state_2.set(0)

        all_right = True
        try:
            libr = open("substance_library.txt", "r")
        except FileNotFoundError:
            messagebox.showerror("Ошибка", "Файл substance_library.txt отсутствует")
            all_right = False
        else:
            str_sub_name = entry_s1.get()
            str_sub_name = str_sub_name.replace(' ', '_')
            if str_sub_name == '':
                messagebox.showerror("Ошибка", "Отсутствует название соединения")
                all_right = False
            elif len(str_sub_name) > 15:
                messagebox.showerror("Ошибка", "Максимально допустимая длина названия составляет 15 символов")
                all_right = False
        if all_right:
            for line in libr:
                if line[0] != '#':
                    spl_string = line.split()
                    if len(spl_string) == 0:
                        continue
                    if spl_string[0] == str_sub_name:
                        messagebox.showinfo("Поиск", "Соединение {} найдено в базе данных".format(str_sub_name))
                        all_right = True
                        '''без кнопок btn_0 и btn_1 не работают переключатели агрегатного состояния'''
                        btn_0 = Button(subfin, text="1", background="#555", foreground="#ccc",
                                       padx="20", pady="8", font="7", command=click_button_1)
                        btn_1 = Button(subfin, text="0", background="#555", foreground="#ccc",
                                       padx="20", pady="8", font="7", command=click_button_0)
                        break
                    else:
                        all_right = False
        if all_right:
            labels02 = Label(subfin, text='Агрегатное состояние в реакции', font="Arial 12", justify=LEFT)
            labels02.place(x=10, y=35)
            labels03 = Label(subfin, text='dH(298)', font="Arial 12", justify=LEFT)
            labels03.place(x=10, y=85)
            labels04 = Label(subfin, text='Коэффициенты температурной зависимости Cp:', font="Arial 12", justify=LEFT)
            labels04.place(x=10, y=110)
            labels05 = Label(subfin, text='a', font="Arial 12", justify=LEFT)
            labels05.place(x=10, y=135)
            labels06 = Label(subfin, text='b', font="Arial 12", justify=LEFT)
            labels06.place(x=120, y=135)
            labels07 = Label(subfin, text='c', font="Arial 12", justify=LEFT)
            labels07.place(x=230, y=135)
            labels08 = Label(subfin, text='Сp предельное', font="Arial 12", justify=LEFT)
            labels08.place(x=10, y=160)
            labels09 = Label(subfin, text='Комментарий', font="Arial 12", justify=LEFT)
            labels09.place(x=10, y=185)
            labels10 = Label(subfin, text='Элементный состав:', font="Arial 12", justify=LEFT)
            labels10.place(x=10, y=210)
            labels11 = Label(subfin, text='элемент', font="Arial 12", justify=LEFT)
            labels11.place(x=10, y=235)
            labels12 = Label(subfin, text='количество', font="Arial 12", justify=LEFT)
            labels12.place(x=100, y=235)
            entry_s2 = Entry(subfin, width=18, font="Arial 12")  # dH(298)
            entry_s2.place(x=200, y=85)
            entry_s3 = Entry(subfin, width=8, font="Arial 12")  # a
            entry_s3.place(x=30, y=135)
            entry_s4 = Entry(subfin, width=8, font="Arial 12")  # b
            entry_s4.place(x=140, y=135)
            entry_s5 = Entry(subfin, width=8, font="Arial 12")  # c
            entry_s5.place(x=250, y=135)
            entry_s6 = Entry(subfin, width=18, font="Arial 12")  # Cp пред.
            entry_s6.place(x=200, y=160)
            entry_s7 = Entry(subfin, width=18, font="Arial 12")  # комментарий.
            entry_s7.place(x=200, y=185)
            subfin.geometry('380x400')
            try:
                entry_s2.insert(0, spl_string[4])
                string = spl_string[4]
                string = string.replace(',', '.')
                if isnotfloat(string):
                    messagebox.showwarning("Внимание!", "Значение dH(298) не является числом")
                entry_s3.insert(0, spl_string[5])
                string = spl_string[5]
                string = string.replace(',', '.')
                if isnotfloat(string):
                    messagebox.showwarning("Внимание!", "Значение коэффициента a не является числом")
                entry_s4.insert(0, spl_string[6])
                string = spl_string[6]
                string = string.replace(',', '.')
                if isnotfloat(string):
                    messagebox.showwarning("Внимание!", "Значение коэффициента b не является числом")
                entry_s5.insert(0, spl_string[7])
                string = spl_string[7]
                string = string.replace(',', '.')
                if isnotfloat(string):
                    messagebox.showwarning("Внимание!", "Значение коэффициента c не является числом")
                entry_s6.insert(0, spl_string[3])
                string = spl_string[3]
                string = string.replace(',', '.')
                if isnotfloat(string):
                    messagebox.showwarning("Внимание!", "Значение Cp пред не является числом")
                entry_s7.insert(0, spl_string[1])
            except IndexError:
                messagebox.showwarning("Внимание!", "Часть данных о соединении отсутствует")
            try:
                agr_state_2 = IntVar()
                if spl_string[2] == 's':
                    agr_state_2.set(0)
                elif spl_string[2] == 'g':
                    agr_state_2.set(1)
                else:
                    messagebox.showwarning("Внимание!", "Неизвестное агрегатное состояние, приписано твердому веществу")
                    agr_state_2.set(0)
            except IndexError:
                messagebox.showerror("Внимание!", "Информация об агрегатном состоянии отсутствует, приписано твердому веществу")
                agr_state_2.set(0)
            rbtn_g = Radiobutton(subfin, text="газообразное", variable=agr_state_2, value=1, font="Arial 12", justify=LEFT)
            rbtn_g.place(x=200, y=55)
            rbtn_s = Radiobutton(subfin, text="твердое или жидкое", variable=agr_state_2, value=0, font="Arial 12", justify=LEFT)
            rbtn_s.place(x=200, y=35)
            num_e_max = (len(spl_string) - 8)/2
            if true_e:
                while num_e > 0:
                    globals()['entry_el_{}'.format(num_e)].destroy()
                    globals()['entry_ko_{}'.format(num_e)].destroy()
                    num_e -= 1
            else:
                num_e = 0
                true_e = True
            while num_e < num_e_max:
                globals()['entry_el_{}'.format(num_e + 1)] = Entry(subfin, width=3, font="Arial 12")
                globals()['entry_el_{}'.format(num_e + 1)].place(x=10, y=260 + 25 * num_e)
                globals()['entry_el_{}'.format(num_e + 1)].insert(0, spl_string[2*num_e+8])
                if spl_string[2*num_e+8] not in molar_mass:
                    messagebox.showwarning("Внимание!", "Химический элемент {} не опознан".format(spl_string[2*num_e+8]))
                try:
                    globals()['entry_ko_{}'.format(num_e + 1)] = Entry(subfin, width=6, font="Arial 12")
                    globals()['entry_ko_{}'.format(num_e + 1)].place(x=100, y=260 + 25 * num_e)
                    globals()['entry_ko_{}'.format(num_e + 1)].insert(0, spl_string[2 * num_e + 9])
                    string = spl_string[2 * num_e + 9]
                    string = string.replace(',', '.')
                    if isnotfloat(string):
                        messagebox.showwarning("Внимание!", "Коэффициент элемента {} не является числом".format(spl_string[2 * num_e + 8]))
                except IndexError:
                    messagebox.showwarning("Внимание!", "Ошибка в записи элементного состава")
                    globals()['entry_ko_{}'.format(num_e + 1)] = Entry(subfin, width=6, font="Arial 12")
                    globals()['entry_ko_{}'.format(num_e + 1)].place(x=100, y=260 + 25 * num_e)
                num_e += 1
            if num_e == 0:
                globals()['entry_el_{}'.format(num_e + 1)] = Entry(subfin, width=3, font="Arial 12")
                globals()['entry_el_{}'.format(num_e + 1)].place(x=10, y=260 + 25 * num_e)
                globals()['entry_ko_{}'.format(num_e + 1)] = Entry(subfin, width=6, font="Arial 12")
                globals()['entry_ko_{}'.format(num_e + 1)].place(x=100, y=260 + 25 * num_e)
                num_e = 1
            dist = 25 * (num_e - 5)
            btn_sp.place(x=150, y=393 + dist, anchor="c", height=12, width=12, bordermode=OUTSIDE)
            btn_sm.place(x=133, y=393 + dist, anchor="c", height=12, width=12, bordermode=OUTSIDE)
            btn_search.place(y=400 + dist)
            btn_del.place(x=300, y=365 + dist, anchor="c", height=30, width=135, bordermode=OUTSIDE)
            btn_rw.place(x=300, y=330 + dist, anchor="c", height=30, width=135, bordermode=OUTSIDE)
            subfin.geometry('380x{}'.format(430 + dist))

        else:
            messagebox.showinfo("Поиск", "Соединение {} отсутствует в базе данных".format(str_sub_name))

    def click_button_del():
        global str_sub_name
        try:
            libr = open("substance_library.txt", "r")
        except FileNotFoundError:
            messagebox.showerror("Ошибка", "Файл substance_library.txt отсутствует")
        else:
            temp_file = open("temp.txt", "w")
            i = 0  # счетчик количества удаляемых строк
            j = 0  # счетчик количества строк в новом файле
            for line in libr:
                split_line = line.split()
                if len(split_line) == 0:
                    continue
                if split_line[0] != str_sub_name:
                    temp_file.write(line)
                    j += 1
                elif split_line[0] == str_sub_name and i > 0:
                    temp_file.write(line)
                    j += 1
                else:
                    i += 1
            libr.close()
            temp_file.close()
            os.remove('substance_library.txt')
            os.replace('temp.txt', 'substance_library.txt')
            if i == 0:
                messagebox.showerror("Ошибка", "Не удалено ни одной записи")
            else:
                messagebox.showinfo("Удаление", "Запись {} успешно удалена".format(str_sub_name))
                subfin.destroy()

    def click_button_rw():
        global str_sub_name, entry_s2, entry_s3, entry_s4, entry_s5, entry_s6, entry_s7, agr_state_2, num_e
        try:
            libr = open("substance_library.txt", "r")
        except FileNotFoundError:
            messagebox.showerror("Ошибка", "Файл substance_library.txt отсутствует")
        else:
            temp_file = open("temp.txt", "w")
            all_right = True
            p = 0
            for line in libr:
                split_line = line.split()
                if len(split_line) == 0:
                    continue
                if split_line[0] != str_sub_name:
                    temp_file.write(line)
                elif split_line[0] == str_sub_name and p > 0:
                    temp_file.write(line)
                    p += 1
                else:
                    if agr_state_2.get() == 0:
                        agr_val = 's'  # solid
                    elif agr_state_2.get() == 1:
                        agr_val = 'g'  # gas
                    if entry_s1.get() != str_sub_name:
                        messagebox.showwarning("Внимание!", "Название записи было изменено на исходное")
                    if entry_s7.get() != '':
                        str_comm = entry_s7.get()
                        str_comm = str_comm.replace(' ', '_')
                        if len(str_comm) > 12:
                            messagebox.showerror("Ошибка", "Превышено допустимое количество символов комментария")
                            all_right = False
                    else:
                        str_comm = '-'
                    str_cp = entry_s6.get()
                    if str_cp != '':
                        str_cp = str_cp.replace(',', '.')
                        if isnotfloat(str_cp):
                            messagebox.showerror("Ошибка", "Введенное значение Cp пред. не является числом")
                            all_right = False
                        else:
                            str_cp = '{:9.3f}'.format(float(str_cp))
                            if len(str_cp) > 9:
                                messagebox.showerror("Ошибка", "Превышено допустимое количество символов Cp пред.")
                                all_right = False
                    else:
                        messagebox.showerror("Ошибка", "Значение Cp пред. не указано")
                        all_right = False
                    str_dh = entry_s2.get()
                    if str_dh != '':
                        str_dh = str_dh.replace(',', '.')
                        if isnotfloat(str_dh):
                            messagebox.showerror("Ошибка", "Введенное значение dH(298) не является числом")
                            all_right = False
                        else:
                            str_dh = '{:9.3f}'.format(float(str_dh))
                            if len(str_dh) > 9:
                                messagebox.showerror("Ошибка", "Превышено допустимое количество символов dH(298)")
                                all_right = False
                    else:
                        messagebox.showerror("Ошибка", "Значение dH(298) не указано")
                        all_right = False

                    str_a = entry_s3.get()
                    if str_a != '':
                        str_a = str_a.replace(',', '.')
                        if isnotfloat(str_a):
                            messagebox.showerror("Ошибка", "Введенное значение коэффициента a не является числом")
                            all_right = False
                        else:
                            str_a = '{:7.3f}'.format(float(str_a))
                            if len(str_a) > 7:
                                messagebox.showerror("Ошибка",
                                                     "Превышено допустимое количество символов коэффициента a")
                                all_right = False
                    else:
                        messagebox.showerror("Ошибка", "Значение коэффициента a не указано")
                        all_right = False
                    str_b = entry_s4.get()
                    if str_b != '':
                        str_b = str_b.replace(',', '.')
                        if isnotfloat(str_b):
                            messagebox.showerror("Ошибка", "Введенное значение коэффициента b не является числом")
                            all_right = False
                        else:
                            str_b = '{:7.3f}'.format(float(str_b))
                            if len(str_b) > 7:
                                messagebox.showerror("Ошибка",
                                                     "Превышено допустимое количество символов коэффициента b")
                                all_right = False
                    else:
                        messagebox.showerror("Ошибка", "Значение коэффициента b не указано")
                        all_right = False
                    str_c = entry_s5.get()
                    if str_c != '':
                        str_c = str_c.replace(',', '.')
                        if isnotfloat(str_c):
                            messagebox.showerror("Ошибка", "Введенное значение коэффициента c не является числом")
                            all_right = False
                        else:
                            str_c = '{:7.3f}'.format(float(str_c))
                            if len(str_c) > 7:
                                messagebox.showerror("Ошибка",
                                                     "Превышено допустимое количество символов коэффициента c")
                                all_right = False
                    else:
                        messagebox.showerror("Ошибка", "Значение коэффициента c не указано")
                        all_right = False

                    str_elem_co = ''
                    i = 1
                    elem_not_found = True
                    while i < num_e + 1:
                        str_elem = globals()['entry_el_{}'.format(i)].get()
                        str_elem = str_elem.capitalize()
                        str_co = globals()['entry_ko_{}'.format(i)].get()
                        if len(str_co) > 6:
                            messagebox.showerror("Ошибка",
                                                 "Превышено допустимое количество символов (6) для коэффициента элемента {}".format(
                                                     str_elem))
                            all_right = False
                        if str_elem != '' and str_co != '':
                            if str_elem in molar_mass:
                                str_co = str_co.replace(',', '.')
                                if isnotfloat(str_co) == False:
                                    str_elem_co = str_elem_co + '{:<2}'.format(str_elem) + ' ' + '{:<6}'.format(
                                        str_co) + ' '
                                    elem_not_found = False
                                else:
                                    messagebox.showerror("Ошибка",
                                                         "Введенное значение коэффициента для элемента {} не является числом".format(
                                                             str_elem))
                                    all_right = False
                            else:
                                messagebox.showerror("Ошибка",
                                                     "Элемент {} отсутствует в списке элементов программы".format(
                                                         str_elem))
                                all_right = False
                        elif str_elem != '' and str_co == '':
                            messagebox.showerror("Ошибка", "Отсутствует коэффициент для элемента {}".format(str_elem))
                            all_right = False
                        elif str_elem == '' and str_co != '':
                            messagebox.showerror("Ошибка", "Отсутствует химический элемента в строке № {}".format(i))
                            all_right = False
                        i += 1
                    if elem_not_found:
                        messagebox.showerror("Ошибка", "Отсутствуют химические элементы, входяшие в соединение")
                        all_right = False

                    if all_right:
                        string_0 = '{:<15}'.format(str_sub_name) + ' ' + '{:<12}'.format(str_comm) + '{:^3}'.format(
                            agr_val) + '{:9.3f}'.format(float(str_cp)) + ' ' + '{:9.3f}'.format(
                            float(str_dh)) + ' ' + '{:7.3f}'.format(float(str_a)) + ' ' + '{:7.3f}'.format(
                            float(str_b)) + ' ' + '{:7.3f}'.format(float(str_c)) + ' ' + str_elem_co + '\n'
                        temp_file.write(string_0)
                        p += 1
                    else:
                        messagebox.showerror("Ошибка", "Запись не была переписана в сязи с возникновением ошибки")
                        temp_file.write(line)
            libr.close()
            temp_file.close()
            os.remove('substance_library.txt')
            os.replace('temp.txt', 'substance_library.txt')
            if p == 1:
                messagebox.showinfo("Перезапись", "Соединение {} успешно перезаписано".format(str_sub_name))
                subfin.destroy()
            elif p > 1:
                messagebox.showwarning("Внимание!", "Имеется {} записей соединения {}. Перезаписана первая из них.".format(p, str_sub_name))
                subfin.destroy()

    subfin = Toplevel(root)
    subfin.title('Поиск соединения в базе данных')
    subfin.geometry('380x100')
    labels01 = Label(subfin, text='Название соединение', font="Arial 12", justify=LEFT)
    labels01.place(x=10, y=10)
    entry_s1 = Entry(subfin, width=18, font="Arial 12")  # формула искомого соединения
    entry_s1.place(x=200, y=10)
    btn_search = Button(subfin, text="Поиск", background="#555", foreground="#ccc",
               padx="20", pady="8", font="16", command=click_button_search)
    btn_search.place(x=300, y=70, anchor="c", height=30, width=135, bordermode=OUTSIDE)
    btn_del = Button(subfin, text="Удалить", background="#555", foreground="#ccc",
                        padx="20", pady="8", font="16", command=click_button_del)
    btn_rw = Button(subfin, text="Перезаписать", background="#555", foreground="#ccc",
                        padx="20", pady="8", font="16", command=click_button_rw)
    btn_sp = Button(subfin, text="+", background="#555", foreground="#ccc",
                    padx="20", pady="8", font="7", command=click_button_sp)
    btn_sm = Button(subfin, text="-", background="#555", foreground="#ccc",
                    padx="20", pady="8", font="7", command=click_button_sm)


def click_button_return():
    '''функция возврата на стартовый экран'''
    global num_str, btn_0, btn_exit, label01, label02, label03,  filename1, filename2, filename3, background_label, \
        background_labe2, background_labe3, etemp
    for i in range(1, 22):
        globals()['label{}'.format(i)].destroy()
    btn_1.destroy()
    btn_2.destroy()
    btn_3.destroy()
    btn_p.destroy()
    btn_m.destroy()
    btn_u.destroy()
    btn_ns.destroy()
    btn_del_reag.destroy()
    btn_del_prod.destroy()
    mass.destroy()
    area.destroy()
    ftime.destroy()
    tig.destroy()
    nh2o.destroy()
    mainmenu.destroy()
    etemp.destroy()
    ltemp.destroy()
    i = 0
    while i < num_str:
        globals()['reag_{}o'.format(i + 1)].destroy()
        globals()['reag_{}'.format(i + 1)].destroy()
        globals()['reag_{}k'.format(i + 1)].destroy()
        globals()['prod_{}o'.format(i + 1)].destroy()
        globals()['prod_{}'.format(i + 1)].destroy()
        globals()['prod_{}k'.format(i + 1)].destroy()
        i += 1

    for i in fi_list:
        globals()['fi_{}'.format(i)].destroy()
        globals()['label{}_fi'.format(i)].destroy()
        globals()['label{}_ra'.format(i)].destroy()
        globals()['label{}_st'.format(i)].destroy()
        globals()['label{}_fn'.format(i)].destroy()
        globals()['label{}_sp'.format(i)].destroy()
        globals()['entry{}_st'.format(i)].destroy()
        globals()['entry{}_fn'.format(i)].destroy()
        globals()['entry{}_sp'.format(i)].destroy()
        globals()['btn_mem_{}'.format(i)].destroy()
        globals()['btn_ref_{}'.format(i)].destroy()
        globals()['btn_ra_{}'.format(i)].destroy()

    root.geometry("500x740")
    root.resizable(width=False, height=False)
    btn_0 = Button(text="Начать работу", background="#555", foreground="#ccc",
                   padx="20", pady="8", font="16", command=click_button_0)
    btn_0.place(x=150, y=620, anchor="c", height=30, width=135, bordermode=OUTSIDE)
    btn_exit = Button(text="Выход", background="#555", foreground="#ccc",
                      padx="20", pady="8", font="16", command=click_button_exit)
    btn_exit.place(x=300, y=620, anchor="c", height=30, width=135, bordermode=OUTSIDE)
    label01 = Label(text='Программа расчета температур горения в реакциях SCS\n(SCSTempCal)', font="Arial 12", justify=LEFT)
    label01.place(x=10, y=20)
    label02 = Label(text='Версия 1.0', font="Arial 12", justify=LEFT)
    label02.place(x=10, y=60)
    label03 = Label(text='Авторы: Халиуллин Ш.М., Попов И.С.', font="Arial 12", justify=LEFT)
    label03.place(x=10, y=80)
    filename1 = PhotoImage(file="fig.png")
    background_label = Label(image=filename1)
    background_label.place(x=0, y=140)
    num_str = 0


def click_button_mem(i):
    '''функция записи значения fi'''
    global num_str
    globals()['log_mem_{}'.format(i)] = False
    fi_val = globals()['fi_{}'.format(i)].get()
    fi_val = fi_val.replace(',', '.')
    if isnotfloat(fi_val):
        messagebox.showerror('Ошибка', 'Значение φ{} должно быть числом'.format(i))
    else:
        try:
            for j in range(1, num_str+1):
                if globals()['reag_{}o'.format(j)].lab['text'][0] == 'F' and int(globals()['reag_{}o'.format(j)].lab['text'][1:]) == i:
                    globals()['fuel_val_{}'.format(i)] = float(globals()['reag_{}k'.format(j)].get()) / float(fi_val)
                    globals()['log_mem_{}'.format(i)] = True
                    print('fi = 1: ', globals()['fuel_val_{}'.format(i)])
        except ValueError:
            messagebox.showerror("Ошибка", "Коэффициент топлива задан неверно")
            globals()['log_mem_{}'.format(i)] = False


def click_button_fi(q):
    '''пересчет коэффициентов уравнения при заданном fi'''
    global num_str
    log_o2 = False                                 # проверка наличия O2 в реагентах или продуктах
    if globals()['log_mem_{}'.format(q)]:
        fi_val = globals()['fi_{}'.format(q)].get()
        fi_val = fi_val.replace(',', '.')
        new_2k = globals()['fuel_val_{}'.format(q)] * float(fi_val)
        for h in range(1, num_str+1):
            if globals()['reag_{}o'.format(h)].lab['text'] != 'Ox' and globals()['reag_{}o'.format(h)].lab['text'][0] != 'F':
                globals()['reag_{}k'.format(h)].delete(0, END)
            elif globals()['reag_{}o'.format(h)].lab['text'][0] == 'F' and int(globals()['reag_{}o'.format(h)].lab['text'][1:]) == q:
                globals()['reag_{}k'.format(h)].delete(0, END)
                globals()['reag_{}k'.format(h)].insert(0, new_2k)
            globals()['prod_{}k'.format(h)].delete(0, END)
            if globals()['prod_{}'.format(h)].get() == 'O2' or globals()['reag_{}'.format(h)].get() == 'O2':
                log_o2 = True
        if log_o2 is False:
            i = 1
            while i <= num_str:
                if globals()['reag_{}'.format(i)].get() == '' and log_o2 is False:
                    globals()['reag_{}'.format(i)].insert(0, 'O2')
                    log_o2 = True
                    break
                i += 1
            if log_o2 == False:
                click_button_p()
                globals()['reag_{}'.format(i)].insert(0, 'O2')
        click_button_u()
        '''перенос O2 с отрицательным значением'''
        i = 1
        while i <= num_str:
            if globals()['reag_{}'.format(i)].get() == 'O2' and float(globals()['reag_{}k'.format(i)].get()) < 0:
                j = 1
                o_val = float(globals()['reag_{}k'.format(i)].get()) * -1
                globals()['reag_{}'.format(i)].delete(0, END)
                globals()['reag_{}k'.format(i)].delete(0, END)
                log_o2 = False
                while j <= num_str:
                    if globals()['prod_{}'.format(j)].get() == '':
                        globals()['prod_{}'.format(j)].insert(0, 'O2')
                        globals()['prod_{}k'.format(j)].insert(0, o_val)
                        log_o2 = True
                        break
                    j += 1
                if log_o2 is False:
                    click_button_p()
                    globals()['prod_{}'.format(j)].insert(0, 'O2')
                    globals()['prod_{}k'.format(j)].insert(0, o_val)
            if globals()['prod_{}'.format(i)].get() == 'O2' and float(globals()['prod_{}k'.format(i)].get()) < 0:
                k = 1
                o_val = float(globals()['prod_{}k'.format(i)].get()) * -1
                globals()['prod_{}'.format(i)].delete(0, END)
                globals()['prod_{}k'.format(i)].delete(0, END)
                log_o2 = False
                while k <= num_str:
                    if globals()['reag_{}'.format(k)].get() == '':
                        globals()['reag_{}'.format(k)].insert(0, 'O2')
                        globals()['reag_{}k'.format(k)].insert(0, o_val)
                        log_o2 = True
                        break
                    k += 1
                if log_o2 is False:
                    click_button_p()
                    globals()['reag_{}'.format(k)].insert(0, 'O2')
                    globals()['reag_{}k'.format(k)].insert(0, o_val)
            i += 1
    elif globals()['log_mem_{}'.format(q)] is False:
        messagebox.showerror("Ошибка", "Нет коэффициента топлива при φ{} = 1".format(q))


def click_button_range(q):
    '''просчитать диапазон значений fi'''
    global cbtn_1, cbtn_2, cbtnvar_1, cbtnvar_2, log_range
    globals()['log_range_{}'.format(q)] = True
    range_ok = True
    e_from = globals()['entry{}_st'.format(q)].get()
    e_to = globals()['entry{}_fn'.format(q)].get()
    e_step = globals()['entry{}_sp'.format(q)].get()
    if e_from != '':
        e_from = e_from.replace(',', '.')
        if isnotfloat(e_from):
            messagebox.showerror("Ошибка", "Введенное значение φ{}(нач.) не является числом".format(q))
            range_ok = False
        else:
            e_from = float(e_from)
    else:
        messagebox.showerror("Ошибка", "Значение φ{}(нач.) не указано".format(q))
        range_ok = False
    if e_to != '':
        e_to = e_to.replace(',', '.')
        if isnotfloat(e_to):
            messagebox.showerror("Ошибка", "Введенное значение φ{}(кон.) не является числом".format(q))
            range_ok = False
        else:
            e_to = float(e_to)
    else:
        messagebox.showerror("Ошибка", "Значение φ{}(кон.) не указано".format(q))
        range_ok = False
    if e_step != '':
        e_step = e_step.replace(',', '.')
        if isnotfloat(e_step):
            messagebox.showerror("Ошибка", "Введенное значение шага φ{} не является числом".format(q))
            range_ok = False
        else:
            e_step = round(float(e_step), 3)
    else:
        messagebox.showerror("Ошибка", "Значение шага φ{} не указано".format(q))
        range_ok = False
    if range_ok:
        for f in glob.glob('output*.txt'):
            os.remove(f)
        file = open("output_temp.txt", "w")
        file.write('#ф{}        T1    T2    T3\n'.format(q))
        file.close()
        list_val = []
        while e_to > e_from:
            list_val.append(e_from)
            e_from = round((e_from + e_step), 3)
        list_val.append(e_to)
        for elem in list_val:
            globals()['fi_{}'.format(q)].delete(0, END)
            globals()['fi_{}'.format(q)].insert(0, elem)
            click_button_fi(q)
            log_range = True
            click_button_3(q)
            log_range = False
        globals()['log_range_{}'.format(q)] = False
        if cbtnvar_2.get() == 1:
            os.startfile('output_temp.txt')
        if cbtnvar_1.get() == 1:
            with open("output_temp.txt") as file:
                '''построение графика T = f(φ) по полученным точкам'''
                x = np.array([])
                y1 = np.array([])
                y2 = np.array([])
                y3 = np.array([])
                for line in file:
                    if line[0] != '#':
                        spl_string = line.split()
                        x = np.append(x, float(spl_string[0]))
                        y1 = np.append(y1, float(spl_string[1]))
                        y2 = np.append(y2, float(spl_string[2]))
                        y3 = np.append(y3, float(spl_string[3]))
            plt.plot(x, y1, marker='o', color='r', label='T1 data')
            plt.plot(x, y2, marker='o', color='g', label='T2 data')
            plt.plot(x, y3, marker='o', color='b', label='T3 data')
            plt.ylim(273, )
            plt.legend(loc='upper left')
            plt.title('T = f(ф)')
            plt.ylabel('T, K')
            plt.xlabel('ф')
            plt.grid(True)
            plt.show()
    else:
        globals()['log_range_{}'.format(q)] = False


def click_button_save():
    global mass, area, ftime, tig, nh2o, fi, num_str
    file_name = fd.asksaveasfilename(filetypes=[('text files', '*.txt')])
    if len(file_name) > 4:
        file_name_end = file_name[-4:-1] + file_name[-1]
        if file_name_end != '.txt':
            file_name = file_name + '.txt'
    file = open(file_name, 'w')
    string = 'Tcalc input file\n------------------------------------------------------------------------\n' \
             'Коэффициент                Соединение\n' \
             '---------------Реагенты-------------------------------------------------\n'
    file.write(string)
    i = 1
    while i < num_str + 1:
        s2 = globals()['reag_{}'.format(i)].get()
        s1 = globals()['reag_{}k'.format(i)].get()
        if s1 == '':
            s1 = 'non'
        if s2 == '':
            s2 = 'non'
        string = s1 + ' ' + s2 + '\n'
        file.write(string)
        i += 1
    string = '---------------Продукты-------------------------------------------------\n'
    file.write(string)
    i = 1
    while i < num_str + 1:
        s2 = globals()['prod_{}'.format(i)].get()
        s1 = globals()['prod_{}k'.format(i)].get()
        if s1 == '':
            s1 = 'non'
        if s2 == '':
            s2 = 'non'
        string = s1 + ' ' + s2 + '\n'
        file.write(string)
        i += 1
    s1 = mass.get()
    s2 = area.get()
    s3 = ftime.get()
    s4 = tig.get()
    s5 = nh2o.get()
    string = '---------------Параметры_реакции----------------------------------------\n' \
             'Масса продукта, г: {}\nПлощадь излучающей поверхности, м^2: {}\n' \
             'Время горения, с: {}\nТемпература возгорания, K: {}\nКоличество воды в кристаллогидрате: {}'.format(s1, s2, s3, s4, s5)
    file.write(string)
    file.close()


def click_button_0():
    '''инициализация перехода со стартового к рабочему окну'''
    global num_str, label10, label11, mass, area, ftime, fi, reag_2k, log_mem, tig, nh2o, label5, label6, label7, \
        label8, label9, label10, label11, label12, label13, label14, label15, label16, label17, label18, label19, \
        label20, label21, btn_1, btn_2, btn_3, btn_u, btn_p, btn_m, btn_ns, btn_del_reag, btn_del_prod, entry_from, \
        entry_to, entry_step, label1, label2, label3, label4, mainmenu, cbtn_1, cbtn_2, cbtnvar_1, \
        cbtnvar_2, ltemp, etemp, fi_list, cbtnvar_1, cbtnvar_2, log_range
    log_mem = False     # есть/нет записанное значение fi = 1
    log_range = False   # нужно/не нужно проводить серию расчетов
    btn_0.destroy()
    btn_exit.destroy()
    label01.destroy()
    label02.destroy()
    label03.destroy()
    background_label.destroy()
    root.resizable(width=True, height=True)
    root.geometry("500x740")
    label1 = Label(text='Реагенты', font="Arial 12", justify=LEFT)
    label1.place(x=9, y=10)
    label2 = Label(text='коэф.', font="Arial 12", justify=LEFT)
    label2.place(x=179, y=10)
    label3 = Label(text='Продукты', font="Arial 12", justify=LEFT)
    label3.place(x=258, y=10)
    label4 = Label(text='коэф.', font="Arial 12", justify=LEFT)
    label4.place(x=428, y=10)
    label5 = Label(text='Масса целевого продукта, г', font="Arial 12", justify=LEFT)
    label5.place(x=10, y=205)
    label6 = Label(text='Площадь излучающей поверхности, м^2', font="Arial 12", justify=LEFT)
    label6.place(x=10, y=230)
    label7 = Label(text='Время горения, с', font="Arial 12", justify=LEFT)
    label7.place(x=10, y=255)
    label8 = Label(text='Температура возгорания, K', font="Arial 12", justify=LEFT)
    label8.place(x=10, y=280)
    label9 = Label(text='Количество воды в кристаллогидрате', font="Arial 12", justify=LEFT)
    label9.place(x=10, y=305)
    ltemp = Label(text='Температурный интервал от 273 K до', font="Arial 12", justify=LEFT)
    ltemp.place(x=10, y=330)

    fi_list = []

    while num_str < 5:
        globals()['reag_{}o'.format(num_str + 1)] = Option_Menu(root, cursor='hand2', name='reag_{}o'.format(num_str), relief=RIDGE)
        globals()['reag_{}o'.format(num_str + 1)].opt_num = num_str + 1
        globals()['reag_{}o'.format(num_str + 1)].relief(RIDGE, RAISED)
        globals()['reag_{}o'.format(num_str + 1)].place(x=10, y=35 + 25 * num_str)
        globals()['reag_{}'.format(num_str + 1)] = Entry(width=15, font="Arial 12")
        globals()['reag_{}'.format(num_str + 1)].place(x=32, y=35 + 25 * num_str)
        globals()['reag_{}k'.format(num_str + 1)] = Entry(width=5, font="Arial 12")
        globals()['reag_{}k'.format(num_str + 1)].place(x=180, y=35 + 25 * num_str)
        globals()['prod_{}o'.format(num_str + 1)] = Option_Menu(root, cursor='hand2', name='prod_{}o'.format(num_str), relief=RIDGE, value=('-', 'Целевой продукт (Ob)'))
        globals()['prod_{}o'.format(num_str + 1)].opt_num = num_str + 1
        globals()['prod_{}o'.format(num_str + 1)].relief(RIDGE, RAISED)
        globals()['prod_{}o'.format(num_str + 1)].place(x=260, y=35 + 25 * num_str)
        globals()['prod_{}'.format(num_str + 1)] = Entry(width=15, font="Arial 12")
        globals()['prod_{}'.format(num_str + 1)].place(x=282, y=35 + 25 * num_str)
        globals()['prod_{}k'.format(num_str + 1)] = Entry(width=5, font="Arial 12")
        globals()['prod_{}k'.format(num_str + 1)].place(x=430, y=35 + 25 * num_str)
        num_str += 1

    reag_1o.remap_default(1, value=('-', 'Окислитель (Ox)', 'Топливо (F)'))
    reag_2o.remap_default(2, value=('-', 'Окислитель (Ox)', 'Топливо (F)'))
    prod_1o.remap_default(1, value=('-', 'Целевой продукт (Ob)'))

    mass = Entry(width=12, font="Arial 12")  # масса продукта
    mass.place(x=365, y=205)
    mass.insert(0, 2)
    area = Entry(width=12, font="Arial 12")  # площадь поверхности
    area.place(x=365, y=230)
    area.insert(0, 0.002376)
    ftime = Entry(width=12, font="Arial 12")  # время горения
    ftime.place(x=365, y=255)
    ftime.insert(0, 1.446)
    tig = Entry(width=12, font="Arial 12")  # температура возгорания
    tig.place(x=365, y=280)
    tig.insert(0, 438)
    nh2o = Entry(width=12, font="Arial 12")  # количество воды в кристаллогридрате
    nh2o.place(x=365, y=305)
    nh2o.insert(0, 0)
    etemp = Entry(width=12, font="Arial 12")  # предел температурного интервала поиска
    etemp.place(x=365, y=330)
    etemp.insert(0, 3500)

    btn_1 = Button(text="Очистить", background="#555", foreground="#ccc",
                   padx="20", pady="8", font="16", command=click_button_1)
    btn_1.place(x=75, y=380, anchor="c", height=30, width=135, bordermode=OUTSIDE)

    btn_2 = Button(text="Загрузить данные", background="#555", foreground="#ccc",
                   padx="20", pady="8", font="16", command=click_button_2)
    btn_2.place(x=245, y=380, anchor="c", height=30, width=135, bordermode=OUTSIDE)

    btn_3 = Button(text="Пуск", background="#555", foreground="#ccc",
                   padx="20", pady="8", font="16", command=click_button_3)
    btn_3.place(x=411, y=380, anchor="c", height=30, width=135, bordermode=OUTSIDE)

    btn_p = Button(text="+", background="#555", foreground="#ccc",
                   padx="20", pady="8", font="7", command=click_button_p)
    btn_p.place(x=222, y=167, anchor="c", height=12, width=12, bordermode=OUTSIDE)

    btn_m = Button(text="-", background="#555", foreground="#ccc",
                   padx="20", pady="8", font="7", command=click_button_m)
    btn_m.place(x=205, y=167, anchor="c", height=12, width=12, bordermode=OUTSIDE)

    btn_u = Button(text="Уравнять", background="#555", foreground="#ccc",
                   padx="20", pady="8", font="7", command=click_button_u)
    btn_u.place(x=411, y=177, anchor="c", height=30, width=135, bordermode=OUTSIDE)

    btn_ns = Button(text="Новое соединение", background="#555", foreground="#ccc",
                   padx="20", pady="8", font="7", command=click_button_ns)
    btn_ns.place(x=75, y=177, anchor="c", height=30, width=135, bordermode=OUTSIDE)

    btn_del_reag = Button(text="Del", background="#555", foreground="#ccc",
                       padx="20", pady="8", font="Arial 8", command=click_button_del_reag)
    btn_del_reag.place(x=205, y=8, anchor="c", height=15, width=40, bordermode=OUTSIDE)

    btn_del_prod = Button(text="Del", background="#555", foreground="#ccc",
                          padx="20", pady="8", font="Arial 8", command=click_button_del_prod)
    btn_del_prod.place(x=455, y=8, anchor="c", height=15, width=40, bordermode=OUTSIDE)

    label10 = Label(text='1) Адиабатическое приближение при стандартных dH и Cp:', font="Arial 12", justify=LEFT)
    label10.place(x=10, y=410)
    label11 = Label(text='Максимальная температура горения:', font="Arial 12", justify=LEFT)
    label11.place(x=10, y=435)
    label12 = Label(text='Температурный эффект:', font="Arial 12", justify=LEFT)
    label12.place(x=10, y=460)
    label13 = Label(text='2) Адиабатическое приближение с учетом dH = f(T) и Cp = f(T):', font="Arial 12", justify=LEFT)
    label13.place(x=10, y=485)
    label14 = Label(text='Максимальная температура горения:', font="Arial 12", justify=LEFT)
    label14.place(x=10, y=510)
    label15 = Label(text='Температурный эффект:', font="Arial 12", justify=LEFT)
    label15.place(x=10, y=535)
    label16 = Label(text='3) Учет расширения газа:', font="Arial 12", justify=LEFT)
    label16.place(x=10, y=560)
    label17 = Label(text='Максимальная температура горения:', font="Arial 12", justify=LEFT)
    label17.place(x=10, y=585)
    label18 = Label(text='Температурный эффект:', font="Arial 12", justify=LEFT)
    label18.place(x=10, y=610)
    label19 = Label(text='4) Учет расширения газа и излучения:', font="Arial 12", justify=LEFT)
    label19.place(x=10, y=635)
    label20 = Label(text='Максимальная температура горения:', font="Arial 12", justify=LEFT)
    label20.place(x=10, y=660)
    label21 = Label(text='Температурный эффект:', font="Arial 12", justify=LEFT)
    label21.place(x=10, y=685)

    mainmenu = Menu(root)
    root.config(menu=mainmenu)
    filemenu = Menu(mainmenu, tearoff=0)
    filemenu.add_command(label='Открыть...', command=click_button_open)
    filemenu.add_command(label='Очистить', command=click_button_1)
    filemenu.add_command(label='Сохранить...', command=click_button_save)
    filemenu.add_command(label='Начальный экран', command=click_button_return)
    filemenu.add_command(label='Выход', command=exit)
    bdmenu = Menu(mainmenu, tearoff=0)
    bdmenu.add_command(label='Найти в базе...', command=click_button_fs)
    bdmenu.add_command(label='Новое соединение', command=click_button_ns)
    helpmenu = Menu(mainmenu, tearoff=0)
    helpmenu.add_command(label='Помощь', command=click_button_help)
    helpmenu.add_command(label='О программе', command=click_button_info)
    mainmenu.add_cascade(label="Файл", menu=filemenu)
    mainmenu.add_cascade(label='База данных', menu=bdmenu)
    mainmenu.add_cascade(label="Справка", menu=helpmenu)

molar_mass = {'H': 1.008, 'He': 4.003, 'Li': 6.941, 'Be': 9.0122, 'B': 10.811, 'C': 12.011, 'N': 14.007, 'O': 15.999,
              'F': 18.998, 'Ne': 20.179, 'Na': 22.99, 'Mg': 24.312, 'Al': 26.092, 'Si': 28.086, 'P': 30.974,
              'S': 32.064, 'Cl': 35.453, 'Ar': 39.948, 'K': 39.102, 'Ca': 40.08, 'Sc': 44.956, 'Ti': 47.956,
              'V': 50.941, 'Cr': 51.996, 'Mn': 54.938, 'Fe': 55.849, 'Co': 58.933, 'Ni': 58.7, 'Cu': 63.546,
              'Zn': 65.37, 'Ga': 69.72, 'Ge': 72.59, 'As': 74.922, 'Se': 78.96, 'Br': 79.904, 'Kr': 83.8, 'Rb': 85.468,
              'Sr': 87.62, 'Y': 88.906, 'Zr': 91.22, 'Nb': 92.906, 'Mo': 95.94, 'Tc': 99, 'Ru': 101.07, 'Rh': 102.906,
              'Pd': 106.4, 'Ag': 107.868, 'Cd': 112.41, 'In': 114.82, 'Sn': 118.69, 'Sb': 121.75, 'Te': 127.6,
              'I': 126.905, 'Xe': 131.3, 'Cs': 132.905, 'Ba': 137.34, 'La': 138.906, 'Ce': 140.12, 'Pr': 140.908,
              'Nd': 144.24, 'Pm': 145, 'Sm': 150.4, 'Eu': 151.96, 'Gd': 157.25, 'Tb': 158.926, 'Dy': 162.5,
              'Ho': 164.93, 'Er': 167.26, 'Tm': 168.934, 'Yb': 173.04, 'Lu': 174.97, 'Hf': 178.49, 'Ta': 180.948,
              'W': 183.85, 'Re': 186.207, 'Os': 190.2, 'Ir': 192.22, 'Pt': 195.09, 'Au': 196.967, 'Hg': 200.59,
              'Tl': 204.37, 'Pb': 207.19, 'Bi': 208.98, 'Po': 210, 'At': 210, 'Rn': 222, 'Fr': 223, 'Ra': 226,
              'Ac': 227, 'Th': 232.038, 'Pa': 231.036, 'U': 238.029, 'Np': 237, 'Pu': 244, 'Am': 243, 'Cm': 247,
              'Bk': 247, 'Cf': 251, 'Es': 252, 'Fm': 257, 'Md': 258, 'No': 259, 'Lr': 260.11, 'Rf': 261, 'Db': 262}

root = Tk()
root.title("SCSTempCal")
root.geometry("500x740")
root.resizable(width=False, height=False)

cbtnvar_1 = IntVar()
cbtnvar_1.set(1)
cbtnvar_2 = IntVar()
cbtnvar_2.set(0)
cbtn_log = False

btn_0 = Button(text="Начать работу", background="#555", foreground="#ccc",
               padx="20", pady="8", font="16", command=click_button_0)
btn_0.place(x=150, y=620, anchor="c", height=30, width=135, bordermode=OUTSIDE)
btn_exit = Button(text="Выход", background="#555", foreground="#ccc",
               padx="20", pady="8", font="16", command=click_button_exit)
btn_exit.place(x=300, y=620, anchor="c", height=30, width=135, bordermode=OUTSIDE)
label01 = Label(text='Программа расчета температур горения в реакциях SCS\n(SCSTempCal)', font="Arial 12", justify=LEFT)
label01.place(x=10, y=20)
label02 = Label(text='Версия 1.0', font="Arial 12", justify=LEFT)
label02.place(x=10, y=60)
label03 = Label(text='Авторы: Халиуллин Ш.М., Попов И.С.', font="Arial 12", justify=LEFT)
label03.place(x=10, y=80)

filename1 = PhotoImage(file="fig.png")
background_label = Label(image=filename1)
background_label.place(x=0, y=140)

num_str = 0

root.mainloop()
