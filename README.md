# election-analysis
python

## Project Overview
A Colorado Board of Elections has given you the following tasks to complere the election audit of a recent local congressional election.

1. Total number of votes cast
2. A complete list of candidates who received votes
3. Total number of votes each candidate received
4. Percentage of votes each candidate won
5. The winner of the election based on popular vote

## Resources
- Data Source: election_results.csv
- Software: Python 3.9.1. Visisual Studio Code: 1.52.1

## Audit Results
The analysis of the elections shows that:
- There were 369,711 votes cast in the election
- The counties in the Election were:
  1. Jefferson
  2. Denver
  3. Aranpahoe
- The results per county were:
  - Jefferson had 10.5% of all votes and 38,855 number of votes.
  - Denver had 82.8% of all votes and 306,055 number of votes.
  - Aranpahoe had 6.7% of all votes and 24,801 number of votes.
- The county with the largest turnout was:
  - Denver
- The candidates were:
  1. Charles Casper Stockham
  2. Diana DeGette
  3. Raymon Anthony Doane
- The candidate results were:
  - Charles Casper Stockham received 23.0% of votes and 85,213 number of votes.
  - Diana DeGette received 73.8% of votes and 272,892 number of votes.
  - Raymon Anthony Doane received 3.1% of votes 11,606 number of votes.
- The winner of the election was:
  - Diana DeGette who received 73.8% of votes and 272,892 number of votes.
 
## Audit Summary
This script can be used for any election, based on the data received in the csv. 

### Modification
If more information is provided for each vote, i.e. each vote has more columns, all the new information can be extracted into list containing the unique information. For example, if you want a list of all the races which the voters indentified whith, you can make changes in lines 18 and 50-60.

In line 18, change candidates_names to an appropriate name, i.e. races_identification
PICTURE
In lines 50, for candidate_name = row[2]:
Replace candidate_name to an appropriate name for each item on the list, such as race_id. Replace '2' with the numbber of the column containing the data you are creating a list for. In  python, the first data in a list is in the position [0], so if the new data is in the 4th column, replace [2] with [3].
PICTURE
In line 57:
Replace candidate_name to race_id and candidate_options to races_identification
In line 60:
Replace candidate_options to race_indentification and candidates_name to race_id. Keep all punctuation.
Making these changes will return a list of all the races that casted a vote.

### Modification 1
