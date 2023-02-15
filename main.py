from rdkit import rdBase, Chem
from rdkit.Chem import AllChem, Draw
from rdkit.Chem.Draw import rdMolDraw2D
from IPython.display import SVG
import pubchempy as pcp

benzene = pcp.get_compounds('acetic acid', 'name')
# benzene = pcp.get_compounds('benzene', 'name')
if len(benzene) == 1: benzene = benzene[0]
smiles = benzene.canonical_smiles
print(smiles)  # 'C1=CC=CC=C1'
mol_ben = Chem.MolFromSmiles(smiles)
print(type(mol_ben))  #
print(Chem.MolToMolBlock(mol_ben))

#Draw.MolToImage(mol_ben) # doesn't work in replit
Draw.MolToFile(mol_ben, 'output.svg')
