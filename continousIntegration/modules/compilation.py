##### IMPORTS #####

import os
from datetime import datetime

##### PARAMETERS #####

#PYTHON_VER = '3.9.8'
PYTHON_VER = '3'

##### PROGRAM #####

# To be called from main.py.
# Compiles files within the cloned repository which is specified using the path in the PATH argument.

def compile(PATH):
    
    ''' Checks all the files that end .py and test if they can be compiled.
        
        Parameters
        ----------
        PATH: The path to the project.
        
        Returns
        -------
        STATUS:
            ERROR: At least one test failed.
            SUCCESS: All tests passed.

        See Also
        -------
        tests.test : Functions that tests this compile function
    '''
    
    # Create a list to store all file paths.
    pythonFiles = []
    
    # Fetch all python files.
    for root, dirs, files in os.walk(PATH): # Traverse directory storing relevant information, from PATH path.

        for file in files: # Go through all files in current directory.
            
            if file.endswith('.py'): # If the file is of type .py.
                pythonFiles.append(os.path.join(root, file)) # Add it to the list as a complete file path.

    for file in pythonFiles:
        out = os.system('python' + PYTHON_VER + ' ' + '-m py_compile' + ' ' + file)

        # An error code of 0 corresponds to success.
        if out > 0:
            return ('ERROR in ' + file, out) # Return message stating an error occurred during compilation.

    # Return a message stating success during compilation.
    return ('SUCCESS', 0)

def logger(PATH_REPO, name, message, sender, sha):
    ''' Logs the activity when a webhook is activated.

               Parameters
               ----------
               PATH: The path to the project.
               name: name of the repo
               message: Status of the build
               sender: The person who created the webhook

               Returns
               -------
               none

               See Also
               -------
               main : Functions that calls this logger function
       '''
    #Checks if the file exist
    file_exists = os.path.exists('../../../logging.txt') #will hold a True or False value

    #Creates the file if it does not exist
    if(file_exists == False):
        f = open("../../../logging.txt", "x")

    # Append-adds at last of the file
    time = datetime.now()
    path = PATH_REPO + '/' + name

    file1 = open("../../../logging.txt", "a")  #append mode
    file1.write("Push event from: " + sender + "\n" + "Path: " + path + "\n" + "Compiled at:" + str(time) + "\n" + "Status: " + message + "\n" + "Sha: " + sha + "\n\n")
    file1.close()
