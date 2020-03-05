# Chanono Eiemrod, eiemrodc@gmail.com
import random
import re
class BadPredictor(Exception):
    def __init__(self):
        self.msg = """Bad input for predictor, 
Input should contain only 3 characters where the start of first two characters is 'C' or 'D'  
and third character is a number in range of 0-4"""

    def __str__(self):
        return self.msg

class BadNonPredictor(Exception):
    def __init__(self):
        self.msg = """Bad input for non-predictor, 
Input should contain only 3 characters where the start of first two characters is 'C' or 'D'"""

    def __str__(self):
        return self.msg

class GameException():
    def __init__(self, ply):
        self.player = ply # this object refers to player which is person
        if self.player.predictor:
            resultRegex = self.isPredictor()
            if not resultRegex:
                raise BadPredictor()
        else:
            resultRegex = self.notPredictor()
            if not resultRegex:
                raise BadNonPredictor()

    def isPredictor(self):
        compileObj = re.compile(r"^([CO]{2}[0-4])$")
        matchObj = compileObj.match(self.player.answer)
        return bool(matchObj)

    def notPredictor(self):
        compileObj = re.compile(r"^([CO]{2})$")
        matchObj = compileObj.match(self.player.answer)
        return bool(matchObj)

class Player:
    def __init__(self, predictor=None, ans=None, ai=None):
        self.mode = predictor # determine that is predictor or not, boolean
        self.ans = ans # input of player, string
        self.ai = ai # determine that is predictor or not, boolean
        self.result = None # win or lose,

    @property
    def answer(self):
        return self.ans

    @answer.setter
    def answer(self, setAns):
        self.ans = setAns

    @property
    def predictor(self):
        return self.mode

    @predictor.setter
    def predictor(self, setMode):
        self.mode = setMode

    def AI_random(self):
        answer = ""
        if self.predictor:
            for _ in range(2):
                answer += random.choice(["C", "O"])
            answer += str(random.randint(0, 4))
            return answer
        else:
            for _ in range(2):
                answer += random.choice(["C", "O"])
            return answer

    def person(self):
        answer = input().strip(" ").upper()
        return answer

class OpenClosedGame:

    msgPredictor = ["You are the predictor", "AI is the predictor"]
    win = True

    def __init__(self, ply1:Player, ply2:Player):
        self.player1 = ply1  # person
        self.player2 = ply2  # AI

    def checkAnswer(self):
        if self.player1.predictor: # player1 is predictor, input is in form cc3
            numberOfO = int(self.player1.answer[-1]) # extract the last character(a number) of input of player1
            setCharacter = self.player1.answer[:-1]+self.player2.answer # concatenate the literals of play1, play2
            cntO = setCharacter.count("O") # count O
            if cntO == numberOfO:
                print("you win")
                return OpenClosedGame.win
            else:
                print("no one win")
                return not OpenClosedGame.win
        elif self.player2.predictor: # player2 is predictor, input is in form cc3
            numberOfO = int(self.player2.answer[-1])
            setCharacter = self.player2.answer[:-1]+self.player1.answer
            cntO = setCharacter.count("O")
            if cntO == numberOfO:
                print("AI win")
                return OpenClosedGame.win
            else:
                print("no one win")
                return not OpenClosedGame.win

    def letlnput(self):
        while True:
            self.player1.answer = self.player1.person() # input of person player
            try:
                GameException(self.player1) # check that person's input is valid or not
            except (BadPredictor, BadNonPredictor) as e:
                print(e)
                print("try again!")
                continue
            else:
                break
        self.player2.answer = self.player2.AI_random() # input of AI player
        msg = f"AI: {self.player2.answer}"
        print(msg)

    def letPlay1(self):
        while True:
            if self.player1.predictor: # person
                print(OpenClosedGame.msgPredictor[0]+", What is your input?")
                self.letlnput() # method for player to input
                if self.checkAnswer(): # check that player1 win or not
                    break
                else: # if player1 doesn't win, so another player becomes predictor and continue playing
                    self.player1.predictor = False
                    self.player2.predictor = True
                    print("-"*20)
                    continue
            elif self.player2.predictor:
                print(OpenClosedGame.msgPredictor[1]+", What is your output?")
                self.letlnput()
                if self.checkAnswer():
                    break
                else:
                    self.player1.predictor = True
                    self.player2.predictor = False
                    print("-" * 20)
                    continue
        again = input("Do you want to play it again?(y/n): ").upper()
        if again in ("YES", "Y"):
            return True
        elif again in ("NO", "N"):
            print("ok, bye")
            return False
def main():
    personPly = Player(predictor=True, ai=False)
    AiPly = Player(predictor=False, ai=True)
    playGame = OpenClosedGame(personPly, AiPly)
    while True:
        again = playGame.letPlay1()
        if again: # set predictor to default if you want to play again
            personPly.predictor = True
            AiPly.predictor = False
            continue
        else:
            break
if __name__=="__main__":
    main()
    # person = Player(True, "CC1", False)
    # ai = Player(False, "CC", True)
    # gameResult = OpenClosedGame(person, ai)
    # print(gameResult.checkAnswer())
    # person = Player(True, "CC0", False)
    # ai = Player(False, "CC", True)
    # gameResult = OpenClosedGame(person, ai)
    # print(gameResult.checkAnswer())








