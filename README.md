# PythonExamples
All the three Python MS examples are given in this directory as separate folders. 
To run the examples locally execute the following command for each example:
python <filename> For Example : python StoreApp.py
  
To deploy the examples on PCF
Install the CLI installer of PCF

1. Go to the base directory of the project.
2. cf push ## It will pick the  dependencies from the requirements.txt  file and execute commands from the Procfile kept inside the base directory of each project.

If you are missing any dependency then execute: pip install <dependency_name>
Check the already installed dependencies by executing: pip freeze
