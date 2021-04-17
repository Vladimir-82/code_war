def pig_it(text):
    '''Move the first letter of each word to the end of it,
    then add "ay" to the end of the word. Leave punctuation marks untouched.
    pig_it('Pig latin is cool') # igPay atinlay siay oolcay
    pig_it('Hello world !')     # elloHay orldway !
    '''
    splt = text.split()
    out = []
    for i in splt:
        if i.isalpha():
            out.append(i[1:] + i[0] + 'ay')
        else:
            out.append(i[1:] + i[0])

    return ' '.join(out)

print(pig_it('O tempora o mores !'))
# Oay emporatay oay oresmay !ay
# Oay emporatay oay oresmay !