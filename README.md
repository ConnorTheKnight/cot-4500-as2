# cot-4500-as2
> Summary
  
  This is my submission for programming assignment 2, it contains 4 algorithms for approximating lines

> Instructions to Compile
  
  in order to compile the files in the src/test/ folder, 
    
    Type: "python3 src/test/Q#.py" in the terminal from the directory containing src
      or
    Type: "py src/test/Q#.py" in the terminal from the directory containing src
  Note that the # should be replaces by the question number of the file that you want to compile and execute

  in order to compile the files in the src/main/ folder the user must provide input according to the specifications listed in a following section, 
  it is reccomended that this is done by piping in input from a text file,
  (the example terminal commands provided will pipe in input from an input file named input.txt)
    
    Type: "python3 src/main/Q#.py < input.txt"
      or
    Type: "python3 src/main/Q#.py < input.txt"
> Instructions for Input for files in the src/main/ folder
  
  Instructions for Q1
    
    The first line of input should be a positive integer representing the number of datapoints to be entered (number of X values)
    The following n (where n is the number of datapoints specified in the first line) lines should be a pair of floating point numbers representing X and f(X) separated by a space
    The next line should be an integer representing the maximum degree of the polynomial that you want to approximate with (it should not exceed the number of data points)
    The next line should be a floating point number representing the x value that you want to get an approximate f(x) for
  Example input for Q1
    
    3
    3.6 1.675
    3.8 1.436
    3.9 1.318
    2
    3.7
  Instructions for Q2
    
    The first line of input should be a positive integer representing the number of datapoints to be entered (number of X values)
    The following n (where n is the number of datapoints specified in the first line) lines should be a pair of floating point numbers representing X and f(X) separated by a space
    The next line should be a space separated list of integers representing the degrees of the polynomials that you want to get coefficients for
  Example input for Q2
    
    4
    7.2,23.5492
    7.4,25.3913
    7.5,26.8224
    7.6,27.4589
    1 2 3
  Instructions for Q3
    
    The first line of input should be a positive integer representing the number of datapoints to be entered (number of X values)
    The following n (where n is the number of datapoints specified in the first line) lines should be a pair of floating point numbers representing X and f(X) separated by a space
    The next line should be a floating point number representing the x value that you want to get an approximate f(x) for
  Example input for Q3
    
    4
    7.2,23.5492
    7.4,25.3913
    7.5,26.8224
    7.6,27.4589
    7.3
  Instructions for Q4
    
    The first line of input should be a positive integer representing the number of datapoints to be entered (number of X values)
    The following n (where n is the number of datapoints specified in the first line) lines should be 3 floating point numbers representing X, f(X), and f'(x) separated by a space
  Example input for Q4
    
    3
    3.6,1.675,-1.195
    3.8,1.436,-1.188
    3.9,1.318,-1.182
  Instructions for Q5
    
    The first line of input should be a positive integer representing the number of datapoints to be entered (number of X values)
    The following n (where n is the number of datapoints specified in the first line) lines should be a pair of floating point numbers representing X and f(X) separated by a space
  Example input for Q5
    
    4
    2 3
    5 5
    8 7
    10 9
> Requirements
  
  requirements.txt is not needed as the only imported package was NumPy

> Additional Note
  
  the tests for Q2 and Q3 do not match the provided expected output but both matched the sample outputs provided in the book and seem to be correct
  also the test for Q4 matches the provided expected output for all but one value with the provided output being incorrect from my own calculations
