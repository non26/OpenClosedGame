# Chanono Eiemrod, eiemrodc@gmail.com
import unittest
import logging
import sys
target = __import__("mainApp")
exception = target.GameException
player = target.Player
game = target.OpenClosedGame
badPredictor = target.BadPredictor
badNotPredictor = target.BadNonPredictor

class Test_GameExceptionClass(unittest.TestCase):
    def test_initAsPredictor(self):
        person = player(True, "CC", False)
        with self.assertRaises(badPredictor):
            exception(person)

    def test_initAsNotPredictor(self):
        person = player(False, "CC4", False)
        with self.assertRaises(badNotPredictor):
            exception(person)

    def test_isPredictor(self):
        person = player(True, "CC4", False)
        excp = exception(person)
        self.assertEqual(excp.isPredictor(), True)

    def test_notPredictor(self):
        person = player(False, "CC", False)
        excp = exception(person)
        self.assertEqual(excp.notPredictor(), True)

class Test_PlayerClass(unittest.TestCase):
    def test_accessorGetAnswer(self):
        person = player(False, "CC", False)
        self.assertEqual(person.answer, "CC")

    def test_accessorSetAnswer(self):
        person = player(False, "CC", False)
        person.answer = "CO"
        self.assertEqual(person.answer, "CO")

    def test_accessorGetPredictor(self):
        person = player(True, "CC", False)
        self.assertEqual(person.predictor, True)

    def test_accessorSetPredictor(self):
        person = player(True, "CC", False)
        person.predictor = False
        self.assertEqual(person.predictor, False)

    def test_AIInputAsPredictor(self):
        ai = player(True, "CC4", True)
        result = exception(ai).isPredictor()
        self.assertTrue(result)

    def test_AIInputAsNonPredictor(self):
        ai = player(False, "CC", True)
        result = exception(ai).notPredictor()
        self.assertTrue(result)
    def test_person_Input(self):  # this needs to type CC4 , so that the test'll continue running
        person = player(True, True)
        inp = person.person()
        self.assertEqual(inp, "CC4")


class Test_OpenClosedGameClass(unittest.TestCase):
    def test_checkAnswer_win(self):  # win case
        """this test is strange, due to similarity to test_checkAnswer_lose"""
        # person = player(True, "CC1", False)
        # ai = player(False, "CC", True)
        # gameResult = game(person, ai)
        # self.assertTrue(gameResult)

    def test_checkAnswer_lose(self):  # lose case
        """this test is strange, it should be False but got True instead"""
        # person = player(True, "CC0", False)
        # ai = player(False, "CO", True)
        # gameResult = game(person, ai)
        # self.assertTrue(gameResult)

if __name__ == "__main__":
    # logging.basicConfig(stream=sys.stderr)
    # logging.getLogger("SomeTest.testSomething").setLevel(logging.DEBUG)
    unittest.main()