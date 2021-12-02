# install and Import module & library
import PIL.Image
import datefinder
import numpy as np
import pytesseract
import re

# image OCR
# use Tesseract Open Source OCR Engine
image = PIL.Image.open("rihal.png")
text = pytesseract.image_to_string(image)
# print(text)

#  i. Find all dates. Standardize the output to this format YYYY-MM-DD
Dates = datefinder.find_dates(text)
for Date in Dates:
    print("The Dates :", Date)

# ii. Room Names
Rooms = re.findall(r'Room: ([\w.+-]+)', text)
print("The room names: ", Rooms)

# iii. Room Rates
Rooms1 = re.findall(r'Room: ([\w.+-]+)', text)
Rate = re.findall(r'Rate: [£$€]{1}[,\d]+.?\d*', text)
Room_array = np.array(Rooms1)
Rate_array = np.array(Rate)
print("The Room Rates :", Room_array[0], Rate_array[0], "|", Room_array[1], Rate_array[1], "|", Room_array[2],
      Rate_array[2], "|", Room_array[3], Rate_array[3])

# iv. Individual Names. Standardize the output to this format "Firstname Lastname"
Fname = re.findall(r',\s+[A-Z$]+[a-zA-Z]{3,8}', text)
Sname = re.findall(r'A[a-zA-Z]\s+[a-zA-Z]+,', text)
F_array = np.array(Fname)
S_array = np.array(Sname)
print("The Individual names:", F_array[0], S_array[0], "|", F_array[1], S_array[1], "|", F_array[2], S_array[2], "|",
      F_array[3])

# v. All emails
emails = re.findall(r'[\w.+-]+@[" "\w-]+\.[\w.-]+', text)
print("The Emails : ", emails)
