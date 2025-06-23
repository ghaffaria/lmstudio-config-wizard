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

    # Refactor `recommend_settings` to handle quantization and model size more cleanly
    # Extract logic for model size recommendations
    model_size = model_profile.get("model_size", "Other")
    size_recommendations = {
        "Under 2 GB": {"batch_size": 64, "context_length": 1024},
        "2-4 GB": {"batch_size": 128, "context_length": 2048},
        "4-8 GB": {"batch_size": 256, "context_length": 4096},
        "8-13 GB": {"batch_size": 512, "context_length": 8192},
        "More than 13 GB": {"batch_size": 1024, "context_length": 16384},
        "Other": {"batch_size": 128, "context_length": 2048},
    }

    size_config = size_recommendations.get(model_size, size_recommendations["Other"])

    # Extract logic for quantization recommendations
    quantization = model_profile.get("quantization", "Other")
    quantization_recommendations = {
        "Q4_K_M": {"gpu_offload": 1},
        "Q4_K_S": {"gpu_offload": 1},
        "Q8_0": {"gpu_offload": 2},
        "4bit": {"gpu_offload": 0},
        "Q3_K_M": {"gpu_offload": 0},
        "Other": {"gpu_offload": 0},
    }

    quantization_config = quantization_recommendations.get(quantization, quantization_recommendations["Other"])

    # Update final config assembly
    config.update(size_config)
    config.update(quantization_config)

    return config
