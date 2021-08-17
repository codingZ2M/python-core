# Functions with Parameters to make it dynamic
""" Parameterized functions are able to receive values for its parameters
dynamically and function parameters can be used inside the  function
"""

# Arguments are passed when we call the function
# Functions that do things based on the parameters / arguments that we give it.

# Indentation:
def product_display(product):
    if product == "iPhone":
        print("iPhone")
    elif product == "Laptop":
        print("Laptop")
    else:
        print("No Product Selected")

product_display("iPhone") # Calling a function by passing an argument

print('**********************************************')
print()



# function with declaration with 'positional' parameters /variables
def getAuto(model, engine, tech_specs):
         print(f" Auto: {model} \n" 
               f" Engine: {engine}  \n"  # code block
               f" Tech Specs: {tech_specs} \n"
            )



# Arguments - The actual values, we provide to the function parameters
# Here function is made more extensible, can be used in multiple places.
# Positional Arguments are arguments which require to be in the proper position

# calling/invoking the function with positional 'Arguments'
getAuto("812 Superfast", " CV AT 8500 RPM", "Power Train: V12 "
        " | 0-100 KM/H: 2.9sec | Specific Output: 123 cv/I | Max Power: 800cv")
getAuto("SF90 Spider", " CV AT 8500 RPM", "Power Train: V12 "
        " | 0-100 KM/H: 2.9sec | Specific Output: 123 cv/I | Max Power: 800cv")

print()



# Defining the method that has default parameters
def getAuto(model,  tech_specs, engine="CV AT 8500 RPM"):
    print(f" Auto: {model} \n"
          f" Engine: {engine}  \n"  # code block
          f" Tech Specs: {tech_specs} \n"
          )

# Calling the method (without argument) that has default parameter
getAuto("SF90 Spider", "Power Train: V12 "
        " | 0-100 KM/H: 2.9sec | Specific Output: 123 cv/I | Max Power: 800cv",
        engine="VAT 800")
