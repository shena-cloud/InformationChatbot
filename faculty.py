import mysql.connector
db = mysql.connector.connect(host = "localhost",
        user = "root",
        passwd = "rasachatbot123",
        database = "faculty")




#mycursor.execute("CREATE DATABASE faculty")

#mycursor.execute("CREATE TABLE faculties (name VARCHAR(50), qualification VARCHAR(50), joining_year DATE, specialisation VARCHAR(50), email_id VARCHAR(50), id INT PRIMARY KEY AUTO_INCREMENT) ")

#sql = "INSERT INTO faculties (name, qualification,joining_year, specialisation, email_id) VALUES (%s, %s, %s, %s, %s)"
#val = [
  #("Amal S Kannan", "M Tech", "2019-08-25", "Advanced Communication and Information System", "amal@gcek.ac.in"),
  #("Hareesh K", "M Tech","2019-07-22", "Communication and Signal Processing", "hareesh@gcek.ac.in"),
  #("Ajith K K", "PhD", "2019-07-29", "RF and Microwave", "ajithkk@gcek.ac.in"),
  #("Binoy K P", "M Tech", "2019-07-22", "Communication Engineering and Signal Processing", "binoykp@gcek.ac.in"),
  #("Sajeev K Jose", "M Tech", "2019-07-22", "Communication Engineering and Signal Processing", "sajeev@gcek.ac.in"),
  #("Sreejesh K V", "M Tech", "2019-08-01", "Signal Processing and Embedded Systems", "sreejeshkv@gcek.ac.in"),
  #("Jobin Jose", "M Tech", "2015-06-01", "Biomedical Engineering", "jobin2jose@gmail.com"),
  #("Anoob B", "M Tech", "2017-10-19", "Communication Systems", "anoobbabu@gcek.ac.in"),
  #("Rejeesh R", "M Tech","2018-04-17", "Remote Sensing and Wireless Sensing Network", "rejeesh@gcek.ac.in"),
  #("Swathi K", "M Tech", "2019-08-05", "Signal Processing and Communication Engineering", "swathikpoduval@gmail.com"),
  #("Gopika G", "M Tech", "2019-08-05", "VLSI Design and Embedded Systems", "gopikagopinathe@gmail.com"),
  #("Liji C A", "M Tech", "2019-08-05", "Advanced ECE", "lijialfred@gmail.com"),
  #("Anjana P M", "M Tech", "2019-08-05", "VLSI and Embedded System", "pmanjana.nambiar@gmail.com")
  #]

#mycursor.executemany(sql,val)
#db.commit()
#print(mycursor.rowcount,"was inserted.")
#q = "SELECT email_id FROM faculties WHERE name = 'Jobin Jose'"
#mycursor.execute(q)
#results = mycursor.fetchone()[0]
#print(results)

mycursor = db.cursor()
#q = "CREATE TABLE subject_b (subject_name VARCHAR(50), faculty_name VARCHAR(50), class VARCHAR(50), id INT PRIMARY KEY AUTO_INCREMENT)"
#q = "ALTER TABLE subjects ADD COLUMN id INT PRIMARY KEY AUTO_INCREMENT"
q = "INSERT INTO subject_a (subject_name, faculty_name, class) VALUES (%s, %s, %s)"
val = [
  #("Basics of Electrical and Electronics Engineering", "Dinesh BAbu M", "S2 EC B"),
  #("Electronics Workshop", "Laseena C A", "S2 EC B"),
  #("Programming in C", "Jobin Jose", "S2 EC B"),
  #("Professional Communication", "Gopika Gopinath", "S2 EC B"),
  #("Signals and Systems", "Sajeev K Jose", "S4 EC B"),
  #("Analog Integrated Circuits", "Ajith K K", "S4 EC B"),
  #("Computer Organisation", "Amal S Kannan", "S4 EC B"),
  #("Analog Communication Engineering", "Ramanand A C", "S4 EC B"),
  #("Analog Integrated Circuits Lab", "Ajith K K", "S4 EC B"),
  #("Logic Circuit Design Lab", "Amal S Kannan", "S4 EC B"),
  #("Digital Communication", "Hareesh K", "S6 EC B"),
  #("VLSI", "Binoy K P", "S6 EC B"),
  #("Embedded Systems", "Ramanand A C", "S6 EC B"),
  #("Object Oriented Programming", "Sreejesh K V", "S6 EC B"),
  #("Digital Image Processing", "Swathi K", "S6 EC B"),
  #("Communication Engineering Lab", "Rejeesh R", "S6 EC B"),
  #("Microcontroller Lab", "Ramanand A C", "S6 EC B"),
  #("Comprehensive Exam", "V Vinod Kumar", "S6 EC B"),
  #("Nano Electronics", "Rejeesh R", "S8 EC B"),
  #("Advanced Communication Systems", "Anoob B", "S8 EC B"),
  #("Low Power VLSI", "Anjana P M", "S8 EC B"),
  #("Non Departmental Elective", "Jayakrishna Raj", "S8 EC B"),
  #("Project", "Binoy K P", "S8 EC B"),
  #("Digital Image Processing", "K A Navas", "S2 MTech"),
  ("Antenna and Wave Propogation", "Nishil Kumar P P", "S6 EC A")
]
mycursor.executemany(q, val)
db.commit()
