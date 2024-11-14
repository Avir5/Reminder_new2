from tkinter import *
from tkinter import simpledialog as sd
from tkinter import messagebox as mb
import datetime
import pygame
import time

t = None #переменная для хранения метки времени
music = False  #Переменная для отслеживания проигрывания музыки


def set(): #функция установки напоминания
    global t, reminder_text
    rem_time = sd.askstring("Время напоминания", "Введите время напоминания в формате ЧЧ:ММ (в 24-часовом формате):")
    if rem_time:
        try:
            hour = int(rem_time.split(":")[0])
            minute = int(rem_time.split(":")[1])
            now = datetime.datetime.now()
            dt = now.replace(hour=hour, minute=minute, second=0)
            t = dt.timestamp()
            reminder_text = sd.askstring("Текст напоминания", "Введите текст напоминания:")
            label.config(text=f"Напоминание на {hour:02}:{minute:02} с текстом: {reminder_text}")
        except Exception as e:
            mb.showerror("Ошибка!", f"Произошла ошибка: {e}")


def check(): #функция проверки срабатывания таймера и запуска всплывающего окна
    global t
    if t:
        now = time.time()
        if now >= t:
            play_snd()
            t = None
            popup_window = Toplevel()
            popup_window.title('Сообщение о напоминании')
            popup_window.geometry("300x40")
            label_popup = Label(popup_window, text=reminder_text, font="Arial 17 bold")
            label_popup.pack()

    window.after(10000, check)

def play_snd(): #функция иницилизации звука, загрузки файла и проигрования мелодии
    global music
    music = True
    pygame.mixer.init()
    pygame.mixer.music.load("reminder.mp3")
    pygame.mixer.music.play()

def stop_music(): #функция для остановки проигрования мелодии
    global music
    if music:
        pygame.mixer.music.stop()
        music = False
    label.config(text="Установить новое напоминание")

window = Tk() #создание главного окна
window.title("Напоминание")

#блок меток и кнопок для задания параметров напоминания, остановки музыки
label = Label(text="Установите напоминание", font=("Arial", 14))
label.pack(pady=10)

set_button = Button(text="Установить напоминание", command=set)
set_button.pack(pady=10)

stop_button = Button(text="Остановить музыку", command=stop_music)
stop_button.pack(pady=5)

check()

# функция бесконечного цикла окна для ожидания любого взаимодействия с пользователем
window.mainloop()