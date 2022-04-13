# Datebase Code for Attendance System
# Written by Isaac Woollen

import mysql.connector
from datetime import datetime

# Links mysql database to the program
mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="",
	database="attendance"
)

# Assigns database cursor to mycursor
mycursor = mydb.cursor()

# Dictionary for converting day numbers into initials
day_of_week = {
	1:"M",
	2:"T",
	3:"W",
	4:"R",
	5:"F",
	6:"S"
}

# Function takes in data from database and current datetime, formats the data, 
# then checks if attendance needs to be taken. Takes in student_id as parameter.

def check_attendance(student_id, time):
	# Query database for courses that the student is enrolled in and assigns to courses variable
	sql = "SELECT * FROM enrolled_in, course WHERE sid = " + str(student_id) + " and cid =  course_id;"
	mycursor.execute(sql)
	courses = mycursor.fetchall()

	# Getting the current time and day then formating it for comparison
	# current_time = datetime.now().strftime("%H:%M").split(":")
	current_time_in_minutes = int(time[0])*60 + int(time[1])
	day = day_of_week[datetime.today().isoweekday()]

	# Check every course the student is enrolled in
	for course in courses:
		# Default status is 'Ontime'
		status = 'Ontime'

		# If the current day is not a day the class is held, then the loop moves to the next course
		if day not in course[5]:
			continue

		# Format the current course time being compared
		course_time_in_minutes = int(course[3].split(":")[0])*60 + int(course[3].split(":")[1])

		# If the current time is not within 10 minutes before or after the start time,
		# then the loop moves to the next course
		if abs(current_time_in_minutes - course_time_in_minutes) > 10:
			continue

		# The the current time is after the start time, then the student is late,
		# but attendance will be taken as late
		if current_time_in_minutes > course_time_in_minutes:
			status = 'Late'

		# mark_attendance function is call because all attendance criteria is met
		mark_attendance(course[0], course[1], day, time[0] +":"+ time[1], status)

# Function marks attendance based on the student_id, course_id, the day and time it was taken,
# and whether the student is late for the class or not
def mark_attendance(student_id, course_id, day, time, status):

	# Formatting for recording attendance into the database
	time_recorded = "'" + day + " " + time + "'"
	status = "'" + status + "'"
	data = ", ".join((str(student_id), str(course_id), time_recorded, status))

	# SQL query is generated for with data and outputted to the terminal
	sql = "INSERT INTO attended (sid, cid, time_recorded, status) VALUES (" + data + ");"
	print(sql)

	# SQL query is excuted and database is updated 
	mycursor.execute(sql)
	mydb.commit()
	print("Attendance taken for " + str(student_id))

# Example with student that has an id = "807007246"
# attendance(807007246)

    