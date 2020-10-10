import asn1tools as asn
import json

### STUDENT PERSPECTIVE (example) ###

# Below code should behave like a black-box.
# That means that by clicking RUN (and, perhaps, changing the location of the exercise file), your output file should be generated.

base_location = '/Users/lunguteodor/OneDrive/Documents/Facultate/2020-2021 (Second Year)/Quarter 1 - 2020-2021/Week 7 - 12 Oct 2020/AfS'
ops_loc = base_location + 'operations.asn'
exs_loc = base_location + 'input.ops'

# Compile specification
spec = asn.compile_files(ops_loc, codec = "jer")

# Read exercise list
exercise_file = open(exs_loc, 'rb') # open binary file
file_data = exercise_file.read() # read byte array
my_exercises = spec.decode('Exercises', file_data) # decode after specification
exercise_file.close() # close file

# Create answer JSON
my_answers = {'exercises': []}

# Loop over exercises and solve
for exercise in my_exercises['exercises']:
    operation = exercise[0] # get operation type
    params = exercise[1] # get parameters
    
    if operation == 'add-field':
        params['answer'] = 'X+3'
        params['answer-poly'] = [1,3]
    
    if operation == 'add-table':
        params['answer'] = ['X+1', '2X+1']
        params['answer-poly'] = [[1,1], [2,1]]

    # Save answer
    my_answers['exercises'].append({operation : params})

# Save exercises with answers to file
my_file = open(base_location + "output.ops", "wb+") # write to binary file
my_file.write(json.dumps(my_answers).encode()) # add encoded exercise list
my_file.close()

###### Functions #########

def display_poly(poly , mod):
    s = "" #The final result will be stored in string s
    SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹") #Make translation table to display superscripts
    k = len(poly) #Store the power for each term

    for i in range(len(poly)): #Iterate through the coefficients of the polynomial starting with the leading coefficient
        k = k - 1 #Subtract 1 from the current power. If this is the first subtraction then this will be the leading power of the polynomial
        #If the powers are 1 or 0 then the formatting of those terms doesn't need superscripts or even the X
        if (i != len(poly) - 1 and i != len(poly) - 2):
            term = "X" + str(k)
            term = term.translate(SUP)
        elif i == len(poly) - 2:
            term = "X"
        else:
            term = ""

        #Reduce modulo mod if necessary
        if poly[i] >= mod or poly[i] < 0:
            poly[i] = poly[i] - mod * (poly[i]//mod)
        
        #If the coefficient is 1 or 0 then it doesn't need to be shown
        if(poly[i] != 0 and (poly[i] != 1 or i == len(poly) - 1)):
            term = str(poly[i]) + term

        #The leading term does not need a + and if it is 0 then the following term doesn't need a plus either
        if (k != len(poly) - 1 and not (k == len(poly) - 2 and poly[0] == 0)):
                term = "+" + term
        
        #If the coefficient is 0 then the entire term doesn't need to be shown
        if (poly[i] != 0):
            s = s + term
    
    #Print and return the result
    print(s)
    return s

display_poly([5,1,1,-2,1,3,2,1,1,1,1,1,1,24,1,0],5)