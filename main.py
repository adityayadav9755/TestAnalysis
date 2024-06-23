import data
from gui import Gui

analysis = data.Database(pwd="Aditya2612", dbname="Analysis")
grph = data.Graph
window = Gui(1000, 800, "Test Analysis")
window.sidebar()
cmnd = window.pg1()
window.mainloop()

print(cmnd)
if cmnd == "graph":
    for a in [96, 300, 180]:
        mydata = analysis.read(table="Tests", fields="ObtainedMarks", where=f"TotalMarks={a}", orderby="Class")
        print(mydata)
        x = list(mydata.index)
        y = mydata['ObtainedMarks']
        grph.graph(x, y, lbl=f"{a}")
    grph.show()


# analysis.insert("Tests", {"TestName": 'Advance Test 1 P1', "Class": 'XII', "TotalMarks": 180, "ObtainedMarks": 141,
#                           "Percentage": 78, "Percentile": 99.8})
# print(analysis.read("Tests").columns)
