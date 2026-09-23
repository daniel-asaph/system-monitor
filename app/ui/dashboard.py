import tkinter as tk
from tkinter import ttk

from app.services.metrics_service import get_system_metrics
from app.services.processes_service import (
    get_all_processes,
    get_top_cpu_processes,
    get_top_memory_processes
)


class Dashboard:
    def __init__(self, root):
        self.root = root

        self.root.title("System Monitor")
        self.root.geometry("1000x650")

        self.create_widgets()
        self.update_dashboard()

    def create_widgets(self):
        # ===== CPU =====
        cpu_frame = ttk.LabelFrame(self.root, text="CPU")
        cpu_frame.pack(fill="x", padx=10, pady=10)

        self.cpu_label = ttk.Label(cpu_frame, text="CPU: 0%")
        self.cpu_label.pack(anchor="w", padx=10, pady=5)

        self.cpu_frequency_label = ttk.Label(
            cpu_frame,
            text="Frequência: 0 MHz"
        )
        self.cpu_frequency_label.pack(anchor="w", padx=10, pady=5)

        # ===== MEMÓRIA =====
        memory_frame = ttk.LabelFrame(self.root, text="Memória")
        memory_frame.pack(fill="x", padx=10, pady=10)

        self.memory_label = ttk.Label(
            memory_frame,
            text="RAM: 0%"
        )
        self.memory_label.pack(anchor="w", padx=10, pady=5)

        # ===== DISCO =====
        disk_frame = ttk.LabelFrame(self.root, text="Disco")
        disk_frame.pack(fill="x", padx=10, pady=10)

        self.disk_label = ttk.Label(
            disk_frame,
            text="Disco: 0%"
        )
        self.disk_label.pack(anchor="w", padx=10, pady=5)

        # ===== PROCESSOS =====
        process_frame = ttk.LabelFrame(
            self.root,
            text="Processos"
        )
        process_frame.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        self.process_label = ttk.Label(
            process_frame,
            text="Processos: 0"
        )
        self.process_label.pack(
            anchor="w",
            padx=10,
            pady=5
        )

        self.process_table = ttk.Treeview(
            process_frame,
            columns=(
                "pid",
                "name",
                "cpu",
                "memory",
                "threads"
            ),
            show="headings"
        )

        self.process_table.heading("pid", text="PID")
        self.process_table.heading("name", text="Processo")
        self.process_table.heading("cpu", text="CPU %")
        self.process_table.heading("memory", text="RAM %")
        self.process_table.heading("threads", text="Threads")

        self.process_table.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

    def update_dashboard(self):
        metrics = get_system_metrics()

        # CPU
        cpu = metrics["cpu"]

        self.cpu_label.config(
            text=f"CPU: {cpu['usage']:.1f}%"
        )

        frequency = cpu["frequency"]

        if frequency is not None:
            self.cpu_frequency_label.config(
                text=f"Frequência: {frequency:.0f} MHz"
            )

        # RAM
        memory = metrics["memory"]

        self.memory_label.config(
            text=f"RAM: {memory['percent']:.1f}%"
        )

        # DISCO
        disk = metrics["disk"]["usage"]

        self.disk_label.config(
            text=f"Disco: {disk['percent']:.1f}%"
        )

        # PROCESSOS
        processes = get_all_processes()

        self.process_label.config(
            text=f"Processos: {len(processes)}"
        )

        self.update_process_table(
            get_top_cpu_processes(10)
        )

        # Atualiza novamente daqui a 1 segundo
        self.root.after(
            1000,
            self.update_dashboard
        )

    def update_process_table(self, processes):
        # Limpa a tabela
        for item in self.process_table.get_children():
            self.process_table.delete(item)

        # Adiciona os novos processos
        for process in processes:
            self.process_table.insert(
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


def start_dashboard():
    root = tk.Tk()

    Dashboard(root)

    root.mainloop()
