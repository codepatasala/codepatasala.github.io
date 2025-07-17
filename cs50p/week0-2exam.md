# CS50P Week 0/Week 1/Week 3 Practice Exam

There are 4 questions below. All four need to be attempted.

## Submission Instructions

* Create one file for each challenge.
  * For example, `challenge1.py` for the first one.
* Each file should have the given function implemented.
  * For example, `challenge1.py` should have the `even_or_odd` function which takes a number as input.
* Zip all of them to `exam1.zip` and share on WhatsApp.

## Challenges
### Challenge 1: Even or Odd
Write a Python function that takes an integer as input and returns "Even" if the number is even, and "Odd" otherwise.
**Example:**
```python
print(even_or_odd(4))  # Output: "Even"
print(even_or_odd(3))  # Output: "Odd"
```
### Challenge 2: Grade Calculator
Write a Python function that takes a score (0-100) as input and returns the corresponding grade (A, B, C, D, or F).
Use the following grading scale:

- A: 90-100
- B: 80-89
- C: 70-79
- D: 60-69
- F: below 60

**Example:**
```python
print(calculate_grade(85)) # Output: "B"
print(calculate_grade(42)) # Output: "F"
```
### Challenge 3: String Manipulation
Write a Python function that takes a string as input and returns the string with all vowels removed.
**Example:**
```python
print(remove_vowels("Hello World")) # Output: "Hll Wrld"
```
### Challenge 4: Rock, Paper, Scissors
Write a Python function that simulates a game of Rock, Paper, Scissors between two players.
The function should take two inputs (player 1's choice and player 2's choice) and return the winner.
Each player's choice should be one of the following: "Rock", "Paper", or "Scissors".
The function should return a string indicating the winner of the game. For example:

- "Player 1 wins!" if player 1 wins
- "Player 2 wins!" if player 2 wins
- "It's a tie!" if both players make the same choice

**Example:**
```python
print(rock_paper_scissors("Rock", "Scissors")) # Output: "Player 1 wins!"
print(rock_paper_scissors("Scissors", "Paper")) # Output: "Player 1 wins!"
print(rock_paper_scissors("Paper", "Rock")) # Output: "Player 1 wins!"
print(rock_paper_scissors("Rock", "Rock")) # Output: "It's a tie!"
```