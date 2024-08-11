from Letter import Letter
def do_comparisons(file_variable, bst):
    """
    -------------------------------------------------------
    Retrieves every letter in file_variable from bst. Generates
    comparisons in bst objects. Each Letter object in bst contains
    the number of comparisons found by searching for that Letter
    object in file_variable.
    Use: do_comparisons(file_variable, bst)
    -------------------------------------------------------
    Parameters:
        file_variable - the already open file containing data to evaluate (file)
        bst - the binary search tree containing 26 Letter objects
            to retrieve data from (BST)
    Returns:
        None
    -------------------------------------------------------
    """

    line = file_variable.readline()
    lines = []

    while line != "":
        line = line.strip()
        lines.append(line)
        line = file_variable.readline()
    
    for line in lines:
        for letter in line:
            if letter.isalpha():
                letter = letter.upper()
                letter_obj = Letter(letter)
                bst.retrieve(letter_obj)
    
    file_variable.close()
    return



def comparison_total(bst):
    """
    -------------------------------------------------------
    Sums the comparison values of all Letter objects in bst.
    Use: total = comparison_total(bst)
    -------------------------------------------------------
    Parameters:
        bst - a binary search tree of Letter objects (BST)
    Returns:
        total - the total of all comparison fields in the bst
            Letter objects (int)
    -------------------------------------------------------
    """
    a = bst.inorder()
    total = 0
    for letter in a:
        total += letter.comparisons

    return total



def letter_table(bst):
    """
    -------------------------------------------------------
    Prints a table of letter counts for each Letter object in bst.
    Use: letter_table(bst)
    -------------------------------------------------------
    Parameters:
        bst - a binary search tree of Letter objects (BST)
    Returns:
        None
    -------------------------------------------------------
    """
    letters = bst.inorder()
    total = 0
    for letter in letters:
        total += letter.count

    print("Letter Count Table")
    print()
    print("Total Count: {:,}", format(total))
    print()
    print("Letter  Count       %")
    print("---------------------")
    for letter in letters:
        per = letter.count / total * 100
        print("{:>4s}{:>7,d}{:9.2f}%".format(letter.letter,letter.count,per))
    
    return

    