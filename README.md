## Python Strings
### HackerRank Challenges
#### Domain:Python
#### Sub Domain:Strings

#### Swap Case
For Example:
         Www.HackerRankSolution.in → wWW.hACKERrANKsOLUTION.IN
         Pythonist 2 → pYTHONIST 2


#### String Split and Join
In Python, a string can be split on a delimiter.
Example:
      >>> a = "this is a string" 
      >>> a = a.split(" ") # a is converted to a list of strings. 
      >>> print a
      ['this', 'is', 'a', 'string']
Joining a string is simple:
      >>> a = "-".join(a)
      >>> print a
      this-is-a-string 

#### What's Your Name?

#### Mutations
We have seen that lists are mutable (they can be changed), and tuples are immutable (they cannot be changed).
Let's try to understand this with an example.
You are given an immutable string, and you want to make changes to it.
Example:
     >>> string = "abracadabra"
You can access an index by:
     >>> print string[5]
            a
What if you would like to assign a value?
           >>> string[5] = 'k' 
          Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
          TypeError: 'str' object does not support item assignment
How would you approach this?
        One solution is to convert the string to a list and then change the value.
Example:
>>> string = "abracadabra"
>>> l = list(string)
>>> l[5] = 'k'
>>> string = ''.join(l)
>>> print string
abrackdabra
Another approach is to slice the string and join it back.
Example:
>>> string = string[:5] + "k" + string[6:]
>>> print string
abrackdabra

#### Find a String
In this challenge, the user enters a string and a substring. 
NOTE: String letters are case-sensitive.


#### String Validators
Python has built-in string validation methods for basic data. It can check if a string is composed of alphabetical characters, alphanumeric characters, digits, etc.

str.isalnum()
This method checks if all the characters of a string are alphanumeric (a-z, A-Z and 0-9).

>>> print 'ab123'.isalnum()
True
>>> print 'ab123#'.isalnum()
False

str.isalpha()
This method checks if all the characters of a string are alphabetical (a-z and A-Z).

>>> print 'abcD'.isalpha()
True
>>> print 'abcd1'.isalpha()
False

str.isdigit()
This method checks if all the characters of a string are digits (0-9).

>>> print '1234'.isdigit()
True
>>> print '123edsd'.isdigit()
False

str.islower()
This method checks if all the characters of a string are lowercase characters (a-z).

>>> print 'abcd123#'.islower()
True
>>> print 'Abcd123#'.islower()
False

str.isupper()
This method checks if all the characters of a string are uppercase characters (A-Z).

>>> print 'ABCD123#'.isupper()
True
>>> print 'Abcd123#'.isupper()
False

#### Text Alignment
In Python, a string of text can be aligned left, right and center.

.ljust(width)

This method returns a left aligned string of length width.

>>> width = 20
>>> print 'HackerRank'.ljust(width,'-')
HackerRank---------- 
 
.center(width)

This method returns a centered string of length width.

>>> width = 20
>>> print 'HackerRank'.center(width,'-')
-----HackerRank----
-
.rjust(width)

This method returns a right aligned string of length width.

>>> width = 20
>>> print 'HackerRank'.rjust(width,'-')
----------HackerRank

#### Text Wrap
You are given a string S and width w.


#### Designer Door Mat
Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

     1. Mat size must be MXN. (N is an odd natural number, and M is 3 times N.)
     2. The design should have 'WELCOME' written in the center. 
     3. The design pattern should only use |, . and - characters.


Sample Designs:

    Size: 7 x 21 
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------
    
    Size: 11 x 33
    ---------------.|.---------------
    ------------.|..|..|.------------
    ---------.|..|..|..|..|.---------
    ------.|..|..|..|..|..|..|.------
    ---.|..|..|..|..|..|..|..|..|.---
    -------------WELCOME-------------
    ---.|..|..|..|..|..|..|..|..|.---
    ------.|..|..|..|..|..|..|.------
    ---------.|..|..|..|..|.---------
    ------------.|..|..|.------------
    ---------------.|.---------------



### String Formatting
Given an integer, n, print the following values for each integer i from 1 to n:

     1. Decimal
     2. Octal
     3. Hexadecimal (capitalized)
     4. Binary

The four values must be printed on a single line in the order specified above for each i from 1 to n. Each value should be space-padded to match the width of the binary value of n.


#### Alphabet Rangoli
You are given an integer, N. Your task is to print an alphabet rangoli of size N. (Rangoli is a form of Indian folk art based on creation of patterns.)

Different sizes of alphabet rangoli are shown below:

#size 3

----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

#size 5

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------

#size 10

------------------j------------------
----------------j-i-j----------------
--------------j-i-h-i-j--------------
------------j-i-h-g-h-i-j------------
----------j-i-h-g-f-g-h-i-j----------
--------j-i-h-g-f-e-f-g-h-i-j--------
------j-i-h-g-f-e-d-e-f-g-h-i-j------
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
------j-i-h-g-f-e-d-e-f-g-h-i-j------
--------j-i-h-g-f-e-f-g-h-i-j--------
----------j-i-h-g-f-g-h-i-j----------
------------j-i-h-g-h-i-j------------
--------------j-i-h-i-j--------------
----------------j-i-j----------------
------------------j------------------
The center of the rangoli has the first alphabet letter a, and the boundary has the Nth alphabet letter (in alphabetical order).


#### Capitalize!
You are asked to ensure that the first and last names of people begin with a capital letter in their passports. For example, alison heck should be capitalised correctly as Alison Heck.

alison heck => Alison Heck

Given a full name, your task is to capitalize the name appropriately.

#### The Minion Game
Kevin and Stuart want to play the 'The Minion Game'.

Game Rules

Both players are given the same string, S.
Both players have to make substrings using the letters of the string S.
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string S.

For Example:
String S = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

#### Merge the Tools!
Consider the following:

     1. A string, s, of length  where s=c0,c1.....cn-1.
     2. An integer, k, where k is a factor of n.

We can split s into n/k subsegments where each subsegment, ti, consists of a contiguous block of k characters in s. Then, use each ti to create string ui such that:
 
      1. The characters in ui are a subsequence of the characters in ti.
      2. Any repeat occurrence of a character is removed from the string such that each character in ui 
           occurs exactly once. In other words, if the character at some index j in ti occurs at a previous 
           index <j in ti, then do not include the character in string ui.

Given s and k, print n/k lines where each line  denotes string ui.



