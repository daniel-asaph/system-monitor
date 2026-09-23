from app.monitor import memory
from app.monitor import cpu
from app.monitor import disk

def get_system_metrics():
    """Retorna as principais métricas do sistema."""

    return {
        "cpu": {
            "usage": cpu.get_cpu_usage(),
            "per_core": cpu.get_cpu_per_core(),
            "count": cpu.get_cpu_count(),
            "frequency": cpu.get_cpu_frequency()
        },
        "memory": memory.get_memory(),
        "disk": {
            "usage": disk.get_disk_usage(),
            "io": disk.get_disk_io()
        }
    }

# print(get_system_metrics())
