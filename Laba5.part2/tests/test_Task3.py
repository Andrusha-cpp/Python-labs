from src.Task3 import polindrom_check

def test_lower_polindrom():
    assert polindrom_check("tenet") == True

def test_upper_lower_polindrom():
    assert polindrom_check("TEnet") == False

def test_upper_polindrom():
    assert polindrom_check("TENET") == True

def test_not_polindrom():
    assert polindrom_check("Tennant") == False