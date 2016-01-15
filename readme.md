# Data to xml
Python program to convert a structured data into a valid xml file.
Currently the process of giving data as input is very tedious as there is no interface to do so, the data is given input programmatically inside the 'sampledata.py' script

**xmlclass**
Contains a python class xmldata which can be used to represent any xml element with or without children, attributes & data. The entire data that is processed upon is stored using nested 'xmldata' classes.

**xmlconv.py**
Takes a xmlclass object as input, changes the data contained into valid xml format and writes it in a new file. If file is already present, then overwrites it.

**sampledata.py**
Imports both the above functions. The hardcoded data on which the other functions are being tested upon is given as commented code. Here the hardcoded input is given programmatically, the way the data is stored in the xmlclass is printed, and a xml file is created which contains the valid xml format of the data.
