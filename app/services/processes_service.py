from app.monitor import processes


def get_all_processes():
    """Retorna todos os processos ativos."""
    return processes.get_processes()


def get_top_cpu_processes(limit=10):
    """Retorna os processos que mais utilizam CPU."""
    all_processes = processes.get_processes()

    return sorted(
        all_processes,
        key=lambda process: process["cpu_percent"],
        reverse=True
    )[:limit]


def get_top_memory_processes(limit=10):
    """Retorna os processos que mais utilizam memória."""
    all_processes = processes.get_processes()

    return sorted(
        all_processes,
        key=lambda process: process["memory_percent"],
        reverse=True
    )[:limit]

# print(get_all_processes())