import csv

class VersionSelector:
    vSelectorFile = None
    versionSelectionMap = None

    def __init__(self, fileName):
        self.vSelectorFile = fileName
        self.versionSelectionMap = {}
        try:
            with open(self.vSelectorFile,'rt')as f:
                data = csv.reader(f)
                for row in data:
                    self.versionSelectionMap[row[0].upper()] = row[1].upper()

        except OSError:
            print("File Doesn't Exist")
        
    def printversionSelectionMap(self):
        print(self.versionSelectionMap)

    def getVersionValue(self, vname):
        return self.versionSelectionMap[vname.upper()]

if __name__ == '__main__':
    vs = VersionSelector("mapping.csv")
    vs.printversionSelectionMap()
    print(vs.getVersionValue("Head_LINE"))
