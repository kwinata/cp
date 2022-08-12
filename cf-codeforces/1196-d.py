#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
RGB Substring

You are given a string 𝑠 consisting of 𝑛 characters, each character is 'R', 'G' or 'B'.

You are also given an integer 𝑘.
Your task is to change the minimum number of characters in the initial string 𝑠 so that after the changes
there will be a string of length 𝑘 that is a substring of 𝑠,
and is also a substring of the infinite string "RGBRGBRGB ...".

A string 𝑎 is a substring of string 𝑏 if there exists
a positive integer 𝑖 such that 𝑎1=𝑏𝑖, 𝑎2=𝑏𝑖+1, 𝑎3=𝑏𝑖+2, ..., 𝑎|𝑎|=𝑏𝑖+|𝑎|−1.
For example, strings "GBRG", "B", "BR" are substrings of the infinite string "RGBRGBRGB ..."
while "GR", "RGR" and "GGG" are not.

You have to answer 𝑞 independent queries.

Input
The first line of the input contains one integer 𝑞
(1≤𝑞≤2000) — the number of queries. Then 𝑞 queries follow.

The first line of the query contains two integers 𝑛
and 𝑘 (1≤𝑘≤𝑛≤2000) — the length of the string 𝑠 and the length of the substring.

The second line of the query contains a string 𝑠 consisting of 𝑛 characters 'R', 'G' and 'B'.

It is guaranteed that the sum of 𝑛
over all queries does not exceed 2000 (∑𝑛≤2000).

Output
For each query print one integer — the minimum number of characters you need to change in the initial string 𝑠
so that after changing there will be a substring of length 𝑘 in 𝑠
that is also a substring of the infinite string "RGBRGBRGB ...".


Example

Input
3
5 2
BGGGG
5 3
RBRGR
5 5
BBBRR

Output
1
0
3

Note
In the first example, you can change the first character to 'R' and obtain the substring "RG", or change the second
character to 'R' and obtain "BR", or change the third, fourth or fifth character to 'B' and obtain "GB".
In the second example, the substring is "BRG".
"""