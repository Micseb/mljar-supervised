import os
import sys
import unittest


from tests.test_iterative_learner_framework import IterativeLearnerTest
from tests.test_iterative_learner_framework_with_preprocessing import (
    IterativeLearnerWithPreprocessingTest,
)
from tests.test_automl import AutoMLTest

# from tests.test_automl_with_data import AutoMLTestWithData

# from .test_metric import MetricTest

if __name__ == "__main__":
    unittest.main()
