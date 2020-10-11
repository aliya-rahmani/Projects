import itertools
import random


class Minesweeper():
    """
    Minesweeper game representation
    """

    def __init__(self, height=8, width=8, mines=8):

        # Set initial width, height, and number of mines
        self.height = height
        self.width = width
        self.mines = set()

        # Initialize an empty field with no mines
        self.board = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(False)
            self.board.append(row)

        # Add mines randomly
        while len(self.mines) != mines:
            i = random.randrange(height)
            j = random.randrange(width)
            if not self.board[i][j]:
                self.mines.add((i, j))
                self.board[i][j] = True

        # At first, player has found no mines
        self.mines_found = set()

    def print(self):
        """
        Prints a text-based representation
        of where mines are located.
        """
        for i in range(self.height):
            print("--" * self.width + "-")
            for j in range(self.width):
                if self.board[i][j]:
                    print("|X", end="")
                else:
                    print("| ", end="")
            print("|")
        print("--" * self.width + "-")

    def is_mine(self, cell):
        i, j = cell
        return self.board[i][j]

    def nearby_mines(self, cell):
        """
        Returns the number of mines that are
        within one row and column of a given cell,
        not including the cell itself.
        """

        # Keep count of nearby mines
        count = 0

        # Loop over all cells within one row and column
        for i in range(cell[0] - 1, cell[0] + 2):
            for j in range(cell[1] - 1, cell[1] + 2):

                # Ignore the cell itself
                if (i, j) == cell:
                    continue

                # Update count if cell in bounds and is mine
                if 0 <= i < self.height and 0 <= j < self.width:
                    if self.board[i][j]:
                        count += 1

        return count

    def won(self):
        """
        Checks if all mines have been flagged.
        """
        return self.mines_found == self.mines


class Sentence():
    """
    Logical statement about a Minesweeper game
    A sentence consists of a set of board cells,
    and a count of the number of those cells which are mines.
    """

    def __init__(self, cells, count):
        self.cells = set(cells)
        self.count = count

    def __eq__(self, other):
        return self.cells == other.cells and self.count == other.count

    def __str__(self):
        return f"{self.cells} = {self.count}"

    def known_mines(self):
        """
        Returns the set of all cells in self.cells known to be mines.
        """
        if len(self.cells)== self.count:
            return self.cells
        else:
            return None
        

    def known_safes(self):
        """
        Returns the set of all cells in self.cells known to be safe.
        """
        if self.count==0:
            return self.cells
        else:
            return None
    

    def mark_mine(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be a mine.
        """
        try:
            self.cells.remove(cell)
            self.count = self.count -1
        except:
            pass
    def mark_safe(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be safe.
        """
        try:
            self.cells.remove(cell)
        except:
            pass


class MinesweeperAI():
    """
    Minesweeper game player
    """

    def __init__(self, height=8, width=8):

        # Set initial height and width
        self.height = height
        self.width = width

        # Keep track of which cells have been clicked on
        self.moves_made = set()

        # Keep track of cells known to be safe or mines
        self.mines = set()
        self.safes = set()

        # List of sentences about the game known to be true
        self.knowledge = []

    def mark_mine(self, cell):
        """
        Marks a cell as a mine, and updates all knowledge
        to mark that cell as a mine as well.
        """
        self.mines.add(cell)
        for sentence in self.knowledge:
            sentence.mark_mine(cell)

    def mark_safe(self, cell):
        """
        Marks a cell as safe, and updates all knowledge
        to mark that cell as safe as well.
        """
        self.safes.add(cell)
        for sentence in self.knowledge:
            sentence.mark_safe(cell)

    def add_knowledge(self, cell, count):
        """
        Called when the Minesweeper board tells us, for a given
        safe cell, how many neighboring cells have mines in them.
        """
        #the current move is made is safe
        self.moves_made.add(cell)
        self.mark_safe(cell)
        #add a new sentece to the Knowledge base
        new_knowledge = set()
        for i in range(cell[0]-1,cell[0]+2):
            for j in range(cell[1]-1, cell[1]+2):
                if (i,j)==cell:
                    continue
                else:
                    if 0<=i<self.width and 0<=j<self.height:
                        new_knowledge.add((i,j))
        new_sentence= Sentence(cells=new_knowledge, count=count)
        
        

        #check if new_sentence contains all mines or 0 mines
        if new_sentence.known_mines() is not None:
            for cell in new_sentence.cells:
                self.mines.add(cell)
                for sentence in self.knowledge:
                    sentence.mark_mine(cell)
        elif new_sentence.known_safes() is not None:
            for cell in new_sentence.cells:
                self.safes.add(cell)
                for sentence in self.knowledge:
                    sentence.mark_safe(cell)
        else:
            self.knowledge.append(new_sentence)

            
        
        #update already existing sentences based on new cell
        for sentence in self.knowledge:
            sentence.mark_safe(cell)
        #for every sentence, check if new_knowledge is a subset of sentence.cells or vice versa.    
            if new_knowledge.issubset(sentence.cells):
                inferred_knowledge = sentence.cells - new_knowledge
                if len(inferred_knowledge)==0:
                    continue
                inferred_sentence= Sentence(inferred_knowledge,sentence.count - count)
                #if inferred sentence cell count is equal to mine count 
                #update mines in Knowledge Base and self.mines
                if inferred_sentence.known_mines() is not None:
                    for cell in inferred_sentence.cells:
                        self.mark_mine(cell)
                        for entry in self.knowledge:
                            entry.mark_mine(cell)
                else:
                #delete superset from knowledge base and add inferred knowledge
                    self.knowledge.remove(sentence)
                    self.knowledge.append(inferred_sentence)
            #vice versa part
            elif sentence.cells.issubset(new_knowledge):
                inferred_knowledge = new_knowledge - sentence.cells
                inferred_sentence = Sentence(inferred_knowledge,count- sentence.count)
                #if inferred sentence cell count is equal to mine count 
                #update mines in Knowledge Base and self.mines
                if inferred_sentence.known_mines() is not None:
                    for cell in inferred_sentence.cells:
                        self.mark_mine(cell)
                        for entry in self.knowledge:
                            entry.mark_mine(cell)
                else:
                    #delete superset from knowledge base and add inferred knowledge
                    self.knowledge.remove(sentence)
                    self.knowledge.append(inferred_sentence)





          

    def make_safe_move(self):
        """
        Returns a safe cell to choose on the Minesweeper board.
        The move must be known to be safe, and not already a move
        that has been made.

        This function may use the knowledge in self.mines, self.safes
        and self.moves_made, but should not modify any of those values.
        """
        availabe_moves= self.safes - self.moves_made
        if len(availabe_moves)!=0:
            for e in availabe_moves:
                break
            return e


        else:
            return None

    def make_random_move(self):
        """
        Returns a move to make on the Minesweeper board.
        Should choose randomly among cells that:
            1) have not already been chosen, and
            2) are not known to be mines
    
        """
        for i in range(0,8):
            for j in range(0,8):
                if (i,j) not in self.moves_made and (i,j) not in self.mines:
                    return (i,j)
        
        return None
