import sys

class InputFile:
    cases = 0
    filename = ''
    caseLength = 0
    lines = []

    def __init__(self, filename, caseLength):
        self.filename = filename
        self.caseLength = caseLength

    def read(self):
        with open(self.filename, 'r') as f:
            self.lines = f.readlines()
        self.lines = [line.strip() for line in self.lines]
        self.cases = int(self.lines[0])

    def getCases(self):
        return self.cases

    def getCase(self, index):
        caseLines = []
        startOffset = (index-1)*self.caseLength + 1
        endOffset = index*self.caseLength + 1
        for i in range(startOffset, endOffset):
            caseLines.append(self.lines[i])
        return caseLines


class CaseSolver:
    def __init__(self, caseNumber, caseInfo):
        self.number = caseNumber
        self.params = caseInfo

    def doMovements(self, sequence):
        if sequence.count('+') == len(sequence):
            result = 0
        else:
            pos = sequence.index('-')
            if pos == 0:
                while pos < len(sequence) and sequence[pos] == '-':
                    sequence[pos] = '+'
                    pos = pos + 1
                result = 1 + self.doMovements(sequence)
            else:
                pos = 0
                while pos < len(sequence) and sequence[pos] == '+':
                    sequence[pos] = '-'
                    pos = pos + 1
                result = 1 + self.doMovements(sequence)
        return result

    def solve(self):
        sequence = list(self.params[0])
        result = str(self.doMovements(sequence))
        return "Case #" + str(self.number) + ": " + result


if __name__ == '__main__':
    if len(sys.argv) == 2:
        # 1. Update the number of lines per case
        linesPerCase = 1
        input_file = InputFile(sys.argv[1], linesPerCase);
        input_file.read()
        for i in range(1, input_file.getCases() + 1):
            print CaseSolver(i, input_file.getCase(i)).solve()
    else:
        usage = "Usage :"
        usage = usage + sys.argv[0]
        usage = usage + " <input_file>"
        print usage
