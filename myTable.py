from prettytable import PrettyTable
# Specify the Column Names while initialling the Table
myTable = PrettyTable(["Student Name", "Class", "Section", "Percentage"])
# Add rows
myTable.add_row(["Leanord", "X", "B", "91.2 %"])
myTable.add_row(["Tomy", "X", "C", "63.5 %"])
myTable.add_row(["Raij", "X", "A", "90.23 %"])
myTable.add_row(["Howard", "X", "D", "92.7 %"])
myTable.add_row(["Penny", "X", "C", "88.1 %"])
myTable.add_row(["Amy", "X", "B", "95.0 %"])
print(myTable)