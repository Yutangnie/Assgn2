import numpy as np
import scipy.io as matIO

from collections import Counter

# load label and ads files and create data matrix
labelFile = file("farm-ads-label.txt", "r")
labels = labelFile.read().splitlines()
labelArray = []
for label in labels:
    labelArray.append(label.split(" ")[1])

adFile = file("test.txt", "r", )
ads = adFile.read().splitlines()
wordSet = set()
bagsOfWords = []
for ad in ads:
    bag = Counter(ad.split(" ")[1: ])
    bagsOfWords.append(bag)
    for word in bag:
        wordSet.add(word)

dataMatrix = np.zeros((len(wordSet), len(ads)))
wordIndex = {}
index = 0
for word in wordSet:
    wordIndex[word] = index
    index += 1
# traverse bag of each ads and put the frequency into dataMatrix
for j in range(len(bagsOfWords)):
    for key in bagsOfWords[j]:
        dataMatrix[wordIndex[key]][j] = bagsOfWords[j][key]

# save dataMatrix to .mat file
index = 0
results = {}
for word in wordSet:
    results[word] = dataMatrix[index]
    index += 1
matIO.savemat("myfile", results, do_compression=True)

print len(dataMatrix)
print len(dataMatrix[0])
# a = matIO.loadmat("myfile")
# for word in wordSet:
    # print a[word]
