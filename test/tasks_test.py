import unittest
from tasks.tasks import is_unique, is_permutation, urlify, permutationPalindrome, oneAway, compression


class TestTasks(unittest.TestCase):
    def test_string_is_unique(self):
        self.assertTrue(is_unique('Hungry'))

    def test_that_string_has_duplicate(self):
        self.assertFalse(is_unique('Buddy'))

    def test_that_permutation_of_a_string_can_be_detected(self):
        self.assertTrue(is_permutation('abc', 'cba'))

    def test_that_permutation_with_diff_length(self):
        self.assertFalse(is_permutation('abca', 'hcd'))

    def test_that_string_is_not_a_permutation(self):
        self.assertFalse(is_permutation('arcade', 'facade'))

    def test_that_string_can_is_in_url_pattern(self):
        expected = "Mr%20John%20Smith"
        self.assertEqual(expected, urlify("Mr John Smith"))

    def test_that_should_return_true_if_string_is_permutation_palindrome(self):
        self.assertTrue(permutationPalindrome("tactcoa"))

    def test_should_return_true_if_it_one_way_diff(self):
        self.assertTrue(oneAway('pale', 'ple'))
        self.assertTrue(oneAway('pales', 'ple'))
        self.assertTrue(oneAway('pale', 'bale'))
        self.assertFalse(oneAway('pale', 'bake'))

    def test_should_compress_string_to_smallest_form(self):
        expected = "a2b1c5a3"
        self.assertEqual(expected, compression("aabcccccaaa"))
        self.assertEqual("abcd", compression("abcd"))


if __name__ == '__main__':
    unittest.main()
