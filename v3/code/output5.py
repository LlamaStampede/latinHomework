def format(final_list,errors):
    afile = open("../site/address.txt","r")
    address = afile.read()
    address = "".join(address.split(";"))
    address = "".join(address.split("\g"))
    afile.close()
    
    import sys
    if 'PyMySQL' not in sys.modules: import PyMySQL
    
    db = PyMySQL.connect("127.0.0.1","tld_main","paramus","TLD_SHT")
    cursor = db.cursor()
    
    cursor.execute("""CREATE TABLE {0}_error (
        trm varchar(20) NOT NULL,
        type varchar(8) NOT NULL,
        conf1 varchar(50),
        conf2 varchar(50),
        conf3 varchar(50),
        CONSTRAINT PK_{0}_errors PRIMARY KEY (trm),
);""".format(address))
    
    cursor.execute("""CREATE TABLE {0}_main (
        id INT UNSIGNED AUTO_INCREMENT,
        trm varchar(20) NOT NULL,
        dct varchar(20),
        prs varchar(20),
        trn varchar(20),
        cmt varchar(20),
        CONSTRAINT PK_{0}_main PRIMARY KEY (id),
        CONSTRAINT FK_{0}_main FOREIGN KEY (trm) REFERENCES {0}_error (trm),
    );""".format(address))
    
    
    for err in errors: #err format: [type, term, *confs]
        insert = ""
        values = ",".join(err[:2])
        for x in range(len(err)-2):
            insert += ", conf%i" % (x+1)
            values += "," + " ".join(err[x+2])
        cursor.execute("INSERT INTO {0}_error (type,trm{1}) VALUES ({2});".format(address,insert,values))
        cursor.commit() #I think this should be indented (commit after every change), but maybe not (commit after all the changes)
    for col in final_list:
        cursor.execute("INSERT INTO {0}_main (trm,dct,prs,trn,cmt) VALUES ({1});".format(address,",".join(col)))
    
    db.close()

