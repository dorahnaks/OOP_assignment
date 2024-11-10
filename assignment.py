# add a constructor for the cohort class
# create a function/ add a method to the class that prints the cohort name and the total number of students
# create a new instance/ object of the cohort class 





class Cohort:  # defining the class
     # __init__() function is the constuctor always executed when the class is being initiated. self refers to an instance being created
    def __init__(self, name, student_total_num):
        self.name = name 
        self.student_total_num = student_total_num
    def print_cohort_info(self):      # Method that prints the cohort name and total number of students
        print(f"Cohort Name: {self.name}")
        print(f"Total Number of Students: {self.student_total_num}")

cohort4 = Cohort("Python Class", 54)  # an instance/ object of the Cohort class
cohort4.print_cohort_info()           # Calling the method to print the cohort details