from Bio.Blast import NCBIWWW
from Bio import SeqIO

def sequence_blaster(fasta_path, results_path):
    #check file format
    result_path = SeqIO.read(fasta_path, format="fasta")
    result_path = NCBIWWW.qblast("blastn", "nt", record.format("fasta"))

    save_file = open("results_path", "w")
    save_file.write(result_handle.read())
    save_file.close()
    assert os.stat(results_path).st_size != 0
    #results file is not size 0