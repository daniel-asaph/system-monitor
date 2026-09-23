import psutil


def get_cpu_usage():
    """Retorna o uso total da CPU em porcentagem."""
    return psutil.cpu_percent(interval=1)


def get_cpu_per_core():
    """Retorna o uso de cada núcleo lógico da CPU em porcentagem."""
    return psutil.cpu_percent(interval=1, percpu=True)


def get_cpu_count():
    """Retorna a quantidade de CPUs lógicas."""
    return psutil.cpu_count(logical=True)


def get_cpu_frequency():
    """Retorna a frequência atual da CPU em MHz."""
    frequency = psutil.cpu_freq()

    if frequency is None:
        return None

    return frequency.current

# print(get_cpu_count())
# print(get_cpu_per_core())
# print(get_cpu_usage())
# print(get_cpu_frequency())