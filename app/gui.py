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
    CODE_DE = 'de'
    CODE_RU = 'ru'
    LEFT_MOUSE_BUTTON = "<Button-1>"
    PAD_X = 18
    PAD_Y = 24

    # инициализация переменных окон
    def __init__(self):
        self.window_layer_0 = tk.Tk()
        self.window_layer_1 = None
        self.window_layer_2 = None

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
    def make_window_layer_0(self):
        self.window_layer_0.configure(bg=self.BG)
        self.window_layer_0.resizable(False, False)

        frame = tk.Frame(self.window_layer_0, relief=tk.RAISED, background=self.BG)
        frame.grid(padx=self.PAD_X, pady=self.PAD_Y)

        label = self.make_label('Выберите запрос', frame)
        label.grid(column=0, row=0, columnspan=4, pady=self.PAD_Y)

        button_news = self.make_button('Новости', frame, lambda event: self.make_window_layer_1('news'))
        button_news.grid(column=0, row=1, padx=self.PAD_X, pady=self.PAD_Y)

        button_weather = self.make_button('Погода', frame, lambda event: self.make_window_layer_1('weather'))
        button_weather.grid(column=1, row=1, padx=self.PAD_X, pady=self.PAD_Y)

        button_rate = self.make_button('Курс', frame, lambda event: self.make_window_layer_1('rate'))
        button_rate.grid(column=2, row=1, padx=self.PAD_X, pady=self.PAD_Y)

        button_covid = self.make_button('COVID-19', frame, lambda event: self.make_window_layer_1('covid'))
        button_covid.grid(column=3, row=1, padx=self.PAD_X, pady=self.PAD_Y)

    # создания окна выбора страны или вывода курса
    def make_window_layer_1(self, action):
        if self.window_layer_1:
            self.window_layer_1.destroy()

        if action == 'rate':
            self.make_window_result(lambda: ButtonRate().action(), layer_2=False)
            return

        window = tk.Toplevel(self.window_layer_0, bg=self.BG)
        window.resizable(False, False)
        self.window_layer_1 = window

        frame = tk.Frame(window, relief=tk.RAISED, background=self.BG)
        frame.grid(padx=self.PAD_X, pady=self.PAD_Y)

        label = self.make_label('Какая страна?', frame)
        label.grid(column=0, row=0, columnspan=2, pady=self.PAD_Y)

        button_de = self.make_button('Германия', frame)
        button_de.grid(column=0, row=1, padx=self.PAD_X, pady=self.PAD_Y)

        button_ru = self.make_button('Россия', frame)
        button_ru.grid(column=1, row=1, padx=self.PAD_X, pady=self.PAD_Y)

        if action == 'covid':
            button_de.bind(self.LEFT_MOUSE_BUTTON,
                           lambda event: self.make_window_result(lambda: ButtonCovid().action(self.CODE_DE)))
            button_ru.bind(self.LEFT_MOUSE_BUTTON,
                           lambda event: self.make_window_result(lambda: ButtonCovid().action(self.CODE_RU)))
        elif action == 'news':
            button_de.bind(self.LEFT_MOUSE_BUTTON,
                           lambda event: self.make_window_result(lambda: ButtonNews().action(self.CODE_DE)))
            button_ru.bind(self.LEFT_MOUSE_BUTTON,
                           lambda event: self.make_window_result(lambda: ButtonNews().action(self.CODE_RU)))
        elif action == 'weather':
            button_de.bind(self.LEFT_MOUSE_BUTTON,
                           lambda event: self.make_window_result(lambda: ButtonWeather().action(self.CODE_DE)))
            button_ru.bind(self.LEFT_MOUSE_BUTTON,
                           lambda event: self.make_window_result(lambda: ButtonWeather().action(self.CODE_RU)))

    # создание окна с ответом на запрос
    def make_window_result(self, action, layer_2=True):
        if self.window_layer_2:
            self.window_layer_2.destroy()

        if layer_2:
            window = tk.Toplevel(self.window_layer_1, bg=self.BG, padx=self.PAD_X, pady=self.PAD_Y)
            self.window_layer_2 = window
        else:
            window = tk.Toplevel(self.window_layer_0, bg=self.BG, padx=self.PAD_X, pady=self.PAD_Y)
            self.window_layer_1 = window

        window.resizable(False, False)

        label = self.make_label(action(), window, 12)
        label.pack()

    # выполнение приложения
    def run(self):
        self.make_window_layer_0()
        self.window_layer_0.mainloop()


if __name__ == '__main__':
    App().run()
