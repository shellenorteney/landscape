import math


#Calculate the number of bags required for a given area
def calculate_bags (length,width):
   bags = math.ceil((length * width))/2000
   return round(math.ceil((length * width))/2000)
   
#Calculate the cost of fertilizer
def calculate_cost_bag(bags_needed):
    return bags_needed * 27

#Calculate the minimum number of hours required
def calculate_hours_work(area):
    return math.ceil(area/2500)

#Calculate the cost of work
def calculate_cost(work_time):
    return work_time * 20

#Calculate the total cost
def calculate_total_cost(fertilize_cost, work_cost):
    return fertilize_cost + work_cost

#Calculate the nitrogen and potassium applied
def calculate_nitrogen_potassium(bags_needed):
    nitrogen = bags_needed * 1
    potassium = bags_needed * 0.125
    return round(nitrogen,3), round(potassium,3)

#Main program
def main():
    sections = ['front', 'rear', 'left', 'right']
    totalbags_needed = 0
    totalarea = 0
    work_cost = 0
    hours = 0

    print("Welcome to to the Fertilizer Calculator!!!")
    print("")
    print("I will ask you for the length and width of four rectangular sections. Please enter your measurements in feet (numbers only, please). If you do not have a particular section, simply enter zero (0) for those dimensions!")
    print("")
    print("Press ENTER to start!")

    for section in sections:
        length = int(input(f"What is the length(in feet) of the {section} section? "))
        width = int(input(f"What is the width(in feet) of the {section} section? "))
    
        #Calculate area
        area = length * width
        bags_needed = calculate_bags(length, width)
        totalbags_needed += (bags_needed)
        totalarea += area
        
    print(f"\nResults:")
    print(f"Your application has a total area of: {totalarea} sq. feet.")
    
    fertilizer_cost = calculate_cost_bag(totalbags_needed)
    hours = calculate_hours_work(totalarea)
    work_cost = calculate_cost (hours)
    totalcost = calculate_total_cost(fertilizer_cost,work_cost)
    nitrogen, potassium = calculate_nitrogen_potassium(totalbags_needed)

    #Results2
    print(f"That will require {totalbags_needed} bags of fertilizer.")
    print(f"The cost of fertilizer will be ${fertilizer_cost:.2f}")
    print(f"Our technicians will require {hours} hours to finish the job and the labor cost will be ${work_cost:.2f}.")
    print(f"The total cost to the company will be ${totalcost:.2f}")
    print(f"The application will result in {nitrogen:.3f} pounds of nitrogen and {potassium:.3f} pounds of potassium being added to the soil.")

if __name__ == "__main__":
    main()