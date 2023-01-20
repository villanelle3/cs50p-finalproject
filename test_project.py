from project import brawlers, printar, seprar_palavras, battlelog, validar_pais

def test_brawlers():
    assert brawlers('laura') == "Brawler not found!"

def test_printar():
    assert printar('laura') == None

def test_battlelog():
    assert battlelog('YG898Q9GP') == "OK"

def test_function_separar():
    assert seprar_palavras('gemGrab') == "Gem Grab"
    assert seprar_palavras('hotZone') == "Hot Zone"

def test_validar_pais():
    assert validar_pais('BR') == "Brazil"
    assert validar_pais('IO') == "British Indian Ocean Territory"
    assert validar_pais('jk') == "invalido"