# Protein motif finder

Motifs play a crucial role in protein functions. For example, short linear motifs (SLiMs) are known to mediate protein–protein interactions. In our research projects, we study protein structures and identifying motifs is integral in understanding protein functional properties. With the recent revolution in the structural biology field, [AlphaFold Database](https://alphafold.ebi.ac.uk/) now contains predicted structures of almost all sequences deposed in the proteome database [Uniprot](https://www.uniprot.org/). We can use the AlphaFold predicted structures to investigate motifs of interest on the structural level.

Our project is to create a tool that allows scientists to find and visualize motifs in their proteins of interest to get more insights about their function. 

The program's input will be a UniProt sequence ID and the amino acid sequence of the motif. 
Our program will retrieve the protein sequence and a PDB file with the structure from the AlphaFold database, find the indicated motif, and visualize it using [PyMOL](https://pymol.org/2/).
The output will be a PyMOL session file (.pse) with all proteins and their colored motifs.

## Installation

You need to clone this repository.
```bash
git clone https://github.com/Bodya-Huri/AlphaFoldMotif afmotif
cd afmotif
```

Now, create a conda environment with all the requirements installed.
```bash
conda create -n afmotif
conda activate afmotif
conda install conda-forge::biopython
conda install conda-forge::pymol-open-source
```

## How to use Protein Motif Finder

First, activate the working environment.
```bash
conda activate afmotif
```

Then, launch the program.

#### Providing Uniprot Accession IDs from a command line.
```bash
python3 motif_finder.py -i Q9NT68 -m VM
```

#### Using a txt file with a list of Uniprot Accession IDs.
```bash
python3 motif_finder.py -f data.txt -m VM
```

## Testing

Run a test from the folder with ```def.py``` file.
```bash
pytest
```

You might need to install pytest first.
```bash
conda install pytest
```

## Authors
Simona Manasra: https://mlkndt.github.io/

Bohdana Hurieva: https://bodya-huri.github.io/

