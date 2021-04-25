from buttons.covid import ButtonCovid
from buttons.news import ButtonNews
from buttons.rate import ButtonRate
from buttons.weather import ButtonWeather
from tkinter import ttk
import tkinter as tk
import tkinter.font as tkfont


class App:
    BUTTON_BG = '#767777'
    BUTTON_HEIGHT = 4
    BUTTON_WIDTH = 9

    BG = '#434444'
    FG = '#FFFFFF'
    CODE_BY = 'by'
    CODE_RU = 'ru'
    LEFT_MOUSE_BUTTON = "<Button-1>"
    PAD_X = 18
    PAD_Y = 24

    # инициализация переменных окон
    def __init__(self):
        self.window_main = tk.Tk()
        self.window_choice = None
        self.window_result = None

    # создание кнопки
    def make_button(self, text, master, action=None, font_size=12):
        font = tkfont.Font(size=font_size)

        button = tk.Button(master, text=text, width=self.BUTTON_WIDTH, height=self.BUTTON_HEIGHT, fg=self.FG,
                           bg=self.BUTTON_BG, highlightthickness=0, bd=0, font=font)

        if action:
            button.bind(self.LEFT_MOUSE_BUTTON, action)

        return button

    # создание надписи
    def make_label(self, text, master, font_size=18):
        font = tkfont.Font(size=font_size)
        return ttk.Label(master, text=text, foreground=self.FG, background=self.BG, font=font)

    # создание главного окна
    def make_window_main(self):
        self.window_main.configure(bg=self.BG)
        self.window_main.resizable(False, False)

        frame = tk.Frame(self.window_main, relief=tk.RAISED, background=self.BG)
        frame.grid(padx=self.PAD_X, pady=self.PAD_Y)

        label = self.make_label('Выберите запрос', frame)
        label.grid(column=0, row=0, columnspan=4, pady=self.PAD_Y)

        button_news = self.make_button('Новости', frame, lambda event: self.make_window_choice('news'))
        button_news.grid(column=0, row=1, padx=self.PAD_X, pady=self.PAD_Y)

        button_weather = self.make_button('Погода', frame, lambda event: self.make_window_choice('weather'))
        button_weather.grid(column=1, row=1, padx=self.PAD_X, pady=self.PAD_Y)

        button_rate = self.make_button('Курс', frame, lambda event: self.make_window_choice('rate'))
        button_rate.grid(column=2, row=1, padx=self.PAD_X, pady=self.PAD_Y)

        button_covid = self.make_button('COVID-19', frame, lambda event: self.make_window_choice('covid'))
        button_covid.grid(column=3, row=1, padx=self.PAD_X, pady=self.PAD_Y)

    # создания окна выбора страны
    def make_window_choice(self, action):
        if self.window_choice:
            self.window_choice.destroy()

        window = tk.Toplevel(self.window_main, bg=self.BG)
        window.resizable(False, False)
        self.window_choice = window

        frame = tk.Frame(window, relief=tk.RAISED, background=self.BG)
        frame.grid(padx=self.PAD_X, pady=self.PAD_Y)

        label = self.make_label('Какая страна?', frame)
        label.grid(column=0, row=0, columnspan=2, pady=self.PAD_Y)

        button_by = self.make_button('Белоруссия', frame)
        button_by.grid(column=0, row=1, padx=self.PAD_X, pady=self.PAD_Y)

        button_ru = self.make_button('Россия', frame)
        button_ru.grid(column=1, row=1, padx=self.PAD_X, pady=self.PAD_Y)

        if action == 'covid':
            button_by.bind(self.LEFT_MOUSE_BUTTON,
                           lambda event: self.make_window_result(lambda: ButtonCovid().action(self.CODE_BY)))
            button_ru.bind(self.LEFT_MOUSE_BUTTON,
                           lambda event: self.make_window_result(lambda: ButtonCovid().action(self.CODE_RU)))
        elif action == 'news':
            button_by.bind(self.LEFT_MOUSE_BUTTON,
                           lambda event: self.make_window_result(lambda: ButtonNews().action(self.CODE_BY)))
            button_ru.bind(self.LEFT_MOUSE_BUTTON,
                           lambda event: self.make_window_result(lambda: ButtonNews().action(self.CODE_RU)))
        elif action == 'rate':
            button_by.bind(self.LEFT_MOUSE_BUTTON,
                           lambda event: self.make_window_result(lambda: ButtonRate().action(self.CODE_BY)))
            button_ru.bind(self.LEFT_MOUSE_BUTTON,
                           lambda event: self.make_window_result(lambda: ButtonRate().action(self.CODE_RU)))
        elif action == 'weather':
            button_by.bind(self.LEFT_MOUSE_BUTTON,
                           lambda event: self.make_window_result(lambda: ButtonWeather().action(self.CODE_BY)))
            button_ru.bind(self.LEFT_MOUSE_BUTTON,
                           lambda event: self.make_window_result(lambda: ButtonWeather().action(self.CODE_RU)))

    # создание окна с ответом на запрос
    def make_window_result(self, action):
        if self.window_result:
            self.window_result.destroy()

        window = tk.Toplevel(self.window_choice, bg=self.BG, padx=self.PAD_X, pady=self.PAD_Y)
        window.resizable(False, False)
        self.window_result = window

        label = self.make_label(action(), window, 12)
        label.pack()

    # выполнение приложения
    def run(self):
        self.make_window_main()
        self.window_main.mainloop()


if __name__ == '__main__':
    App().run()
