
# import OS module
import os
from re import S
import smtplib
import time
import imaplib
import email
import traceback 
import xlsxwriter
from datetime import datetime, timedelta
import datetime
import exiftool
from exiftool import ExifToolHelper
# Get the list of all files and directories
path = "/home/bvm/Desktop/imagemetadata/pic"
dir_list = os.listdir(path)
count = 1
row = 0
col = 0
workbook = xlsxwriter.Workbook('metadata.xlsx')
worksheet = workbook.add_worksheet()
for f in dir_list:
    infoDict = {} #Creating the dict to get the metadata tags
    exifToolPath = exiftool
    imgPath = f"pic/{f}"
    with ExifToolHelper() as et:
        for d in et.get_metadata(imgPath):
            FName = d.get('File:FileName')
            Model = d.get('EXIF:Model')
            ExposureTime  = d.get('EXIF:ExposureTime')
            FNumber  = d.get('EXIF:FNumber')
            ISO  = d.get('EXIF:ISO')
            # EXIF:ApertureValue = 5.60000067086021
            ExposureCompensation  = d.get('EXIF:ExposureCompensation')
            # EXIF:MaxApertureValue = 5.65685424949238
            LightSource  = d.get('EXIF:LightSource')
            Flash  = d.get('EXIF:Flash')
            FocalLength  = d.get('EXIF:FocalLength')
            LensInfo  = d.get('EXIF:LensInfo')
            Finfo = f"Model: {Model}, Exposure Time: {ExposureTime}, FNumber: {FNumber}, ISO: {ISO}, Exposure Compensation:  {ExposureCompensation}, Light Source: {LightSource}, Flash: {Flash}, Focal Length: {FocalLength}, Lens Info: {LensInfo}"
            print(Finfo)
            worksheet.write(row, col, row+1)
            worksheet.write(row, col + 1, FName)
            worksheet.write(row, col + 2, Finfo)
            row +=1
workbook.close()



