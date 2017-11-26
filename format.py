def flipped(block):
    table = []
    for height in block[0]:
        table.append([]) # this just appends 5 []'s
    for col in block:
        for row_id in range(len(col)):
            table[row_id].append(col[row_id])
    return table
def main(example_list):
    #example_list = [
    #[11,12,13,14,15],
    #[21,22,23,24,25],
    #[31,32,33,"mix_it_up",35],
    #[41,42,43,44,45],
    #[51,52,53,54,55],
    #[61,62,63,64,65]
    #] # This is an example list.
    # In reality we would plug in a list of anlyzed terms, something that included elements like ["bonarum","us-a-um","F-G-P","good",""] (format not final)
    #################### very intuitive ######################
    col_widths = []
    for col_id in range(len(example_list)):
        lens = [] # used for appending spaces later on
        width = 0
        for row in example_list[col_id]:
            l = len(str(row))
            lens.append(l)
            if l > width: width = l
        col_widths.append(width) #col_width = [longest length of each row segment for each column, ...]
        for row_id in range(len(example_list[col_id])):
            example_list[col_id][row_id] = str(example_list[col_id][row_id])
            for b in range(width - lens[row_id]):
                example_list[col_id][row_id] += " "
    # Used for final printing. Modifies each term to be equal length.
    # For example: [
    # "bonarum"
    # "us-a-um"
    # "F-G-P  "
    # "good   "
    # "       "]
    #for term in example_list:
        #print term
    #print col_widths
    # (debugging)

    doc_width = 140 # change this to widen or lengthen the final product
    indent = 4
    all_lines = []
    line_group = []
    for col_id in range(len(example_list)):
        if indent + col_widths[col_id] > doc_width:
            line_group.insert(0,["txt","dct","prs","trn","cmt"])
            all_lines.append(line_group) # archives old line
            indent = 4
            line_group = [] # begins new line
        line_group.append(example_list[col_id])
        indent += col_widths[col_id] + 1
    line_group.insert(0,["txt","dct","prs","trn","cmt"])
    all_lines.append(line_group)

    horizon = ""
    for i in range(doc_width):
        horizon += "-"

    for block in all_lines:
        for row in flipped(block):
            for col_id in range(len(row)):
                if col_id == len(row) - 1:
                    print row[col_id]
                else:
                    print row[col_id], "|",
        print horizon
