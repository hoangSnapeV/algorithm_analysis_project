import random

class Operators():

    # OnWall Ineffective Colision
    def OnWall (self,molecule):
        m = molecule[:]
        i = random.randint(0, len(molecule)-1)
        j = random.randint(0, len(molecule)-1)

        if (molecule[i] + j <= len(molecule)):
            m[i] = molecule[i] + j
        else:
            if(molecule[i]>j):
                m[i] = molecule[i] - j
            else:
                m[i] =  j - molecule[i]
            # Endif
        #Endif
        print(molecule)
        print(m)
        return m

    # Intermolecular Ineffective Colision
    def Intermolecular(self,molecule1, molecule2):
        
        length1 = len(molecule1)
        length2 = len(molecule2)
    
        #first crossover
        m1 = list(range(length1))
        m2 = list(range(length2))
        #second crossover
        m11 = [0] * length1
        m22 = [0] * length2
        
        #Random numbers x1, x2 generation
        x1 = random.randint(0, length1-2)
        x2 = random.randint(x1+1, length2-1)
    
        # Randormly choose form molecule1 or molecule2
        ## Crossover 1
        for i in range(0,length1):
            if (i<x1 or i>x2):  #if odd segments
                m1[i] = molecule1[i]
                m2[i] = molecule2[i]
            elif (i>=x1 and x2>=i): # if even segment
                m1[i] = molecule2[i]
                m2[i] = molecule1[i]
            # Endif
        # Endfor
        
        # Crossover 2
        for j in range(0,length1):
            if (j < x1):  #if odd segments
                m11[length1 - x1 + j] = m1[j]
                m22[length1 - x1 + j] = m2[j]
            elif (j>=x1 and x2>=j): # if even segment
                m11[length1 - x1 - x2 + j - 1] = m1[j]
                m22[length1 - x1 - x2 + j- 1] = m2[j]
            else:
                m11[j - x2-1] = m1[j]
                m22[j - x2-1] = m2[j]
            # Endif
        # Endfor
        return m1,m2
    
    # Decomposition
    def Decomposition(self, molecule):
        '''
        The decomposition involves randomly selecting two numbers 'a' and 'b', and then splitting the input molecule into two new molecules, 'm1' and 'm2', based on the selected numbers.

        Input:
            molecule (list): the input molecule and it represent by list

        Output:
            list: The new list.
        '''
        # Step 1: Select two numbers a and b randomly
        a = random.randint(-len(molecule), 0)
        b = random.randint(0, len(molecule))
        
        # Initialize m1 and m2
        m1 = [0] * len(molecule)
        m2 = [0] * len(molecule)

        # Step 2: Decomposition of molecule into m1
        for i in range(len(molecule)):
            if i + 1 <= -a:
                m1[len(molecule) - (-a) + i] = molecule[i]
            else:
                m1[i - (-a)] = molecule[i]

        # Step 3: Decomposition of molecule into m2
        for j in range(len(molecule)):
            if j + 1 <= len(molecule) - b:
                m2[j + b] = molecule[j]
            else:
                m2[j - len(molecule) + b] = molecule[j]
        return m1, m2

    # Synthesis
    def Synthesis(self, molecule1, molecule2):
        """
        Object: Generates a new list by combining two input lists in a way that preserves the frequency of the symbols used in each input list.

        Input:
            molecule1 (list): The first input list.
            molecule2 (list): The second input list.

        Output:
            list: The new list.
        """
        # Generate dictionaries for the frequencies of the symbols used in each input list.
        array1 = {}
        for symbol in molecule1:
            if symbol not in array1:
                array1[symbol] = 0
            array1[symbol] += 1

        array2 = {}
        for symbol in molecule2:
            if symbol not in array2:
                array2[symbol] = 0
            array2[symbol] += 1

        # Initialize the output list.
        m_prime = []

        # Iterate over the symbols in the first input list.
        for i in range(len(molecule1)):
            symbol1 = molecule1[i]
            symbol2 = molecule2[i]

            frequency_in_array1 = array1.get(symbol1, 0)
            frequency_in_array2 = array2.get(symbol2, 0)

            if frequency_in_array1 >= frequency_in_array2:
                m_prime.append(symbol1)
            # Otherwise, add the symbol from the second input list to the output list.
            else:
                m_prime.append(symbol2)

        return m_prime


# end class
#Module Tes
op = Operators()
mol = [3, 2, 0, 5, 7, 9, 5, 2, 3, 4]
mol2 = [1, 2, 4, 5, 8, 10, 0, 3, 5, 1]
m1 = [3, 1, 2, 0, 3, 0, 1, 3]
m2 = [1, 3, 0, 1, 2, 1, 3, 0]
# print(mol)
# print(mol2)
# print(m1)
# print(m2)
# print("\n")


# op.OnWall(mol)
# op.OnWall(mol2)
# op.Intermolecular(mol,mol2)

op.Decomposition(mol)

# print(op.Synthesis(m1,m2))
