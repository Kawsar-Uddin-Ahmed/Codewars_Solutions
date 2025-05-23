def generate_tap_grid():
    alphabet = "a b c/k d e f g h i j l m n o p q r s t u v w x y z".split()# string to list. If you
    # write this string without space then there will only two part on is 'abc' another is the rest.because of '/'"
    dictionary = {}
    row = 1
    col = 1
    for char in alphabet:
        for c in char.split("/"): # Split the string char into parts wherever there is " /",
                                # and then loop through each part . char.split("/") breaks a string like
                                # "C/K" into dictionary["C", "K"], and then loops through both so that C
                                # and K share the same tap code position.for other alphabets it will
                                # work as normal.
            dictionary[c] = (row , col)
        col+=1
        if (col>5):
            col = 1
            row+=1
    return dictionary
#print(generate_tap_grid())
def tap_code_translation(text):
    a = text.lower()
    grid = generate_tap_grid()
    result = []
    for char in a:
        #if char == ' ':
         #   result.append(" ")
          #  continue
        #if char not in grid:
         #   continue
        row , col = grid[char]
        rol_tap = "."*row
        col_tap = "."*col
        result.append(f"{rol_tap} {col_tap}")
    return ' '.join(result)


a = tap_code_translation("BREAK")
print(a)

