def loadData(query,uid,pwd,host,port,db = 'BLUDB', driver = '{IBM DB2 ODBC Driver}', protocol = 'TCPIP', security = 'SSL'):
    import ibm_db
    import pandas
    import ibm_db_dbi as dbi
    dsn =(
        "DRIVER={0};"
        "DATABASE={1};"
        "HOSTNAME={2};"
        "PORT={3};"
        "PROTOCOL={4};"
        "UID ={5};"
        "PWD={6};"
        "SECURITY={7};").format(driver,db,host,port,protocol,uid,pwd,security)
    try:
        conn = ibm_db.connect(dsn, "", "")
        #print('Connected to database:', db, 'as user:', uid, 'on host:', host)
    except:
        print('')
        #print('Unable to connect:', ibm_db.conn_errormsg())
    pd_conn = dbi.Connection(conn)
    dataframe = pandas.read_sql(query, pd_conn)
    ibm_db.close(conn)
    print('Extracted to dataframe.')
    return dataframe
