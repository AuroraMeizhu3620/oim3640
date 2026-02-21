# My Project Proposal

# What I'm building:
### Classroom SuperAssitant 1.0 

I am building a classroom management web application that allows an instructor to design a seating layout, assign students to seats, track attendance, participation counts, and attention status across multiple class sessions, persist all data, and export structured historical records to an Excel file for grading.

# Why I chose this:
While serving as a TA for Professor Gilleran, I observed that manually maintaining seating charts and tracking participation in Excel is time-consuming and inefficient.

Currently:
- Seating charts are recreated manually each semester.
- Attendance and participation are recorded in Excel rows.
- The instructor must locate each student by name and manually tally responses.

This application aims to provide:
- A visual seating interface
- One-click attendance and participation tracking
- Automated aggregation for grading


# Core features:
- Seating system that allows users to crete classroom template, assign students to seats, and store the mapping
- Tracking system for attendance, participation count, and attention flag
- Data keeping for all sessions, appending new session, and student data protection 
- Excel export that include fields like total attendance, total participation, attention, and possibly participation score formula
- Calculation of participation scores for each entry based on user-inputted weighting

# What I don't know yet
- How to structure and store relational data
- How to link backend seat coordinates to a visual seating layout
- How to append session records without influencing previous entries
- How to export the stored data as an organized excel file

# Future developments:
- Supporting multiple users
- Automated email generation notifying students about their participation scores
- Summary report generation on habitual slackers or good students