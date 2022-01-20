from tkinter import messagebox
from enum import IntEnum
import numpy as np
import OutputScreen


def get_PAM_Matrix():
    try:
        data = open("PAM.txt", 'r')
        dimensions = data.readline()

        # get matrix dimensions
        n = int(dimensions)

        # get protein Letters
        letters = data.readline()
        letters = letters.replace('\n', '')
        letters_arr = letters.split('\t')

        # Create Pam Matrix
        score_matrix = np.zeros((n, n))
        for i in range(0, n):
            arr = data.readline().split("\t")
            for j in range(0, n):
                score_matrix[i][j] = float(arr[j])
        score_matrix = score_matrix.astype(int)
        return score_matrix, letters_arr

    except FileNotFoundError:
        print("There is no matrix file.")



Protein_Letters = {"A": 0, "R": 1, "N": 2, "D": 3, "C": 4, "Q": 5, "E": 6, "G": 7, "H": 8, "I": 9, "L": 10, "K": 11,
                   "M": 12, "F": 13, "P": 14, "S": 15, "T": 16, "W": 17, "Y": 18, "V": 19}
key_list = list(Protein_Letters.keys())
val_list = list(Protein_Letters.values())


class Trace(IntEnum):
    STOP = 0
    LEFT = 1
    UP = 2
    DIAGONAL = 3


# function to check if two sequence are protein
def check_input(seq):
    if seq == "":
        return False
    for i in seq:
        if i not in Protein_Letters.keys():
            return False
    return True


# Do a local alignment between x and y
def Local_Alignment_Protein(seq1, seq2, gap):
    # create array contain alignment two sequence position
    align_loc = []
    PAM_matrix = get_PAM_Matrix()[0]
    print(PAM_matrix)

    # Define matrix dimension
    row = len(seq2) + 1
    col = len(seq1) + 1

    # create a zero-filled matrix using numpy module for score matrix
    matrix = np.zeros((row, col))

    # create a zero-filled matrix using numpy module for tracing matrix
    tracing_matrix = np.zeros((row, col))

    # Initialising the variables to find the highest scoring cell
    max_score = -1
    max_index = (-1, -1)

    # Calculating the scores for all cells in the matrix
    for i in range(1, row):
        for j in range(1, col):
            # Calculating the diagonal score (match score)

            diagonal_score = matrix[i - 1, j - 1] + PAM_matrix[
                Protein_Letters[seq1[j - 1]], Protein_Letters[seq2[i - 1]]]

            # Calculating the  (UP) gap score
            up_score = matrix[i - 1, j] + gap

            # Calculating the (left) gap score
            left_score = matrix[i, j - 1] + gap

            # Taking the highest score
            matrix[i, j] = max(0, diagonal_score, up_score, left_score)

            # Tracking where the cell's value is coming from
            if matrix[i, j] == 0:
                tracing_matrix[i, j] = Trace.STOP

            elif matrix[i, j] == left_score:
                tracing_matrix[i, j] = Trace.LEFT

            elif matrix[i, j] == up_score:
                tracing_matrix[i, j] = Trace.UP

            elif matrix[i, j] == diagonal_score:
                tracing_matrix[i, j] = Trace.DIAGONAL

            # Tracking the cell with the maximum score
            if matrix[i, j] >= max_score:
                max_index = (i, j)
                max_score = matrix[i, j]

    # Initialising the variables for tracing
    aligned_seq1 = ""
    aligned_seq2 = ""
    current_aligned_seq1 = ""
    current_aligned_seq2 = ""
    max_i, max_j = max_index

    # Tracing and computing the pathway with the local alignment
    while tracing_matrix[max_i, max_j] != Trace.STOP:
        if tracing_matrix[max_i, max_j] == Trace.DIAGONAL:
            current_aligned_seq1 = seq1[max_j - 1]
            current_aligned_seq2 = seq2[max_i - 1]
            align_loc.append((max_i, max_j))
            max_i = max_i - 1
            max_j = max_j - 1


        elif tracing_matrix[max_i, max_j] == Trace.UP:
            current_aligned_seq1 = '-'
            current_aligned_seq2 = seq2[max_i - 1]
            align_loc.append((max_i, max_j))
            max_i = max_i - 1


        elif tracing_matrix[max_i, max_j] == Trace.LEFT:
            current_aligned_seq1 = seq1[max_j - 1]
            current_aligned_seq2 = '-'
            align_loc.append((max_i, max_j))
            max_j = max_j - 1

        aligned_seq1 = current_aligned_seq1 + aligned_seq1
        aligned_seq2 = current_aligned_seq2 + aligned_seq2
    align_loc.append((max_i, max_j))

    # send result to output screen to show it
    OutputScreen.output_Screen(matrix, align_loc, aligned_seq1, aligned_seq2, seq1, seq2, max_score)


# function to check sequence and start  Protein alignment
def get_arguments_Protein(seq1, seq2, gap, window):
    TOP_SEQ = check_input(seq1)
    BOTTOM_SEQ = check_input(seq2)
    if TOP_SEQ and BOTTOM_SEQ:
        window.destroy()
        Local_Alignment_Protein(seq1, seq2, gap)
    else:
        messagebox.showerror("ERROR", "Please Enter A Correct Protein Sequence Letters")
