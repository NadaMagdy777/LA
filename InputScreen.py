# Import the required libraries
from tkinter import ttk
from tkinter import *
import DnaAlignment
import ProteinAlignment


# Draw PAM Matrix
def draw_matrix(Protein_LF):
    Label(Protein_LF,text="PAM 250",foreground="#800080",font=("Georgia", 15, "bold")).place(x=800, y=5)
    matrix, letters_arr = ProteinAlignment.get_PAM_Matrix()
    f = Frame(Protein_LF)
    for i in range(0, len(matrix) + 1):
        for j in range(0, len(matrix) + 1):
            if i == 0 and j != 0 and j != len(matrix) + 1:
                Label(f, text=letters_arr[j - 1], background="#800080", foreground="white", width=2, height=1).grid(row=i,
                                                                                                                 column=j,
                                                                                                                 padx=1,
                                                                                                                 pady=1)
            elif j == 0 and i != 0:
                Label(f, text=letters_arr[i - 1], background="#800080", foreground="white", width=2, height=1).grid(row=i,
                                                                                                                 column=j,
                                                                                                                 padx=1,
                                                                                                                 pady=1)
            elif i != 0 and j != 0:
                Label(f, text=matrix[i - 1, j - 1], background="white", width=2, height=1).grid(row=i, column=j, padx=1,
                                                                                                pady=1)
    f.place(x=600, y=50)

#when protein button click in protein label frame
def protein_button_click(seq1, seq2, gap, window):
    ProteinAlignment.get_arguments_Protein(seq1, seq2, gap, window)


# Create protein Label frame Components and send its arguments to protein Alignment
def protein_LF(window, Protein_LF):
    Label(Protein_LF, text="Hint:", foreground="#800080", font=('Georgia', 10, "bold")).place(x=25, y=50, height=25)

    Label(Protein_LF, text="Use nucleotide A C D E F G H I K L M N P Q R S T V W Y only ", foreground="#800080",
          font=("Arial", 10)).place(x=100, y=50, height=25)
    seq1 = StringVar()
    Label(Protein_LF, text="Top Sequence", font=("Aerial", 10)).place(x=25, y=100, height=25)
    Entry(Protein_LF, textvariable=seq1).place(x=200, y=100, width=200, height=25)
    seq2 = StringVar()

    Label(Protein_LF, text="Bottom Sequence", font=("Aerial", 10)).place(x=25, y=150, height=25)
    Entry(Protein_LF, textvariable=seq2).place(x=200, y=150, width=200, height=25)

    Label(Protein_LF, text="Scoring:-", font=("Aerial", 10)).place(x=25, y=200, height=25)

    gap = IntVar(value=-8)
    Label(Protein_LF, text="gap", font=("Aerial", 10)).place(x=200, y=200, height=25)

    Spinbox(Protein_LF, from_=-10, to=0, textvariable=gap).place(x=250, y=200, height=25, width=50)

    Button(Protein_LF, text="Result", background="#800080", foreground="white", cursor="hand2",
           command=lambda: protein_button_click(seq1.get(), seq2.get(), gap.get(), window)).place(x=200, y=300,
                                                                                                  height=50, width=100)

# when dna button in dnal label frame click
def dna_button_click(seq1, seq2, match, mismatch, gap, window):
    DnaAlignment.get_arguments_DNA(seq1, seq2, match, mismatch, gap, window)


