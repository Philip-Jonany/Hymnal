from enum import Enum
from html.parser import HTMLParser
import requests

#total hymns 1348
#choruses, 7, 19

NUM_HYMNS = 1348


class ParserState(Enum):
  FINDING_DIV = 1
  JUST_FOUND_DIV = 2
  CHOMPING_LYRICS = 3


"""
looking for div w/ class = stanza
saw div w/ that class
found tr right after this div
"""


class MyHTMLParser(HTMLParser):
    def __init__(self):
      self.stanzas = []
      self.current_stanza = ""
      self.state = ParserState.FINDING_DIV
      super(MyHTMLParser, self).__init__()

    def handle_starttag(self, tag, attrs):
      if self.state == ParserState.FINDING_DIV and tag == "div" and len(attrs) == 1 and attrs[0] == ("class", "stanza-num") :
        self.state = ParserState.JUST_FOUND_DIV
      elif self.state == ParserState.JUST_FOUND_DIV and tag == "td":
        self.state = ParserState.CHOMPING_LYRICS

      if self.state == ParserState.FINDING_DIV and tag == "td" and len(attrs) == 1 and attrs[0] == ("class", "chorus"):
        self.state = ParserState.CHOMPING_LYRICS
        self.current_stanza += "Chorus:\n"



      if self.state == ParserState.CHOMPING_LYRICS and tag == "br":
        self.current_stanza += "\n"


    def handle_data(self, data):
      if self.state == ParserState.CHOMPING_LYRICS:
        self.current_stanza += data.replace("\xa0", " ");

    def handle_endtag(self, tag):
      if self.state == ParserState.CHOMPING_LYRICS and tag == "td":
        self.state = ParserState.FINDING_DIV
        self.stanzas.append(self.current_stanza)
        self.current_stanza = "\n\n"
      

    def get_stanzas(self):
      return self.stanzas

def ExtractTitle(s, f): 
  start = s.find("<title>") + 6 
  end = s.find("</title>") 
  print(s[start:end], end = "\n\n", file=f)


def ExtractLyrics(s, f):
  parser = MyHTMLParser()
  parser.feed(s)

  for x in parser.get_stanzas():
    print(x, end = "", file = f)
  
  
  # s.stanzas = []

for i in range(1, NUM_HYMNS + 1):

  r = requests.get(url = "https://www.hymnal.net/en/hymn/h/" + str(i))
  data = r.text
  f = open ('hymn' + str(i) + '.txt', 'w')
  ExtractTitle(data, f)
  ExtractLyrics(data, f)

  words = 0;
  f.close()

  f = open ('hymn' + str(i) + '.txt', 'r')

  for word in f.read().split():
    words += 1;

  if words < 30: 
    print("Hymn " + str(i) + " is incomplete.")








