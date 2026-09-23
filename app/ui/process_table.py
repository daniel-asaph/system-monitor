import tkinter as tk
from tkinter import ttk


class ProcessTable:
    def __init__(self, parent):
        self.table = ttk.Treeview(
            parent,
            columns=(
                "pid",
                "name",
                "cpu",
                "memory",
                "threads"
            ),
            show="headings"
        )

        self.table.heading("pid", text="PID")
        self.table.heading("name", text="Processo")
        self.table.heading("cpu", text="CPU %")
        self.table.heading("memory", text="RAM %")
        self.table.heading("threads", text="Threads")

        self.table.pack(
            fill="both",
            expand=True
        )

    def update(self, processes):
        for item in self.table.get_children():
            self.table.delete(item)

        for process in processes:
            self.table.insert(
                "",
                "end",
                values=(
                    process["pid"],
                    process["name"],
                    f"{process['cpu_percent']:.1f}",
                    f"{process['memory_percent']:.1f}",
                    process["threads"]
                )
            )
