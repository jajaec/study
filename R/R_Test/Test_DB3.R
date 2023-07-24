library (RODBC)

driver.name <- "{IBM DB2 ODBC DRIVER}"
db.name <- "SALPGM3"
host.name <- "AS400.IROYAL.KR"
port <- "60012"
user.name <- "CSPRO"
pwd <- "CSPRO"

#Connection String
con.text <- paste ("DRIVER =", driver.name,
                   "; Database =", db.name,
                   "; Hostname =", host.name,
                   "; Port =", port,
                   "; PROTOCOL = TCPIP",
                   "; UID =", user.name,
                   "; PWD =", pwd, sep = "")

con1 <- odbcDriverConnect (con.text)