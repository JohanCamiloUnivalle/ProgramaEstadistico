import tkinter as tk
import pandas as pd
from pandastable import Table, TableModel




class DataFrameTable(tk.Frame):
    def __init__(self, parent=None, df=pd.DataFrame()):
        super().__init__()
        self.parent = parent
        self.pack(fill=tk.BOTH, expand=True)
        self.table = Table(
            self, dataframe=df,
            showtoolbar=False,
            showstatusbar=True,
            editable=False)
        self.table.show()


df = pd.DataFrame({"Foo": (1, 2, 3, 4), "Bar": (7, 13, 17, 19)})
root = tk.Tk()
table = DataFrameTable(root, df)
root.mainloop()