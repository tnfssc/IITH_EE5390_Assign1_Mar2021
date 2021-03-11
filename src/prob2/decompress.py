import dict


def get_key(val, my_dict):
    for key, value in my_dict.items():
        if val == value:
            return key
    return "||key doesn't exist||"


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
    for key, value in dict.ShannonEncodeDict.items():
        if (shannonEncodedData[0:len(value)] == value):
            shannonDecodedData = shannonDecodedData + key
            shannonEncodedData = shannonEncodedData[len(
                value): len(shannonEncodedData)]
with open('output/prob2/decompressed/shannon.txt', 'w') as f:
    f.write(shannonDecodedData)

huffmanDecodedData = ""
while huffmanEncodedData != "":
    for key, value in dict.HuffmanEncodeDict.items():
        if (huffmanEncodedData[0:len(value)] == value):
            huffmanDecodedData = huffmanDecodedData + key
            huffmanEncodedData = huffmanEncodedData[len(
                value): len(huffmanEncodedData)]
with open('output/prob2/decompressed/huffman.txt', 'w') as f:
    f.write(huffmanDecodedData)

shannonFanoDecodedData = ""
while shannonFanoEncodedData != "":
    for key, value in dict.ShannonFanoEncodeDict.items():
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
