#TODO
#change doc strings 
#Colorclass not working on windows 
#change 
import sys
from colorclass import Color, Windows
from core.qm.petrick import multiply, remove_dups, multiply_all,reduce_expr,min_len_terms,count_literals, fewest_literals
from terminaltables import AsciiTable
import string
import random


class QM:
    '''QM is the main class for that with operations for the quine mccluskey 
        circuit minimization

    Args:
        minterms (list): compulsary list of minterms
        *args: The variable arguments are used for...
        **kwargs: The keyword arguments are used for...

    Attributes:
        arg (str): This is where we store arg,
    '''

    def __init__(self,minterms,dcares=[], chars = []):

        
        #holds the procedure leading up to the solution
        #used to allow user to have the option to print the solution steos or not
        self.procedure = ""

        #ensure that elements in minterms and dont_cares
        #are all integers
        minterms = [int(x) for x in minterms]

        #ensure the dont cares are initially integers
        if dcares:
            dcares = [int(x) for x in dcares]
    

        #get the number of bits to represent each binary
        #string. number of bits is the same as that needed
        # to represent the longest binary string 


        self.nbits = len(bin(max(minterms+dcares))[2:])
        
        #convert minterms and dont cares to binary
        self.minterms =  self.to_binary(minterms)
        
        
        if dcares:
            self.dont_cares = self.to_binary(dcares)

        else:
            self.dont_cares = []

        #holds all prime implicants based on dont cares and minterms
        self.prime_implicants = []

        #holds all minterms and dont cares that have combined
        #allows easy reference accross different methods to 
        #know which minterms have or have not combined
        self.combined = []

        #holds all essential prime implicants based on minterms
        #dont cares
        self.essential_prime_implicants = []

        #coverage table used in determining essential prime implicants
        self.coverage_table = {}

        #for example x,y,z  or a,b,c etc
        #wether or not to sort chars
        self.chars = sorted(chars)


    def to_binary(self,minterms=[],nbits = 0):
        """
        Converts every element in minterms to its binary representation.

        Args:
            minterms: A list of minterms.
            nbits: is the the number of bits to be used for the representation
                    if not specided the value defaults to the len of longest 
                    binary string in list 

        Returns:
            A list containing the binary represenation of each minterm in minterms
            Each binary string nbits long

        Example:
             if minterms[]
        """
        
        
        #get the max number of digits in any minterm
        if nbits:
            mx = nbits
        else:
            mx = self.nbits

        bminterms = [] #binary minterms
        for minterm in minterms:
            # [2:]remove's 0b from the begining of the binary string 
            bstr = bin(minterm)[2:] 
            #get the difference in length (bits) between the minterm 
            #and the longest minterm and prepend zeros to fillup
            bstr = (mx - len(bstr))*'0'+bstr #append zeroes to the string 
            bminterms.append(bstr)

        return bminterms
   

    def combine(self,min1,min2):
        """
        Combines two minterms if they differ by exactly one position.

        Args:
            min1: Binary representation of of the first minterm.
            min2: Binary represenation of the second minterm.
            

        Returns:
            A new minterm with a dash in the position where the two minterms differ or
            None if they differ by more or less than one position

        """

        if len(min1) != len(min2):
            raise ValueError("Both terms vary in length")
        #get the positions where the two strings differ    
        pos = [i for i in range(len(min1)) if min1[i] != min2[i]]

        #if two terms differ by exactly 1 position return a new string with an underscore
        #in the positions in which they differ
        if len(pos) == 1:
            i = pos[0] #i is the index of the single difference position
            return min1[:i] + '_' + min1[i+1:]

        #nothing returned if both cant combined. 

    def combine_groups(self,group1=[],group2=[]):
        """
        Combines the in minterms in two groups of minterms.

        Args:
            group1: First group of minterms.
            group2: Second group of minterms.
            

        Returns:
            A dictionary {'combined': [], 'uncombined': []}
            uncombined are the minterms in the first group that failed to combine
            offspring are the results of the combination of the minterms in the first and second group

        """
        #holds the result from the combination of the two groups
        result = []


        #prime_implicants+=group1 + group2
        for mt1 in group1:
            has_combined = False #holds if the minterm has been able to combine atleast once
            for mt2 in group2:
                offspring = self.combine(mt1,mt2)
                
                #if both minterms combine add the offspring to those that have combined
                if offspring:
                    has_combined = True

                    self.combined.append(mt1)
                    self.combined.append(mt2)

                    #prevent duplicates in the results
                    if offspring not in result:
                        result.append(offspring)
    
        return result


    def combine_generation(self,generation=[]):
        """
        Combines the groups in each generation.

        Args:
            generation:  A collection [] of groups to be combined
            

        Returns:
            A new generation [] of groups 

        """
        #A  generation is defined as a collection of groups of minterms 
        # during a given stage of the minimization Ex.
        # [[0000],[0001,1000],[1100,0101,1001]] is a generation
        new_gen = []
    
        for i in range(len(generation)-1):
            new_group = self.combine_groups(generation[i],generation[i+1])
                    
            #a group may not result from the combination i.e no minterms combine
            if new_group:
                new_gen.append(new_group)

        
        return new_gen

    def group_minterms(self,mts=[]):
        """
        Groups the elements in minterms according to the number of ones in their binary representation.

        Args:
            minterms: A non empty list of minterms in binary form.

        Returns:
            A dictionary of minterms where each key represents the number of ones present in the binary
            representation and each value is a list of minterms with an equal number of ones in their 
            binary representation
            
        Raises:
        """
        #sort  the minterms for presentation purpose
        mts.sort()
        grps = []

        #maximum possible number of groups
        num_groups = len(mts[0])


        ##########################for printing to the console##################################
        table_data = [
        [Color('{autogreen}Group{/autogreen}'),Color('{autogreen}Minterms (decimal){/autogreen}'), Color('{autogreen}Minterms (binary){/autogreen}')]
        ]
        table = AsciiTable(table_data)
        table.inner_row_border = True

        self.procedure+=Color('{autoblue}==========================\nStep 1 : Grouping Minterms\n==========================\n{/autoblue}\n')
        #########################################################################################

        for i in range(num_groups+1):
            grp = [x for x in mts if x.count('1')==i]

            if grp:
                grps.append(grp)

        for i in range(len(grps)):
        ##################################for printing to the console###############################
            num_ones = grps[i][0].count('1')
            grp = grps[i]
            table_data.append([num_ones,str(int(grp[0],2)),grp[0]])
     
            for j in range(1,len(grp)):
                table.table_data[i+1][1]+="\n"+str(int(grp[j],2))
                table.table_data[i+1][2]+="\n"+grp[j]
                
        self.procedure+=str(table.table)
        ###########################################################################################

        return grps

    def pis(self):
        """
        Computes the prime implicants based on the minterms and dont cares

        Returns:
            A list containing the prime implicants 
        """
        mts = self.minterms + self.dont_cares
        new_gen = self.group_minterms(mts)
    
        #holds all the generations that are reached, used mainly for printing
        all_gens = [new_gen]
        
        #combine groups in each generation to form a new generation as long 
        #as there is offspring giving rise to a new generation
        while new_gen:
            for group in new_gen:
                for term in group:
                    #first consider all minterms in the group as potential prime implicants
                    self.prime_implicants.append(term)

            new_gen = self.combine_generation(new_gen)
            
              
            if new_gen:
                all_gens.append(new_gen)

        #filter self.prime_implicants to contain only those terms that failed to combine i.e actual prime
        #implicants
        self.prime_implicants = [pi for pi in self.prime_implicants if pi not in self.combined]
        
        #holds the table data to be stored in the procedure
        table_data = [
            []
        ]

        #add all the data for all the generations to table data to allow them to be displayed as 
        #part of the procedure

        #add the heading for each generation
        for gen in all_gens:
            i = all_gens.index(gen)

            table_data[0].append(Color('{autogreen} Stage '+str(i)+'{/autogreen}'))
            
        #add the actual data for each generation
        for gen in all_gens:
            i = all_gens.index(gen)
            for grp in gen:
                #only add rows for the first generation
                j = gen.index(grp)

                if i == 0:
                    temp = ["" for x in table_data[0]]
                    table_data.append(temp)
                
                # for subsequent generations append data to appropriate locations
                for mt in grp:
                    table_data[j+1][i]+=str(mt)+"  "

                    #add a tick to the side of all terms that combined
                    if mt in self.combined:
                        table_data[j+1][i]+=Color('{autocyan} '+u'\u2713'+'{/autocyan}')
                    #add a star to the side of all prime implicants t            
                    else:
                        table_data[j+1][i]+=Color('{autored} '+'*'+'{/autored}')

                    table_data[j+1][i]+="\n"

        table = AsciiTable(table_data)
        table.inner_row_border = True

        self.procedure+=Color('\n\n{autoblue}===========================\nStep 2 : Combining Minterms\n===========================\n{/autoblue}\n')
        #add the table with the steps to be added to procedure
        self.procedure+=table.table

        self.procedure+=Color('\n\n{autoblue} Prime Implicants {/autoblue}\n ----------------\n')
        
        #print each prime implicant alongside its character represenation if it exits
        for pi in self.prime_implicants:
            ch = ' ('+self.to_char(pi,self.chars)+') ' if self.chars else ''
            self.procedure+=('  '+pi+ch+'\n')

        return self.prime_implicants
        
            
    def can_cover(self,pi,minterm):
        """
        Checks if a prime implicant (pi) can cover the minterm

        Args:
            pi: A binary string representing the prime implicant
            minterm: A binary string representing the minterm in question

        Returns:
            A list containing all possible permutations of the prime implicant
        Raises:
        """
        #extract the minterm to also contain dashes where pi contains them 

        pos = [i for i in range(len(pi)) if pi[i]=='_']

        for i in range(len(pi)):
            if i not in pos and pi[i]!=minterm[i]:
                return False

        return True




    def primary_epis(self):
        """
        Computes the essential prime implicants based on the minterms and dont cares

        Returns:
            A list containing the essential prime implicants 
        """
        #for each minterm determine all the prime implicants that 
        #can cover it 
        for minterm in self.minterms:
            self.coverage_table[minterm] = []
            for pi in self.prime_implicants:
                if self.can_cover(pi,minterm):
                    self.coverage_table[minterm].append(pi)

        #find the prime implicants that are the only one covering any minterm
         #for printing the coverage table

        ####################################for printing to terminal#####################################
        table_data = [['']+[Color('{autogreen}'+str(int(x,2))+'{/autogreen}') for x in self.minterms]]

    
        for pi in self.prime_implicants:
            table_data.append([pi]+['' for x in self.minterms])

            for mt in self.minterms:
                if pi in self.coverage_table[mt]:
                    table_data[self.prime_implicants.index(pi)+1][self.minterms.index(mt)+1]='X'

                    if len(self.coverage_table[mt]) == 1:
                        table_data[self.prime_implicants.index(pi)+1][self.minterms.index(mt)+1]=Color('{autored}X{/autored}')

        table_data.append(['']+['' for x in self.minterms])
       
        #################################################################################################

        for minterm in self.minterms:
            if len(self.coverage_table[minterm]) == 1:
                self.essential_prime_implicants.append(self.coverage_table[minterm][0])
           
        
        #tick for the prime implicants that are covered
        for minterm in self.minterms:
            if set(self.coverage_table[minterm]).intersection(set(self.essential_prime_implicants)):
                table_data[-1][self.minterms.index(minterm)+1]=Color('{autocyan} '+u'\u2713'+'{/autocyan}')

        #filter out any prime implicants that appear twice
        self.essential_prime_implicants = list(set(self.essential_prime_implicants))

        #reduce the coverage table to include only minterms not covered by the 
        #essential prime implicants

        self.coverage_table = {k:v for k,v in self.coverage_table.items() if \
            not set(v).intersection(set(self.essential_prime_implicants))}
      
        table = AsciiTable(table_data)
        table.inner_row_border = True

        self.procedure+=Color('\n\n{autoblue}=======================\nStep 3 : Coverage Chart\n=======================\n{/autoblue}\n')
        self.procedure+=table.table

        if self.essential_prime_implicants:
            self.procedure+=Color('\n\n{autoblue} Primary Essential Prime Implicants {/autoblue}\n ----------------------------------\n')
        
            for pi in self.essential_prime_implicants:
                ch = ' ('+self.to_char(pi,self.chars)+') ' if self.chars else ''
                self.procedure+=('  '+pi + ch +'\n')
    
        return self.essential_prime_implicants

    def secondary_epis(self):
        """
        Computes the secondary essential prime implicants

        Returns:
            A list containing the secondary essential prime implicants 
        """
        #adds the secondary essential prime implicants to the epis
        #returns the other non essential prime implicants necessary to  complete the coverage table
        #uses petricks method for computation

        #TODO
        #Modify algorithm from petrick section to be more robust 
        #currently limited by mapvals


        #holds possible map values the bit strings e.g 10_1 to be characters 
        #petrick's method is then applied to the the character representation
        #For a better visualization view https://en.wikipedia.org/wiki/Petrick%27s_method
        mapvals = list(string.ascii_letters + string.digits)
        
        mapped = []#already mapped bit strings
        charmap = {}#structure that holds maps
        prod = [] #product or result from petrick algoirthm

        for mterm in self.coverage_table:
            strrep = ""
            for t in self.coverage_table[mterm]:
                #map it to a character 
                if t not in mapped:
                    ch= random.choice(mapvals)
                    charmap[ch] = t
                    mapped.append(t)
                    mapvals.remove(ch)
                else:
                    for key in charmap:
                        if t in charmap[key]:
                            ch = key

                #add the corresponding character to a list
               # c = [x for x in mapped if t in self.coverage_table[x]][0]
                if t == self.coverage_table[mterm][-1]:
                    strrep+=ch

                else:
                    strrep+=ch+'+'
            prod.append(strrep)

        # print('prime implicants',self.prime_implicants)
        # print('essential prime implicants ',self.essential_prime_implicants)
        
        new_prod = []

        #if there is a need to compute secondary essential prime implicants 
        if prod:
            #use petrick's method for minimizaition
            prod = multiply_all(prod)

            prod = remove_dups(prod)
            
            prod = (reduce_expr(prod))
      
            prod = min_len_terms(prod)
        
            prod = fewest_literals(prod)
       
            for t in prod:
                tempstr = ""
                for s in t:
                    ch = self.to_char(charmap[s],self.chars) if self.chars else charmap[s]
                    if s == t[-1]:
                        tempstr+= ch
                    else:
                        tempstr+=ch+' + '
                new_prod.append(tempstr)

            #convertback
        return new_prod

    def minimize(self):
        """
        Minimizes the circuit and returns the list of terms for minimized circuit

        Returns:
            A list containing all possible solutions to the minimization problem
        """

        #actual process of minimization

        #find the prime implicants
        pis = self.pis()

        #essential prime implicant portion of the solution
        essential_pi_sol = ""

        primary_epis = self.primary_epis()

        for pi in primary_epis:
            #if the user specified variables e.g a,b,c,d then make the solution
            #in terms of this
            ch = self.to_char(pi,self.chars) if self.chars else pi

            #don't add a + to the end if this is the las pi in the list
            #e.g [ab,cd,dg] don't add a + to the end of dg as in ab + cd +dg +
            if pi == primary_epis[-1]:
                essential_pi_sol+=ch
            else:
                essential_pi_sol+=ch+' + '
        
        #compute the part of the solution that should come from the secondary essential prime
        #implicants
        secondary_epi_sols = self.secondary_epis()
        possible_solutions = []

        if secondary_epi_sols:
            for spi in secondary_epi_sols:
                if essential_pi_sol:
                    #combine each possible solution due to secondary essential
                    #prime implicants with that from primary essential prime
                    #implicants 
                    possible_solutions.append(essential_pi_sol+' + '+spi)
                else:
                    possible_solutions.append(spi)
        else:
            possible_solutions.append(essential_pi_sol)

        self.procedure+=Color('\n\n{autoblue}========\nSolution \n========\n{/autoblue}\n')
        self.procedure+=possible_solutions[0]+'\n'

        if len(possible_solutions) > 1:
            self.procedure+=Color('\n\n{autoblue}========================\nOther Possible Solutions \n========================\n{/autoblue}\n')
            
            for i in range(1,len(possible_solutions)):
                self.procedure+=possible_solutions[i]+'\n'

        return possible_solutions

    def to_char(self,term,chars):
        """
        Converts the binary term to its character representation

        Args:
            term : A binary string representing the prime implicant

        Returns:
            A string with the character represenation fro the string
        """

        i = 0 
        res = ''
        for ch in term:
            if ch == '1':
                res+=chars[i]

            elif ch == '0':
                res=res+chars[i]+"'"

            i+=1

        return res


    #implementation of petrick's algorithm
    