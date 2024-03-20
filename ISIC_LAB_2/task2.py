def function(file):
            f = open(file, 'r')
            words = f.read().split()
            longest_word = max(words, key=len)
            return longest_word

file = 'test.txt'
longest_word = function(file)
print("Najdłuższy wyraz w pliku:", longest_word)