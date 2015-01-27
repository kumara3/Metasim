'''
Created on Jun 2, 2014

@author: Ashwani

Downlaod the genebank files
set up taxon input file
Load and call the input file via command line
perform the simulation
Get the output
'''

from pkg_resources import resource_filename  # @UnresolvedImport
import subprocess 
import tempfile

from ReadSimulator.ReadSimulator import ReadSimulator


class MetaSimSimulator( ReadSimulator ):
    '''
    #Constructor
    classdocs
    '''
    def __init__(self,error_model):
        self.error_model = resource_filename("/home/kumara3/Read_simulator/input_data/errormodel-218bp.mconf",'r')
        print self.error_model
        
    '''
    start the simulation code
    
    '''
    def simulate(self,output_file):
     
        if not self.readlength == 200:
            raise ValueError ("Read length should be 200 bp.")
        
        output_dir = tempfile.mkdtemp()
        
        subprocess.call(["MetaSim","cmd","-r","1000000","-m","-g",self.error_model,"-2",self.error_model,"--empirical-pe-probability","100","--clones-mean",str(self.mean),"--clones-param2",str(self.std),"-d","/home/kumara3/Read_simulator/output_dir","/home/kumara3/Read_simulator/input_data/lc.mprf"], stdout=open("/home/kumara3/Read_simulator/input_data/","w"))
        
        
