# n-gram-morse-solver
A solver for morse code puzzles where no character separator is given, but a word separator is.

How to use
-----
Open GeoSolver.py in your favourite IDE, and change the variable ciphertext at the beginning to the morse you want to decode. It should be dots and dashes (not dashes and dots), with each word separated by a space. Optionally, if you do not have anything you want to decode, but still want to test the program you can leave the ciphertext as is. You can now run the module.

some things to consider:
-----
The program is currently slow to process long words, and has no support for punctuation. This may or may not change in the future. Feel free to submit a PR if you think you can improve it in any way.

How it works!
----
The program generates all possible variations of the word, and sorts them by a couple of metrics:
1. how many characters are likely to be part of a word
2. how much like an english word it is, which is determined by what substrings (from 2 to 5 characters) it has. Substrings that appear more often in natural english should be given a higher score.
