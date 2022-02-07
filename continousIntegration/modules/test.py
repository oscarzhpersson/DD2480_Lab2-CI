##### IMPORTS #####

import os

##### PARAMETERS #####

#PYTHON_VER = '3.9.8'
PYTHON_VER = '3'

##### PROGRAM #####

# To be called from main.py.
# Compiles files within the cloned repository which is specified using the path in the PATH argument.

def test(PATH):

    # Create a list to store all file paths.
    pythonFiles = []

    # Fetch all python files.
    for root, _, files in os.walk(f'{PATH}/tests'): # Traverse directory storing relevant information, from PATH path.
        for file in files: # Go through all files in current directory.
            if file.endswith('.py'): # If the file is of type .py.
                pythonFiles.append(os.path.join(root, file)) # Add it to the list as a complete file path.

    print("PERFORMS TESTS")

    for file in pythonFiles:
        out = os.system(f'python{PYTHON_VER} {file}')

        # An error code of 0 corresponds to success.
        if out > 0:
            return ('ERROR', out) # Return message stating an error occurred during compilation.

    # Return a message stating success during compilation.
    return ('SUCCESS', out)

print(test('../.'))