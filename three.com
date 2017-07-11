from urllib.request import urlopen
from bs4 import BeautifulSoup
import re