# b.ignited codechallenge: square root

### Prerequisites

- Python 3

### Run

`python3 main.py`

### Test

`python3 -m unittest test_square.py -v`

### Description:

Tijd voor het berekenen van de vierkantswortel van een getal. Zonder vierkantswortel functies te gebruiken. Met andere woorden, geen .rooted() of .squared().
Print dit getal uit top op 5 komma getallen. Bv. De vierkantswortel van 15 is 3.87298.

### Solution:

1. Created squareroot method in square.py which calculates the exponent 0.5 of a given number, this results in the root of the given number.  
The method throws an exception when the given number is negative.  

2. The main method uses the squareroot method and formats the result to 5 decimals. It also catches the exception and prints the message.