# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    with open(filename) as myFile:
        content = myFile.readlines()
        return(content)


def count_words():
    words = []
    text = read_file_content("story.txt")
   
    for t in text:
        t = t.split()

    for i in t:
        words.append(i)
    print (words)

    final_dict = {}
    for word in words:
        final_dict[word] = words.count(word)
    print (final_dict)

print (count_words())
