def snowflake(my_moves, opp_moves, comp_matrix, type_of_comp):
  """
  
  :Params: my_moves: array of nums 1-9 to be compared as a subset (sample array)
  :Params: opp_moves: array of nums 1-9 to be compared as a subset (sample array)
  :Params: comp_matrix: array of arrays to be compared as a superset (comparison array)


  :Output: returns 0/1/2/3 if neither/first/second/both sample array(s) are present in comparison array
  """
  new_array = []


def test(combos_of=3, arr=[1,2,3,4,5]):
  combos = []
  i = 2


  while i <= combos_of:
    for num in arr:
      new_item = [num]
      for x in range(i):
        for other_num in arr:
          if num == other_num:
            pass
          else:
            new_item.append(other_num)
            if len(new_item) == i: combos.append(new_item)
      i += 1

  print("hello!", combos)

test(3)