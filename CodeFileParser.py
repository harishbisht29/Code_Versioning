class CodeFileParser:
    mappingFile= None
    codeFile= None
    outputFile = None

    codeFileLines = None
    versionStartString = "#Version_Start:"
    justParenthesis = None

    def __init__(self, mappingFile, codeFile, outputFile):
        self.mappingFile= mappingFile
        self.codeFile= codeFile
        self.outputFile= outputFile
        self.codeFileLines= []

        with open(self.codeFile) as cf:
            self.codeFileLines = cf.readlines()

        self.justParenthesis = [''.join(c for c in s if c in '{}') for s in self.codeFileLines]

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

if __name__ == '__main__':
    cfp = CodeFileParser("mapping.csv", "Test_Code.sas", "output.sas")
    out = cfp.findMatchingClosedParenthesis((49,3))
    print(out)
    # cfp.printJustParenthesis()
    # cfp.printCodeFileLines()





    