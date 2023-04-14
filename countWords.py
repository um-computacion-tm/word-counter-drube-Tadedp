def countWords(words):
    result = {}
    counter = 0

    for i in range(len(words)):
        if words[i].isalpha():
            counter += 1
            if i == len(words) - 1:
                word = words[i - counter + 1:].lower()
                if word in result:
                    result[word] += 1
                
                else:
                    result[word] = 1
        else:
            if counter > 0:
                word = words[i - counter:i].lower()
                if word in result:
                    result[word] += 1
                
                else:
                    result[word] = 1
            counter = 0                
    return result

if __name__ == '__main__':
    pass