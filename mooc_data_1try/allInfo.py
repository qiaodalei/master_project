from pandas import DataFrame, read_csv
import pandas as pd 

allInfo = []
fileList = ['Bio.csv', 'Computer.csv', 'History.csv', 'Philo.csv', 'Science.csv', 'Engineer.csv', 'Psyco.csv', 'Design.csv', 'Law.csv', 'Manager.csv', 'Teaching.csv', 'Foreign.csv']

for fileName in fileList:
    df = pd.DataFrame(pd.read_csv(fileName))
    for i in range (df.shape[0]):
        allInfo.append(df.loc[i])
        print(df.loc[i])

df1 = pd.DataFrame(data = allInfo, columns=['courseName', 'courseLink', 'courseIntro', 'courseSchool', 'courseBook', 'courseAgenda', 'coursePreKnowledge'])  
df1.to_csv('AllInfo.csv', index=False, header=['courseName', 'courseLink', 'courseIntro', 'courseSchool', 'courseBook', 'courseAgenda', 'coursePreKnowledge'])

