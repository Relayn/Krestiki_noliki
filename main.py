import tkinter as tk
from tkinter import messagebox


class TicTacToe:
    """
    Класс для реализации игры "Крестики-нолики".
    Управляет состоянием игры, интерфейсом и логикой.
    """

    def __init__(self):
        """Инициализация игры."""
        # Настройки интерфейса
        self.BG_COLOR = "#2E3440"  # Цвет фона
        self.BUTTON_COLOR = "#4C566A"  # Цвет кнопок
        self.TEXT_COLOR = "#ECEFF4"  # Цвет текста
        self.WIN_COLOR = "#A3BE8C"  # Цвет для победного сообщения
        self.DRAW_COLOR = "#EBCB8B"  # Цвет для ничьей

        self.BUTTON_FONT = ("Arial", 24, "bold")  # Шрифт для кнопок
        self.SCORE_FONT = ("Arial", 16, "bold")  # Шрифт для счёта

        # Инициализация окна
        self.window = tk.Tk()
        self.window.title("Крестики-нолики")
        self.window.geometry("345x450")
        self.window.configure(bg=self.BG_COLOR)

        # Переменные игры
        self.current_player = "X"
        self.buttons = []
        self.score_X = 0  # Счётчик побед игрока X
        self.score_0 = 0  # Счётчик побед игрока 0

        # Создание интерфейса
        self.create_buttons()
        self.create_reset_button()
        self.create_score_label()

    def create_buttons(self):
        """Создаёт кнопки для игрового поля."""
        for i in range(3):
            row = []
            for j in range(3):
                btn = tk.Button(
                    self.window,
                    text="",
                    font=self.BUTTON_FONT,
                    width=5,
                    height=2,
                    bg=self.BUTTON_COLOR,
                    fg=self.TEXT_COLOR,
                    relief="flat",
                    command=lambda r=i, c=j: self.on_click(r, c),
                )
                btn.grid(row=i, column=j, padx=5, pady=5)
                row.append(btn)
            self.buttons.append(row)

    def create_reset_button(self):
        """Создаёт кнопку сброса."""
        self.reset_button = tk.Button(
            self.window,
            text="Сброс",
            font=self.SCORE_FONT,
            bg=self.BUTTON_COLOR,
            fg=self.TEXT_COLOR,
            relief="flat",
            command=self.reset_game,
        )
        self.reset_button.grid(row=3, column=0, columnspan=3, sticky="we", padx=10, pady=10)

    def create_score_label(self):
        """Создаёт метку для отображения счёта."""
        self.score_label = tk.Label(
            self.window,
            text=f"X: {self.score_X} | 0: {self.score_0}",
            font=self.SCORE_FONT,
            bg=self.BG_COLOR,
            fg=self.TEXT_COLOR,
        )
        self.score_label.grid(row=4, column=0, columnspan=3, pady=10)

    def check_winner(self):
        """
        Проверяет, есть ли победитель на текущем поле.
        Возвращает True, если победитель найден, иначе False.
        """
        for i in range(3):
            if self.buttons[i][0]["text"] == self.buttons[i][1]["text"] == self.buttons[i][2]["text"] != "":
                return True
            if self.buttons[0][i]["text"] == self.buttons[1][i]["text"] == self.buttons[2][i]["text"] != "":
                return True

        if self.buttons[0][0]["text"] == self.buttons[1][1]["text"] == self.buttons[2][2]["text"] != "":
            return True
        if self.buttons[0][2]["text"] == self.buttons[1][1]["text"] == self.buttons[2][0]["text"] != "":
            return True

        return False

    def check_draw(self):
        """
        Проверяет, является ли текущее состояние игры ничьей.
        Возвращает True, если ничья, иначе False.
        """
        for row in self.buttons:
            for btn in row:
                if btn["text"] == "":
                    return False  # Если есть пустая клетка, ничьей нет
        return True  # Все клетки заполнены

    def highlight_buttons(self, color):
        """Подсвечивает все кнопки указанным цветом."""
        for row in self.buttons:
            for btn in row:
                btn.config(bg=color)

    def handle_win(self):
        """Обрабатывает победу текущего игрока."""
        if self.current_player == "X":
            self.score_X += 1
        else:
            self.score_0 += 1

        self.score_label.config(text=f"X: {self.score_X} | 0: {self.score_0}")  # Обновляем счёт
        self.highlight_buttons(self.WIN_COLOR)  # Подсветка кнопок при победе
        messagebox.showinfo("Игра окончена", f"Игрок {self.current_player} победил!")

        if self.score_X == 3 or self.score_0 == 3:
            messagebox.showinfo("Конец игры", f"Игрок {self.current_player} выиграл матч!")
            self.reset_game(full_reset=True)  # Полный сброс (включая счёт)
        else:
            self.reset_game()  # Сброс только поля

    def handle_draw(self):
        """Обрабатывает ничью."""
        self.highlight_buttons(self.DRAW_COLOR)  # Подсветка кнопок при ничьей
        messagebox.showinfo("Игра окончена", "Ничья!")
        self.reset_game()  # Сброс поля после ничьей

    def on_click(self, row, col):
        """
        Обрабатывает клик по кнопке.
        Обновляет состояние игры и интерфейс.
        """
        if self.buttons[row][col]['text'] != "":
            return

        self.buttons[row][col]['text'] = self.current_player

        if self.check_winner():
            self.handle_win()
        elif self.check_draw():
            self.handle_draw()

        self.current_player = "0" if self.current_player == "X" else "X"

    def reset_game(self, full_reset=False):
        """
        Сбрасывает игру.
        Если full_reset=True, сбрасывает и счёт.
        """
        self.current_player = "X"  # Сброс текущего игрока
        for row in self.buttons:
            for btn in row:
                btn["text"] = ""  # Очистка текста на кнопках
                btn.config(bg=self.BUTTON_COLOR)  # Возвращаем стандартный цвет кнопок

        if full_reset:
            self.score_X = 0
            self.score_0 = 0
            self.score_label.config(text=f"X: {self.score_X} | 0: {self.score_0}")  # Обновляем счёт

    def run(self):
        """Запускает игру."""
        self.window.mainloop()


if __name__ == "__main__":
    game = TicTacToe()
    game.run()