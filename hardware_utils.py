import platform
import psutil
import subprocess
from rich.console import Console
from rich.table import Table
import re


def get_gpu_info():
    system = platform.system()
    gpu_name = "Unknown"
    gpu_memory = "Unknown"

    try:
        if system == "Darwin":  # macOS
            output = subprocess.check_output(
                ["system_profiler", "SPDisplaysDataType"],
                stderr=subprocess.DEVNULL
            ).decode()

            current_gpu = None
            for line in output.splitlines():
                if "Chipset Model" in line or "Model" in line:
                    current_gpu = line.split(":")[1].strip()
                    gpu_name = current_gpu

                if "VRAM" in line:
                    vram_match = re.search(r"(\d+)\s?([MG]B)", line)
                    if vram_match:
                        gpu_memory = f"{vram_match.group(1)} {vram_match.group(2)}"

            # Fallback: use ioreg to estimate shared memory (in MB)
            if gpu_memory == "Unknown":
                try:
                    ioreg_out = subprocess.check_output(
                        ["ioreg", "-l"],
                        stderr=subprocess.DEVNULL
                    ).decode()

                    match = re.search(r"VRAM,Total.*?=(\d+)", ioreg_out)
                    if match:
                        mem_bytes = int(match.group(1))
                        gpu_memory = f"{round(mem_bytes / (1024 * 1024))} MB"
                except Exception:
                    pass

        elif system == "Linux":
            try:
                lspci_output = subprocess.check_output(
                    ["lspci"], stderr=subprocess.DEVNULL
                ).decode()
                for line in lspci_output.splitlines():
                    if "VGA compatible controller" in line or "3D controller" in line:
                        gpu_name = line.split(":")[2].strip()

                # Try nvidia-smi for NVIDIA GPUs
                try:
                    nvidia_output = subprocess.check_output(
                        ["nvidia-smi", "--query-gpu=memory.total", "--format=csv,nounits,noheader"],
                        stderr=subprocess.DEVNULL
                    ).decode().strip()
                    if nvidia_output:
                        gpu_memory = f"{nvidia_output} MB"
                except FileNotFoundError:
                    pass  # nvidia-smi not available

            except Exception:
                pass

        elif system == "Windows":
            try:
                output = subprocess.check_output(
                    ["wmic", "path", "win32_VideoController", "get", "Name,AdapterRAM"],
                    stderr=subprocess.DEVNULL
                ).decode()
                lines = output.strip().splitlines()[1:]
                if lines:
                    parts = lines[0].split()
                    gpu_name = " ".join(parts[:-1])
                    memory_bytes = int(parts[-1])
                    gpu_memory = f"{round(memory_bytes / 1024 / 1024)} MB"
            except Exception:
                pass

    except Exception:
        pass

    return gpu_name, gpu_memory


def get_system_info():
    cpu = platform.processor() or platform.machine()
    physical_cores = psutil.cpu_count(logical=False)
    logical_cores = psutil.cpu_count(logical=True)
    ram_gb = round(psutil.virtual_memory().total / 1024 / 1024 / 1024, 1)
    gpu_name, gpu_memory = get_gpu_info()

    return {
        "CPU": cpu,
        "Cores (Physical/Logical)": f"{physical_cores} / {logical_cores}",
        "RAM (GB)": ram_gb,
        "GPU": gpu_name,
        "GPU Memory (MB)": gpu_memory,
    }


def display_system_info():
    console = Console()
    table = Table(title="🧠 System Hardware Info", title_style="bold cyan")
    table.add_column("Component", style="bold magenta")
    table.add_column("Details", style="green")

    info = get_system_info()
    for key, value in info.items():
        table.add_row(key, str(value))

    console.print(table)

def get_hardware_profile():
    system_info = get_system_info()
    return {
        "cpu": system_info["CPU"],
        "physical_cores": system_info["Cores (Physical/Logical)"].split(" / ")[0],
        "logical_cores": system_info["Cores (Physical/Logical)"].split(" / ")[1],
        "ram_gb": system_info["RAM (GB)"],
        "gpu": system_info["GPU"],
        "gpu_memory_mb": system_info["GPU Memory (MB)"],
    }


if __name__ == "__main__":
    display_system_info()
