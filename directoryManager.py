import unittest

class recordManager:
    def __init__(self):
        self.records_file = "directory.txt"

    def addRecord(self, name, email, age, country):
        f = open(self.records_file, "a")
        f.write(str(name) + "\n" + str(email) + "\n" + str(age) + "\n" + str(country) + "\n")
        f.close()
        return 0

    def deleteRecord(self, name, email, age, country):
        f = open(self.records_file, "r")
        data = f.readlines()
        f.close()
        idx = data.index(name + "\n")
        del data[idx:idx + 4]
        f = open(self.records_file, "w")
        for line in data:
            f.write(line)
        f.close()
        return 0

    def lookbyMail(self, email):
        f = open(self.records_file, "r")
        data = f.readlines()
        f.close()
        idx = data.index(email + "\n")
        print("\n")
        for i in range(-1, 3):
            print(data[idx + i].strip("\n"))
        return 0

    def lookbyAge(self, age):
        f = open(self.records_file, "r")
        data = f.readlines()
        f.close()
        for i in range(data.count(age + "\n")):
            idx = data.index(age + "\n")
            print("\n")
            for j in range(-2, 2):
                print(data[idx + j].strip("\n"))
            del data[idx - 2:idx + 2]
        return 0

    def printRecords(self):
        f = open(self.records_file, "r")
        data = f.readlines()
        f.close()
        print("\n")
        for line in data:
            print(line.strip("\n"))
        return 0

class recordManagerTest(unittest.TestCase):
    def test_add_record(self):
        manager = recordManager()
        self.assertAlmostEqual(manager.addRecord("Eduardo", "lalo@itesm.mx", "27", "Mexico"), 0)
    def test_add_two_records(self):
        manager = recordManager()
        self.assertAlmostEqual(manager.addRecord("Juan", "juan@itesm.mx", "33", "Mexico"), 0)
        self.assertAlmostEqual(manager.addRecord("Pedro", "pedro@itesm.mx", "25", "Nicaragua"), 0)
    def test_add_incomplete_record(self):
        manager = recordManager()
        with self.assertRaises(TypeError):
            manager.addRecord("Alberto", "beto@itesm.mx")
    def test_add_not_string_record(self):
        manager = recordManager()
        self.assertAlmostEqual(manager.addRecord("Alberto", "beto@itesm.mx", 35, "Mexico"), 0)  #No error expected
    def test_delete_record(self):
        manager = recordManager()
        self.assertAlmostEqual(manager.deleteRecord("Juan", "juan@itesm.mx", "33", "Mexico"), 0)
    def test_delete_non_existent_record(self):
        manager = recordManager()
        with self.assertRaises(ValueError):
            manager.deleteRecord("Pepito", "pepito@itesm.mx", "55", "Mexico")
    def test_look_by_mail(self):
        manager = recordManager()
        self.assertAlmostEqual(manager.lookbyMail("lalo@itesm.mx"), 0)
    def test_look_by_non_existent_mail(self):
        manager = recordManager()
        with self.assertRaises(ValueError):
            manager.lookbyMail("pepito@itesm.mx")
    def test_look_by_age(self):
        manager = recordManager()
        self.assertAlmostEqual(manager.lookbyAge("25"), 0)
    def test_look_by_non_existent_age(self):
        manager = recordManager()
        self.assertAlmostEqual(manager.lookbyAge("999999999"), 0)   #No error expected
    def test_print_records(self):
        manager = recordManager()
        self.assertAlmostEqual(manager.printRecords(), 0)

if __name__ == '__main__':
    unittest.main()