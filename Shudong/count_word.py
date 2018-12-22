#!/usr/bin/env python
# coding=utf-8

'''
file name: count_word.py
function: caculate word number
'''
import jieba
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# read from txt
path = './user/xxx.txt'
with open(path, 'r') as novelFile:
    novel = novelFile.read()

with open('punctuation.txt', 'r') as punctuationFile:
    for punctuation in punctuationFile.readlines():
        novel = novel.replace(punctuation[0], ' ')

# Filter Special Symbols
# punctuations = """!#$%&()*+-/<>=@?_""''^[]~`{}:\n,.。"""
# for punctuation in punctuations:
#     novel = novel.replace(punctuation,' ')

# add special world
jieba.add_word('深大')
jieba.add_word('树洞')

# read meaningless word from txt
with open('meaningless.txt', 'r') as meaninglessFile:
    meaningless = meaninglessFile.read().replace('\r', '')
    mLessSet = set(meaningless.split('\n'))
mLessSet
mLessSet.add(' ')

novelList = list(jieba.cut(novel))
novelSet = set(novelList) - mLessSet # delete meaningless word from blog
novelDict = {}

# count word dict
for word in novelSet:
    novelDict[word] = novelList.count(word)

# sort word
novelListSorted = list(novelDict.items())
novelListSorted.sort(key=lambda e: e[1], reverse=True)

# print top 20 word
topWordNum = 0
for topWordTup in novelListSorted:
    if topWordNum == 20:
        break
    print str(topWordTup[0]), topWordTup[1]
    topWordNum += 1