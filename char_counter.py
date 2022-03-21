def char_counter(phrase):
    char_counts = {i: phrase.count(i) for i in phrase}
    return char_counts
print(char_counter("hippo runs to us!"))
