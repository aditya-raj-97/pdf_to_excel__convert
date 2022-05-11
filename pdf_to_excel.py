#prerequisites:
#install tabula --- pip install tabula-py
#install java
#Add java installation folder (C:\Program Files (x86)\Java\jre1.8.0_251\bin) to the environment path variableā


# Import Module 
import tabula
  
# Read PDF File
# this contain a list
df = tabula.read_pdf("PDF File Path", pages = 1)[0]
  
# Convert into Excel File
df.to_excel('Excel File Path')
