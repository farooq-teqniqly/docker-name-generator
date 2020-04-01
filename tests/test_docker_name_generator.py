import unittest
from docker_name_generator import generate_name

class TestDockerNameGenerator(unittest.TestCase):
    def test_generate_names_returns_formatted_names(self):
        # Arrange
        tup = ["Farooq"], ["pizza"]

        # Act
        generated_name = generate_name(tup)

        # Assert
        self.assertEqual(generated_name, "farooq_pizza")

if __name__ == "__main__":
    unittest.main()