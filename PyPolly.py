#%%
import os
#%%
import csv
# %%
path_ElectionResults = 'Resources\\election_results.csv'
# %%
path_NewFile = os.path.join('Analysis','election_results.txt')
saved_file = open(path_NewFile, "w") ##when i dont do this, 
# the file does not pop up in my Analysis folder, but this 
# piece of code is not included in the module example.
# %%
with open(path_ElectionResults) as data_analysis:
    file_reader = csv.reader(data_analysis)

    headers = next(file_reader)
    print(headers) #i thought next() skipped the first row and printed the
    # next row so how does it print only the Header

    #for row in data_analysis:
     #   print(row)
# %%

# %%
