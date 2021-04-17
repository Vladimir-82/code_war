def pig_it(text):
    '''Move the first letter of each word to the end of it,
    then add "ay" to the end of the word. Leave punctuation marks untouched.
    pig_it('Pig latin is cool') # igPay atinlay siay oolcay
    pig_it('Hello world !')     # elloHay orldway !
    '''
    splt = text.split()
    out = []
    for i in splt:
        out.append(i[1:] + i[0] + 'ay')
    for i in out:
        if "!" in i:
            out[out.index(i)] = "!"
        if "?" in i:
            out[out.index(i)] = "?"
    return ' '.join(out)

print(pig_it('O tempora o mores !'))
# Oay emporatay oay oresmay !ay
# Oay emporatay oay oresmay !