import sys

from crossword import *
from copy import *


class CrosswordCreator():

    def __init__(self, crossword):
        """
        Create new CSP crossword generate.
        """
        self.crossword = crossword
        self.domains = {
            var: self.crossword.words.copy()
            for var in self.crossword.variables
        }

    def letter_grid(self, assignment):
        """
        Return 2D array representing a given assignment.
        """
        letters = [
            [None for _ in range(self.crossword.width)]
            for _ in range(self.crossword.height)
        ]
        for variable, word in assignment.items():
            direction = variable.direction
            for k in range(len(word)):
                i = variable.i + (k if direction == Variable.DOWN else 0)
                j = variable.j + (k if direction == Variable.ACROSS else 0)
                letters[i][j] = word[k]
        return letters

    def print(self, assignment):
        """
        Print crossword assignment to the terminal.
        """
        letters = self.letter_grid(assignment)
        for i in range(self.crossword.height):
            for j in range(self.crossword.width):
                if self.crossword.structure[i][j]:
                    print(letters[i][j] or " ", end="")
                else:
                    print("█", end="")
            print()

    def save(self, assignment, filename):
        """
        Save crossword assignment to an image file.
        """
        from PIL import Image, ImageDraw, ImageFont
        cell_size = 100
        cell_border = 2
        interior_size = cell_size - 2 * cell_border
        letters = self.letter_grid(assignment)

        # Create a blank canvas
        img = Image.new(
            "RGBA",
            (self.crossword.width * cell_size,
             self.crossword.height * cell_size),
            "black"
        )
        font = ImageFont.truetype("assets/fonts/OpenSans-Regular.ttf", 80)
        draw = ImageDraw.Draw(img)

        for i in range(self.crossword.height):
            for j in range(self.crossword.width):

                rect = [
                    (j * cell_size + cell_border,
                     i * cell_size + cell_border),
                    ((j + 1) * cell_size - cell_border,
                     (i + 1) * cell_size - cell_border)
                ]
                if self.crossword.structure[i][j]:
                    draw.rectangle(rect, fill="white")
                    if letters[i][j]:
                        w, h = draw.textsize(letters[i][j], font=font)
                        draw.text(
                            (rect[0][0] + ((interior_size - w) / 2),
                             rect[0][1] + ((interior_size - h) / 2) - 10),
                            letters[i][j], fill="black", font=font
                        )

        img.save(filename)

    def solve(self):
        """
        Enforce node and arc consistency, and then solve the CSP.
        """
        self.enforce_node_consistency()
        self.ac3()
        return self.backtrack(dict())

    def enforce_node_consistency(self):
        #update the dictionary of variable-domains
        # such that for any word in the domain,
        # if word.length> variable.length,
        #remove it
      for var in self.domains:
          for word in self.crossword.words:
              if len(word)!= var.length:
                  self.domains[var].remove(word)


    def revise(self, x, y):
        revised = False
        remove= []
        #if they don't have any common block, there is nothing to revise
        if self.crossword.overlaps[x,y]==None:
            return revised
        else:
            intersection = self.crossword.overlaps[x,y]
            X_index= intersection[0]
            Y_index= intersection[1]
            #loops over all the words in the domain of X
            #for each word check if the letter at X_index doesn't match
            #the letter at Y_index for 0some word in Y's domain
            for X_word in self.domains[x]:
                c= X_word[X_index]
                flag=0
                for Y_word in self.domains[y]:
                    if Y_word[Y_index] != c:
                        continue
                    else:
                        flag=1
                if(flag==0):
                    remove.append(X_word)
                    revised= True
        for word in remove:
            self.domains[x].remove(word)
        
        return revised


    def ac3(self, arcs=None):
        #if arcs is empty , use intial list of arcs
        if arcs==None:
            arcs= []
            for var1 in self.crossword.variables:
                for var2 in self.crossword.variables:
                    if var1== var2:
                        continue
                    else:
                        if self.crossword.overlaps[var1,var2]== None:
                            continue
                        else:
                            arcs.append((var1,var2))
        
        #rest of the logic is same for both cases
        #while stack is non empty
        while (len(arcs))!=0:
            arc= arcs.pop()
            X= arc[0]
            Y= arc[1]
            if self.revise(X,Y):
                #check if revise emptied the domain of X
                if len(self.domains[X])==0:
                    return False
                #check if current revision affected any other neighbours of X
                for neighbour in self.crossword.neighbors(X):
                    if neighbour==Y:
                        continue
                    else:
                        arcs.append((neighbour,X))
        
        return True






    def assignment_complete(self, assignment):
        return (len(assignment)== len(self.crossword.variables))

    def consistent(self, assignment):
        #parse into a list
        #for efficiency purposes 
        #i.e if X,Y is consistent , there is no need to check Y,X
        assigned= list(assignment.items())
        n= len(assigned)

        for i,kv in enumerate(assigned):
            var1= kv[0]
            #if assignemnt lenth is not equal to variable length, incorrect assignment
            if len(assignment[var1])!= var1.length:
                return False

            for j in range (i+1,n):
                var2= assigned[j][0]
                if len(assignment[var2])!= var2.length:
                    return False
                if assignment[var2]== assignment[var1]:
                    return False
                if self.crossword.overlaps[var1,var2]!= None:
                    intersection = self.crossword.overlaps[var1,var2]
                    index1= intersection[0]
                    index2= intersection[1]
                    if assignment[var1][index1]!= assignment[var2][index2]:
                        return False

        return True    


    def order_domain_values(self, var, assignment):
       #stores no of contrained values for each value in the domain of var
       number_constrained= dict()
       for value in self.domains[var]:
           count = 0
           for neighbour in self.crossword.neighbors(var):
               if neighbour in assignment:
                   continue
               else:
                    if value in self.domains[neighbour]:
                        count +=1 

           number_constrained[value] = count 

         #sort the dictionary in ascending order
       number_constrained= sorted(number_constrained,key=number_constrained.get)
       return number_constrained


    def select_unassigned_variable(self, assignment):
        #stores number of values left in the domain & degree for each unassigned variable
        result= dict()
        for var in self.crossword.variables:
            if var in assignment:
                continue
            else:
                domain_count= len(self.domains[var])
                degree_count= len(self.crossword.neighbors(var))
                result[var]= (domain_count,degree_count)

        #sort-> first by domain_count and then by degree_count
        result= sorted(result, key=result.get)
        return result[0]

    def backtrack(self, assignment):
        #if all the variables are assigned values, return assignment
        if self.assignment_complete(assignment):
            return assignment
        var= self.select_unassigned_variable(assignment)
        for value in self.order_domain_values(var,assignment):
            assigned= assignment.copy()
            assigned[var]= value
            if self.consistent(assigned):
                assignment[var]= value
                #make inferences from the new assignment
                arcs= [(neighbour,var) for neighbour in self.crossword.neighbors(var)
                       if neighbour not in assignment
                     ]
                #make a copy of domains before calling ac3 so that
                #changes to domains can be reverted if needed
                domain_copy= deepcopy(self.domains)
                if self.ac3(arcs=arcs):
                    result= self.backtrack(assignment)
                    if result!= None:
                        return result
                assignment[var].remove(value)
                self.domains= domain_copy
        return None

                 






def main():

    # Check usage
    if len(sys.argv) not in [3, 4]:
        sys.exit("Usage: python generate.py structure words [output]")

    # Parse command-line arguments
    structure = sys.argv[1]
    words = sys.argv[2]
    output = sys.argv[3] if len(sys.argv) == 4 else None

    # Generate crossword
    crossword = Crossword(structure, words)
    creator = CrosswordCreator(crossword)
    assignment = creator.solve()

    # Print result
    if assignment is None:
        print("No solution.")
    else:
        creator.print(assignment)
        if output:
            creator.save(assignment, output)


if __name__ == "__main__":
    main()
