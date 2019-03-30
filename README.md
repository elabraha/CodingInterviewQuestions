# CodingInterviewQuestions
A compilation of interview questions solved by me mostly in python.
___
#### 1. k_closest_points.py 
+ **Question:** Find the k closest points to the origin from a list of points.
+ **Solution:** I solved this problem by checking the euclidean distance between the point and the origin. Then I went through the list of points and checked each point against all k minimum distances (initialized with sys.maxint) and then if the distance was smaller than one of them on the list. I shifted the list of points and distances to the right by one. When the program has gone through the entire list of points I return the list of k closest points.
#### 2. Sudoku Solver
+ **Question:** Make a program that solves sudoku and checks if it is a valid solution.
+ **Solution:** My solution solves sudoku using backtracking a more thorough explaination is [here](https://en.wikipedia.org/wiki/Sudoku_solving_algorithms#Backtracking), [here](https://www.geeksforgeeks.org/backtracking-set-7-suduku/), and [here](https://algorithms.tutorialhorizon.com/backtracking-sudoku-solver/). 
    - I wrote my sudoku solver in two ways <sup>[[1]](#1)</sup>:
        1. Recursivly (outlined in the links above). 
        2. Iterativly which I sort of converted from my recursive solution using the idea that you can use a stack to make a recursive algorithm into an iterative one. The main differences are: A while loop with the base case (in the recursive solution) as a condition, a stack append replaced the recursive call, and a step to check for a valid placement that replaces the backtracking trigger in the recursive solution (checking if the recursive call returned true from the previous call).<sup>[[2]](#2)</sup>
    - I wrote my sudoku checker in a very weird way because I orginally wrote it for a daily codefights challange (or maybe it was for leetcode?). The question used strings instead of numbers for the cells. Anyway the solve is rediculous and uses a list of dictionaries. The dictionary is being used more like a set. The point is that, insted of iterating to check if number has been used in a section, I accumulate them in the dictionaries (sets) as I check so as not to check the whole section if the cells are empty.
#### 3. I started doing the daily coding challange problems will do a write up on those in that folder. See folder for write ups.
#### 4. Interview questions I didn't and I thought were difficult willl be posted in another folder for anyone's use.
#### 5. I want to do a write up of a topological sort problem.
#### 6. In the next few days I might start writing my code interview questions from my code interview question book in other languages. The list of languages I want to learn is currently way too long hahaha. But here it is:
    1) Haskell, 2) Erlang, 3) Go, 4) Ruby, 5) Get better at javascript (Typscript, Coffeescript), 6) Write more Java code, 7) Kotlin, 8) Dart (Flutter), 9) Haskell, 5) Elixer, etc., etc. 
#### 7. Write-up for egg drop coming soon.

###### 1
> There is a much better explanation about my solution in the comments of my code. I explain each line step by step.

###### 2
> If none of this makes any sense I assure you that, if you read about backtracking and/or look at my solution while you read this, it will.
