import identifyVerb
import format
import featureA

import os

os.environ['PYTHONDONTWRITEBYTECODE'] = "whatever"

usableText = featureA.getUsableText("rawText.txt")

wordList = []

for word_id in range(0, len(usableText)):
    dic, trn = identifyVerb.main(usableText[word_id])
    #print dic, trn
    if isinstance(dic, list):
        dic = ", ".join(dic)
    currentList = [usableText[word_id], dic, None, trn, None]
    for i in range(len(currentList)):
        if currentList[i] == None:
            currentList[i] = ""
    wordList.append(currentList)
#print(wordList) the output here is
#[['quae', None, None, None, None], ['cum', None, None, None, None], ['ita', None, None, None, None], ['sint', None, None, None, None], ['Catilina', None, None, None, None], ['dubitas', ['dubito', 'dubitare', 'dubitavi', 'dubitatum'], None, 'doubt, hesitate', None], ['si', None, None, None, None], ['emori', None, None, None, None], ['aequo', None, None, None, None], ['animo', None, None, None, None], ['non', None, None, None, None], ['potes', None, None, None, None], ['abire', None, None, None, None], ['in', None, None, None, None], ['aliquas', None, None, None, None], ['terras', None, None, None, None], ['et', None, None, None, None], ['vitam', None, None, None, None], ['istam', None, None, None, None], ['multis', None, None, None, None], ['suppliciis', None, None, None, None], ['iustis', None, None, None, None], ['debitisque', None, None, None, None], ['ereptam', ['eripio', 'eripere', 'eripui', 'ereptum'], None, 'snatch away', None], ['fugae', None, None, None, None], ['solitudinique', None, None, None, None], ['mandare', None, None, None, None]]
format.main(wordList)
