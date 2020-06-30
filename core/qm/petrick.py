

#read more about petrick's method here https://en.wikipedia.org/wiki/Petrick%27s_method
def multiply(t1,t2):
    """
        Multiplies (expands) two binary expressions t1 and t2 based on the distributive rule

        Args:
            t1 (str): first binary expression
            t2 (str): second binary expression

        Returns:
            A string representing the expansion of the boolean algebraic expressions


        """
    t1 = t1.split('+')
    t2 = t2.split('+')

    prod = ''
    for m in t1:
        temp = ""
        for n in t2:
         
            if t1.index(m) == len(t1)-1 and t2.index(n) == len(t2)-1:
                if m!=n:
                    temp=(temp+m+n)
                else:
                    temp += m
  
            else:
                if m!=n:
                    temp=temp + m+n+'+'
                else:
                    temp+=m+'+'
        
        prod+=temp
    
    return prod



def remove_dups(expr):
    """
        Removes duplicates from an expression 

        Args:
            expr (str): Expression to be simplified

        Returns:
            A string representing the simplified version of the expression

        """
    #removes duplicates from the expression both repeating characters and 
    #repeating terms

    #removes any duplicate terms in the expression
    expr = expr.split('+')
    
    #now remove any duplicate characters in the expression
    temp_expr = []
    for term in expr:
        # print(term)
        #allow the characters to appear in a specific order e.g abcd to allow easy comparison
        temp_term = list(term)
        temp_term.sort()

        term = ''
        for char in temp_term:
            term+= char
        
        new_term =""
        for char in term:
            if char not in new_term:
                new_term+=char
        temp_expr.append(new_term)

        #remove any repeating terms from the expression
        temp_expr = list(set(temp_expr))
    return temp_expr

def multiply_all(terms):

    prod = terms[0]
    for i in range(1,len(terms)):
        # print('terms [i] ',terms[i])
        # print('prod', prod)
        prod = (multiply(terms[i],prod))
        # print(prod)
    return prod

def reduce_expr(expr):
    """
        Reduces a boolean algebraic expression based on the identity X + XY = X

        Args:
            expr (str): representation of the boolean algebraic expression

        Returns:
            A string representing the reduced algebraic expression

        """
    reduced = True
    for term in expr:
        matches = [t for t in expr if t!=term and len(set(term).intersection(set(t))) == len(term)]
        if(matches):
            reduced = False

    if reduced:
        return expr
        
    new_expr = []
    temp_expr = expr
    for term in expr:
        #find the term that differs with it by at most one position
        matches = [t for t in expr if t!=term and len(set(term).intersection(set(t))) == len(term)]
        if(matches):
            new_expr.append(term)
            temp_expr.remove(term)
            for match in matches:
                temp_expr.remove(match)
        #if such a term is found reduce it by the rule x+ xy =x
            #remove both terms from the list and add to new expression
        #if no term is found add the term to the next expression
    expr = reduce_expr(new_expr+temp_expr)

    return expr

def min_len_terms(terms):
    """
        Finds the shortest term

        Args:
            terms: A list of terms 

        Returns:
           The terms that have the minimum length

        """

    minlen = len(min(terms,key=lambda x: len(x)))

    terms = [term for term in terms if len(term) == minlen]

    return terms

def count_literals(term):
    """
        Counts the number of literals in a term

        Args:
            term : A string containing literals
            

        Returns:
            The number of literals in term
        """

    count = 0
    for char in term:
        if char != "_":
            count+=1

    return count

def fewest_literals(terms):
    """
        Returns the terms that contain the fewest number of literals

        Args:
            terms: A list of of terms 

        Returns:
            A list of minterms with the fewest number of literals

        """

    #returns the terms with the fewest literals
    min_count = count_literals(min(terms,key=lambda x: count_literals(x)))

    min_lits = []

    for term in terms:
        if count_literals(term) == min_count:
            min_lits.append(term)
    
    return min_lits



