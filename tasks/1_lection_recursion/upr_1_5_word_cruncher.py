def find_all_solutions(index, target, index_word, words_counter, used_words):
    if index>=len(target):
        print(" ".join(used_words))
        return
    if index not in index_word:
        return
    for word in index_word[index]:
        if words_counter[word]==0:
            continue
        used_words.append(word)
        words_counter[word]-=1
        find_all_solutions(index+len(word), target, index_word, words_counter, used_words)
        used_words.pop()
        words_counter[word]+=1



def sort_the_words(input, target):
    index_dict = {}
    words_counter = {}

    for word in input:
        if word in words_counter:
            words_counter[word] += 1
            continue
        words_counter[word] = 1
        try:
            idx = 0
            while True:
                idx = target.index(word, idx)
                if idx not in index_dict:
                    index_dict[idx] = []
                index_dict[idx].append(word)
                idx += len(word)

        except ValueError:
            pass

    return index_dict,words_counter

#input=['text', 'me', 'so', 'do', 'm', 'ran']
#target="somerandomtext"
input_=input().split(", ")
target=input()


index_dict,words_counter=sort_the_words(input_, target)
find_all_solutions(0,target,index_dict,words_counter,[])







