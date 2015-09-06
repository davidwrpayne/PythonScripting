import csv
import sys
from operator import methodcaller


def main():
    if len(sys.argv) != 6:
        printUsage()
    file1RowStart = int(sys.argv[1])
    file2RowStart = int(sys.argv[2])
    f1ColumnTof2Column = sys.argv[3]
    file1 = sys.argv[4]
    file2 = sys.argv[5]


    # convert columns to array indices
    f1ColumnTof2Column = map(methodcaller('rsplit','-'),f1ColumnTof2Column[1:len(f1ColumnTof2Column)-1].rsplit(','))
    columnPairs = []

    for i in f1ColumnTof2Column:
        f = lambda x:x-1
        columnPairs.append( map(f,map(int,i)) )
    # print columnPairs



    file1Rows = getRows(file1,file1RowStart)
    # print f1Rows
    file2Rows = getRows(file2,file2RowStart)
    # print f2Rows

    row1 = 0
    for file1Row in file1Rows:
        row2 = 0
        row1 += 1
        for file2Row in file2Rows:
            row2 += 1
            for i,j in columnPairs:
                if( file1Row[i] == file2Row[j]):
                    print file1Row[i] + " : " + file2Row[j]
                    print "match in \ncolumn:" + str(i + 1) + " in row: " + str(row1) + " from file1 \nto\ncolumn: " +str(j +1 ) + " in row: " + str(row2) + " from file2"
                    print


def getRows(fileName,rowStart):
    f1Rows = []
    with open(fileName,'rb') as f1:
        reader = csv.reader(f1, delimiter=',')
        rowNumber = 1
        for row in reader:
            if( rowNumber < rowStart):
                rowNumber += 1
                continue
            f1Rows.append(row)

    return f1Rows



# def compareColumns(row1,row2,column1,column2):
#     if( row1.equ)




def printUsage():
    thisFile = sys.argv[0].rsplit("/",1)[1]
    usage = "How to use AddressMatcher:\n" +"python " + thisFile + " X Y (a-b,c-d,e-f) file1 file2\n"

    print usage
    print "\tX      = the row to start on in file 1"
    print "\tY      = the row to start on in file 2"
    print "\ta-b    = is file1 column a  matched to file2 column b,  i.e. 1-2 matches file1's column 1 to file2's column 2"
    print "\tc-d    = the above is the same for this "
    print "\te-f    = is the same as the above two lines"
    print "\tfile1  = file name of first  csv to check. Should be in same folder as " + thisFile
    print "\tfile2  = file name of second csv to check. Should be in same folder as " + thisFile





main()

