# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 14:32:11 2023

@author: SSB-Digital-05
"""
import os
import tempfile
import json

import networkx as nx
import matplotlib.pyplot as plt

# importing the sys module
import sys        
 
# appending the directory of mod.py
# in the sys.path list
# print(sys.path)
sys.path.append('C:/Users/SSB-Digital-05/Downloads/CERN/packages')

from packages.dep_graph import file_reader


def test_file_reader():
    # Create a temporary file with sample data
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as tmp:
        graph = {
            "pkg1": ["pkg2", "pkg3", "pkg5", "pkg6"],
            "pkg2": ["pkg3", "pkg5"],
            "pkg3": ["pkg4", "pkg5"],
            "pkg4": ["pkg6"],
            "pkg5": ["pkg4"],
            "pkg6": []
        }
        json.dump(graph, tmp)
        tmp.flush()

        # Save the temporary file path and change the working directory
        tmp_file_path = tmp.name
        os.chdir(os.path.dirname(tmp_file_path))

        # Call the function with the temporary file path
        file_reader(tmp_file_path)

        # Check if the graph is visualized
        plt.show()

    # Cleanup the temporary file
    os.remove(tmp_file_path)

