import random
from argparse import ArgumentParser
from simulator import Simulator
from state import *
from probability import *
from agents import MarkovAgent, ParticleAgent
from grade_helpers import load_test, convert_solution

SCALE_FACTOR = 15 # DO NOT ALTER
WAIT_TIME = 0.2
VERBOSE = False

# These can 100% be written as one, but to keep things easy to understand and
# simplicitic we keep them as below

def markov_listen_test(simulator, state, solution):
  markov_agent = MarkovAgent(GameStateHandler(state).get_valid_positions())
  score = simulator.simulate_probability_agent(markov_agent, markov_agent.listen)
  if type(solution) == int:
    return score >= solution
  return markov_agent.thoughts() == convert_solution(solution)

def markov_predict_test(simulator, state, solution):
  markov_agent = MarkovAgent(GameStateHandler(state).get_valid_positions())
  score = simulator.simulate_probability_agent(markov_agent, markov_agent.predict)
  if type(solution) == int:
    return score >= solution
  return markov_agent.thoughts() == convert_solution(solution)

def particle_predict_test(simulator, state, solution):
  particle_agent = ParticleAgent(GameStateHandler(state).get_valid_positions())
  score = simulator.simulate_probability_agent(particle_agent, particle_agent.predict)
  if type(solution) == int:
    return score >= solution
  return particle_agent.thoughts() == convert_solution(solution)

def particle_listen_test(simulator, state, solution):
  particle_agent = ParticleAgent(GameStateHandler(state).get_valid_positions())
  score = simulator.simulate_probability_agent(particle_agent, particle_agent.listen)
  if type(solution) == int:
    return score >= solution
  return particle_agent.thoughts() == convert_solution(solution)

def particle_reset_test(simulator, state, solution):
  # Don't actually need simulator for this test
  # To make our lives simple we will match the maps open tiles (for divisibility purposes) when giving a particle count

  valid_positions = GameStateHandler(state).get_valid_positions()
  grid = ParticleGrid(valid_positions, len(valid_positions) * SCALE_FACTOR)

  particle_dist = grid.get_particle_distribution()

  # Mess up the distribution
  for key in particle_dist:
    particle_dist[key] = random.random()

  # Reset the distribution
  grid.reset()

  return grid.get_particle_distribution() == convert_solution(solution)

def particle_reweight_test(simulator, state, solution):
  # Don't actually need simulator for this test
  # To make our lives simple we will match the maps open tiles (for divisibility purposes) when giving a particle count

  valid_positions = GameStateHandler(state).get_valid_positions()
  grid = ParticleGrid(valid_positions, len(valid_positions) * SCALE_FACTOR)


  # Generate a random distribution
  dist = { key:random.random() for key in grid.get_particle_distribution() }

  # Reweight the particles
  grid.reweight_particles(dist)
  
  return grid.get_particle_distribution() == convert_solution(solution)

def test(tests, tester):
  total_marks, earned_marks = 0, 0

  for test in tests:
    name, map_file, seed, solution = load_test(test)

    total_marks += 1

    try:
      # Run the test
      state = GameState(map_file)
      random.seed(seed)

      sim = Simulator(map_file, WAIT_TIME)
      sim.verbose(VERBOSE)
      
      result = tester(sim, state, solution)
      earned = int(result) 
      print("Testing: {}\t [{}/{}]".format(name, earned, 1))

      earned_marks += earned
      
    except NotImplementedError as e:
      print("Testing {}\t [{}]\t [0/1]".format(name, e))

  return earned_marks, total_marks
  
if __name__ == "__main__":
  parser = ArgumentParser(description = "Running Autograder for Assignment 4")
  parser.add_argument("-v", "--verbose", help = "Displays the actions the agent is taking during the simulation",
                      required = False, default = "")
  parser.add_argument("-w", "--waitTime", type = float,
                      help = "How long the simulation waits before taking another action", required = False, default=0.1)

  # Setting up based on arguments
  args = parser.parse_args()
  VERBOSE = args.verbose
  if args.waitTime :
    WAIT_TIME = args.waitTime

  # Start the tests  
  total_marks, earned_marks = 0, 0
  
  print("------ Question 1 ------")
  e, t = test(["listen/small_markov_test", "listen/small_markov_test_2",
               "listen/markov_confirm_test", "listen/markov_confirm_test_2"], markov_listen_test)
  total_marks += t
  earned_marks += e
  
  print("\n------ Question 2 ------")
  e, t = test(["predict/small_markov_test", "predict/medium_markov_test",
               "predict/markov_confirm_test", "predict/markov_confirm_test_2"], markov_predict_test)
  total_marks += t
  earned_marks += e
  
  print("\n------ Question 3 ------")
  e, t = test(["particles/open_test", "particles/entity_test"], particle_reset_test)
  total_marks += t
  earned_marks += e

  print("\n------ Question 4 ------")
  e, t = test(["particles/weight_test", "particles/weight_test_2"], particle_reweight_test)
  total_marks += t
  earned_marks += e
  
  print("\n------ Question 5 ------")
  e, t = test(["listen/small_particle_test", "listen/small_particle_test_2",
               "listen/particle_confirm_test", "listen/particle_confirm_test_2"], particle_listen_test)
  total_marks += t
  earned_marks += e
  
  print("\n------ Question 6 ------")
  e, t = test(["predict/small_particle_test", "predict/medium_particle_test",
               "predict/particle_confirm_test", "predict/particle_confirm_test_2"], particle_predict_test)
  total_marks += t
  earned_marks += e
  
  print("\n\nTotal Grade: {}/{}".format(earned_marks, total_marks))
