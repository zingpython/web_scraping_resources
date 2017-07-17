from urllib.request import urlopen
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO
from io import open
import ssl


def read_file(pdfFile):
	rsrcmgr = PDFResourceManager()
	retstr = StringIO()
	laparams = LAParams()
	device = TextConverter(rsrcmgr, retstr, laparams=laparams)
	process_pdf(rsrcmgr, device, pdfFile)
	device.close()
	content = retstr.getvalue()
	retstr.close()
	return content



