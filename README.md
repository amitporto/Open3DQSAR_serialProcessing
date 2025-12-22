# Open3DQSAR_serialProcessing
This program allows automated generation of multiple Open3DQSAR based model development with a single run.

Steps for generating multiple Open3DQSAR models in single run.
Step 1. Preparation of input scripts Open3DQSAR as per the instruction provided in input file named sample_input_MM.inp provided with Open3DQSAR.

Step 2: Create a folder (say C:\myfile) where the input file and placed with open3DQSAR_filegenerator.py. 

Step 3: Use open3DQSAR_filegenerator.py to generate as many as input files where only test set compounds will be altered. This script takes the input file name, number of dataset (training set + test set) compounds, number of test set compounds and number of new input files to be generated. Therefore, run the file as:
python open3DQSAR_filegenerator.py --input sample_coumarin.txt --trn 45 --tsn 9 --num 10

Step 4: After successful generation of these new files, run process_open3DQSAR.py from ‘bin’ folder under open3dtools, where open3DQSAR.exe file is located. It should be run as:
python process_open3DQSAR.py C:\myfile. Warning: The input files are generated as .txt files. Do not keep any other .txt file in this folder. 

Step 5: Check, summary files (Summary_FFDSEL_results.txt and Summary_UVEPLS_results.txt) to find the most statistically robust model. Individually, log output files may further be checked. 

