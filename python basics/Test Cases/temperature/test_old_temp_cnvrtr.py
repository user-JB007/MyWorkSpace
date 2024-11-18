from io import StringIO

import pytest
import learnings.temp_cnvrtr as temp_cnvrtr

def test_celsius_to_fahrenheit_kelvin(monkeypatch, capsys):
    input_data = '1\n25\nn\n'
    monkeypatch.setattr('sys.stdin', StringIO(input_data))
    temp_cnvrtr.main()
    captured = capsys.readouterr()
    assert "Thanks for using temperature unit converter." in captured.out

def test_fahrenheit_to_celsius_kelvin(monkeypatch, capsys):
    input_data = '2\n77\nn\n'
    monkeypatch.setattr('sys.stdin', StringIO(input_data))
    temp_cnvrtr.main()
    captured = capsys.readouterr()
    assert "Thanks for using temperature unit converter." in captured.out

def test_kelvin_to_celsius_fahrenheit(monkeypatch, capsys):
    input_data = '3\n298.15\nn\n'
    monkeypatch.setattr('sys.stdin', StringIO(input_data))
    temp_cnvrtr.main()
    captured = capsys.readouterr()
    assert "Enter temperature unit code- 1 for Celsius, 2 for Fahrenheit, 3 for Kelvin: " in captured.out

def test_invalid_temperature_code(monkeypatch, capsys):
    input_data = '4\nn\n'
    monkeypatch.setattr('sys.stdin', StringIO(input_data))
    temp_cnvrtr.main()
    captured = capsys.readouterr()
    assert "Please enter a valid integer for the temperature code: " in captured.out

def test_invalid_temperature_value(monkeypatch, capsys):
    input_data = '1\ninvalid\n25\nn\n'
    monkeypatch.setattr('sys.stdin', StringIO(input_data))
    temp_cnvrtr.main()
    captured = capsys.readouterr()
    assert "Enter the temperature in integer or float:" in captured.out
