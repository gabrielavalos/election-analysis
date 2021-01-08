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
# innitiate accumulator for Total Votes
total_votes = 0

# create an empty list for Candidate Options
candidate_options =[]

#create a dictionary to hold candidate(key): votes(value)
candidate_votes = {}

#empty string for winning candidate
winning_candidate = ''

#setting winning count and percentage to 0
winning_count = 0
winning_percentage = 0

# open election_results.csv file and read it
with open(path_ElectionResults) as data_analysis:
    file_reader = csv.reader(data_analysis)

    # read header row
    headers = next(file_reader)
    #print(headers) #i thought next() skipped the first row and printed the
    # next row so how does it print only the Header

    # iterate through each row
    for row in file_reader:
        # add to get the total vote count
        total_votes += 1

        # get the candidate name from each row
        candidate_name = row[2]

        # if statement to only add candidates name to candidates option list
        # one time
        if candidate_name not in candidate_options:
            # append the candidate name to the candidate options list 
            candidate_options.append(candidate_name)

            # Initiating each candidates count as 0
            candidate_votes[candidate_name] = 0
        
        #Add a vote to each candidates count
        candidate_votes[candidate_name] += 1 #It iterates through every row
        # and everytime a canditates name is shown, it adds 1, but why
        # can we do this without an "if statement"?
    
    for each in candidate_votes:
        votes = candidate_votes[each]
        candidate_percentage = float(votes) / float(total_votes) * 100
        print(f'{each}: {candidate_percentage:.1f}% ({votes:,})\n')
        #print(f'{each} received {candidate_percentage:.1f}% of all votes')

        #print(f'{each} received {float(votes) / float(total_votes) * 100:.2f}% of all votes')

        #Determine the winning vote count and candidate
        if (votes > winning_count) and (candidate_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = candidate_percentage
            winning_candidate = each
        
    winning_candidate_summary = (
        f'-------------------------\n'
        f'Winner: {winning_candidate}\n'
        f'Winning Vote Count: {winning_count:,}\n'
        f'Winning Percentage: {winning_percentage:.1f}%\n'
        f'-------------------------\n')
    print( winning_candidate_summary)


        
  
#print(total_votes)
#print(candidate_options)
#print(candidate_votes)  
# %%

# %%
