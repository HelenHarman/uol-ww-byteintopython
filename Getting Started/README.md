# Introduction to Python

Open the ByteIntoPython_GettingStarted_guide.pdf file for detailed instructions. This file contains an outline of the instructions within that PDF file.

This activity gets you to write your first lines of Python (if you haven't written Python before). 

1. Open up the hello_world.py file and try running it.
2. Use the pytest command to run the tests contained within test_hello_world.py. (The tests should all fail.)
3. Copy the following block of code into hello_world.py:
    ```
    # We use "def" to define a function.
    # This sum function takes two parameters, a and b. 
    def sum_two_values(a, b):
        return a + b
    
    # create two variables and assign integer values to them: 
    first = 2 
    second = 3
    # call our sum function and store the result in "result":
    result = sum_two_values(first, second)
    # print the result to the console:
    print (result)
    ```
4. Try running the code.
5. Copy in and run the following code:
    ```
    def sum_all(values):
        total = 0
        # loop through all values, and add them to total
        for value in values:
            total = total + value
        return total
        
    values = [3,4,5]
    # Call the sum_all function, pass it "values".
    # Print the result
    ```
6. Check your code runs. Re-running pytest should result in two tests passing.

See [https://derekfoster1976.github.io/GenAI_WW_Activity/genai_activity.html](https://derekfoster1976.github.io/GenAI_WW_Activity/WW_GenAI.html) for you Generative AI activity (i.e. Activity 2).
