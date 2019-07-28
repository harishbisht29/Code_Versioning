import re
import Version_Selector

class CodeFileParser:

    versionMap = None
    codeFile= None
    outputFile = None
    codeFileContent = None
    codeFileLines = None
    startKeyword = "#Version_Start:"
    readPoint = 0

    def __init__(self, mappingFile, codeFile, outputFile):
        self.versionMap = Version_Selector.VersionSelector(mappingFile).getVersionMapping()

        self.codeFile= codeFile
        self.outputFile= outputFile

        with open(self.codeFile) as cf:
            self.codeFileContent = cf.read()
            # print(self.codeFileContent)
            # print(len(self.codeFileContent))
            # self.codeFileContent = "   #Version_Start: Head_Line=None    { {} This is just a test     }   "


    def setVersionStartIndentifier(self,vIdentifier="#Version_Start:"):
        self.startKeyword = vIdentifier

    def findMatchingClosedParenthesis(self,openIndex):
       content = self.codeFileContent[openIndex+1:]
       extraOpenBrackets = 0
       for i in range(len(content)):
           char = content[i]
           if char == "{":
               extraOpenBrackets = extraOpenBrackets+ 1
           elif char == "}" and extraOpenBrackets == 0:
               return openIndex+i+1
           elif char == "}":
               extraOpenBrackets = extraOpenBrackets -1

    def checkVersionEntry(self, pos):
        return True if self.codeFileContent[pos:pos+ len(self.startKeyword)] == self.startKeyword else False
                   
    def createOutputFile(self):

        keywordLength = len(self.startKeyword) 
        outputFile = open(self.outputFile,"w")
        isVersionStart= False
        stallingFlag = False

        while True:
            if (self.readPoint == len(self.codeFileContent)):
                break;
            if self.checkVersionEntry(self.readPoint):
                print("Version Start Keyword Detected at ",self.readPoint)

                reg_exp = self.startKeyword+r"\s*(\w+)=\s*(\w+)"
                pattern = re.compile(reg_exp)
                search = pattern.search(self.codeFileContent,pos=self.readPoint)
                versionName = search.group(1).upper()
                versionValue = search.group(2).upper()
        
                openBracket = self.codeFileContent.find("{",self.readPoint)
                closedBracket = self.findMatchingClosedParenthesis(openBracket)
                print("version open bracket-",openBracket)
                print("version closed bracket-",closedBracket)
                x,y = search.span()

                print("versionName-",versionName+ " versionValue-"+ versionValue)

                if self.versionMap[versionName] == versionValue:
                    self.codeFileContent = self.codeFileContent[:x]+ self.codeFileContent[openBracket+1:closedBracket]+ self.codeFileContent[closedBracket+1:];
                    
                    print(versionName," should be included")
                    print("Opening bracket ", openBracket)
                    print("Closing bracket ", closedBracket)
                else:
                    print(versionName," shouldn't be included")
                    self.codeFileContent = self.codeFileContent[:x]+ self.codeFileContent[closedBracket+1:]

            outputFile.write(self.codeFileContent[self.readPoint])
            self.readPoint = self.readPoint+ 1

        outputFile.close()



if __name__ == '__main__':
    cfp = CodeFileParser("mapping.csv", "Test_Code.sas", "output.sas")
    cfp.createOutputFile()
    # cfp.printJustParenthesis()
    # cfp.printCodeFileLines()
