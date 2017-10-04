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
