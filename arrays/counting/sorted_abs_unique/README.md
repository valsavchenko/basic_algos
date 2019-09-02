Problem Formulation
===================

Given an ordered array of integers. Count the number of unique, in terms of absolute values, elements at it:

{-11, -7, -5, -1, 0, 1, 3} => 6
{-11, 11} => 1
{-11, -7, 11, 11} => 2

How to deploy the solution
========================
$ mkdir build
$ cd build
$ cmake <a path to a checkout of sorted_abs_unique>
$ make 
$ ./test/unittests
