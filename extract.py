from zipfile import ZipFile

filePath = "Congrats! you have extracted file.zip"

with ZipFile(filePath, "r") as zip:
    zip.printdir()
    zip.extractall()