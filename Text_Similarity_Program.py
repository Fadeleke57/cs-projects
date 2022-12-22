#
# finalproject.py - CS111 Final Project
#
# Similarity of text samples
#
# partner's name: Luan (Tommy) Nguyen
# partner's email: lhnguy@bu.edu
#
import math

def test():
    """ your docstring goes here """
    source1 = TextModel('source1')
    source1.add_string('It is interesting that she is interested.')

    source2 = TextModel('source2')
    source2.add_string('I am very, very excited about this!')

    mystery = TextModel('mystery')
    mystery.add_string('Is he interested? No, but I am.')
    mystery.classify(source1, source2)

def run_tests():
    """ your docstring goes here """
    source1 = TextModel('pixar')
    source1.add_file('pixar.txt')

    source2 = TextModel('dreamworks')
    source2.add_file('dreamworks.txt')

    new1 = TextModel('shrek')
    new1.add_file('shrek.txt')
    new1.classify(source1, source2)
    
    new2 = TextModel('a_bugs_life')
    new2.add_file('a_bugs_life.txt')
    new2.classify(source1, source2)
    
    new3 = TextModel('moana')
    new3.add_file('moana.txt')
    new3.classify(source1, source2)
    
    new4 = TextModel('coco')
    new4.add_file('coco.txt')
    new4.classify(source1, source2)
    
    
  
def clean_text(txt):
  '''takes a string of text txt as a parameter and returns a list containing the words in txt after it has been cleaned.
  '''
  for symbol in """.,?"'!;:""":
    txt = txt.replace(symbol, '')
  return txt.lower().split()


def stem(s):
  ''' Returns the stem of s. The stem of a word is the root part of the word, which excludes any prefixes and suffixes.
  input: s is a string
  '''
  word = s
  if len(word) <= 3:  # don't think any words 3 or less have stems
    if word[-1] == 'y':  # all y words should end in i
      return word[:-1] + 'i'
    else:
      return word
  if word[-4:] == 'ness' or word[-4:] == 'less':
    if len(word) > 4:
      word = word[:-4]
      word = stem(word)  # recursive call, ex: "completedness"
    else:
      word = word
  if word[-1] == 's':
    word = word[:-1]
    word = stem(word)  # recursive call again because there can still be a stem to be found. "readings"
  if word[-3:] == 'ing':
    if len(word) >= 5:  # makes sure there's no out of bounds
      if word[-4] == word[-5]:  # ex: word is "stemming"
        word = word[:-4]  # stem only goes to "stem"
      else:
        word = word[:-3]  # "firing" -> "fir", not "firi"
    else:  # cases like "ring" or "wing"
      word = word[:]  # I don't think there's any 4 letter abnormalities.
  elif word[-2:] == 'er':
    if len(word) >= 5:
      if word[-3] == word[-4]:  # ex: word is "ripper"
        word = word[:-3]  # "rip"
      else:
        word = word[:-2]  # "rider" -> "rid"
    elif len(word) == 4:  # "user", "icer", idk
      word = word[:-1]
  elif word[-2:] == 'ed':
    if len(word) >= 5:
      if word[-4] == word[-5]:  # ex: word is "ripped"
        word = word[:-3]  # "rip"
      else:
        word = word[:-2]  # "abided" -> "abid"
    elif len(word) == 4:  # "used", "iced", idk
      word = word[:-1]
  elif word[-3:] == 'ies':
    word = word[:-2]

  elif word[-2:] == 'ly' or word[-2:] == 'li' :
    word = word[:-2]
    word = stem(word)  # recursive call, ex: "hurriedly"
  #
  # Separate because checks more generic endings.
  #
  if word[-1] == 'e':  # if a word ends in e e isn't apart of the stem. any examples against this? can't think of any. 'dye'?
    word = word[:-1]
    word = stem(
      word)  # basically the only example I had to add this was 'happinesses'
  elif word[-1] == 'y':
    word = word[:-1] + 'i'
  #
  # now doing prefixes
  #
  if len(word) <= 3:  # words less than 3 at this point shouldn't have prefixes, right?
    return word
  if word[:2] == 'un':  # maybe we could put something that checks the length of the word after you remove "un" ?
    word = word[2:]
  elif word[:2] == 're':
    word = word[2:]
  if len(word) <= 5:
    if word[:2] == 'fore':
      word = word[4:]
  return word

def compare_dictionaries(d1, d2):
  """ Takes two feature dictionaries and returns their log similarity score. 
  input: d1 and d2 are dictionaries of features of a string of text.
  """
  if d1 == {}:
    return -50
  score = 0
  total = 0
  for key in d1:
    total += d1[key]
  for count in d2:
    if count in d1:
      score += math.log(d1[count] / total) * d2[count]
    else:
      score += math.log(0.5 / total) * d2[count]
  return score
      
