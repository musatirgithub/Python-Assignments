def chars(users_phrase):
    char_list = []
    new_phrase = None
    for i in users_phrase:
        if i.isalnum():
            char_list.append(i)
            new_phrase = ''.join(char_list)
    return new_phrase

def palind(phrase1):
    if list(phrase1.lower()) == list(reversed(phrase1.lower())):
        return True
    else:
        return False
phrase = input("Please enter something: ")
if palind(chars(phrase)):
    print(phrase, "is a palindrome")
else:
    print(phrase, "is not a palindrome")