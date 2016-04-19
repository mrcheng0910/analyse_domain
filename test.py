# Expect true
dictionary1 = ['fe', 'fee', 'ed']
test1 = 'feed'

# Expect true
dictionary2 = ['programcree', 'program', 'creek']
test2 = 'programcreek'

# Expect false
dictionary3 = ['let', 'code']
test3 = 'leetcode'

def word_break(word, dictionary, start, end):
    for i in range (start, len(word)):
        if word[start:start+i] in dictionary:
            if start+i+1 < len(word):
                return True and word_break(word, dictionary, start+i, end)
            else:
                return True
    return False

print word_break(test1, dictionary1, 0, len(test1))
print word_break(test2, dictionary2, 0, len(test2))
print word_break(test3, dictionary3, 0, len(test3))