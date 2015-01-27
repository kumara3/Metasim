'''
Created on Jun 5, 2014

@author: kumara3

This module download the gene sequences from genbank
'''
from Bio import Entrez
from Bio import SeqIO

fh = open('/home/kumara3/workspace/Read_simulator/input_data/gene_id.csv','r')
output_file = "/home/kumara3/workspace/Read_simulator/High_complexity/Metasim_data/fastafile.fasta"

def download(fp):
    gene_id_list = []
    for each in fp:
        gene_id_list.append(each)
    #print gene_id_list 
    Entrez.email="ashwani.vit@gmail.com"
    file_handle = Entrez.efetch(db="nucleotide",id=gene_id_list,rettype="fasta",retmode="text")
    output_file_handle = open(output_file,'w')
    
    for eachline in file_handle:
        output_file_handle.write(eachline)
    output_file_handle.close()
   
download(fh)
    
