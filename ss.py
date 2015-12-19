# Secret Santa matcher
import math
class OutOfRangeError(ValueError): pass

participants = (
  'Kayla Alva',
  'Linh Alva',
  'Mia Alva',
  'Joseph Nguyen',
  'Stephen Nguyen',
  'Yuki Garza',
  'Jill Williams',
  'Cecilia Williams',
  'James Williams',
  'Annie Puri',
  'Naveen Puri',
  'Chris Puri',
  'Demarco Frankel',
  'Ximena Frankel',
  'Xuan Thomas',
  'George Thomas',
  'Priya Thomas'
)

def are_related(person1, person2):
  '''check if person1 has the same last name as person2
      i.e.: are they related?
      this also serves as a check if person1 is identical to person2

      @arg1: a string in the format "firstname lastname"
      @arg2: a string in the format "firstname lastname"

      returns true if the last names match
  '''
  name1 = person1.split(" ")
  name2 = person2.split(" ")

  return ( name1[1] == name2[1] )

def match(group, offset):
  '''for each person in the group, pair them with another person
  so that everyone has a unique partner and each person is paired
  once as gifter and once as giftee

  @arg1: a tuple or list of participants to be matched together
  @arg2: an integer offset to randomize the matching process

  returns a list of tuples with each set of partners
  the first name in each tuple is the gifter, the second is the giftee

  '''

  # turn offset into an acceptable index within the list of participants
  offset %= (len(group)-1)

  # make sure offset isn't 0 - person would be matched with themself
  offset += 1

  giftees = list(group[offset:] + group[:offset])
  return zip(group, giftees)


  # for i in range(len(group)):
  #   n %= len(giftees)

  #   while ( are_related(group[i], giftees[n]) and len(giftees) > 1 ):
  #     n+=1
  #     n %= len(giftees)

  #   partners.append((group[i], giftees.pop(n)))

  # return partners

if __name__ == '__main__':
  match(participants, 3)

  # for i in range(1, len(participants) ):
  #   pairs = match(participants, i)
  #   for x, y in pairs:
  #     print("{}'s partner is {}".format(x, y))



