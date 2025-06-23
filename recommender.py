import math

def recommend_settings(hardware_info: dict, model_profile: dict) -> dict:
    """
    Generate recommended LM Studio configuration values based on hardware and user needs.
    """
    ram_gb = hardware_info.get("RAM_GB", 8)
    cpu_cores = hardware_info.get("Cores_Logical", 4)
    gpu_name = hardware_info.get("GPU", "None")
    gpu_memory = hardware_info.get("GPU_Memory_MB", 0)

    needs = model_profile.get("usage_needs", "balanced")

    # === Context Length ===
    if ram_gb >= 32:
        context_length = 8192
    elif ram_gb >= 16:
        context_length = 4096
    else:
        context_length = 2048

    # === GPU Offload ===
    if gpu_name != "None" and gpu_memory >= 4096:
        gpu_offload = 1  # at least one layer
    else:
        gpu_offload = 0

    # === CPU Threads ===
    cpu_threads = cpu_cores

    # === Evaluation Batch Size ===
    if ram_gb >= 32:
        batch_size = 512
    elif ram_gb >= 16:
        batch_size = 256
    else:
        batch_size = 128

    # === Creativity Parameters ===
    if needs == "creative":
        temp = 0.95
        top_p = 0.95
        top_k = 100
    elif needs == "precise":
        temp = 0.2
        top_p = 0.8
        top_k = 40
    else:  # balanced
        temp = 0.7
        top_p = 0.9
        top_k = 60

    # === Other params ===
    repeat_penalty = 1.1
    max_tokens = 1024
    keep_model_in_memory = ram_gb >= 24
    flash_attention = gpu_memory >= 8192
    try_mmap = True

    # === Assemble final config ===
    config = {
        "context_length": context_length,
        "gpu_offload": gpu_offload,
        "cpu_threads": cpu_threads,
        "batch_size": batch_size,
        "temperature": temp,
        "top_p": top_p,
        "top_k": top_k,
        "repeat_penalty": repeat_penalty,
        "max_tokens": max_tokens,
        "keep_model_in_memory": keep_model_in_memory,
        "flash_attention": flash_attention,
        "try_mmap": try_mmap
    }

    # Update recommendations based on grouped model sizes
    model_size = model_profile.get("model_size", "Other")

    if model_size == "Under 2 GB":
        batch_size = 64
        context_length = 1024
    elif model_size == "2-4 GB":
        batch_size = 128
        context_length = 2048
    elif model_size == "4-8 GB":
        batch_size = 256
        context_length = 4096
    elif model_size == "8-13 GB":
        batch_size = 512
        context_length = 8192
    elif model_size == "More than 13 GB":
        batch_size = 1024
        context_length = 16384
    else:
        batch_size = 128
        context_length = 2048

    # Update final config assembly
    config.update({
        "batch_size": batch_size,
        "context_length": context_length
    })

    return config
