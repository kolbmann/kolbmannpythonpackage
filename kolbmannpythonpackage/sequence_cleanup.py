import dendropy
import os
    
def sequence_cleanup(sequence_set, out_file, taxon, gene_start, gene_end): 
    #do files have taxon and gene
    assert sequence_set[taxon]
    #check what type the data are ie: object, float64, int
    
    my_taxon_sequence = sequence_set[taxon].symbols_as_string()
    my_taxon_sequence = my_taxon_sequence[gene_start:gene_end]
    #my_taxon_sequence[int(gene[0]) : int(gene[1])]
    
    ofile = open(out_file, "w")
    ofile.write(">" + taxon + "\n" + my_taxon_sequence + "\n")
    ofile.close()
    assert os.stat(out_file).st_size != 0