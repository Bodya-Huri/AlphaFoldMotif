import subprocess
from Bio import SeqIO, BiopythonParserWarning
from pymol import cmd
import warnings
import os
import argparse
import subprocess

warnings.filterwarnings("ignore", category=BiopythonParserWarning)

def parse_arguments():
    parser = argparse.ArgumentParser(description='Analyze files')
    parser.add_argument('-f', '--file', metavar='FILE', help='input file', required=False)
    parser.add_argument('-i', '--ids', metavar='ID', nargs='+', help='uniprot id', required=False)
    parser.add_argument('-m', '--motif', metavar='MOTIF', nargs='+', type=str, help='a motif', required=True)
    return parser.parse_args()

def process_file(file):
    if file.endswith('.txt'):
        return read_args_from_file(file)
    return []

def print_motif_info(id, motif_positions):
    print(id, '---> ')
    for motif, position in motif_positions.items():
        print(f"{motif}: {position}")

def process_ids(ids, motifs):
    bad_ids = []
    for id in ids:
        if not fetch_structure(id):
            bad_ids.append(id)
        else:
            seq = fetch_sequence_from_pdb(id)
            motif_positions = find_motif(seq, motifs)
            if any(motif_positions.values()):
                print_motif_info(id, motif_positions)
                pymol_session(id, motif_positions)
            else:
                print(id, ': no hits', '\n', end='')
            remove_tmp(id)
    if bad_ids:
        print('WARNING: THERE ARE NO STRUCTURES IN ALPHAFOLD DATABASE FOR', *bad_ids)

def run_pymol():
    subprocess.Popen(f"pymol result.pse", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

def read_args_from_file(filename):
    """Parse the input file
    """
    with open(filename, 'r') as file:
        lines = file.read().split()
    return lines

def fetch_structure(uniprot_id):
    """Fetch desired UniProt entry structure from the AlphaFold database

    Args:
        uniprot_id (str): protein ID

    Returns:
        boolean: return if the UniProt ID has a structure in the AF database
    """
    subprocess.run('curl https://alphafold.ebi.ac.uk/files/AF-{}-F1-model_v4.pdb >> ./tmp/{}-F1-model_v4.pdb'.format(uniprot_id, uniprot_id),
        shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    with open('./tmp/{}-F1-model_v4.pdb'.format(uniprot_id), 'r') as f:
        pdb_file = f.read().split()
        if pdb_file[0] == 'HEADER':
            return True
        else:
            subprocess.run('rm ./tmp/{}-F1-model_v4.pdb'.format(uniprot_id),
                           shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) # check again
            
            subprocess.run('rm ./tmp/{}'.format(uniprot_id),
                           shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return False

def fetch_sequence_from_pdb(uniprot_id):
    """Retrieve the amino acid sequence of the protein 

    Args:
        uniprot_id (str): protein ID

    Returns:
        Bio.Seq.Seq: amino acid sequence of the protein
    """
    for record in SeqIO.parse('./tmp/{}-F1-model_v4.pdb'.format(uniprot_id), "pdb-atom"):
        return record.seq

def find_motif(sequence, motifs):
    """Return motif positions in the sequence (start, end). Numeration starts at 1 as in the AF pdb files

    Args:
        sequence (Bio.Seq.Seq): amino acid sequence of the protein
        motifs (str): motifs 

    Returns:
        dict: motifs with the positions where they were found
    """
    motif_positions = {}
    for motif in motifs:
        positions = []
        start = 0
        while True:
            start = sequence.find(motif, start)
            if start == -1:
                break
            positions.append([start + 1, start + len(motif)])
            start += 1
        motif_positions[motif] = positions
    return motif_positions

def pymol_session(uniprot_id, motif_positions):
    """Create a pymol session in which highlight all found motifs in different colors

    Args:
        uniprot_id (str): protein ID
        motif_positions (dict): motifs with the positions where they were found
    """
    cmd.disable('all')
    cmd.load(f"./tmp/{uniprot_id}-F1-model_v4.pdb")
    cmd.color("grey50", f"{uniprot_id}-F1-model_v4")
    cmd.bg_color("white")

    colors = ['red', 'yellow', 'forest', 'blue', 'teal', 'olive', 'salmon', 'violet', 'wheat']*10

    i = 0
    for motif in motif_positions.keys():
        for position in motif_positions[motif]:
            cmd.color(f"{colors[i]}", f"resi {position[0]}-{position[-1]} and {uniprot_id}-F1-model_v4")
            cmd.show("sticks", f"resi {position[0]}-{position[-1]} and {uniprot_id}-F1-model_v4")
        i+=1
    cmd.save(f"result.pse")

def remove_tmp(uniprot_id):
    """Remove a temporary file

    Args:
        uniprot_id (str): protein ID
    """
    os.remove(f"./tmp/{uniprot_id}-F1-model_v4.pdb")