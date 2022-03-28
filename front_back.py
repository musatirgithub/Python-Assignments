def front_back(word):
    if len(word) > 1:
        word2 = word[-1] + word[1:-1] + word[0]
        return word2
    else:
        return word
print(front_back('clarusway'))
