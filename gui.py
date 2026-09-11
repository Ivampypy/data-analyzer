import tkinter as tk
from tkinter import messagebox
from dataanalyzer import*

root=tk.Tk()

info={"Median": "Медиана — это число, которое стоит посередине, если все числа расположить по порядку. Например:"
    "2,4,5,7,8 - медиана 5; если чисел четное кол-во, то для  2 4 5 6 7 8 медиана - 5+6/2=1=5.5",
      "Mode": "Мода - это самое часто встречаемое число в массиве. Например, для 2 2 4 5 6 7 модой будет число 2. ",
      "Q1": " Q1 (первый квартиль) — значение, ниже которого находится 25% всех данных. Иначе говоря, медиана первой половины в упорядоченном массиве.",
      "Variance":" Дисперсия — показывает, насколько сильно значения разбросаны относительно среднего. Чем больше дисперсия, тем сильнее разброс.",
      "Q3":"Q3 (третий квартиль) — значение, ниже которого находится 75% всех данных. Иначе говоря, медиана второй половины в упор. массиве",
      "Standard devation": " Стандартное отклонение — показывает, насколько в среднем значения отклоняются от среднего. Чем больше оно, тем сильнее разброс.",
      "IQR":"Iqr = Q3 - Q1"}


def show_page2():
    page1.pack_forget()
    page2.pack(fill='both',expand=True)


def back_to_1():
    page2.pack_forget()
    page1.pack(fill='both',expand=True)

def back_to_2():
    page3.pack_forget()
    page2.pack(fill='both',expand=True)


root.title('Data Analyzer')
root.geometry('700x500')

page1=tk.Frame(root)

label_welcome=tk.Label(page1,text='Welcome to Trial! To start, please enter parameters of your array')
label_welcome.pack(pady=40,padx=50)

label_l=tk.Label(page1,text='LENGTH:')
label_l.pack()

length_entry=tk.Entry(page1)
length_entry.pack()

label_borders=tk.Label(page1,text='BORDERS (with _):')
label_borders.pack()

borders_entry=tk.Entry(page1)
borders_entry.pack()

data=None
def get_data():
    global data
    try:
        length = int(length_entry.get())
        low_b, high_b = map(int, borders_entry.get().split())

        data=create_array(length,low_b,high_b)
        show_page2()
    except ValueError as error:
        messagebox.showerror('Input error',str(error))
  



button_start=tk.Button(page1,text='<<<<<<<Click here to continue and check sizes to avoid problems before>>>>>>>',command=get_data)
button_start.pack(pady=40)



page2=tk.Frame(root)

page1.pack(fill='both',expand=True)

buttons_frame=tk.Frame(page2)
buttons_frame.grid(row=1, column=0, padx=100, pady=50)

label_swipe=tk.Label(page2,text='WELCOME TO DATA ANALYZER!')
label_swipe.grid(row=0,column=0,columnspan=3)

page3=tk.Frame(root)

label_result=tk.Label(page3)
label_result.pack(pady=100)

def swipe(result):
    page2.pack_forget()
    page3.pack(fill='both',expand=True)
    label_result.config(text=f'<<<<<<<<Your result is {result}>>>>>>>>>>>',bg='white')



button_min=tk.Button(buttons_frame,text='1. Click to see minimum!',command=lambda: swipe(find_min(data)))
button_min.grid(column=0,row=1,padx=40,pady=15)



button_back_to_1=tk.Button(page2,text='<<<<Back to page 1>>>>>',command=back_to_1)
button_back_to_1.grid(row=10,
    column=0,
    columnspan=2)

button_back_to_2=tk.Button(page3,text='<<<<Back to page 2>>>>',command=back_to_2)
button_back_to_2.pack(pady=10)

button_max=tk.Button(buttons_frame,text='2. Click to see maximum!',command=lambda: swipe(find_max(data)))
button_max.grid(row=1,
    column=1,
    padx=40,
    pady=15)

button_mean=tk.Button(buttons_frame,text='3. Click to see average!',command=lambda: swipe(find_average(data)))
button_mean.grid(column=0,row=2,padx=40,pady=15)

button_median=tk.Button(buttons_frame,text='4. Click to see median!',command=lambda: (swipe(find_median(data)),messagebox.showinfo("What is Median?", info["Median"])))
button_median.grid(row=2,
    column=1,
    padx=40,
    pady=15)

button_mode=tk.Button(buttons_frame,text='5. Click to see mode!',command=lambda: (swipe(find_mode(data)),messagebox.showinfo("What is mode?",info["Mode"])))
button_mode.grid(column=0,row=3,padx=40,pady=15)

button_variance=tk.Button(buttons_frame,text='6. Click to see variance!',command=lambda: (swipe(find_variance(data)),messagebox.showinfo("What is variance",info['Variance'])))
button_variance.grid(row=3,
    column=1,
    padx=40,
    pady=15)

button_std=tk.Button(buttons_frame,text='7. Click to see standart deviation!',command=lambda: (swipe(find_stdev(data)),messagebox.showinfo("What is standard deviation",info['Standard devation'])))
button_std.grid(column=0,row=4,padx=40,pady=15)

button_q1=tk.Button(buttons_frame,text='8. Click to see Q1!',command=lambda: (swipe(find_q1(data)),messagebox.showinfo("What is Q1?",info["Q1"])))
button_q1.grid(row=4,
    column=1,
    padx=40,
    pady=15)

button_q3=tk.Button(buttons_frame,text='9. Click to see Q3!',command=lambda: (swipe(find_q3(data)),messagebox.showinfo("What is Q3?",info["Q3"])))
button_q3.grid(column=0,row=5,padx=40,pady=15)

button_iqr=tk.Button(buttons_frame,text='10. Click to see IQR!',command=lambda: (swipe(find_iqr(data)),messagebox.showinfo("What is IQR",info["IQR"])))
button_iqr.grid(row=5,
    column=1,
    padx=40,
    pady=15)

button_array=tk.Button(page2,text='11. Click to see array!',command=lambda: swipe((data)))
button_array.grid(column=0,row=6,columnspan=2,padx=40,pady=15)








root.mainloop()