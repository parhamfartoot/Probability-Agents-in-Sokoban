from json import load

def convert_solution(solution):
  return { tuple(pos):prob for pos, prob in solution }

def load_test(test_name):
  with open("assets/tests/{}.json".format(test_name), "r") as f:
    test = load(f)
    
  return test["test_name"], test["map"], test["seed"], test["solution"]
