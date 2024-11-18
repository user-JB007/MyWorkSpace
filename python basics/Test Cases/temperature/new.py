import pytest
from io import StringIO
import sys
import os

# Add the learnings module to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import learnings.temp_cnvrtr as temp_cnvrtr

def test_celsius_to_fahrenheit_kelvin(monkeypatch, capsys):
    # Simulate user input
    monkeypatch.setattr('sys.stdin', StringIO('1\n25'))

    # Call the function that handles user input
    temp_cnvrtr.main()

    # Capture the output printed by the function
    captured = capsys.readouterr()

    # Split the captured stdout by newlines
    outputs = captured.out.split('\n')

    # Print the captured outputs for debugging purposes
    for i, output in enumerate(outputs, start=1):
        print(f"Output {i}: {output}")

    # You can now access the second output (if it exists)
    if len(outputs) > 1:
        print("Second output:", outputs[1])

    # Perform assertions
    # assert "Enter temperature unit code- 1 for Celsius, 2 for Fahrenheit, 3 for Kelvin:" in captured.out
