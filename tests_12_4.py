import rt_with_exceptions
from rt_with_exceptions import Runner, Tournament
import logging
import unittest


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        Runner(name='Alex')

        for i in range(10):
            Runner.walk = 50
            self.assertEqual(Runner.walk, 50)

        try:
            logging.info('"test_walk" выполнен успешно')
        except:
            logging.warning('Неверный скорость для Runner', exc_info=True)

    def test_run(self):
        Runner(name='Pavel')

        for i in range(10):
            Runner.run = 100
            self.assertEqual(Runner.run, 100)

        try:
            logging.info('"test_run" выполнен успешно')
        except:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)

    def test_challenge(self):
        Runner(name='Lena')
        Runner(name='Vova')

        for i in range(10):
            Runner.walk = 50
            Runner.run = 100
            self.assertNotEqual(Runner.walk, 100)
            self.assertNotEqual(Runner.run, 50)


logging.basicConfig(level=logging.INFO, filemode="w", filename="runner_tests.log", encoding='utf-8',
                    format="%(asctime)s | %(levelname)s | %(message)s")


class TournamentTest(unittest.TestCase):
    def setUpClass(self):
        self.all_finishers = {}
        print(self.all_finishers)

    def setUp(self):
        self.runer_1 = rt_with_exceptions.Runner('Усэйн', 10)
        self.runer_2 = rt_with_exceptions.Runner('Андрей', 9)
        self.runer_3 = rt_with_exceptions.Runner('Ник', 3)

    def tearDownClass(self):
        for i in self.all_finishers:
            print(i)

    def race_1_test(self):
        race_1 = rt_with_exceptions.Tournament(90, self.runer_1, self.runer_3)
        result = race_1.start()
        print(result[list(result.keys())[-1]] == 'Ник')
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник', 'Error!')
        self.all_finishers[1] = result
        self.assertEqual(Tournament.start, 90)

    def race_2_test(self):
        race_2 = rt_with_exceptions.Tournament(90, self.runer_2, self.runer_3)
        result = race_2.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник', 'Error!')
        self.all_finishers[2] = result
        self.assertEqual(Tournament.start, 90)

    def race_3_test(self):
        race_3 = rt_with_exceptions.Tournament(90, self.runer_1, self.runer_2, self.runer_3)
        result = race_3.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник', 'Error!')
        self.all_finishers[3] = result
        self.assertEqual(Tournament.start, 90)

    if __name__ == "__main__":
        unittest.main()

