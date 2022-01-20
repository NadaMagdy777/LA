# Import the required libraries
from tkinter import ttk
from tkinter import *
import InputScreen


# draw output alignment matrix
def draw_matrix(matrix, align_loc, f, seq1, seq2):
    matrix = matrix.astype(int)
    frame = ttk.LabelFrame(f, height=500, width=500, text="Matrix")
    for i in range(0, len(matrix) + 1):
        for j in range(0, len(matrix[0]) + 1):
            loc = (i - 1, j - 1)
            if i == 0 and j > 1:
                Label(frame, text=seq1[j - 2], foreground="white", background="#800080", borderwidth=2).grid(row=i,
                                                                                                             column=j,
                                                                                                             padx=1,
                                                                                                             pady=1)
            elif i > 1 and j == 0:
                Label(frame, text=seq2[i - 2], foreground="white", background="#800080", borderwidth=2).grid(row=i,
                                                                                                             column=j,
                                                                                                             padx=1,
                                                                                                             pady=1)

            elif loc in align_loc and i != 0 and j != 0:
                Label(frame, text=matrix[i - 1, j - 1], foreground="white", background="#800080", borderwidth=2).grid(
                    row=i, column=j, padx=1, pady=1)

            elif i != 0 and j != 0 and loc not in align_loc:
                Label(frame, text=matrix[i - 1, j - 1], background="white", borderwidth=2).grid(row=i, column=j, padx=1,
                                                                                                pady=1)

    frame.pack(pady=10)


# Return to input Window
def back_window(window):
    window.destroy()
    InputScreen.DNA_PROTEIN_LF()


# output screen component
def output_Screen(matrix, align_loc, align1, align2, seq1, seq2, score):
    window = Tk()
    window.geometry()
    window.geometry("1500x900")
    window.title("LOCAL ALIGNMENT APP")
    f = ttk.LabelFrame(window, height=500, width=500, text="Alignment Output", )
    Label(f, text="Align Seq 1:- " + align1, font=('Georgia', 10, 'bold')).pack(pady=10,
                                                                                padx=50)
    Label(f, text="Align Seq 2:- " + align2, font=('Georgia', 10, 'bold')).pack(pady=10,
                                                                                padx=50)
    Label(f, text="Score :- " + str(score), font=('Georgia', 10, 'bold')).pack(pady=10,
                                                                               padx=50)
    draw_matrix(matrix, align_loc, f, seq1, seq2)
    Button(f, text="Back", foreground="white", background="#800080", command=lambda: back_window(window), width=10, height=2).pack()

    f.pack(fill="both", padx=50, pady=50)
    window.mainloop()
