import dendropy
import os.path

def sequence_reader(filepath):
    #that the file exists
    #that the file is in the right format
    assert os.path.exists(filepath)
    sequence_set = dendropy.DnaCharacterMatrix.get(
        path=filepath,
        schema="phylip"
)
      #right return type - DNA character matrix
    assert type(sequence_set) == dendropy.datamodel.charmatrixmodel.DnaCharacterMatrix
    return(sequence_set)
    
    # is that could be asserted