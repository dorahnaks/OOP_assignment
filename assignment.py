# create a cohort class with:
# name, description, start date , end date
# add a constructor for the cohort class
# create a function/ add a method to the class that prints the cohort name and the total number of students
# create a new instance/ object of the cohort class 





class Cohort:  # defining the class
     # __init__() function is the constuctor always executed when the class is being initiated. self refers to an instance being created
    def __init__(self, name, description, start_date, end_date, student_total_num):
        self.name = name
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.student_total_num= student_total_num
    def print_cohort_info(self):      # Method printing the cohort name and total number of students
        print(f"Cohort Name: {self.name}")
        print(f"Total Number of Students: {self.student_total_num}")

cohort4 = Cohort(name="Python Programming", 
                description="A course on Python programming.", 
                start_date="28-08-2024", end_date="04-12-2024", 
                student_total_num=25) # an instance/ object of the Cohort class
cohort4.print_cohort_info()           # Calling the method to print the cohort details