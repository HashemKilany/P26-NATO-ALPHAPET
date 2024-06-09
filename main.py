# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }

import pandas

df = pandas.DataFrame(pandas.read_csv("nato_phonetic_alphabet.csv"))

# a dictionary in this format:{"A": "Alfa", "B": "Bravo"}
codes = {row.letter: row.code for (index, row) in df.iterrows()}


# a list of the phonetic code words from a word that the user inputs.

def generate_phonetic():
    user_input = input('enter a word: ').upper()
    try:
        phonetic_code = [codes[n] for n in user_input]
    except KeyError:
        print(" please enter english alphabet only!")
        generate_phonetic()
    else:
        print(phonetic_code)


generate_phonetic()

# print(codes)
#Access index and row
#Access row.student or row.score
# pass
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
