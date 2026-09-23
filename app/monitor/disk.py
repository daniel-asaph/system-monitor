import psutil


def get_disk_usage(path="\\"):
    """Retorna informações sobre o espaço disponível no disco."""
    disk = psutil.disk_usage(path)

    return {
        "total": disk.total,
        "used": disk.used,
        "free": disk.free,
        "percent": disk.percent
    }


def get_disk_io():
    """Retorna informações de leitura e escrita do disco."""
    disk = psutil.disk_io_counters()

    return {
        "read_bytes": disk.read_bytes,
        "write_bytes": disk.write_bytes
    }

# print(get_disk_usage())
# print(get_disk_io())
