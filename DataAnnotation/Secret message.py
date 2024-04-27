def decode(message_file):
  """Reads the file"""
  
  # Reads the file
  file = open(message_file, "r")

  # Creates an array that consist of each line of value
  lines = file.readlines()

  # Initialises a dictionary
  numword_dict = {}

  # Inputs the dictionary with respective num as key and word as value
  for line in lines:
    num , word = line.split(" ")
    word = word.replace("\n","")
    numword_dict.update({int(num) : word})

  # Returns the sorted dictionary in terms of its keys
  numword_dict = dict(sorted(numword_dict.items()))

  nums = list(numword_dict.keys())

  i , j = 0 , 2
  while(i < len(nums)):
    print(f"{numword_dict[nums[i]]} ")
    i += j
    j += 1

decode("coding_qual_input.txt")



  
     
  