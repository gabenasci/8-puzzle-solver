class EightPuzzle():

  def __init__(self):
    self.sequence = []
    

  def sequence_input(self):
    self.sequence = list(input("Digite a sequência do 8-puzzle (use 0 para espaço vazio): "))
    try:
      # set([num for num in self.sequence if self.sequence.count(num) > 1])
      if len(self.sequence) == 9 and '0' in self.sequence:
        for i in range(len(self.sequence)):
          # if int(number) < 9 and int(number) >= 0:
          if(self.sequence[i] == '0'):
            self.sequence[i] = ' '
          else:
            pass
      else:
        print("Não é uma sequência válida")
    except IndexError:
      print("Não é uma sequência válida")
      

  def print_puzzle(self):
      print(self.sequence[0], self.sequence[1], self.sequence[2])
      print(self.sequence[3], self.sequence[4], self.sequence[5])
      print(self.sequence[6], self.sequence[7], self.sequence[8]+'\n')  

  # Mover quadrado vazio para cima e setar self.sequence com a nova sequência  
  def move_up(self):
    new_sequence = self.sequence[:] 
    empty_sq = new_sequence.index(' ') # Descobrir indice do quadrado vazio

    if empty_sq not in [0, 1, 2]:
      moved_sq = new_sequence[empty_sq - 3]
      new_sequence[empty_sq - 3] = new_sequence[empty_sq]
      new_sequence[empty_sq] = moved_sq
      self.sequence = new_sequence
      return self.sequence

    # Se quadrado vazio estiver na primeira linha, não é possível movê-lo
    else:
      return None
   
  def move_down(self):
    new_sequence = self.sequence[:]
    empty_sq = new_sequence.index(' ')

    if empty_sq not in [6, 7, 8]:
      moved_sq = new_sequence[empty_sq + 3]
      new_sequence[empty_sq + 3] = new_sequence[empty_sq]
      new_sequence[empty_sq] = moved_sq
      self.sequence = new_sequence
      return self.sequence
    else:
      return None

    
  def move_left(self):
    new_sequence = self.sequence[:]
    empty_sq = new_sequence.index(' ')

    if empty_sq not in [0, 3, 6]:
      moved_sq = new_sequence[empty_sq - 1]
      new_sequence[empty_sq - 1] = new_sequence[empty_sq]
      new_sequence[empty_sq] = moved_sq
      self.sequence = new_sequence
      return self.sequence
    else:
      return None

  def move_right(self):
    new_sequence = self.sequence[:]
    empty_sq = new_sequence.index(' ')

    if empty_sq not in [2, 5, 8]:
      moved_sq = new_sequence[empty_sq + 1]
      new_sequence[empty_sq + 1] = new_sequence[empty_sq]
      new_sequence[empty_sq] = moved_sq
      self.sequence = new_sequence
      return self.sequence
    else:
      return None
  
  @property
  def sequence(self):
    return self.sequence



