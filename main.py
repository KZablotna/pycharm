from data import data
import os
import datetime
print(os.environ['USERPROFILE'])
user = (os.getenv('username'))
now = datetime.datetime.now()
print(now.strftime("%x %X"), "\n")


def main():
  
  my = data('Carla James', '85 Broad Street', '22', '555-555-1281')
  print("My information:")
  print("Name:", my.get_name())
  print("Address:", my.get_address())
  print("Age:", my.get_age())
  print("Phone Number:", my.get_phone())
  print()
  friend = data('Juan Carlos','86 Broad Street', '24', '555-555-1234')
  print("Friend's information:")
  print("Name:", friend.get_name())
  print("Address:", friend.get_address())
  print("Age:", friend.get_age())
  print("Phone Number:", friend.get_phone())
  print()
  coach = data('Alex Cruz', '87 Broad Street', '32', '555-555-4444')
  print("Coach's information:")
  print("Name:", coach.get_name())
  print("Address:", coach.get_address())
  print("Age:", coach.get_age())
  print("Phone Number:", coach.get_phone())
  

main()

