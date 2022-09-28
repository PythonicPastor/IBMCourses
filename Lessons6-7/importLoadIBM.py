import loadIBM as ibm

df = ibm.loadData("SELECT * FROM employees",
              "rrf19314",
              "LisSXUFYqb5DxlmA",
              "ba99a9e6-d59e-4883-8fc0-d6a8c9f7a08f.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud",
              "31321")
print(df)

