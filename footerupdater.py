import os
import re

currDir = os.getcwd()

with open(os.path.join(currDir, "footer.txt"), 'r') as footerFile:
	footerText = footerFile.read()

for file in os.listdir(currDir):
	if file.endswith(".html"):
		with open(os.path.join(currDir, file), 'r') as htmlFile:
			fileContent = htmlFile.read()
		outFileBK = open(os.path.join(currDir, file + ".bk"), "w")
		outFileBK.write(fileContent)
		outFile = open(os.path.join(currDir, file), "w")
		outFile.write(re.sub("\t\t<!-- Begin Footer -->.*?<!-- End Footer -->", footerText, fileContent, flags=re.DOTALL))