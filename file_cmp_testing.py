import filecmp
import unittest

class FileCmpTest(unittest.TestCase):
    #RIGHT testing
    def test_strings(self):
        f1 = open("file1.txt", "w")
        f1.write("hola")
        f1.close()
        f2 = open("file2.txt", "w")
        f2.write("hola")
        f2.close()
        f1 = "file1.txt"
        f2 = "file2.txt"
        self.assertAlmostEqual(filecmp.cmp(f1, f2), True)
    def test_text(self):
        f1 = open("file1.txt", "w")
        f1.write("hola mundo, editar archivo para su posterior comparacion")
        f1.close()
        f2 = open("file2.txt", "w")
        f2.write("hola mundo, editar archivo para su posterior comparacion")
        f2.close()
        f1 = "file1.txt"
        f2 = "file2.txt"
        self.assertAlmostEqual(filecmp.cmp(f1, f2), True)
    def test_diff(self):
        f1 = open("file1.txt", "w")
        f1.write("esta vez el texto es diferente")
        f1.close()
        f2 = open("file2.txt", "w")
        f2.write("hola mundo, editar archivo para su posterior comparacion")
        f2.close()
        f1 = "file1.txt"
        f2 = "file2.txt"
        self.assertAlmostEqual(filecmp.cmp(f1, f2), False)
    def test_empty(self):
        f1 = open("file1.txt", "w")
        f1.write("")
        f1.close()
        f2 = open("file2.txt", "w")
        f2.write("")
        f2.close()
        f1 = "file1.txt"
        f2 = "file2.txt"
        self.assertAlmostEqual(filecmp.cmp(f1, f2), True)
    #Boundary testing
    def test_lots_of_text(self):
        f1 = open("file1.txt", "w")
        f1.write("The horse (Equus ferus caballus)[2][3] is a domesticated odd-toed ungulate mammal. It belongs to the taxonomic family Equidae and is one of two extant subspecies of Equus ferus. The horse has evolved over the past 45 to 55 million years from a small multi-toed creature, Eohippus, into the large, single-toed animal of today. Humans began domesticating horses around 4000 BC, and their domestication is believed to have been widespread by 3000 BC. Horses in the subspecies caballus are domesticated, although some domesticated populations live in the wild as feral horses. These feral populations are not true wild horses, as this term is used to describe horses that have never been domesticated, such as the endangered Przewalski's horse, a separate subspecies, and the only remaining true wild horse. There is an extensive, specialized vocabulary used to describe equine-related concepts, covering everything from anatomy to life stages, size, colors, markings, breeds, locomotion, and behavior.")
        f1.close()
        f2 = open("file2.txt", "w")
        f2.write("Los cocodrilos o cocodrilos verdaderos son grandes reptiles semiacuáticos que viven en los trópicos de África, Asia, América y Australia. Crocodylinae, cuyos miembros se consideran verdaderos cocodrilos, se clasifica como una subfamilia biológica.")
        f2.close()
        f1 = "file1.txt"
        f2 = "file2.txt"
        self.assertAlmostEqual(filecmp.cmp(f1, f2), False)
    #Error testing
    def test_no_exist(self):
        f1 = "filenoexist1.txt"
        f2 = "filenoexist2.txt"
        with self.assertRaises(FileNotFoundError):
            filecmp.cmp(f1, f2)    
    def test_different_than_string(self):
        f1 = 11235
        f2 = 25465
        with self.assertRaises(OSError):
            filecmp.cmp(f1, f2)

if __name__ == '__main__':
    unittest.main()