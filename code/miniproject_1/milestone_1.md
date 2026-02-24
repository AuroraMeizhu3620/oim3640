# storing student names
student names, with fields first name, middle name, last name, and each with a unique id

# assigning student names to seats
- seats will have auto-generated numbers as their primary key
- the student will be assigned to a seat through being assigned to the auto-generated number

# attendance tracking
1. ask if the user is taking attendance or tracking participation, if tracking attendance, then continue on to the next steps
2. each time the data is inputted, the field will be the day when the inputs are put in, while all the inputs will be under the same field
3. ask if the user is inputting students that are here or students that are not here
4. if the user says based on students that are here, then student names inputted by the user will receive a 1, and once the user confirms they have put in all names for this session, all other names will receive a 0
5. if the user says based on students that are not here, then student names inputted will receive a 0, and once the user confirms they have put in all names for this session, all other names will receive a 1

# participation tracking
1. ask if the user is taking attendance or tracking participation, if tracking participation, then continue on to the next steps
2. each time the data is inputted, the field will be the day when the inputs are put in, while all the inputs will be under the same field
3. for every time a student name is inputted for participation, the student will receive +1. If their name is inputted twice for participation, they will have a total of 2 for participation in today's field

# excel export
1. the fields will be student first name, student middle name, student last name, and a list of dates where the teacher did input an entry
2. the excel will have a calculated field called participation score
3. when the user commands to export the excel file, ask the user whether they want to have a calculated overall participation grade. If yes, continue to step 4. If no, export the excel file.
4. ask the user for the weight, out of 100%, they want to assign to attendance, and return both the attendance weight and the participation weight (100-attendance weight) and ask for their confirmation. If yes, continue to the next step. If no, repeat step 4.
5. display the calculation to the user, weight of attendance * (attended class/total class times) + weight of participation * (student participation/ participation times of the student who participated the most) 
6. generate the excel file for the user