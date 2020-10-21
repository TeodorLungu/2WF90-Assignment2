import asn1tools as asn
import json
from add_field import add_field
from add_table import add_table
from add_poly import add_poly
from display_field import display_field
from display_poly import display_poly
from div_field import div_field
from equals_field import equals_field
from equals_poly_mod import equals_poly_mod
from extended_euclid import extended_euclid
from find_irred import find_irred
from findPrim import find_prim
from inverseField import inverseField
from irreducible import irreducible
from longdivision import long_div_poly
from mul_field import mul_field
from mul_poly import mul_poly
from mul_table import mul_table
from primitive import primitive
from sub_poly import sub_poly
from subtract_field import subtract_field
from variousFunctions import isPrime
### STUDENT PERSPECTIVE (example) ###

# Below code should behave like a black-box.
# That means that by clicking RUN (and, perhaps, changing the location of the exercise file), your output file should be generated.

base_location = '/Users/lunguteodor/Documents/GitHub/2WF90-Assignment2'
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
        mod = params['mod']
        mod_poly = params['mod-poly']
        a = params['a']
        b = params['b']
        if (isPrime(mod)==False or mod_poly==0):
            params['answer'] = "ERROR"
            params['answer-poly'] = []
        else:    
            params['answer'] = add_field(mod,mod_poly,a,b)[0]
            params['answer-poly'] = add_field(mod,mod_poly,a,b)[1]
    
    if operation == 'add-poly':
        mod = params['mod']
        a = params['f']
        b = params['g']
        params['answer'] = add_poly(mod,a,b)[0]
        params['answer-poly'] = add_poly(mod,a,b)[1]

    if operation == 'add-table':
        mod = params['mod']
        mod_poly = params['mod-poly']
        if (isPrime(mod)==False or mod_poly==0):
            params['answer'] = "ERROR"
            params['answer-poly'] = []
        else:   
            params['answer'] = add_table(mod,mod_poly)[0]
            params['answer-poly'] = add_table(mod,mod_poly)[1] 
    
    if operation == 'display-field':
        mod = params['mod']
        mod_poly = params['mod-poly']
        a = params['a']
        if isPrime(mod)==False:
            params['answer'] = "ERROR"
            params['answer-poly'] = []
        else:
            params['answer'] = display_field(mod,mod_poly,a)[0]
            params['answer-poly'] = display_field(mod,mod_poly,a)[1]

    if operation == 'display-poly':
        mod = params['mod']
        a = params['f']
        params['answer'] = display_poly(mod,a)[0]
        params['answer-poly'] = display_poly(mod,a)[1]

    if operation == 'div-field':
        mod = params['mod']
        mod_poly = params['mod-poly']
        a = params['a']
        b = params['b']
        if (isPrime(mod)==False or b==[0]):
            params['answer'] = "ERROR"
            params['answer-poly'] = []
        else:
            params['answer'] = div_field(mod,mod_poly,a,b)[0]
            params['answer-poly'] = div_field(mod,mod_poly,a,b)[1]

    if operation == 'equals-field':
        mod = params['mod']
        mod_poly = params['mod-poly']
        a = params['a']
        b = params['b']   
        params['answer'] = equals_field(mod,mod_poly,a,b)

    if operation == 'equals-poly-mod':
        mod = params['mod']
        mod_poly = params['f']
        a = params['g']
        b = params['h']
        params['answer'] = equals_poly_mod(mod,mod_poly,a,b)
    
    if operation == 'extended_euclid':
        mod = params['mod']
        a = params['f']
        b = params['g']
        if (isPrime(mod)==False):
            params['answ-a'] = "ERROR"
            params['answ-b'] = "ERROR"
            params['answ-d'] = "ERROR"
            params['answ-a-poly'] = []
            params['answ-b-poly'] = []
            params['answ-d-poly'] = []
        else:    
            params['answ-a'] = extended_euclid(mod,mod_poly,a,b)[0]
            params['answ-b'] = extended_euclid(mod,mod_poly,a,b)[1]
            params['answ-d'] = extended_euclid(mod,mod_poly,a,b)[2]
            params['answ-a-poly'] = extended_euclid(mod,mod_poly,a,b)[3]
            params['answ-b-poly'] = extended_euclid(mod,mod_poly,a,b)[4]
            params['answ-d-poly'] = extended_euclid(mod,mod_poly,a,b)[5]
    
    if operation == 'find-irred':
        mod = params['mod']
        deg = params['deg']
        if (isPrime(mod)==False):
            params['answer'] = "ERROR"
            params['answer-poly'] = []
        else:
            params['answer'] = find_irred(mod,deg)[0]
            params['answer-poly'] = find_irred(mod,deg)[1]
    
    if operation == 'find-prim':
        mod = params['mod']
        mod_poly = params['mod-poly']
        if isPrime(mod)==False:
            params['answer'] = "ERROR"
            params['answer-poly'] = []
        else:
            params['answer'] = find_prim(mod,mod_poly)[0]
            params['answer-poly'] = find_prim(mod,mod_poly)[1]

    if operation == 'inverse-field':
        mod = params['mod']
        mod_poly = params['mod-poly']
        a = params['a']
        if isPrime(mod)==False:
            params['answer'] = "ERROR"
            params['answer-poly'] = []
        else:
            params['answer'] = inverseField(mod,mod_poly,a)[0]
            params['answer-poly'] = inverseField(mod,mod_poly,a)[1]

    if operation == 'irreducible':
        mod = params['mod']
        f = params['f']
        params['answer'] = irreducible(mod,f)

    if operation == 'long-div-poly':
        mod = params['mod']
        f = params['f']
        g = params['g']
        if (isPrime(mod)==False or g==[0]):
            params['answ-q'] = "ERROR"
            params['answ-r'] = "ERROR"
            params['answ-q-poly'] = []
            params['answ-r-poly'] = []
        else:    
            params['answ-q'] = long_div_poly(mod,f,g)[0]
            params['answ-r'] = long_div_poly(mod,f,g)[1]
            params['answ-q-poly'] = long_div_poly(mod,f,g)[2]
            params['answ-r-poly'] = long_div_poly(mod,f,g)[3]

    if operation == 'mult-field':
        mod = params['mod']
        mod_poly = params['mod-poly']
        f = params['a']
        g = params['b']
        if (isPrime(mod)==False or mod_poly==[0]):
            params['answer'] = "ERROR"
            params['answer-poly'] = []
        else:
            params['answer'] = mul_field(mod,mod_poly,f,g)[0]
            params['answer-poly'] = mul_field(mod,mod_poly,f,g)[1]


    if operation == 'mul-poly':
        mod = params['mod']
        f = params['f']
        g = params['g']
        if (isPrime(mod)==False):
            params['answer'] = "ERROR"
            params['answer-poly'] = []
        else:
            params['answer'] = mul_poly(mod,f,g)[0]
            params['answer-poly'] = mul_poly(mod,f,g)[1]

    if operation == 'mul-table':
        mod = params['mod']
        mod_poly = params['mod-poly']
        if (isPrime(mod)==False or mod_poly==[0]):
            params['answer'] = "ERROR"
            params['answer-poly'] = []
        else:
            params['answer'] = mul_table(mod,mod_poly)[0]
            params['answer-poly'] = mul_table(mod,mod_poly)[1]

    if operation == 'primitive':
        mod = params['mod']
        mod_poly = params['mod-poly']
        a = params['a']
        params['answer'] = primitive(mod,mod_poly,a)

    if operation == 'sub-poly':
        mod = params['mod']
        f = params['f']
        g = params['g']
        params['answer'] = sub_poly(mod,f,g)[0]
        params['answer-poly'] = sub_poly(mod,f,g)[1]

    if operation == 'sub-field':
        mod = params['mod']
        mod_poly = params['mod-poly']
        f = params['a']
        g = params['b']
        if (isPrime(mod)==False or mod_poly==[0]):
            params['answer'] = "ERROR"
            params['answer-poly'] = []
        else:   
            params['answer'] = subtract_field(mod,mod_poly,f,g)[0]
            params['answer-poly'] = subtract_field(mod,mod_poly,f,g)[1] 

    # Save answer
    my_answers['exercises'].append({operation : params})

# Save exercises with answers to file
my_file = open(base_location + "output.ops", "wb+") # write to binary file
my_file.write(json.dumps(my_answers).encode()) # add encoded exercise list
my_file.close()

###### Functions #########
#print(display_poly(3,[1,0,1]))

