def format(final_list,errors,parsing,show_errors):
    output = open("../site/output.php","w+")
    
    output.write('<!DOCTYPE html>\n<html lang="en-US">\n<head>\n<meta charset="utf-8">\n<title>Analysis Sheet</title>\n<link rel="stylesheet" type="text/css" href="sheet.css">\n</head>\n<body>\n<h1>Analysis Sheet</h1>\n<p id="Center">Center</p><input type="checkbox"><p id="Embed">Embed Errors</p><input type="checkbox"><!--<p id="Edit">Edit</p><input type="checkbox" id="EditBox">-->\n<form action="output.php" method="post" id="auto">\n<input type="submit" value="Save">\n<div id="sheet">\n')
    
    maincounter = 0
    for col in final_list:
        maincounter += 1
        output.write("<ul id='%i'><input type='checkbox'>"%(maincounter))
        rownum = 1
        for row in col:
            #if row == col[0]: row = "<span>%s</span>"%row
            name = "%i.%i"%(maincounter,rownum)
            if rownum == 1: output.write("<li><span class='rightside'>"+row+"</span></li>")
            else: output.write("<li><input type='text' name='%s' value='<?php if ($_SERVER[REQUEST_METHOD] == 'POST') {echo $_POST[%s];} else {echo %s;} ?>'></li>\n"%(name,name,'"%s"'%(row)))
            rownum += 1
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
    output.write('</li></ul></div></form></body></html>')
    output.close