# Create DNA Label frame Components and send its arguments to Dna Alignment
def dna_LF(window, DNA_LF):
    Label(DNA_LF, text="Hint:", foreground="#800080", font=('Georgia', 10, "bold")).place(x=25, y=50, height=25)
    Label(DNA_LF, text="Use nucleotide [ A ,C ,G, T ] only ", foreground="#800080", font=("Arial", 10)).place(x=100,
                                                                                                              y=50,
                                                                                                              height=25)
    seq1 = StringVar()
    Label(DNA_LF, text="Top Sequence", font=("Aerial", 10)).place(x=25, y=100, height=25)
    Entry(DNA_LF, textvariable=seq1).place(x=200, y=100, width=200, height=25)
    seq2 = StringVar()
    Label(DNA_LF, text="Bottom Sequence", font=("Aerial", 10)).place(x=25, y=150, height=25)

    Entry(DNA_LF, textvariable=seq2).place(x=200, y=150, width=200, height=25)

    Label(DNA_LF, text="Scoring:-", font=("Aerial", 10)).place(x=25, y=200, height=25)
    match = IntVar(value=1)
    Label(DNA_LF, text="Match", font=("Aerial", 10)).place(x=200, y=200, height=25)
    Spinbox(DNA_LF, from_=1, to=15, font=('sans-serif', 14), textvariable=match).place(x=250, y=200, height=25,
                                                                                       width=50)
    mismatch = IntVar(value=-1)
    Label(DNA_LF, text="Mismatch", font=("Aerial", 10)).place(x=350, y=200, height=25)
    Spinbox(DNA_LF, from_=-10, to=0, font=('sans-serif', 14), textvariable=mismatch).place(x=420, y=200, height=25,
                                                                                           width=50)

    gap = IntVar(value=-2)
    Label(DNA_LF, text="Gap", font=("Aerial", 10)).place(x=515, y=200, height=25)
    Spinbox(DNA_LF, from_=-10, to=0, font=('sans-serif', 14), textvariable=gap).place(x=550, y=200, height=25, width=50)

    Button(DNA_LF, text="Result", background="#800080", foreground="white", cursor="hand2",
           command=lambda: dna_button_click(seq1.get(), seq2.get(), match.get(), mismatch.get(), gap.get(),
                                            window)).place(x=400, y=300, height=50, width=100)


# Switch to Dna Label Frame
def change_to_DNA(window, DNA_LF, Protein_LF):
    dna_LF(window, DNA_LF)
    DNA_LF.pack(fill='both', padx=50, pady=10)
    Protein_LF.pack_forget()


# Switch to Protein Label Frame
def change_to_PROTEIN(window, DNA_LF, Protein_LF):
    protein_LF(window, Protein_LF)
    draw_matrix(Protein_LF)
    Protein_LF.pack(fill='both',expand=1, padx=50,pady=10)
    DNA_LF.pack_forget()


# Create Window and its Frames
def CREATE_WINDOW_FRAMES():
    window = Tk()
    # Set the size of the window
    window.geometry("1500x900")
    window.title("LOCAL ALIGNMENT APP")
    label = Label(window, text="LOCAL SEQUENCE ALIGNMENT", fg="#800080", font=("Georgia", 15, "bold"))
    label.pack(pady=5)
    frame = ttk.LabelFrame(window, height=100, width=1000, text="DNA OR PROTEIN")
    DNA_LF = ttk.LabelFrame(window, height=500, width=1000, text="DNA")
    Protein_LF = ttk.LabelFrame(window, height=500, width=1000, text="PROTEIN")
    return window, frame, DNA_LF, Protein_LF


# Create DNA OR Protein Label Frame
def DNA_PROTEIN_LF():
    # Create an instance of tkinter frame or window
    window, frame, DNA_LF, Protein_LF = CREATE_WINDOW_FRAMES()
    var = IntVar()
    var.set(1)
    dna_LF(window, DNA_LF)
    ttk.Radiobutton(frame, text="DNA", value=1, variable=var,
                    command=lambda: change_to_DNA(window, DNA_LF, Protein_LF)).grid(row=1, column=1, padx=50)
    ttk.Radiobutton(frame, text="PROTEIN", value=2, variable=var,
                    command=lambda: change_to_PROTEIN(window, DNA_LF, Protein_LF)).grid(row=1, column=2)
    frame.pack(fill='both', padx=50)
    DNA_LF.pack(fill='both', expand=1, padx=50, pady=10)
    window.mainloop()
