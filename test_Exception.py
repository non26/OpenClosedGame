class BadPredictor(Exception):
    def __init__(self):
        self.msg = """Bad input for predictor, Input should contain only with
                         the start of first two character is 'C' or 'D'
                         and third character is a number in 0-4"""

    def __str__(self):
        return self.msg
def test():
    raise BadPredictor()
try:
    raise BadPredictor()
except BadPredictor as e:
    print(e)
