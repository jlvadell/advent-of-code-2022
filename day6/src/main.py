def find_non_repeating_sequence(text: str, seq_len: int):
    sequence = []
    text_index = 0
    for char in text:
        text_index +=1
        if char in sequence:
            idx = sequence.index(char)
            sequence = sequence[idx+1:len(sequence)]
        sequence.append(char)
        if len(sequence) == seq_len:
            return ''.join(sequence), text_index

def load_datastream(input_file):
    with open(input_file, 'r') as input_text:
        return input_text.read()

def solve_part_1(text):
    seq_len = 4
    _, sequence_index = find_non_repeating_sequence(text, seq_len)
    return sequence_index

def solve_part_2(text):
    seq_len = 14
    _, sequence_index = find_non_repeating_sequence(text, seq_len)
    return sequence_index