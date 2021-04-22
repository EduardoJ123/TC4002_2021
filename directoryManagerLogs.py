import unittest
import logging

logging.basicConfig(level=logging.DEBUG)


class recordManager:
    def __init__(self):
        self.records_file = "directory.txt"

    def addRecord(self, name, email, age, country):
        f = open(self.records_file, "a")
        f.write(str(name) + "\n" + str(email) + "\n" + str(age) + "\n" + str(country) + "\n")
        logging.info("Added new record.")
        f.close()
        return 0

    def deleteRecord(self, name, email, age, country):
        print("Deleting record:\n")
        print(name, email, age, country)
        f = open(self.records_file, "r")
        data = f.readlines()
        f.close()
        idx = data.index(name + "\n")
        del data[idx:idx + 4]
        f = open(self.records_file, "w")
        for line in data:
            f.write(line)
        logging.info("Deleted record from database.")
        f.close()
        return 0

    def lookbyMail(self, email):
        print("Looking by mail:\n")
        f = open(self.records_file, "r")
        data = f.readlines()
        f.close()
        idx = data.index(email + "\n")
        print("\n")
        for i in range(-1, 3):
            print(data[idx + i].strip("\n"))
        return 0

    def lookbyAge(self, age):
        print("Looking by age:\n")
        f = open(self.records_file, "r")
        data = f.readlines()
        f.close()
        for i in range(data.count(age + "\n")):
            print(i)
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
        logging.error("Trying to add incomplete record.")

    def test_add_not_string_record(self):
        manager = recordManager()
        self.assertAlmostEqual(manager.addRecord("Alberto", "beto@itesm.mx", 35, "Mexico"), 0)  # No error expected

    def test_delete_record(self):
        manager = recordManager()
        self.assertAlmostEqual(manager.deleteRecord("Juan", "juan@itesm.mx", "33", "Mexico"), 0)

    def test_delete_non_existent_record(self):
        manager = recordManager()
        with self.assertRaises(ValueError):
            manager.deleteRecord("Pepito", "pepito@itesm.mx", "55", "Mexico")
        logging.error("Look for not-exist value in deleteRecord.")

    def test_add_bunch_of_records(self):
        manager = recordManager()
        self.assertAlmostEqual(manager.addRecord("Ivan", "ivan@itesm.mx", "37", "Mexico"), 0)
        self.assertAlmostEqual(manager.addRecord("Fabiola", "fabiola@itesm.mx", "22", "Bolivia"), 0)
        self.assertAlmostEqual(manager.addRecord("Edwin", "edwin@itesm.mx", "31", "Costa Rica"), 0)
        self.assertAlmostEqual(manager.addRecord("Angelica", "angelica@itesm.mx", "29", "Mexico"), 0)
        self.assertAlmostEqual(manager.addRecord("Diana", "diana@itesm.mx", "45", "Mexico"), 0)
        self.assertAlmostEqual(manager.addRecord("Carlos", "carlos@itesm.mx", "18", "Brasil"), 0)
        self.assertAlmostEqual(manager.addRecord("Mariano", "mariano@itesm.mx", "50", "Mexico"), 0)

    def test_look_by_mail(self):
        manager = recordManager()
        self.assertAlmostEqual(manager.lookbyMail("lalo@itesm.mx"), 0)

    def test_look_by_non_existent_mail(self):
        manager = recordManager()
        with self.assertRaises(ValueError):
            manager.lookbyMail("pepito@itesm.mx")
        logging.error("Look for not-exist value in lookbyMail.")

    def test_look_by_age(self):
        manager = recordManager()
        self.assertAlmostEqual(manager.lookbyAge("25"), 0)

    def test_look_by_non_existent_age(self):
        manager = recordManager()
        self.assertAlmostEqual(manager.lookbyAge("999999999"), 0)   # No error expected

    def test_print_records(self):
        manager = recordManager()
        self.assertAlmostEqual(manager.printRecords(), 0)


if __name__ == '__main__':
    unittest.main()
