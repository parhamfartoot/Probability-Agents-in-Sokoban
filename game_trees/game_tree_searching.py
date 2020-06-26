from state import *
from utils import *

class GameTreeSearching:
  # You will also find that the GameStateHandler class (already imported) will help perform needed operations on the
  # the game states. To declare a GameStateHandler simply wrap it around a GameState like such,
  # handler = GameStateHandler(GameState) where GameState will be an instance of GameState.
  
  # Below is a list of helpful functions:
  # GameStateHandler.get_successors() --> returns successors of the handled state
  # GameStateHandler.get_agents() --> returns a list of the positions of the agents on the map
  # GameStateHandler.get_agent_count() --> returns the number of agents on the map
  # GameStateHandler.get_agent_actions(agent_pos) --> returns a list of the possible actions the given agent can take
  # GameStateHandler.get_successor(agent_pos, action) --> returns the successor state if the given agent took the given action 
  # GameState.get_player_position() --> returns the players position in that game state as (row, col)
  # GameState.copy() --> returns a copy
  # GameState.is_win() --> returns True if the game state is a winning state
  # GameState.is_loss() --> returns True if the game state is a losing state

  # Hint:
  # To avoid unwanted issues with recursion and state manipulation you should work with a _copy_ of the state
  # instead of the original.

  @staticmethod
  def minimax_search(state, eval_fn, depth = 2):
    # Question 1, your minimax search solution goes here
    # Returns a SINGLE action based off the results of the search
    raise NotImplementedError("Minimax search not implemented")

  @staticmethod
  def alpha_beta_search(state, eval_fn, depth):
    # Question 2, your alpha beta pruning search solution goes here
    # Returns a SINGLE action based off the results of the search
    raise NotImplementedError("Alpha Beta Pruning search not implemented")

  @staticmethod
  def expectimax_search(state, eval_fn, depth):
    # Question 3, your expectimax search solution goes here
    # Returns a SINGLE action based off the results of the search
    raise NotImplementedError("Expectimax search not implemented")
