import unittest
from unittest import TestCase

from movie.models import Movie


class MovieTestCase(TestCase):
    def test_movie(self):
        movie = Movie(title = 'Agasobanuye test', description ='Testing Movie')
        self.assertEqual(movie.title, 'Agasobanuye test')  #add assertion here
        self.assertEqual(movie.description, 'Testing Movie')


if __name__ == '__main__':
    unittest.main()
