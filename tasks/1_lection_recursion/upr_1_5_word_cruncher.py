
input=['text', 'me', 'so', 'do', 'm', 'ran']
target="somerandomtext"

index_dict={}
words_counter={}

for word in input:
    if word in words_counter:
        words_counter[word]+=1
        continue
    words_counter[word]=1
    try:
        idx=0
        while True:
            idx=target.index(word,idx)
            if idx not in index_dict:
                index_dict[idx]=[]
            index_dict[idx].append(word)
            idx+=len(word)

    except ValueError:
        pass
    


print(index_dict)
print(words_counter)