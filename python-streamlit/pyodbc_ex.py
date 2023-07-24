import pyodbc

# 서버 주소(DB 접속ip)
server = "서버 주소"

# 접속 유저
user = "CSPRO"

# 패스워드
pasword = "CSPRO"

# 데이터베이스명
db = "as400"

cnxn = pyodbc.connect("Driver={iSeries Access ODBC Driver};System=AS400.IROYAL.KR;char_set=UTF-8;uid=" + user + ";pwd=" + pasword + ";DATABASE=" + db)
cursor = cnxn.cursor()

sql =  '''SELECT * FROM SALPGM3.B2CMBR WHERE MEMBER_SEQ = 1266'''
res =  cursor.execute(sql)
row = cursor.fetchone() 
while row: 
    print(row[1])
    row = cursor.fetchone() # netxt data