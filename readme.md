# alpha-Necklace-Splitting
This repository contains an implementation of the algorithm for alpha-Necklace-Splitting developed during my Master's Thesis.
The implementation can be found in the `Necklace` folder.
Moreover, there is a `usage.py` script showing examples how to use the `Necklace` class.
Furthermore, the file `sat_to_neckl.py` is an implementation of our reduction from 3SAT to alpha-Necklace-Splitting in general necklaces.

## Usage
First install the requirements listed in `requirements.txt`:
```bash
pip install -r requirements.txt
```

### Necklace
A driver program can be invoked by
```bash
python alphacut.py
```
See its documentation (```python alphacut.py --help```) for how to use that program.

Otherwise, you can also use our implementation of necklaces as a library.
To use our implementation of necklaces put the `Necklace` folder in your working directory.
Then you can use 
```python
from Necklace.necklace import *
```
to get access to the `Necklace` class.
To construct a necklace use the constructor:
```python
neckl = Necklace(<<some string representing necklace>>)
```
where ```<<some string representing necklace>>``` is a string or a list that represents the necklace from left to right.
For example, ```"abbbaaa"``` can be used to represent the necklace $C_a = \{1,5,6,7\}, C_b = \{2, 3, 4\}$.
The same necklace can also be represented by the list ```[1, 2, 2, 2, 1, 1, 1]```.

Our implementation of our algorithm of $\alpha$-Necklace-Splitting is given in the function `findAlphaCut`.
It takes as input a dictionary representing $\alpha$ and returns a tuple corresponding to the $\alpha$-cut and $\overline{\alpha}$-cut.
In the above example, a valid dictionary could be
```python
alpha = {"a": 2, "b": 3}
```
then call `findAlphaCut` as 
```python
from Necklace.necklace import *
neckl = Necklace("abbbaaa")
alpha = {"a":2, "b": 3}
alphaCut, negAlphaCut = neckl.findAlphaCut(alpha)
```
See `usage.py` for a more in-depth introduction.

### sat_to_neckl.py
`sat_to_neckl.py` contains an implementation of the reduction from 3SAT to general necklace splitting used to show NP-completeness of the latter.
To see its documentation, run it as
```bash
python sat_to_neckl.py
```
You can specify the clauses of the 3SAT instance as command line arguments and the program will output a necklace and its alpha-vector obtained from the reduction.