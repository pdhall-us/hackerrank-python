
# String Split and Join

**Difficulty:** Easy  
**Category:** Strings  
**Language:** Python

**Problem Link:** [HackerRank - String Split and Join](https://www.hackerrank.com/challenges/python-string-split-and-join/problem)

## Problem Statement

In Python, a string can be split on a delimiter.

**Example:**

```python
>>> a = "this is a string"
>>> a = a.split(" ") # a is converted to a list of strings.
>>> print a
['this', 'is', 'a', 'string']
```

Joining a string is simple:

```python
>>> a = "-".join(a)
>>> print a
this-is-a-string
```

## Task

You are given a string. Split the string on a `" "` (space) delimiter and join using a `-` hyphen.

## Function Description

Complete the `split_and_join` function in the editor below.

`split_and_join` has the following parameters:

- `string line`: a string of space-separated words

## Returns

- `string`: the resulting string

## Input Format

The one line contains a string consisting of space separated words.

## Sample Input

```text
this is a string
```

## Sample Output

```text
this-is-a-string
```
