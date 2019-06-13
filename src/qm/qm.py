import sys
prime_implicants =[]
combined = []


#TODO
#coverage table
#convert to class
#change doc strings 
#add GUI and terminal interfaces
def to_binary(minterms=[]):
    """
    Converts every element in minterms to its binary representation.

    Args:
        minterms: A list of minterms.

    Returns:
        A list containing the binary represenation of each minterm in minterms
    Raises:
    """

    #get the max number of digits in any minterm
    mx = len(bin(max(minterms))[2:])

    bminterms = [] #binary minterms
    for minterm in minterms:
        bstr = bin(minterm)[2:] 
        bstr = (mx - len(bstr))*'0'+bstr #append zeroes to the string 
        bminterms.append(bstr)

    return bminterms
   

def combine(min1,min2):
    """
    Combines two minterms if they differ by exactly one position.

    Args:
        min1: Binary representation of of the first minterm.
        min2: Binary represenation of the second minterm.
        

    Returns:
        A new minterm with a dash in the position where the two minterms differ or
        None if they differ by more or less than one position


    Raises:
        ValueError if minterm1 or minterm2 is not in binary format
        ValueError if both minterms are not of the same length
    """
    #get the positions where the two strings differ
    pos = [i for i in range(len(min1)) if min1[i] != min2[i]]

    if len(pos) == 1:
        i = pos[0] #i is the index of the single difference position
        return min1[:i] + '_' + min1[i+1:]

    

def combine_groups(group1=[],group2=[]):
    """
    Combines the in minterms in two groups of minterms.

    Args:
        group1: First group of minterms.
        group2: Second group of minterms.
        

    Returns:
        A dictionary {'combined': [], 'uncombined': []}
        uncombined are the minterms in the first group that failed to combine
        offspring are the results of the combination of the minterms in the first and second group


    Raises:
        ValueError if any of the minterms in any group is not in binary form
        ValueError if both minterms are not of the same length

    """
    res = []

    global prime_implicants

    #prime_implicants+=group1 + group2
    for mt1 in group1:
        has_combined = False #holds if the minterm has been able to combine atleast once
        for mt2 in group2:
            offspring = combine(mt1,mt2)
            
            if offspring:
                has_combined = True

                global combined

                combined.append(mt1)
                combined.append(mt2)

                if offspring not in res:
                    res.append(offspring)
 
    return res


def combine_generation(generation=[]):
    """
    Combines the groups in each generation.

    Args:
        generation:  A collection {} of groups to be combined
        

    Returns:
        A new generation {'new_generation' : {} , 'uncombined' : []} of groups and a 
        list of uncombined minterms in that generation

    Raises:
        ValueError if any of the minterms in the generation is not in binary form

    """
    new_gen = []
 
    for i in range(len(generation)-1):
        new_group = combine_groups(generation[i],generation[i+1])
                
        if new_group:
            new_gen.append(new_group)

    
    return new_gen

def group_minterms(mts=[]):
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
    grps = []
    num_groups = len(mts[0])

    for i in range(num_groups+1):
        grp = [x for x in mts if x.count('1')==i]

        if grp:
            grps.append(grp)

    return grps
            

def primes(mts=[]):
    gen = group_minterms(mts)
    global prime_implicants
    global combined
   
    new_gen = gen
  
    while new_gen:
        for x in new_gen:
            for y in x:
                prime_implicants.append(y)

        n = combine_generation(new_gen)
        new_gen = n
     
        
    
    

    prime_implicants = [pi for pi in prime_implicants if pi not in combined]
    



if __name__ == '__main__':
    terms = [0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    b = (to_binary(terms))
  
 

    primes(b)
  
    print(prime_implicants)
   