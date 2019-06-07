
import numpy as np
import numpy.core.defchararray as np_f

#the output of this file is a list of ALL THE DISTINCT PROTEIN CHAINS present in the pdb file 
#pdb should be fed as txt file

def extract(address):
    
    
    def gen_divider(d):
        A = []
        B = []
        a = d[:,0][0]
        j = 0
        for i in range(1,len(d[:,0])):


            if a != d[:,0][i] :
                B.append(i-1)
                A.append(j)
                a = d[:,0][i]
                j = i

        A.append(j)
        B.append(len(d[:,0])-1)
        V = []
        V.append(A)
        V.append(B)
        return V
    
    
    prt_container = []
    
    
    with open( address ) as pdbfile:

        for line in pdbfile:

            if line[:6] == 'SEQRES':

                splitted_line = np.array( [str(line[11]),str(line[19:22]), 
                                         str(line[23:26]), str(line[27:30]),
                                         str( line[31:34]), str(line[35:38]),
                                         str( line[39:42]),str (line[43:46]),
                                         str (line[47:50]), str(line[51:54])] )

                prt_container.append(splitted_line)
                
                
                
    d = np.array(prt_container)            

    convert = {'A':'ALA','C':'CYS','D':"ASP",'E':'GLU',
               'F':'PHE','G':'GLY','H':'HIS','I':'ILE',
               'K':'LYS','L':'LEU','N':'ASN','M':'MET',
               'P':'PRO','Q':'GLN','R':'ARG','S':'SER',
               'T':'THR','V':'VAL','W':'TRP','Y':'TYR'}

    dummy = list(dict.fromkeys(convert))
    for i in dummy:    #to convert the array elements to 
        d =  np_f.replace(d ,convert[i], i)
        
    
    z= []
    for j,i in zip(gen_divider(d)[0],gen_divider(d)[1]):
        x = np.concatenate(d[j:i+1,1:], axis = 0)
        z.append(''.join(list(x)))
        
    return z



def main():
    return "pdb_file_extracter"   

if __name__== "__main__":
    main()
