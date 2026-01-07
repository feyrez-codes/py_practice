
def array_evaluator(superset: list, *subset: list, readable: bool=False) -> list:
  """
  :Purpose: Evaluate (a) given list(s) as part of a superset. Initially created to generate intelligent predictions for a tic-tac-toe bot.

  :Param: superset: list to be compared for subset combination matches
  :Param: *subset: list(s) to be compared as subsets to superset arg. 
    \nex: [1,2,3] returns [[1,2], [1,3], [2,3]]
  :Param: readable: If false, output remains as detailed below. if True, the function will return a dictionary with two key values: "array_{x}_combos", "array_{x}_matches" where x = arg index +1.

  :Output: every subset returns an list of two lists, matching the argument index
    \nList 1: Every possible combinations of the subset, up to 3 digit combos
    \nList 2: All partial or full match between list 1 and superset. Note:
        \nIf no matches are found, the second list will be empty
        \nex: a superset of [1,2,3] and a subset of [1,2,3] would return [1,2] as a partial combination. 
  """
  def mini_evaluator(target, test):
    """
    Purpose: convert both arguments to set then check if test is subset of target

    :Params: test: value to be searched for in target
    :Params: target: superset to be scrutinized for presence of test

    :Output: returns test if test is subset of target
    """
    x = set(target)
    y = set(test)
    if (x == y or y.issubset(x)): return list(y)

  expanded_array = []
  if readable: final_array = {}
  else: final_array = []

  for array in subset:
    if readable:
        combo_dkey = f"array_{subset.index(array)+1}_combos"
        match_dkey = f"array_{subset.index(array)+1}_matches"

    #create all combinations
    for seed in array:
      for stem in array:
        if seed != stem:

          #create groups of two:
          x = sorted([seed, stem])
          if x not in expanded_array:
            expanded_array.append(x)

          #create groups of three:
          for leaf in array:
            y = sorted([seed, stem, leaf])

            if (seed != leaf != stem and y not in expanded_array):
              expanded_array.append(y)
    
    #compare combinations to superset:    
    matches = []
    for array in expanded_array:
      if not isinstance(superset[0], list):
        matches.append(mini_evaluator(superset , array))
      else:
        for combo in superset:
          matches.append(mini_evaluator(combo, array))

    if readable:
      final_array[combo_dkey] = matches
      final_array[match_dkey] = expanded_array
    else:
      final_array.append(expanded_array)
      final_array.append(list(filter(None, matches)))

  return final_array