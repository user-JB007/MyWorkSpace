from io import StringIO

import pytest
import learnings.temp as temp
import lib.temp_cnvrtr as temp_cnvrtr


def test_celsius_to_fahrenheit_kelvin():
    cel_far, cel_kel = temp_cnvrtr.cel_to_far_kel(25)
    assert cel_far == 77.0
    assert cel_kel == 298.15

def test_fahrenheit_to_celsius_kelvin():
    far_cel, far_kel = temp_cnvrtr.far_to_cel_kel(77)
    assert far_cel == 25.0
    assert far_kel == 298.15

def test_kelvin_to_celsius_fahrenheit():
    kel_cel, kel_far = temp_cnvrtr.kel_to_cel_far(298.15)
    assert kel_cel == 25.0
    assert kel_far == 77.0

def test_invalid_temperature_code(monkeypatch, capsys):
    monkeypatch.setattr('sys.stdin', StringIO('4\nn\n'))
    temp_cnvrtr.main()
    captured = capsys.readouterr()
    assert (f"Bugger, you've entered an invalid temperature unit.\n Enter a valid temperature unit from the option: ") in captured.out


def test_invalid_temperature_value(monkeypatch, capsys):
    monkeypatch.setattr('sys.stdin', StringIO('1\nvalid\n25\nn\n'))
    temp.main()
    captured = capsys.readouterr()
    assert "Enter the temperature in integer or float:" in captured.out
