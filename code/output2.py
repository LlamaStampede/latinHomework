def format(final_list,errors,show_errors):
    output = open("../site/output.html","w+")
    
    output.write('<!DOCTYPE html><html><head><meta charset="utf-8"><title>Analysis Sheet</title><link rel="stylesheet" type="text/css" href="style.css"></head><body><h1>Analysis Sheet</h1><div id="sheet">')
    
    for col in final_list:
        output.write("<ul>")
        for row in col:
            #if row == col[0]: row = "<span>%s</span>"%row
            output.write("<li>"+row+"</li>")
        for err in errors:
            if show_errors == "y" and col[0] == err[1]:
                output.write('<li class="error">')
                if err[0] == "unknown":
                    output.write("<p>UNKNOWN</p></li>")
                    break
                if err[0] == "multi":
                    output.write("Conflict:<ul>")
                    for possib in err[2:]:
                        output.write("<li>"+" ".join(possib)+"</li>")
                    output.write("</ul>")
                output.write("</li>")
        output.write("</ul>")
    
    output.write('<hr></div><div id="report"><ul><li>')
    for err in errors:
        if err[0] == "unknown": output.write("UNKNOWN: "+err[1])
        elif err[0] == "multi":
            output.write("Conflict: "+err[1]+" might be from:<br>")
            for w in err[2:]: #w = each individual dictionary entry
                output.write("- "+w[0]+" "+w[1]+" "+w[2]+"<br>")
        output.write("</li><li>")
    output.write('</li></ul></div></body></html>')
    output.close