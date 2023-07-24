# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 08:17:43 2019

@author: XKJR
"""

#import ibm_db

#, "cspro", "cspro
#pconn = ibm_db.pconnect("as400.iroyal.kr", "cspro", "cspro")

#conn = ibm_db.connect("DATABASE=SALPGM3;HOSTNAME=as400.iroyal.kr;PORT=8471;PROTOCOL=TCPIP;UID=cspro;PWD=cspro;", "", "")
#ibm_db.connect("Server=as400.iroyal.kr:60000;Database=salpgm3;UID=cspro;PWD=cspro;", "", "")
#pconn = ibm_db.pconnect("as400.iroyal.kr", "cspro", "cspro")

import pyodbc

connection = pyodbc.connect(driver='{iSeries Access ODBC Driver}', system='as400', uid='cspro', pwd='cspro')

c1 = connection.cursor()

# 오프라인(임시) 회원 정보 출력
c1.execute('select * from SELPGM3.B2CMBR_OF')

for row in c1:
	print(row)

connection.close()
