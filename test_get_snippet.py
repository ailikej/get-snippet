import get_snippet
import unittest

class TestGetSnippet(unittest.TestCase):
	def test_case_1(self):
		output = get_snippet.get_snippet("Today we are talking about coding with Java. Also want to talk about python. But I like Java more.", "Java", "python")
		self.assertEqual(output, "python. But I like Java")
	def test_case_2(self):
		output = get_snippet.get_snippet("Someone needs help with HTML and CSS. I am okay with that.", "with", "CSS")
		self.assertEqual(output, "with HTML and CSS.")
	def test_case_3(self):
		output = get_snippet.get_snippet("Someone needs help with HTML and CSS. I am okay with that.", "with", "Javascript")
		self.assertEqual(output, "")
	def test_case_4(self):
		output = get_snippet.get_snippet("", "Java", "Python")
		self.assertEqual(output, "")
	def test_case_5(self):
		output = get_snippet.get_snippet("java python", "python", "java")
		self.assertEqual(output, "java python")
	def test_case_6(self):
		output = get_snippet.get_snippet("java python", "HTML", "CSS")
		self.assertEqual(output, "")
	def test_case_7(self):
		output = get_snippet.get_snippet("Java is the best language in the world, but some people love Python.", "JAVA", "PYTHON")
		self.assertEqual(output, "Java is the best language in the world, but some people love Python.")	
	def test_case_8(self):
		output = get_snippet.get_snippet("Java is the best language in the world. Java is not Python.", "PyThOn", "JaVa")
		self.assertEqual(output, "Java is not Python.")
	def test_case_9(self):
		output = get_snippet.get_snippet("Java Java Java Java _____ Python python python.", "Java", "python")
		self.assertEqual(output, "Java _____ Python")
	def test_case_10(self):
		output = get_snippet.get_snippet("Java Java Java Java _____ Python python python java.", "Java", "python")
		self.assertEqual(output, "python java.")


if __name__ == '__main__':
	unittest.main()
