# Module: dict.py

def flipKeys(z):
    new = {}
    for key, value in z.items():
        new[value] = key
    return new


ShannonEncodeDict = {
    "a": "1111",
    "b": "0",
    "c": "100",
    "d": "1100",
    "e": "1101",
}
ShannonDecodeDict = flipKeys(ShannonEncodeDict)
HuffmanEncodeDict = {
    "a": "0110",
    "b": "1",
    "c": "00",
    "d": "010",
    "e": "0111",
}
ShannonDecodeDict = flipKeys(HuffmanEncodeDict)
ShannonFanoEncodeDict = {
    "a": "1111",
    "b": "0",
    "c": "10",
    "d": "110",
    "e": "1110",
}
ShannonDecodeDict = flipKeys(ShannonFanoEncodeDict)
