def anagrams(word, words):
    '''
    test.assert_equals(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']), ['aabb', 'bbaa'])
    test.assert_equals(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']), ['carer', 'racer'])
    '''
    res = [i for i in words if set(word) == set(i) and len(word) == len(i)]
    return [] if not res else res


print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))