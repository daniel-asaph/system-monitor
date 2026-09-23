import psutil


def get_processes():
    """Retorna informações dos processos ativos."""
    processes = []

    for process in psutil.process_iter(
        ["pid", "name", "cpu_percent", "memory_percent", "num_threads", "status"]
    ):
        try:
            processes.append({
                "pid": process.info["pid"],
                "name": process.info["name"],
                "cpu_percent": process.info["cpu_percent"],
                "memory_percent": process.info["memory_percent"],
                "threads": process.info["num_threads"],
                "status": process.info["status"]
            })

        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    return processes

# print(get_processes())