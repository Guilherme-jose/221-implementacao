import pytest



def test_login() :
    f = open('activities.txt', 'r')
    conteudo = f.readlines()
    
    for i in conteudo:
        i = i.split(',')
        if i[0] == 'energy':
            assert len(i) == 4
        else:
            assert len(i) == 8
