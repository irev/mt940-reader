# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility
# https://regex101.com/r/NSoYCk/1
import re

regex = r":61:(\d+)(\D{1,2})(\d+|\d+,\d{1,2})([A-Z]{4})(.{0,})"

test_str = ("240831C16939776NINT\n"
	":61:240826DR176120660NTRF//0207150143062089\n"
	":61:240826DR176120660,0NTRF//0207150143062089\n"
	":61:240826CR176120660,0NTRF//\n"
	":61:1507020702D115945,00F014NARRATIVE//0207150143062089\n\n"
	":61:170929D546232,05S101PLTOL101-56//C11126A1378\n\n"
	":61:170929D100000,NFEXAAAAUS0369PLATUS//8954321\n\n"
	":61:090124D10000000,S202DRS/06553\n"
	":61:240826CR176120660,0JJII\n"
	":61:240826CR176120660,0\n"
	":61:240826CR176120660JIOP\n"
	":61:240826CR176120660JIOP\n"
	":61:240826CR176120660\n"
	":61:240826D2900NCHG\n"
	"Credit\n"
	":61:240826C2900NCHG\n")

matches = re.search(regex, test_str)

if matches:
    print ("Match was found at {start}-{end}: {match}".format(start = matches.start(), end = matches.end(), match = matches.group()))
    
    for groupNum in range(0, len(matches.groups())):
        groupNum = groupNum + 1
        
        print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = matches.start(groupNum), end = matches.end(groupNum), group = matches.group(groupNum)))

# Note: for Python 2.7 compatibility, use ur"" to prefix the regex and u"" to prefix the test string and substitution.
