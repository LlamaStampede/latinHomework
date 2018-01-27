def format(final_list,errors,parsing,show_errors):
    output = open("../site/sheet.txt","w+")
    
    output.write('#Info\n%s\t%s\n#Sheet\n'%(parsing,show_errors))
    
    maincounter = 0
    for col in final_list:
        maincounter += 1
        rownum = 1
        output.write("\t".join(col))
        for err in errors:
            if show_errors == "y" and col[0] in err and (err[0] == "unknown" or err[1] == maincounter):
                if err[0] == "unknown":
                    output.write("\tUNKNOWN")
                    break
                if err[0] == "multi":
                    output.write("\tConflict:")
                    for possib in err[3:]:
                        output.write("\t{"+"\t".join(possib)+"}")
                    break
        output.write("\n")
    
    output.write('#Report\n')
    report = []
    for err in errors:
        if not err in report: report.append(err)
    errors = report
    for err in errors:
        if err[0] == "unknown": output.write("UNKNOWN: %s\n"%(err[1]))
        elif err[0] == "multi":
            output.write("Conflict: "+err[2]+" might be from:\n")
            for w in err[3:]: #w = each individual dictionary entry
                output.write("- %s %s %s\n"%(w[0],w[1],w[2]))
    output.close