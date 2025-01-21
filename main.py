import tkinter as tk
from tkinter import messagebox

# Настройки интерфейса
BG_COLOR = "#2E3440"  # Цвет фона
BUTTON_COLOR = "#4C566A"  # Цвет кнопок
TEXT_COLOR = "#ECEFF4"  # Цвет текста
WIN_COLOR = "#A3BE8C"  # Цвет для победного сообщения
DRAW_COLOR = "#EBCB8B"  # Цвет для ничьей

BUTTON_FONT = ("Arial", 24, "bold")  # Шрифт для кнопок
SCORE_FONT = ("Arial", 16, "bold")  # Шрифт для счёта

# Инициализация окна
window = tk.Tk()
window.title("Крестики-нолики")
window.geometry("345x450")
window.configure(bg=BG_COLOR)

# Переменные игры
current_player = "X"
buttons = []
score_X = 0  # Счётчик побед игрока X
score_0 = 0  # Счётчик побед игрока 0


def check_winner():
    for i in range(3):
        if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != "":
            return True
        if buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] != "":
            return True

    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        return True
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        return True

    return False


def check_draw():
    for row in buttons:
        for btn in row:
            if btn["text"] == "":
                return False  # Если есть пустая клетка, ничьей нет
    return True  # Все клетки заполнены


def highlight_buttons(color):
    for row in buttons:
        for btn in row:
            btn.config(bg=color)


def on_click(row, col):
    global current_player, score_X, score_0

    if buttons[row][col]['text'] != "":
        return

    buttons[row][col]['text'] = current_player

    if check_winner():
        if current_player == "X":
            score_X += 1
        else:
            score_0 += 1

        score_label.config(text=f"X: {score_X} | 0: {score_0}")  # Обновляем счёт
        highlight_buttons(WIN_COLOR)  # Подсветка кнопок при победе
        messagebox.showinfo("Игра окончена", f"Игрок {current_player} победил!")

        if score_X == 3 or score_0 == 3:
            messagebox.showinfo("Конец игры", f"Игрок {current_player} выиграл матч!")
            reset_game(full_reset=True)  # Полный сброс (включая счёт)
        else:
            reset_game()  # Сброс только поля
    elif check_draw():  # Проверка на ничью
        highlight_buttons(DRAW_COLOR)  # Подсветка кнопок при ничьей
        messagebox.showinfo("Игра окончена", "Ничья!")
        reset_game()  # Сброс поля после ничьей

    current_player = "0" if current_player == "X" else "X"


def reset_game(full_reset=False):
    global current_player, score_X, score_0

    current_player = "X"  # Сброс текущего игрока
    for row in buttons:
        for btn in row:
            btn["text"] = ""  # Очистка текста на кнопках
            btn.config(bg=BUTTON_COLOR)  # Возвращаем стандартный цвет кнопок

    if full_reset:
        score_X = 0
        score_0 = 0
        score_label.config(text=f"X: {score_X} | 0: {score_0}")  # Обновляем счёт


# Создание кнопок для игры
for i in range(3):
    row = []
    for j in range(3):
        btn = tk.Button(
            window,
            text="",
            font=BUTTON_FONT,
            width=5,
            height=2,
            bg=BUTTON_COLOR,
            fg=TEXT_COLOR,
            relief="flat",
            command=lambda r=i, c=j: on_click(r, c),
        )
        btn.grid(row=i, column=j, padx=5, pady=5)
        row.append(btn)
    buttons.append(row)

# Кнопка сброса
reset_button = tk.Button(
    window,
    text="Сброс",
    font=SCORE_FONT,
    bg=BUTTON_COLOR,
    fg=TEXT_COLOR,
    relief="flat",
    command=reset_game,
)
reset_button.grid(row=3, column=0, columnspan=3, sticky="we", padx=10, pady=10)

# Отображение счёта
score_label = tk.Label(
    window,
    text=f"X: {score_X} | 0: {score_0}",
    font=SCORE_FONT,
    bg=BG_COLOR,
    fg=TEXT_COLOR,
)
score_label.grid(row=4, column=0, columnspan=3, pady=10)

window.mainloop()