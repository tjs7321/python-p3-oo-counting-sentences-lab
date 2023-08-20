#!/usr/bin/env python3
import re

class MyString:

  def __init__(self, value=''):
    self.value = value

  def get_value(self):
    return self._value
  
  def set_value(self, value):
    if type(value) == str:
      self._value = value
    else: print("The value must be a string.")

  def is_sentence(self):
    if (list(self.value))[-1] == '.':
      return True
    return False

  def is_question(self):
    if (list(self.value))[-1] == '?':
      return True
    return False

  def is_exclamation(self):
    if (list(self.value))[-1] == '!':
      return True
    return False

  def count_sentences(self):
    spread = re.split(r"[.?!]\s*", self.value)
    a = spread.count('')
    b = len(spread)
    return b-a
  
  value = property(get_value, set_value)
