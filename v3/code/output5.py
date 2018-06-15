def format(final_list,errors):
    afile = open("address.txt","r")
    address = afile.read()
    address = "".join(address.split(";"))
    address = "".join(address.split("\g"))
    afile.close()
    
    import pymysql
    db = pymysql.connect("127.0.0.1","tld_main","paramus","TLD_SHT")
    cursor = db.cursor()
    
    cursor.execute("""SELECT count(*)
    FROM information_schema.TABLES
    WHERE (TABLE_SCHEMA = 'TLD_SHT')
    AND (TABLE_NAME = '{0}_main');""".format(address))
    firsttime = cursor.fetchone()[0]
    if firsttime == 0:
        cursor.execute("""CREATE TABLE IF NOT EXISTS {0}_error (
            trm varchar(20) NOT NULL,
            type varchar(8) NOT NULL,
            conf1 varchar(50),
            conf2 varchar(50),
            conf3 varchar(50),
            CONSTRAINT PK_{0}_errors PRIMARY KEY (trm)
            );""".format(address))
        # If ^ doesn't work, try adding cursor.commit()
    
        cursor.execute("""CREATE TABLE IF NOT EXISTS {0}_main (
            id INT UNSIGNED AUTO_INCREMENT,
            trm varchar(20) NOT NULL,
            dct varchar(30),
            prs varchar(40),
            trn varchar(20),
            cmt varchar(20),
            CONSTRAINT PK_{0}_main PRIMARY KEY (id),
            CONSTRAINT FK_{0}_main FOREIGN KEY (trm) REFERENCES {0}_error (trm)
        );""".format(address))
    
        for err in errors: #err format: [type, term, *confs]
            insert = ""
            values = "'{0}', '{1}'".format(err[0],err[1])
            for x in range(len(err)-2):
                insert += ", conf%i" % (x+1)
                values += ", '{0}'".format(" ".join(err[x+2]))
            cursor.execute("INSERT IGNORE INTO {0}_error (type,trm{1}) VALUES ({2});".format(address,insert,values))
            db.commit() #I think this should be indented (commit after every change), but maybe not (commit after all the changes)
        for col in final_list:
            valueString = ""
            for row in col:
                valueString += "'{0}', ".format(row)
            cursor.execute("INSERT INTO {0}_main (trm,dct,prs,trn,cmt) VALUES ({1});".format(address,valueString[:-2]))
            db.commit()
    
    else: # Maybe in the future change it so that you can change the amount of words in the passage (maybe not)
        for i in range(len(final_list)):
            for j in range(5):
                col = ("trm","dct","prs","trn","cmt")[j]
                cursor.execute("SELECT {0} FROM {1}_main WHERE id={2} LIMIT 1;".format(col,address,i+1))
                result = cursor.fetchone()
                if result[0] == None:
                    cursor.execute("UPDATE {0}_main SET {1}={2} WHERE id={3} LIMIT 1;".format(address,col,final_list[i][j],i+1))
                    db.commit()
    db.close()

