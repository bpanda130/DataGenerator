import sys
import platform
import os
import time

from main import buildJSON, append_to_file, buildXML

if os.environ.get('DISPLAY','') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')

input_file = sys.argv[1]
num_records = sys.argv[2]
output_fileformat = sys.argv[3]

fileName = 'BulkTestData'
print("Platform Name    : "+ platform.system())
print("Given input schema file      : " + input_file)
print("Required no. of Records      : " + num_records)
print("Required Output file format  :" + output_fileformat)

if(output_fileformat == 'csv'):
    append_to_file(num_records, fileName, input_file)
    print("Required output file "+ fileName+".csv generated.")
elif(output_fileformat == 'json'):
    buildJSON(num_records, fileName, input_file)
    print("Required output file " + fileName + ".json generated.")
elif(output_fileformat == 'xml'):
    buildXML(num_records, fileName, input_file)
    print("Required output file " + fileName + ".xml generated.")

