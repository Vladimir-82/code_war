def is_merge(s, part1, part2):
    '''

        s:  c o d e w a r s   = codewars
    part1:  c   d   w         = cdw
    part2:    o   e   a r s   = oears
    '''
    stop = 1
    while s:
        if s[:stop] != part1[:stop] and s[:stop] != part2[:stop]:
            return False
        if s[:stop] == part1[:stop] == part2[:stop]:
            stop += 1
        else:
            if s[:stop] == part1[:stop]:
                part1 = part1[stop:]

            else:
                part2 = part2[stop:]
            s = s[stop:]
            stop = 1

    return True if not part1 and not part2 else False
print((is_merge('codewars', 'code', 'wars')))

# for i in range(len(s)):
#
#     if s[i] == part1[:i] == part2[:i]:
#         continue
#     else:
#         if s[i] != part1[:i]:
#             part2 = part2[:i]
#         else:
#             part1 = part1[:i]
#
#     if part1 and s[i] == part1[0]:
#         part1 = part1[1:]
#     elif part2 and s[i] == part2[0]:
#         part2 = part2[1:]
#     else:
#         return False
# return True if not part1 and not part2 else False