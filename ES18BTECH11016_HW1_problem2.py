import math

rawText = []
with open('inputfile_problem2_58.txt') as f:
    rawText = f.readlines()

data = rawText[0]

all_freq = {}

for i in data:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1

entropy = 0
for key, value in all_freq.items():
    entropy += -value * math.log(value, 2)

print("entropy: ", entropy, "\n")

ShannonEncodeDict = {
    "a": "1111",
    "b": "0",
    "c": "100",
    "d": "1100",
    "e": "1101",
}
HuffmanEncodeDict = {
    "a": "0110",
    "b": "1",
    "c": "00",
    "d": "010",
    "e": "0111",
}
ShannonFanoEncodeDict = {
    "a": "1111",
    "b": "0",
    "c": "10",
    "d": "110",
    "e": "1110",
}

shannonEncodedData = data
for key, value in ShannonEncodeDict.items():
    shannonEncodedData = shannonEncodedData.replace(key, value)
with open('output/prob2/compressed/shannon.txt', 'w') as f:
    f.write(shannonEncodedData)

huffmanEncodedData = data
for key, value in HuffmanEncodeDict.items():
    huffmanEncodedData = huffmanEncodedData.replace(key, value)
with open('output/prob2/compressed/huffman.txt', 'w') as f:
    f.write(huffmanEncodedData)

shannonFanoEncodedData = data
for key, value in ShannonFanoEncodeDict.items():
    shannonFanoEncodedData = shannonFanoEncodedData.replace(key, value)
with open('output/prob2/compressed/shannonfano.txt', 'w') as f:
    f.write(shannonFanoEncodedData)

print(shannonEncodedData, '\n')
print(huffmanEncodedData, '\n')
print(shannonFanoEncodedData, '\n')

print("Wrote files to output/prob2/compressed/*.txt")

shannonEncodedData = ""
with open('output/prob2/compressed/shannon.txt') as f:
    rawText = f.readlines()
    shannonEncodedData = rawText[0]

huffmanEncodedData = ""
with open('output/prob2/compressed/huffman.txt') as f:
    rawText = f.readlines()
    huffmanEncodedData = rawText[0]

shannonFanoEncodedData = ""
with open('output/prob2/compressed/shannonfano.txt') as f:
    rawText = f.readlines()
    shannonFanoEncodedData = rawText[0]


shannonDecodedData = ""
while shannonEncodedData != "":
    for key, value in ShannonEncodeDict.items():
        if (shannonEncodedData[0:len(value)] == value):
            shannonDecodedData = shannonDecodedData + key
            shannonEncodedData = shannonEncodedData[len(
                value): len(shannonEncodedData)]
with open('output/prob2/decompressed/shannon.txt', 'w') as f:
    f.write(shannonDecodedData)

huffmanDecodedData = ""
while huffmanEncodedData != "":
    for key, value in HuffmanEncodeDict.items():
        if (huffmanEncodedData[0:len(value)] == value):
            huffmanDecodedData = huffmanDecodedData + key
            huffmanEncodedData = huffmanEncodedData[len(
                value): len(huffmanEncodedData)]
with open('output/prob2/decompressed/huffman.txt', 'w') as f:
    f.write(huffmanDecodedData)

shannonFanoDecodedData = ""
while shannonFanoEncodedData != "":
    for key, value in ShannonFanoEncodeDict.items():
        if (shannonFanoEncodedData[0:len(value)] == value):
            shannonFanoDecodedData = shannonFanoDecodedData + key
            shannonFanoEncodedData = shannonFanoEncodedData[len(
                value): len(shannonFanoEncodedData)]
with open('output/prob2/decompressed/shannonfano.txt', 'w') as f:
    f.write(shannonFanoDecodedData)


print(shannonDecodedData, '\n')
print(huffmanDecodedData, '\n')
print(shannonFanoDecodedData, '\n')

print("Wrote files to output/prob2/decompressed/*.txt")
