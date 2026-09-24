def count_words(sentence):
    sentence = sentence.lower()
    words = sentence.split()

    count = {}

    for word in words:
        if word in count:
            count[word]+=1
        else:
            count[word] = 1
    return count

sentence = "cat sat on that cat"
print(count_words(sentence))