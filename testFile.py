# testFile.py

from lab03 import integerDivision, collectEvenInts, reverseString, countVowels, removeSubString

def test_integerDivision():
    assert integerDivision(27,4) == 6
    assert integerDivision(20,4) == 5
    assert integerDivision(29,5) == 5
    assert integerDivision(50,8) == 6
    assert integerDivision(15,3) == 5

def test_collectEvenInts():
    assert collectEvenInts([1,2,3,4,5]) == [2,4]
    assert collectEvenInts([5,6,7,8,9]) == [6,8]
    assert collectEvenInts([1,2,5,6,8]) == [2,6,8]
    assert collectEvenInts([12,13,14,15,16]) == [12,14,16]

def test_countVowels():
    assert countVowels("This Is A String") == 4
    assert countVowels("Grace Bianchi") == 5
    assert countVowels("UCSB") == 1
    assert countVowels("Lab Three") == 3
    assert countVowels("Computer Science") == 6

def test_reverseString():
    assert reverseString("CMPSC9") == "9CSPMC"
    assert reverseString("grace") == "ecarg"
    assert reverseString("computer") == "retupmoc"
    assert reverseString("UCSB") == "BSCU"

def test_removeSubString():
    assert removeSubString("Lolololol", "lol") == "Loo"
    assert removeSubString("abcabcde", "abc") == "de"
    assert removeSubString("UCSBUCSDUCLA", "UC") == "SBSDLA"
    assert removeSubString("HelloWorldWorld", "World") == "Hello"

    
