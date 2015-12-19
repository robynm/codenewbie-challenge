import unittest
import ss

# Level 1: Choose a person from list of participants to represent yourself
# write a program that will select a random partner for yourself
# Assertion: running match_partner will return a name from list of participants
# that is not your name

# class LevelOne(unittest.TestCase):
#   participants = (
#     'Kayla Alva',
#     'Linh Alva',
#     'Mia Alva',
#     'Joseph Nguyen',
#     'Stephen Nguyen',
#     'Yuki Garza',
#     'Jill Williams',
#     'Cecilia Williams',
#     'James Williams',
#     'Annie Puri',
#     'Naveen Puri',
#     'Chris Puri',
#     'Demarco Frankel',
#     'Ximena Frankel',
#     'Xuan Thomas',
#     'George Thomas',
#     'Priya Thomas'
#     )


#   def test_pair_returns_partner(self):
#     '''pair function should return a string'''
#     person1 = self.participants[0]
#     partner = ss.pair(person1)
#     self.assertTrue(isinstance(partner, str))

#   def test_pair_not_self(self):
#     '''pair function should return a partner for person who is not person'''
#     for person in self.participants:
#       partner = ss.pair(person)
#       print("{0}'s partner is {1}".format(person, partner))
#       self.assertNotEqual(person, partner)

class UniqueMatches(unittest.TestCase):
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

  def test_match_unique_partner(self):
    '''each participant should be given a partner who is not themself'''
    for i in range(-100, 100):
      partners = ss.match(self.participants, i)
      for gifter, giftee in partners:
        self.assertNotEqual(gifter, giftee)

  def test_match_unique_gifters(self):
    '''each participant should be partnered exactly once as a gifter'''
    for i in range(-100, 100):
      partners = ss.match(self.participants, i)
      gifters = set()
      for gifter, giftee in partners:
        gifters.add(gifter)
      self.assertEqual(gifters, set(self.participants))

  def test_match_unique_giftees(self):
    '''each participant should be partnered exactly once as a giftee'''
    for i in range(-100, 100):
      partners = ss.match(self.participants, i)
      giftees = set()
      for gifter, giftee in partners:
        giftees.add(giftee)
      self.assertEqual(giftees, set(self.participants))

  def test_match_not_within_families(self):
    '''each set of partners should have different last names'''
    for i in range(-100, 100):
      partners = ss.match(self.participants, i)
      for gifter, giftee in partners:
        lname1 = gifter.split(" ")[1]
        lname2 = giftee.split(" ")[1]
        self.assertNotEqual(lname1, lname2)

# class BadInput(unittest.TestCase):
#   participants = (
#     'Kayla Alva',
#     'Linh Alva',
#     'Mia Alva',
#     'Joseph Nguyen',
#     'Stephen Nguyen',
#     'Yuki Garza',
#     'Jill Williams',
#     'Cecilia Williams',
#     'James Williams',
#     'Annie Puri',
#     'Naveen Puri',
#     'Chris Puri',
#     'Demarco Frankel',
#     'Ximena Frankel',
#     'Xuan Thomas',
#     'George Thomas',
#     'Priya Thomas'
#     )

#   def test_bad_offset(self):
#     '''match should fail if offset is not an integer'''


#   def test_bad_participants(self):
#     '''match should fail if particants is not a list or tuple'''



if __name__ == '__main__':
  unittest.main()
