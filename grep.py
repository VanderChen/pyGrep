import sys
import getopt
import re
import os

def excutefilelist(expression,inputfile):

    for file in inputfile:
        fp = open(file, 'r')
        alllines = fp.readlines()
        fp.close()
        line_num = 0
        for line in alllines:
            line_num = line_num + 1
            result = re.findall(expression,line)
            if len(result) > 0:
                print(line,'in',file,"line",line_num)

def excutefilepath(expression,filepath):
    for root, _, files in os.walk(filepath):
        for file in files:
            fp = open(os.path.join(root,file), 'r')
            alllines = fp.readlines()
            fp.close()
            line_num = 0
            for line in alllines:
                line_num = line_num + 1
                result = re.findall(expression,line)
                if len(result) > 0:
                    print(line,'in',file,"line",line_num)

def main(argv):

   try:
      opts, args = getopt.getopt(argv,"hr",["help","reg"])
   except getopt.GetoptError:
      print('test.py -i <inputfile> -o <outputfile>')
      sys.exit(2)

   if (len(opts) == 0) & (len(args) > 0):
       expression = args[0]
       inputfile = args[1:]
       excutefilelist(expression,inputfile)
   else:
       for opt, arg in opts:
           if opt == '-h':
               print('grep.py <Regular Expression> <file>[file1][file2]')
               print('grep.py -r <Regular Expression> <file path>')
               sys.exit()
           elif opt in ("-r", "reg"):
               expression = args[0]
               filepath = args[1]
               excutefilepath(expression,filepath)


if __name__ == "__main__":
   if len(sys.argv) - 1 > 0:
       main(sys.argv[1:])
   else:
       print('Please in put parameter or input -h for help')
