import questionary


def ask_model_profile():
    print("\n📦 Let's configure your LLM model profile based on your needs:\n")

    model_name = questionary.text(
        "🤖 What is the name of your model (e.g., llama3, mythomax, nous-hermes)?"
    ).ask()

    # Update model size question to use grouped ranges
    model_size = questionary.select(
        "📏 What is the size of the model?",
        choices=[
            "Under 2 GB",
            "2-4 GB",
            "4-8 GB",
            "8-13 GB",
            "More than 13 GB",
            "Other",
        ],
    ).ask()

    quantization = questionary.select(
        "🔢 What quantization type is the model?",
        choices=["Q4_K_M", "Q4_K_S", "Q5_K_M", "Q6_K", "FP16", "Other"],
    ).ask()

    format = questionary.select(
        "📂 What format is the model?",
        choices=["GGUF", "GGML", "HF (transformers)", "Other"],
    ).ask()

    language = questionary.select(
        "🈯 What is the primary language of the model?",
        choices=["English", "Multilingual", "Persian (فارسی)", "Code", "Other"],
    ).ask()

    use_case = questionary.select(
        "🎯 What is your intended use case?",
        choices=["RAG (Retrieval Augmented Generation)", "Creative Writing", "Coding", "Chatbot/Assistant", "Translation", "Other"],
    ).ask()

    print("\n🛠️ Now let’s fine-tune the generation behavior based on your goals:\n")

    goal = questionary.select(
        "🎨 What is more important for your task?",
        choices=[
            "💡 Creativity (storytelling, brainstorming, poetry)",
            "🎯 Accuracy (technical answers, documentation)",
            "🗣️ Natural Dialogue (chatbots)",
            "🔍 Factual Recall (retrieval QA)",
            "⚙️ Balanced/general purpose",
        ],
    ).ask()

    # Suggest values based on goal
    config = {
        "temperature": 0.7,
        "top_p": 0.9,
        "top_k": 40,
        "repeat_penalty": 1.1,
        "max_tokens": 1024,
    }

    if "Creativity" in goal:
        config.update({"temperature": 1.0, "top_p": 0.95, "top_k": 100})
    elif "Accuracy" in goal:
        config.update({"temperature": 0.3, "top_p": 0.85, "top_k": 50})
    elif "Natural Dialogue" in goal:
        config.update({"temperature": 0.7, "top_p": 0.9, "top_k": 40})
    elif "Factual Recall" in goal:
        config.update({"temperature": 0.4, "top_p": 0.8, "top_k": 30})
    elif "Balanced" in goal:
        config.update({"temperature": 0.7, "top_p": 0.9, "top_k": 40})

    print("\n📋 Suggested inference configuration based on your goal:")
    print(f" - temperature: {config['temperature']}")
    print(f" - top_p: {config['top_p']}")
    print(f" - top_k: {config['top_k']}")
    print(f" - repeat_penalty: {config['repeat_penalty']}")
    print(f" - max_tokens: {config['max_tokens']}")

    return {
        "model_name": model_name,
        "model_size": model_size,
        "quantization": quantization,
        "format": format,
        "language": language,
        "use_case": use_case,
        "goal": goal,
        "generation_settings": config,
    }


if __name__ == "__main__":
    profile = ask_model_profile()