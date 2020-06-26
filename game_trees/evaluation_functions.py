from state import *

# Here you will implement evaluation functions. Recall that weighing components of your
# evaluation differently can have positive effects on performance. For example, you could
# have your evaluation prioritize running away from opposing agents instead of activiating
# switches. Also remember that for values such as minimum distance to have a positive effect
# you should inverse the value as _larger_ evaluation values are better than smaller ones.

# Helpful Functions:
# You may define any helper functions you want in this file.
# GameState.get_enemies() --> returns a list of opposing agent positions.
# GameState.get_boxes() --> returns a list of (row, col) positions representing where the boxes are on the map
# GameState.get_switches() --> returns a dictionary where the keys are the locations of the switches as (row, col) and the value
#                              being True if the switch is on and False if off.
# GameState.get_player_position() --> returns the current position of the player in the form (row, col)
# GameState.get_remaining_points() --> returns a list of the positions of the remaining armory points of the map in the form (row, col) 
  
class EvaluationFunctions:

  @staticmethod
  def score_evaluation(state):
    return state.get_score()
  
  @staticmethod
  def box_evaluation(state):
    #Question 4, your box evaluation solution goes here
    #Returns a numeric value evaluating the given state where the larger the better
    raise NotImplementedError("Box Evaluation not implemented")

  @staticmethod
  def points_evaluation(state):
    #Question 5, your points evaluation solution goes here
    #Returns a numeric value evaluating the given state where the larger the better
    raise NotImplementedError("Points Evaluation not implemented")
