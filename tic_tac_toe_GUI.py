import tkinter as tk
import random
import webbrowser
import tkinter as tk


root = tk.Tk()
root.title("Tkinter Tic Tac Toe (Conel)")
root.geometry("400x450")


# ---------------- GAME STATE ----------------
board = {}
buttons = {}
current_player = "X"
game_over = False
mode = None  # "P" or "C"

positions = [
    ["a1", "a2", "a3"],
    ["b1", "b2", "b3"],
    ["c1", "c2", "c3"]
]

# ---------------- LOGIC ----------------


def reset_board():
    global board, current_player, game_over
    board = {p: " " for row in positions for p in row}
    current_player = "X"
    game_over = False

    for btn in buttons.values():
        btn.config(text=" ", state="normal")


def check_win():
    wins = [
        ["a1", "a2", "a3"], ["b1", "b2", "b3"], ["c1", "c2", "c3"],
        ["a1", "b1", "c1"], ["a2", "b2", "c2"], ["a3", "b3", "c3"],
        ["a1", "b2", "c3"], ["a3", "b2", "c1"]
    ]
    for w in wins:
        if board[w[0]] == board[w[1]] == board[w[2]] != " ":
            return True
    return False


def computer_move():
    global current_player
    moves = [p for p in board if board[p] == " "]
    if moves:
        move = random.choice(moves)
        board[move] = "O"
        buttons[move].config(text="O")


def on_click(pos):
    global current_player, game_over

    if board[pos] != " " or game_over:
        return

    board[pos] = current_player
    buttons[pos].config(text=current_player)

    if check_win():
        status_label.config(text=f"Player {current_player} wins!")
        end_game()
        return

    if all(board[p] != " " for p in board):
        status_label.config(text="It's a draw!")
        end_game()
        return

    current_player = "O" if current_player == "X" else "X"
    status_label.config(text=f"Player {current_player}'s turn")

    if mode == "C" and current_player == "O":
        root.after(500, computer_turn)


def computer_turn():
    global current_player
    computer_move()
    if check_win():
        status_label.config(text="Computer wins!")
        root.after(3000, play_yt)
        end_game()
        return
    current_player = "X"
    status_label.config(text="Player X's turn")


def end_game():
    global game_over
    game_over = True
    play_again_screen()

# ---------------- SCREENS ----------------


def clear_screen():
    for widget in root.winfo_children():
        widget.destroy()
    buttons.clear()


def title_screen():
    clear_screen()
    tk.Label(
        root,
        text="*** TIC TAC TOE ***",
        font=("Impact", 20, "bold"),
        fg="black" 
    ).pack(pady=20)
    tk.Button(
        root,
        text="be ready! click here to start the game",
        fg="black",  
        command=mode_screen
    ).pack()


def mode_screen():
    clear_screen()
    tk.Label(root, text="pick one :P",
             font=("Impact", 16)).pack(pady=10)
    tk.Button(root, text="Player vs Player",
              command=lambda: start_game("P")).pack(pady=5)
    tk.Button(root, text="Player vs Computer",
              command=lambda: start_game("C")).pack(pady=5)


def play_yt():
    url = "https://www.youtube.com/watch?v=Aq5WXmQQooo"
    webbrowser.open(url)


def start_game(selected_mode):
    global mode
    mode = selected_mode
    clear_screen()
    reset_board()
    build_board()


def build_board():
    global status_label

    frame = tk.Frame(root)
    frame.pack()

    for r in range(3):
        for c in range(3):
            pos = positions[r][c]
            btn = tk.Button(
                frame, text=" ",
                font=("Arial", 24, "bold"),
                width=5, height=2,
                command=lambda p=pos: on_click(p)
            )
            btn.grid(row=r, column=c)
            buttons[pos] = btn

    status_label = tk.Label(root, text="Player X's turn")
    status_label.pack(pady=10)


def play_again_screen():
    tk.Label(root, text="Play again?", font=("Impact", 12)).pack()
    tk.Button(root, text="Yes", command=mode_screen).pack(pady=2)
    tk.Button(root, text="No", command=end_screen).pack(pady=2)


def end_screen():
    clear_screen()
    tk.Label(root, text="Thanks for playing! I hope you enjoy :P",
             font=("Impact", 14)).pack(pady=30)


# ---------------- START ----------------
title_screen()
root.mainloop()