class TextModel:
  ''''''

  def __init__(self, model_name):
    '''constructs a new TextModel object '''
    self.name = model_name
    self.words = {}
    self.word_lengths = {}
    self.stems = {}
    self.sentence_lengths = {}
    self.num_and_or = {}

  def __repr__(self):
    '''Return a string representation of the TextModel.'''
    s = 'text model name: ' + self.name + '\n'
    s += 'number of words: ' + str(len(self.words)) + '\n'
    s += 'number of word lengths: ' + str(len(self.word_lengths)) + '\n'
    s += 'number of stems: ' + str(len(self.stems)) + '\n'
    s += 'number of sentence lengths: ' + str(len(self.sentence_lengths)) + '\n'
    s += 'number of and/or: ' + str(self.num_and_or['and'] + self.num_and_or['or']) + '\n'
    return s

  def add_string(self, s):
    ''' Analyzes the string txt and adds its pieces
       to all of the dictionaries in this text model.'''
    word_list = s.split()
    # Add code to update self.sentence_lengths

    count = 0
    while len(word_list) > 0:
      count += 1
      if word_list[0][0] in ".?!" or len(word_list) == 1: # check if word has sentence-ending punctuation
        if count not in self.sentence_lengths:
          self.sentence_lengths[count] = 1
          count = 0
        else:
          self.sentence_lengths[count] += 1
          count = 0
      word_list = word_list[1:]
      
    # Add code to clean the text and split it into a list of words.
    # *Hint:* Call one of the functions you have already written!
    word_list = clean_text(s)
    # Update self.words to reflect w
    # either add a new key-value pair for w
    # or update the existing key-value pair.
    for w in word_list:
      if w not in self.words:
        self.words[w] = 1
      else:
        self.words[w] += 1

      # Add code to update self.word_lengths
      if len(w) not in self.word_lengths:
        self.word_lengths[len(w)] = 1
      else:
        self.word_lengths[len(w)] += 1

        # Add code to update self.stems
      if stem(w) not in self.stems:
        self.stems[stem(w)] = 1
      else:
        self.stems[stem(w)] += 1
        
      if w == 'and' or w == 'or':
        if w not in self.num_and_or:
          self.num_and_or[w] = 1
        else:
          self.num_and_or[w] += 1
           
  def add_file(self, filename):
    '''adds all of the text in the file identified by filename to the 
      model.'''
    f = open(filename, 'r', encoding='utf8', errors='ignore')
    self.add_string(f.read())

  def save_model(self):
    """Saves the TextModel object self by writing its various feature dictionaries to files. 
    There will be one file for each feature dictionary
    """
    d = self.words  # Assigns words to a variable d
    f = open(self.name + '_' + 'words', 'w')  # Open file for writing words to.
    f.write(str(d))  # Writes the dictionary to the file.
    f.close()  # Close the file.

    d = self.word_lengths  # Assigns words to a variable d
    f = open(self.name + '_' + 'word_lengths','w')  # Open file for writing words to.
    f.write(str(d))  # Writes the dictionary to the file.
    f.close()  # Close the file.
    
    d = self.stems  # Assigns words to a variable d
    f = open(self.name + '_' + 'stems', 'w')  # Open file for writing words to.
    f.write(str(d))  # Writes the dictionary to the file.
    f.close()  # Close the file.

    d = self.sentence_lengths  # Assigns words to a variable d
    f = open(self.name + '_' + 'sentence_lengths', 'w')  # Open file for writing words to.
    f.write(str(d))  # Writes the dictionary to the file.
    f.close()
    
    d = self.num_and_or  # Assigns words to a variable d
    f = open(self.name + '_' + 'num_and_or', 'w')  # Open file for writing words to.
    f.write(str(d))  # Writes the dictionary to the file.
    f.close()  # Close the file.

  def read_model(self):
    """Reads the stored dictionaries for the called TextModel object and assigns them to the attributes of the called TextModel.
    """
    f = open(self.name + '_' + 'words', 'r')  # Open for reading.
    d_str = f.read()  # Read in a string that represents a dict.
    f.close()
    d = dict(eval(d_str))  # Convert the string to a dictionary.
    self.words = d

    f = open(self.name + '_' + 'word_lengths', 'r')
    d_str = f.read()  # Read in a string that represents a dict.
    f.close()
    d = dict(eval(d_str))  # Convert the string to a dictionary.
    self.word_lengths = d
    
    f = open(self.name + '_' + 'sentence_lengths', 'r')
    d_str = f.read()  # Read in a string that represents a dict.
    f.close()
    d = dict(eval(d_str))  # Convert the string to a dictionary.
    self.word_lengths = d
    
    f = open(self.name + '_' + 'stems', 'r')
    d_str = f.read()  # Read in a string that represents a dict.
    f.close()
    d = dict(eval(d_str))  # Convert the string to a dictionary.
    self.word_lengths = d
    
    f = open(self.name + '_' + 'num_and_or', 'r')
    d_str = f.read()  # Read in a string that represents a dict.
    f.close()
    d = dict(eval(d_str))  # Convert the string to a dictionary.
    self.word_lengths = d
    
    


  def similarity_scores(self, other):
    """computes and returns a list of log similarity scores measuring the similarity of self and other – one score for each type of feature (words, word lengths, stems, sentence lengths, and your additional feature).
    """
    word_score = compare_dictionaries(other.words, self.words)
    word_length_score = compare_dictionaries(other.word_lengths, self.word_lengths)
    stems_score = compare_dictionaries(other.stems, self.stems)
    sentence_length_score = compare_dictionaries(other.sentence_lengths, self.sentence_lengths)
    num_and_or_score = compare_dictionaries(other.num_and_or, self.num_and_or)
    return [word_score, word_length_score, stems_score, sentence_length_score, num_and_or_score]

  def classify(self, source1, source2):
    """
    Compares the called TextModel object to two other "source" TextModel objects and determines which of these other TextModels is the more likely source of the called TextModel.
    """
    scores1 = self.similarity_scores(source1)
    scores2 = self.similarity_scores(source2)
    print('Scores for ' + source1.name + ':' + str(scores1))
    print('Scores for ' + source2.name + ':' + str(scores2))
    tally1 = 0
    tally2 = 0
    for i in range(len(scores1)):
      if scores1[i] >= scores2[i]:
        tally1 += 1
      else:
        tally2 += 1
    if tally1 >= tally2:
      print(self.name + ' is more likely to have come from ' + source1.name)
    else:
      print(self.name + ' is more likely to have come from ' + source2.name)
    
