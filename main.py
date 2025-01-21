import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Крестики-нолики")
window.geometry("400x400")

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
        messagebox.showinfo("Игра окончена", f"Игрок {current_player} победил!")

        if score_X == 3 or score_0 == 3:
            messagebox.showinfo("Конец игры", f"Игрок {current_player} выиграл матч!")
            reset_game(full_reset=True)  # Полный сброс (включая счёт)
        else:
            reset_game()  # Сброс только поля

    current_player = "0" if current_player == "X" else "X"


def reset_game(full_reset=False):
    global current_player, score_X, score_0

    current_player = "X"  # Сброс текущего игрока
    for row in buttons:
        for btn in row:
            btn["text"] = ""  # Очистка текста на кнопках

    if full_reset:
        score_X = 0
        score_0 = 0
        score_label.config(text=f"X: {score_X} | 0: {score_0}")  # Обновляем счёт


# Создание кнопок для игры
for i in range(3):
    row = []
    for j in range(3):
        btn = tk.Button(window, text="", font=("Arial", 20), width=5, height=2, command=lambda r=i, c=j: on_click(r, c))
        btn.grid(row=i, column=j)
        row.append(btn)
    buttons.append(row)

# Кнопка сброса
reset_button = tk.Button(window, text="Сброс", font=("Arial", 14), command=reset_game)
reset_button.grid(row=3, column=0, columnspan=3, sticky="we")

# Отображение счёта
score_label = tk.Label(window, text=f"X: {score_X} | 0: {score_0}", font=("Arial", 14))
score_label.grid(row=4, column=0, columnspan=3)

window.mainloop()