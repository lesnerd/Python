import os
import re
import tempfile
import shutil

def GetAllTxtAndLogFileNames(fromDir):
    filesList = []
    for file in os.listdir(fromDir):
        if file.endswith(".txt") or file.endswith(".log"):
            filesList.append(fromDir + '/' + file)
    return filesList


def RemoveAllDateAndTime(lst):   
    regularExpression = r'^([0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1]) (2[0-3]|[01][0-9]):[0-5][0-9]:[0-5][0-9],[0-9]{3}[ ]{1})'
    regex = re.compile(regularExpression)
    for fname in lst:
        with open(fname, mode='r+', encoding="utf8") as f:
            #Create temporary file read/write
            with tempfile.NamedTemporaryFile(mode='r+', encoding="utf8") as temp:
                #Read file -> chage lines -> write to tempFile
                line = f.readline()
                while(line):
                    line = regex.sub('', line)
                    temp.write(line)
                    line = f.readline()

                #Write back form tempFile to original
                temp.seek(0)

                #Delete old file content
                f.truncate(0)

                for l in temp:
                    f.write(l)

                #Close file  
            temp.close()



def main():
    text = input("Path: ")
    lst = GetAllTxtAndLogFileNames(text)
    RemoveAllDateAndTime(lst)
    
if __name__ == "__main__": #ifdef
    main()