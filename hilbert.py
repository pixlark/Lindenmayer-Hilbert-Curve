import turtle as turtle_mod

#
# https://en.wikipedia.org/wiki/Hilbert_curve#Representation_as_Lindenmayer_system
#

axiom = ['a']

def rewrite(theorem):
  new_theorem = []
  for letter in theorem:
    if letter == 'a':
      new_theorem.extend(
        ['-', 'b', 'f', '+', 'a', 'f', 'a', '+', 'f', 'b', '-']
      )
    elif letter == 'b':
      new_theorem.extend(
        ['+', 'a', 'f', '-', 'b', 'f', 'b', '-', 'f', 'a', '+']
      )
    else:
      new_theorem.append(letter)
  return new_theorem

def draw(theorem):
  granularity = 50
  t = turtle_mod.Turtle()
  t.speed(10)
  for letter in theorem:
    if letter in ['a', 'b']:
      continue
    elif letter == 'f':
      t.forward(granularity)
    elif letter == '+':
      t.right(90)
    elif letter == '-':
      t.left(90)
    else:
      raise Exception('Letter not in alphabet')

def iterate(f, n, x):
  acc = x
  for i in range(n):
    acc = f(acc)
  return acc

if __name__ == '__main__':
  draw(iterate(rewrite, 4, axiom))
