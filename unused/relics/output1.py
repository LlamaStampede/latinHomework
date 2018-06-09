def flipped(block):
    table = []
    for height in range(5):
        table.append([]) # this just appends 5 []'s
    for col in block:
        for row_id in range(len(col)):
            table[row_id].append(col[row_id])
    return table
def format(final_list,errors,parsing,show_errors):
    ppls = []
    if not show_errors: errors = []
    col_widths = []
    for col_id in range(len(final_list)):
        lens = [] # used for appending spaces later on
        width = 0
        for row in final_list[col_id]:
            l = len(str(row))
            lens.append(l)
            if l > width: width = l
        col_widths.append(width) #col_width = [longest length of each row segment for each column, ...]
        for row_id in range(len(final_list[col_id])):
            final_list[col_id][row_id] = str(final_list[col_id][row_id])
            for b in range(width - lens[row_id]):
                final_list[col_id][row_id] += " "
    # Modifies each term to be equal length. For example: [
    # "bonarum"
    # "us-a-um"
    # "F-G-P  "
    # "good   "
    # "       "]

    doc_width = raw_input("Document Width: ")
    try:
        if doc_width == "": doc_width = 70
        elif doc_width == " ": doc_width = 182
        else: doc_width = int(doc_width)
    except:
        doc_width = 70
    indent = 6
    all_lines = []
    line_group = []
    page = []
    for col_id in range(len(final_list)):
        if indent + col_widths[col_id] > doc_width:
            line_group.insert(0,["txt","dct","prs","trn","cmt"])
            page.append(line_group) # archives old line
            indent = 6
            line_group = [] # begins new line
            if len(page) == 8:
                all_lines.append(page)
                page = []
        line_group.append(final_list[col_id])
        indent += col_widths[col_id] + 3
    line_group.insert(0,["txt","dct","prs","trn","cmt"])
    page.append(line_group)
    all_lines.append(page)

    horizon = ""
    for i in range(doc_width):
        horizon += "-"

    name = raw_input("Output file name: ")
    if name in ["","y"]: name = "output"
    output = open(name+".txt","w+")
    for pg in all_lines:
        for line_group in pg:
            for row in flipped(line_group):
                for col_id in range(len(row)):
                    output.write(row[col_id])
                    if col_id == len(row) - 1: output.write("\n")
                    else: output.write(" | ")
            output.write(horizon+"\n")
        output.write("\n\n")

    if parsing == "y":
        for ppl in ppls:
            ppl[2] = "\n" + ppl[2]
            output.write("Participle: "+": ".join(ppl)+"\n")
    if errors == "y":
        for err in report:
            if err[0] == "unknown": output.write("UNKNOWN: "+err[1]+"\n")
            elif err[0] == "multi":
                output.write("Conflict: "+err[1]+" might be from:\n")
                for w in err[2:]: #w = each individual dictionary entry
                    output.write("- "+w[0]+" "+w[1]+" "+w[2]+"\n")
    output.close()
