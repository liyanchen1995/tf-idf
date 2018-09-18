import sys
import os
import math
import jieba
i=0
PATH = './allfiles'
file_name_arr = os.listdir(PATH)
file_word = {}
word_stop =['“','\n','”','【','】','（','）']
file_word_table = set()

count_word = 0
for file_name in file_name_arr:
    name = PATH+'/'+file_name
    with open(name,'r',encoding='utf-8') as fd:
        file_word[file_name] = {}
        ss = fd.read().strip().split(' ')
        for word in ss:
            if word in word_stop:
                continue
            file_word_table.add(word)
            count_word +=1
            if file_word[file_name].get(word,-1) == -1:
                file_word[file_name][word] = 1
            else:
                file_word[file_name][word] += 1


############################################### idf
count = 0
idf_word ={}
for word in file_word_table:
    for file_name in file_word.keys():
        if file_word[file_name].get(word,-1)== -1:
            continue
        else:
            count +=1
    # print('\t'.join([word.strip(),str(math.log(100/count))]))
    idf_word[word] = math.log(100/count)
    count = 0
# print(idf_word)


###########################################################TF
tf_word = {}
file_word_tf_idf = {}
for file_name in file_word.keys():
    file_word_tf_idf[file_name]={}
    for word in file_word[file_name].keys():
        tf_word[word] = file_word[file_name][word]/count_word
        file_word_tf_idf[file_name][word] = tf_word[word] * idf_word[word]


print(file_word_tf_idf)
