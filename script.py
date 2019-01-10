import PyPDF2
import re
import matplotlib.pyplot as plt
def readPdf():
    """Translates a pdf file to a string object"""
    # Create a pdf file object
    pdfFileObj = open('salary.pdf','rb')

    # Create a pdf reader object num of pages object
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    pdfNumPages = pdfReader.numPages

    # Generate a string of all info in pdf document
    pdfString = ''
    for i in range(0,pdfNumPages):
        pdfString += pdfReader.getPage(i).extractText()
    
    return pdfString

def getSalaryInfo(pdfString):
    """Uses regex module to extract list of teachers and salaries from pdfString """

    # Create regex pattern to extract name and salary from string
    # pattern = re.compile(r'^([A-Z]{1}\S+?,\s[A-Z]{1}\S+?)(\s.+\s)(.+\s)(.+\s)(.+\s)(.+\s)(.+\s)(.+\s)(.+\s)(.+)', flags = re.M)
    pattern = re.compile(r'^([A-Z]{1}\S+?,\s[A-Z]{1}\S+?)(\s)(.*Department Head)(\s.+\s)(.+\s)(.+\s)(.+\s)(.+\s)(.+\s)(.+\s)(.+)', flags = re.M)

    # Create two lists, teacher names and salaries using regex patterns
    matches = pattern.finditer(pdfString)
    names,salaries = [],[]
    for match in matches:
        names.append(match.group(1))
        salaries.append(match.group(11))

    # Use list comprehension to remove comma and cast string to an integer. This allows lower bounds of plot to begin at 0
    salaries = [int(salaries[i].replace(",","")) for i in range(0,len(salaries))]

    return names, salaries

def plotSalaries(names, salaries):
    x,y = [],[]
    x = [names[i] for i in range(0,len(names))]
    y = [salaries[i]/2000/4 for i in range(0,len(salaries))]
    plt.barh(x, y, edgecolor='black', linewidth=1, height=0.5)
    plt.title('Value of a 5 minute meeting with your teacher')
    plt.xlabel('Teacher')
    plt.ylabel('Value($)')
    plt.show()

    return None

if __name__ == "__main__":
    pdfString = readPdf()
    names, salaries = getSalaryInfo(pdfString)
    plotSalaries(names, salaries)