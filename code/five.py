from urllib.request import urlopen
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO
from io import open
import ssl


def read_file(pdfFile):
	manager = PDFResourceManager()
	string = StringIO()
	laparams = LAParams()
	device = TextConverter(manager, string, laparams=laparams)
	process_pdf(manager, device, pdfFile)
	device.close()
	content = string.getvalue()
	string.close()
	return content



def pdf_to_str():
	context = ssl._create_unverified_context()

	pdfFile = urlopen("https://www.nasa.gov/sites/"\
		"default/files/atoms/files/"\
		"journey-to-mars-next-steps-20151008_508.pdf", context=context);
	outputString = read_file(pdfFile)

	print(outputString)
	pdfFile.close()

pdf_to_str()
