install.packages("odbc")
install.packages("DBI")

library("DBI")

con <- DBI::dbConnect(odbc::odbc(),
                      Driver   = "SQL Server",
                      Server   = "121.173.20.196",
                      Database = "pos",
                      UID      = rstudioapi::askForPassword("royalpos"),
                      PWD      = rstudioapi::askForPassword("royalp0s+_)("),
                      Port     = 1433)


dbListTables(con)

dbListFields(con, "B2CEMNY_OF")

res <- dbSendQuery(con, "SELECT * FROM B2CMBR_OF")
dbFetch(res)
dbClearResult(res)



#b2cemny_of <- DBI::

dbDisconnect(con)