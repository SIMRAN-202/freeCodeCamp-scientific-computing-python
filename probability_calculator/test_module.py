import unittest
import random
from main import Hat, experiment

class TestProbabilityCalculator(unittest.TestCase):

    def test_hat_initialization(self):
        hat = Hat(red=3, blue=2)
        self.assertEqual(len(hat.contents), 5)
        self.assertEqual(hat.contents.count("red"), 3)
        self.assertEqual(hat.contents.count("blue"), 2)

    def test_draw_less_than_contents(self):
        random.seed(0)  # Set seed for reproducibility
        hat = Hat(red=3, blue=2)
        drawn_balls = hat.draw(2)
        self.assertEqual(len(drawn_balls), 2)
        self.assertEqual(len(hat.contents), 3)

    def test_draw_more_than_contents(self):
        hat = Hat(red=2, blue=1)
        drawn_balls = hat.draw(5)
        self.assertEqual(len(drawn_balls), 3)
        self.assertEqual(len(hat.contents), 0)

    def test_experiment_probability(self):
        random.seed(1)  # Set seed for reproducibility
        hat = Hat(blue=4, red=2, green=6)
        probability = experiment(
            hat=hat,
            expected_balls={"blue": 2, "red": 1},
            num_balls_drawn=5,
            num_experiments=1000
        )
        self.assertAlmostEqual(probability, 0.327, delta=0.01)

    def test_experiment_all_drawn(self):
        random.seed(2)  # Set seed for reproducibility
        hat = Hat(blue=3, red=2)
        probability = experiment(
            hat=hat,
            expected_balls={"blue": 3, "red": 2},
            num_balls_drawn=5,
            num_experiments=500
        )
        self.assertAlmostEqual(probability, 1.0, delta=0.01)

if __name__ == "__main__":
    unittest.main()
