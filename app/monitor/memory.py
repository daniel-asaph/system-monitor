import psutil

def get_memory():
    """Retorna informações sobre a memória RAM."""
    memory = psutil.virtual_memory()
    return {
    "total": memory.total,
    "available": memory.available,
    "used": memory.used,
    "percent": memory.percent
    }


def get_swap_memory():
    """Retorna informações sobre a memória swap."""
    swap = psutil.swap_memory()
    return {
    "total": swap.total,
    "used": swap.used,
    "free": swap.free,
    "percent": swap.percent
}

# print(get_memory())
# print(get_swap_memory())