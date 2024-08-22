# import the necklace functionality, in particular this gives access to the Necklace class
from Necklace.necklace import *

# construct a necklace
neckl = Necklace("abbbaaa")
# construct an alpha vector (which is a dictionary, mapping type of beads to numbers)
alpha = {"a": 2, "b": 3}
# find alpha and negalpha cuts
alphaCut, negAlphaCut = neckl.findAlphaCut(alpha)
# display cuts nicely (beads on top are positive, beads on bottom negative, cut beads are in the middle)
print("Alpha cut:")
neckl.displayCut(alphaCut)
print("Negalpha cut:")
neckl.displayCut(negAlphaCut)
print()

# you can also construct a necklace using a list instead of a string
# this is helpful if there are a lot of beads
neckl = Necklace([1, 2, 2, 2, 1, 1, 1])
# need to change alpha accordingly, lets take another vector
alpha = {1: 4, 2: 1}
# only interested in alphaCut
alphaCut, _ = neckl.findAlphaCut(alpha)
print("Alpha Cut:")
neckl.displayCut(alphaCut)
print()

# if you want to have a necklace with a random amount of beads per component
# you can use the pumpNecklace function, use it on the necklace string
neckl = Necklace(pumpNecklace("aba"))
# show the necklace
print(neckl)
# we can search for tangents, by dont specifying an alpha
# that is, alpha will just be (1,1,...,1)
alphaCut, negAlphaCut = neckl.findAlphaCut()
print("Lower tangent:")
neckl.displayCut(alphaCut)
print("Upper tangent:")
neckl.displayCut(negAlphaCut)
print()

# the algorithm also works on larger necklaces (but they need to be n-separable)
neckl = Necklace(pumpNecklace("abcdeadfgdbhijha"))
alphaCut, negAlphaCut = neckl.findAlphaCut()
print("Lower tangent:")
neckl.displayCut(alphaCut)
print("Upper tangent:")
neckl.displayCut(negAlphaCut)
print()

# you can also generate large irreducible necklaces for some n
neckl = Necklace(getRandomIrreducible(10))
# note: neckl will be equivalent to a necklace string
# to have more beads per component use pumpNecklace
print(neckl)
print()

# a necklace object has the following attributes
neckl = Necklace("aabbbcccbb")
print(f"neckl: {neckl}")

# the order of the colours is determined how the colours appear in the necklace
# this is contrary to the definition of the thesis, which uses constant global order
print(f"neckl.typeIndex: {neckl.typeIndex}")

# each type of bead contains beads, which can be mapped
# to indices of the string/list representing the necklace
# so this is the representation as in the definition of the thesis
# where each colour is a set of numbers
print(f"neckl.beadDict: {neckl.beadDict}")

# similarly, each type of bead has occurrances in the necklace string
# in our example the necklace string is "abcb", so the indices of a are [0]
# indices of b are [1, 3] and incides of c are [2]
print(f"neckl.letterDict: {neckl.letterDict}")

# the indices of beads per component, where components are just the indices of the necklace string
# so in our example there are four components: 0,1,2,3, where 0 corresponds to the two 'a'
# 1 corresponds to the first three 'b', 2 corresponds to the three 'c', and 3 corresponds to the last two 'b'
print(f"neckl.componentDict: {neckl.componentDict}")

# the necklace has various metrics for its length/size
# n: number of colours
# N: total number of beads
# size: length of the necklace string
print(f"neckl.n: {neckl.n}")
print(f"neckl.N: {neckl.N}")
print(f"neckl.size {neckl.size}")

# finally, the walk graph of the necklace can also be accessed
print(f"neckl.graph: {neckl.graph}")
# to write the graph to a file use
G = neckl.graph
nx.nx_pydot.write_dot(G, "yourpath.dot")
