def format(final_list,errors,show_errors):
    output = open("../site/output.html","w+")
    
    output.write('<!DOCTYPE html><html lang="en-US"><head><meta charset="utf-8"><title>Analysis Sheet</title><link rel="stylesheet" type="text/css" href="sheet.css"></head><body><h1>Analysis Sheet</h1><p id="Center">Center</p><input type="checkbox"><p id="Embed">Embed Errors</p><input type="checkbox"><div id="sheet">')
    
    maincounter = 0
    for col in final_list:
        maincounter += 1
        output.write("<ul id='%i'><input type='checkbox'>"%(maincounter))
        firstrow = True
        for row in col:
            #if row == col[0]: row = "<span>%s</span>"%row
            string = row
            if firstrow: string = "<span class='rightside'>" + row + "</span>"
            output.write("<li>"+string+"</li>")
            firstrow = False
        counter = 1
        for err in errors:
            if show_errors == "y" and col[0] in err and (err[0] == "unknown" or err[1] == maincounter):
                output.write('<li class="error">')
                if err[0] == "unknown":
                    output.write("<p>UNKNOWN</p></li>")
                    break
                if err[0] == "multi":
                    name = err[2] + str(counter)
                    counter += 1
                    output.write("Conflict:<ul>")
                    for possib in err[3:]:
                        output.write("<li><input type='radio' name='%s'> "%(name)+" ".join(possib)+"</li>")
                    output.write("</ul>")
                output.write("</li>")
        output.write("</ul>")
    
    output.write('<hr></div><div id="report"><ul><li>')
    report = []
    for err in errors:
        if not err in report: report.append(err)
    errors = report
    for err in errors:
        if err[0] == "unknown": output.write("UNKNOWN: "+err[1])
        elif err[0] == "multi":
            output.write("Conflict: "+err[2]+" might be from:<br>")
            for w in err[3:]: #w = each individual dictionary entry
                output.write("- %s %s %s<br>"%(w[0],w[1],w[2]))
        output.write("</li><li>")
    output.write('</li></ul></div></body></html>')
    output.close