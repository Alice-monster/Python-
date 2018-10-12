import jieba
import sys

def stopwordslist(filename):
    stopwords = [line.strip() for line in open(filename, 'r', encoding='utf-8').readlines()]
    return stopwords

def se_sent(sentence):
    sentence_seged = jieba.cut(sentence.strip())
    stopwords = stopwordslist('/Users/huangyabin/Downloads/stopwords.txt')
    outstr = ''
    for word in sentence_seged:
        if word not in stopwords:
            if word != '\t':
                outstr += word
                outstr += " "
    return outstr


inputs = open('/Users/huangyabin/Downloads/input.txt', 'r', encoding='utf-8')
outputs = open('/Users/huangyabin/Downloads/output.txt', 'w', encoding='utf-8')
for line in inputs:
    line_se = se_sent(line)
    outputs.write(line_se + '\n')
outputs.close()
inputs.close()
