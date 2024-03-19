from defs import *

def test_read_args_from_file():
    expected = read_args_from_file('data.txt')
    assert(expected == ['Q9NT68', 'P05129', 'A0A290U7C4'])

def test_fetch_structure():
    expected = fetch_structure('Q9NT68')
    assert(expected == False)

    expected = fetch_structure('A0A290U7C4')
    assert(expected == True)
    os.remove(f"./tmp/A0A290U7C4-F1-model_v4.pdb")

    expected = fetch_structure('P05129')
    assert(expected == True)
    os.remove(f"./tmp/P05129-F1-model_v4.pdb")

def test_fetch_sequence_from_pdb():
    warnings.filterwarnings("ignore", category=BiopythonParserWarning)

    expected = fetch_sequence_from_pdb('AF-Q5VSL9')
    assert(expected.startswith('MEPAVGGPGPLIVNNKQPQPPPPPPPAAA'))

def test_find_motif():
    expected = find_motif('AAAVMAA', ['VM'])
    assert(expected == {'VM' : [[4, 5]]})

    expected = find_motif('AVMAAVM', ['VM', 'A'])
    assert(expected == {'VM' : [[2, 3], [6, 7]], 'A': [[1, 1], [4, 4], [5, 5]]})

def test_pymol_session():
    pymol_session('AF-Q5VSL9', {'VM' : [[2, 3], [6, 7]]})
    assert(os.path.exists('result.pse'))
    os.remove('result.pse')



