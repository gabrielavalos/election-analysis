#1) Total number of votes cast
    #Loop through all rows-1 to get the total number of votes cast
    #RowCount = Cells(Rows.Count, "A").End(xlUp).Row
#2) A complete list of candidates who received votes
    #Create an empty array to add each candidate to it - candidates()
    #Loop through the data to find each candidates name and append 
    #each name to candidates()
#3) Total number of votes each canditate received
    #create an empty dict totals_per_candidate{} 
    #Create a counter for each candidate
    #loop through data to get counts for each candidate
        #Create an if statement for exact match to increase 
        # the corresponding candidates couunter
        #add total values to totals_per_candidate = {candidate;votes}
#4) Percentage of votes each candidate won
    #loop through totals_per_candidate and divide each votes 
    #value by total numbers of votes cast
    #store as a dictionaty
#5) The winner of the election based on the popular vote
    #Loop through dictionary to get the highest percentage and
    #return the candidates 

