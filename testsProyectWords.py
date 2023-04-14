import unittest
from countWords import countWords

class TestCountWords(unittest.TestCase):
    def testEmpty(self):
        result = countWords('')
        self.assertEqual(result, {})

    def testGreeting(self):
        result = countWords('hola')
        self.assertEqual(result, {'hola': 1})
        
    def testFarewell(self):
        result = countWords('Adios')
        self.assertEqual(result, {'adios': 1})
        
    def testFarewell2(self):
        result = countWords('Chau chau')
        self.assertEqual(result, {'chau': 2})

    def testSentence(self):
        result = countWords('Es decir, esto es un test.')
        self.assertEqual(result, {'es': 2, 'decir': 1, 'esto': 1, 'un': 1, 'test': 1})

    def testSentence2(self):
        result = countWords('¿Vas a el banco? Te banco sentado en el banco.')
        self.assertEqual(result, {'vas': 1, 'a': 1, 'el': 2, 'banco': 3, 'te': 1, 'sentado': 1, 'en': 1})

    def testRepetitions(self):
        result = countWords('a b a c a c c b a b c b c a')
        self.assertEqual(result, {'a': 5, 'b': 4, 'c': 5})
        
    def testSimbols(self):
        result = countWords('h/o?La$$com#O 3sT4s')
        self.assertEqual(result, {'h': 1, 'o': 2, 'la': 1, 'com': 1, 'st': 1, 's': 1})        

if __name__ == '__main__':
    unittest.main()