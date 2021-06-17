import csv
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv("DB_URL"))
db = scoped_session(sessionmaker(bind=engine))

path ="/"

def main():
	file = open("users.csv")
	csv_reader = csv.reader(file, delimiter=",")
	#with open("flights.csv") as file:
		#csv_reader = csv.reader(file)
	#print(csv_reader)
	for origin, destination, duration in csv_reader:
		#print(origin, destination, duration)
		QUERY = "INSERT INTO flights (origin, destination, duration) VALUES (:origin, :destination, :duration);"
		db.execute(QUERY, {"origin":origin, "destination":destination, "duration":duration})
		print(f"Added flight from {origin} to {destination}, lasting {duration} minute(s)")
		db.commit()

if __name__ == '__main__':
	main()