"""Protein motif finder: find and visualise motifs in the AlphaFold protein structures
"""
import os
from defs import *

def main():
    args = parse_arguments()
    motifs = args.motif

    if args.file:
        ids = process_file(args.file)
    elif args.ids:
        ids = args.ids

    print('***************** AF MOTIF FINDER *******************')
    print('uniprot ids:', *ids)
    print('motif:', *motifs)

    if not os.path.exists('tmp'):
        os.mkdir('tmp')

    process_ids(ids, motifs)
    run_pymol()

if __name__ == "__main__":
    main()