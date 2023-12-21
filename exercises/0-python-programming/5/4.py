def is_subseq(seq_a, seq_b):
    return all([a in seq_b
               for a in seq_a])


seq_a = (1, 3, 2)
seq_b = (1, 2, 3, 4)
print(is_subseq(seq_a, seq_b))
