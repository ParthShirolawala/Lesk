import sys
import nltk
import nltk.corpus
nltk.download('wordnet')
nltk.download('stopwords')
from nltk.corpus import wordnet as ws
from nltk.corpus import stopwords

def simplified_lesk(word, sentence, syn):
    sentence_list = sentence.split(" ")
    stop = set(stopwords.words('english'))
    filtered = set()
    for wd in sentence_list:
        if wd.lower() not in stop:
            filtered.add(wd)
    filtered.discard(word)

    i = 1
    max = 0
    index = 0

    for sense in range(len(syn)):

        cnt = 0
        temp = set(str(syn[sense].definition()).lower().split(" "))
        filt_int = filtered.intersection(temp)

        for t in syn[sense].examples():
            t_temp = set(str(t).split(" "))
            fin1 = filtered.intersection(t_temp)
            for x in fin1:
                filt_int.add(x)

        cnt += len(filt_int)

        if max<cnt:
            max = cnt
            index = sense

        print(word + " " + str(i) + " : " + str(syn[sense].definition()) + "\n  ->  " + str(cnt) + " Overlapping Words " + str(filt_int))
        i += 1

    return (syn[index].definition()), index


word = sys.argv[1]
sentence = sys.argv[2]
syn = ws.synsets(word, pos='n')
result, ind = simplified_lesk(word, sentence, syn)

print("\n-******************************Final Chosen Sense:************************************* \n")
print(syn[ind])
print(word + " : " + result)
