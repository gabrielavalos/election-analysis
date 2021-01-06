#print("Hello world")

#counties = ["Arapahoe","Denver","Jefferson"]
#if counties[1] == 'Denver':
 #   print(counties[1])

#print(counties)

#temperature = int(input("What is the temperature outside? "))

#if temperature > 80:
 #   print("Turn on the AC.")
#else:
 #   print("Open the windows.")

#counties = ["Arapahoe","Denver","Jefferson"]
#if "El Paso" in counties:
 #   print("El Paso is in the list of counties.")
#else:
 #   print("El Paso is not the list of counties.")

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for counties in counties_dict.keys():
    print(counties)