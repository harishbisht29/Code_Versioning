import re 
import Version_Selector

class CodeFileParser:

    versionMap = None
    codeFile= None
    outputFile = None

    codeFileLines = None
    versionStartString = "#Version_Start:"
    justParenthesis = None

    def __init__(self, mappingFile, codeFile, outputFile):
        self.versionMap = Version_Selector.VersionSelector(mappingFile).versionSelectionMap
    
        self.codeFile= codeFile
        self.outputFile= outputFile
        self.codeFileLines= []

        with open(self.codeFile) as cf:
            self.codeFileLines = cf.readlines()

        # self.justParenthesis = [''.join(c for c in s if c in '{}') for s in self.codeFileLines]

    def printCodeFileLines(self):
        print("--------------------Printing Code File Lines->--------------------")
        print("contents->",self.codeFileLines)
        print("length->", len(self.codeFileLines))

    def printJustParenthesis(self):
        print("---------------------Printing Just Parenthesis Lines------------------")
        print("contents->",self.justParenthesis)
        print("length->",len(self.justParenthesis))

    def setVersionStartIndentifier(self,vIdentifier="#Version_Start:"):
        self.versionStartString = vIdentifier

    def findMatchingClosedParenthesis(self,oParaDimension):
        bracLineNumber = oParaDimension[0]
        bracIndex = oParaDimension[1]
        linesToProcess = self.codeFileLines[bracLineNumber-1:] 

        linesToProcess[0] = linesToProcess[0][bracIndex:]
        innerOpeningBrackets = 0
        foundLineNumber= 0
        foundBracindex= 0
        for lineNumber in range(len(linesToProcess)):
            line = linesToProcess[lineNumber]
            print(line)
            for characterNumber in range(len(line)):
                character = line[characterNumber]
                print(character)
                if character == "{":
                    innerOpeningBrackets  = innerOpeningBrackets + 1
                elif character == "}":
                    if innerOpeningBrackets == 0:
                        foundLineNumber = lineNumber + bracLineNumber
                        foundBracindex = characterNumber + bracIndex
                        break;
                    else:
                        innerOpeningBrackets = innerOpeningBrackets - 1
            if foundLineNumber != 0:
                break;
            bracIndex = 0
        return (foundLineNumber,foundBracindex+1)

    def createOutputFile(self):
        outputFile = open(self.outputFile,"w")
        # outputFile.write("Hello\nworld")
        reg_exp = self.versionStartString+r"\s*(\w+)=\s*(\w+)"
        pattern = re.compile(reg_exp)
        for line_number in range(len(self.codeFileLines)):
            
            codeLine = self.codeFileLines[line_number]
            # codeLine  = "Hi world"+self.versionStartString+"Version_Name=Type"
            search = pattern.search(codeLine)
            if search is not None:
                
                Version_Name = search.group(1).upper()
                Version_Value = search.group(2).upper()                
                print(codeLine)
                print(Version_Name)
                print(Version_Value)

                if self.versionMap.get(Version_Name) == None:
                    print("Version Not Mentioned in mapping file")
                else:
                    
                    if self.versionMap.get(Version_Name) == Version_Value:
                        print("Version Should be selected")
                    else:
                        print("Version Shouldn't be selected")
                    

                starti, endi = search.span();
                print("LineNumber:",line_number,"start_index:",starti,"end_index",endi)
                
        outputFile.close()


if __name__ == '__main__':
    cfp = CodeFileParser("mapping.csv", "Test_Code.sas", "output.sas")
    cfp.createOutputFile()
    # cfp.printJustParenthesis()
    # cfp.printCodeFileLines()





    