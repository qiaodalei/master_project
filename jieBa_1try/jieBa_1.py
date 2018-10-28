# encoding=utf-8
import jieba
import codecs
import math
import pandas as pd
import numpy as np
import jieba.posseg as pseg

df = pd.DataFrame(pd.read_csv('History.csv'))
courseInfoWord = []
allDict = {}
courseWord = []
allFileTF = []
lenFile = []

def str_cut(text_str):

    stop_flag = ['x', 'c', 'u','d', 'p', 't', 'uj', 'm', 'f', 'r']
    result = []
    words = pseg.cut(text_str)
    for word, flag in words:
        if flag not in stop_flag:
            result.append(word)
    return result

if __name__ == "__main__":

    for i in range (df.shape[0]):
        fileDict = {}
        textStr = str(df.loc[i][2]) + str(df.loc[i][5])
        courseCut = str_cut(textStr)

        for cutCourseWord in courseCut:
            if cutCourseWord in fileDict:
                fileDict[cutCourseWord] = fileDict[cutCourseWord] + 1
            else:
                fileDict[cutCourseWord] = 1

        for keys in fileDict.keys():
            if keys in allDict:
                allDict[keys] = allDict[keys] + 1
            else:
                allDict[keys] = 1

        lenFile.append(len(courseCut))
        allFileTF.append(fileDict)

    for i in range (len(allFileTF)):
        keyWordTFIDF = {}

        for keys in allFileTF[i].keys():
            keyTF = float(allFileTF[i][keys]/lenFile[i])
            keyIDF = math.log(float(df.shape[0]/allDict[keys]+1))
            tfIdf = keyTF * keyIDF
            keyWordTFIDF[keys] = tfIdf

        dictSorted = sorted(keyWordTFIDF.items(), key = lambda k: k[1], reverse = True)
        #print(dictSorted)

        key10 = []
        for j in range (10):
            key10.append(dictSorted[j][0])
        
        print(key10)
        print('@@@@@@@@@@@@@')


