import dict

rawText = []
with open('inputfile_problem2_58.txt') as f:
    rawText = f.readlines()

data = rawText[0]

shannonEncodedData = data
for key, value in dict.ShannonEncodeDict.items():
    shannonEncodedData = shannonEncodedData.replace(key, value)
with open('output/prob2/shannon.txt', 'w') as f:
  f.write(shannonEncodedData)

huffmanEncodedData = data
for key, value in dict.HuffmanEncodeDict.items():
    huffmanEncodedData = huffmanEncodedData.replace(key, value)
with open('output/prob2/huffman.txt', 'w') as f:
  f.write(huffmanEncodedData)

shannonFanoEncodedData = data
for key, value in dict.ShannonFanoEncodeDict.items():
    shannonFanoEncodedData = shannonFanoEncodedData.replace(key, value)
with open('output/prob2/shannonfano.txt', 'w') as f:
  f.write(shannonFanoEncodedData)

print(shannonEncodedData, '\n')
print(huffmanEncodedData, '\n')
print(shannonFanoEncodedData, '\n')
