# Simple application that will create a meeting notes template and open the file for you
# Author: Manu Ignatius

import subprocess
import datetime

# filename creation
today = datetime.datetime.today().strftime('%Y-%m-%d')
meeting_name = input("Meeting description (for filename): ")

filename = today + "_" + meeting_name + ".md"
print (filename)

f = open(filename, "w+")

# file header creation
### Date & Time: 19 October 2018, Friday, 15:00
### Attendees:
# - Name, Org
# - Alice, IBM

# ### Venue
# - Subnero

# ### Agenda
# - Agenda 1
# - Agenda 2

# ---

f.write("### Date & Time: " + datetime.datetime.now().strftime("%d %B %Y, %A, %I:%M %p") + "\n\n")

f.write("### Attendees:\n")

inp1 = input("Number of attendees: ")
try:
   count = int(inp1)
except ValueError:
   print("That's not an int! Assigning number of attendees to 1")
   count = 1

for i in range(count):
    name = input("Attendee " + str(i+1) + " name & organization (E.g. Alice, Subnero): ")
    f.write("- " + name + "\n")

f.write("\n### Venue:\n")
venue = input("Venue: ")
f.write("- " + venue + "\n\n")


f.write("\n### Agenda:\n")
inp2 = input("Number of agenda items: ")
try:
   count = int(inp2)
except ValueError:
   print("That's not an int! Assigning number of agenda items to 1")
   count = 1

for i in range(count):
    agenda = input("Agenda item " + str(i+1) + ": ")
    f.write("- " + agenda + "\n")

f.write("---\n\n")

f.write("### Notes\n")
f.write("- [ ] ")

f.close()

subprocess.call( ["/usr/bin/open", "-W", "-n", "-a", "/Applications/TextEdit.app", filename])