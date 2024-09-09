import unittest

def count(sequence, item):
  sum = 0
  for n in sequence:
    if n == item:
      sum += 1
  return sum

class TestCountFunction(unittest.TestCase):
  def test_count_integers(self):
    sequence = [1, 2, 3, 4, 2, 5]
    item = 2
    expected_result = 2
    self.assertEqual(count(sequence, item), expected_result)

  def test_count_strings(self):
    sequence = ["apple", "banana", "orange", "apple"]
    item = "apple"
    expected_result = 2
    self.assertEqual(count(sequence, item), expected_result)

if __name__ == "__main__":
  unittest.main()