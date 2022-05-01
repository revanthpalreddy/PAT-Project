## PAT Project - NumPy

### Generate and View Test Coverage Report
* Run script to generate Test Coverage on Command Line : `python gen-coverage.py`
* Two folders 'html-coverage' and 'json-coverage' will be generated
* Open 'index.html' file within 'html-coverage' folder to view Coverage report for each file
* Open 'coverage.json' file to view coverage data in JSON format

### Test Files Analysis 
* Run the AssertCount.py file,
`python AssertCount.py` to get the assert statement count in test files.
* All the data generated will be stored in the **Data** folder as csv files, 
which will then be used to generate plots in **gen-figures.py**.

### Production Files Analysis 
* Run the AssertLocAndCountInProduction.py file,
`python AssertLocAndCountInProduction.py` to get the assert statement count and location.
* Run the DebugLocAndCountInProduction.py file,
`python DebugLocAndCountInProduction.py` to get the debug statement count and location.
* All the data generated will be stored in the **Data** folder as csv files, 
which will then be used to generate plots in **gen-figures.py**.

### PyDriller
* Run the PyDriller.py file,
`python pydriller.py`
* All the data generated will be stored in the **Data** folder as csv files, 
which will then be used to generate plots in **gen-figures.py**.

### Generate All Figures
* Run script to generate Test Coverage on Command Line : `python gen-figures.py`
* The plots and figures are generated in figures folder.

### Data Folder
* The data folder contains all the csv and json files of the tasks.
