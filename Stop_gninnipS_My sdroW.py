def spin_words(sentence):
    '''
    Write a function that takes in a string of one or more words, and returns the same string,
    but with all five or more letter words reversed (like the name of this kata).

    Strings passed in will consist of only letters and spaces.
    Spaces will be included only when more than one word is present.

    spinWords("Hey fellow warriors") => "Hey wollef sroirraw"
    spinWords("This is a test") => "This is a test"
    spinWords("This is another test") => "This is rehtona test"
    '''
    out =[]
    splt = sentence.split()
    for i in splt:
        if len(i) >= 5:
            out.append(i[::-1])
        else:
            out.append(i)
    return " ".join(out)


print(spin_words("Hey fellow warriors"))