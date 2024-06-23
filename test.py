# import mysql.connector as mc
# import pandas as pd
#
# connection = mc.connect(username="root", passwd="Aditya2612", host="localhost", db="Analysis")
# cursor = connection.cursor()
#
# data = pd.read_sql("select* from tests", connection)["ObtainedMarks"]
# print(data)

from gui import Gui

window = Gui(1000, 800, "Home Page")
window.sidebar()
# window.home()
window.pg2()
window.mainloop()
