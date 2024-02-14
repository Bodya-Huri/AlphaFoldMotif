# Proteins motif finder

Motifs play a key role in protein functions, for example, short linear motifs (SLiMs) are known to mediate protein–protein interactions. In our reserach projects, we study protein structures and identifying motifs is an important part of understanding protein functional properties. With the recent revolution in the structural biology field, [AlphaFold Database](https://alphafold.ebi.ac.uk/) now contains predicted structures of almost all sequences disposed in the proteome database [Uniprot](https://www.uniprot.org/). We can use the AlphaFold predicted structures to investigate motifs of interest on the structural level.

Our project is to create a tool that allows scientists to find and visualise motifs in their proteins of interest to get more insights about their function. 

The input of the program will be a Uniprot sequence id and the nucleotide sequence of the motif. 
Our program will retrieve the protein sequence and a pdb file with the structure from the AlphaFold database, find the indicated motif and visualise it using [PyMOL](https://pymol.org/2/).
The output will be a PyMOL session file (.pse) and a figure of the protein with colored motifs.

Bohdana Hurieva: https://bodya-huri.github.io/

Simona Manasra: https://mlkndt.github.io/
