"""Create all tools classes for use in other projects."""
import json
from socket import gethostbyaddr
class atools():
  """A tools class used to append and get things to and from important save docs."""
  def __init__(self, doc):
    self.doc = doc
  def append(self, userinput):
    self.userinput = userinput
    out_file = open(self.doc, "a")
    json.dump(userinput, out_file, indent = 6)
  def get(self, line = 1):
    in_file = open(self.doc)
    out = json.load(in_file)
    return out
