# The factorial - a digression

We now have almost everything we need in order to write a program to generate all the possible permutations of `n` symbols.  There is, however, one final programming concept that we need if we are to complete this task.  This is the notion of recursion, which we will understand by writing a program to calculate ![](https://render.githubusercontent.com/render/math?math=n!).  Recall that ![](https://render.githubusercontent.com/render/math?math=n!) is calculated as:

![](https://render.githubusercontent.com/render/math?math=n!=n.(n-1).(n-2).(n-3)\dots\3.\2.\1)

A curiosity of n! is thus that:

![](https://render.githubusercontent.com/render/math?math=n!=n.(n-1)!)

Now consider the following code:

````
for i in range(10) : print(i)
````

we can write this using recursion instead of using a loop as follows:

````
def loop(i) : 
    print(i) 
    i = i + 1 
    if i==10 : return 
    loop(i) 

loop(0)
````

Notice here how the function loop calls itself.  The fact that the function calls itself is why, in fact, the action inside the code is performed multiple times.

Your task in this exercise is to write a function called factorial that takes a single argument `n` and that returns `n!`.  You should use recursion in your function so there should not be a for loop anywhere in your function.  
