import os
import sys
import unittest
import pandas as pd
from pathlib import Path
from pdb import set_trace

root = Path(os.path.abspath(os.path.join(
    os.getcwd().split("se4sci")[0], 'se4sci/se4sci')))

if root not in sys.path:
    sys.path.append(str(root))

from data.data_handler import DataHandler

class TestDataHandler(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestDataHandler, self).__init__(*args, **kwargs)
        self.dh = DataHandler(data_path=root.joinpath("data"))

    def test_get_data(self):
        all_data = self.dh.get_data()
        self.assertIsInstance(all_data, dict)
        self.assertIsInstance(all_data["openmm"], list)
        self.assertIsInstance(all_data["openmm"][0], pd.core.frame.DataFrame)
        set_trace()
