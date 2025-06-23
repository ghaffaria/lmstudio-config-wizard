# 🤖 LMstudio Model Config Recommender

**LMstudio Model Config Recommender** is an interactive Python tool that recommends optimal configuration settings for running Large Language Models (LLMs) inside [LM Studio](https://lmstudio.ai), tailored to your **hardware specs** and **model usage goals**.

Whether you're aiming for maximum creativity, high accuracy, or resource-efficient inference, this tool helps generate the right settings for parameters like:

- `context length`
- `batch size`
- `temperature`
- `top-k`
- `top-p`
- `repeat penalty`
- and more

---

## 🔧 Key Features

- 🧠 Auto-detects system hardware (CPU, GPU, RAM)
- 🤖 Asks user-friendly questions to infer usage intent (e.g. creativity vs. precision)
- 📊 Suggests performance-aware values for critical LLM runtime parameters
- 📝 Outputs ready-to-use YAML config for LM Studio
- 🧰 Works across macOS, Linux, and Windows

---

## 📂 Project Structure

```plaintext
LMstudio-model-config-recommender/
│
├── cli.py                  # Command-line interface
├── hardware\_utils.py       # Detect system specs
├── model\_profile.py        # Ask for usage preferences
├── recommender.py          # Generate config from inputs
├── templates/              # Output YAML templates
├── output/                 # Generated configs
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

---

## 🚀 How to Use

### 1. Set up the environment

```bash
git clone https://github.com/your-username/LMstudio-model-config-recommender.git
cd LMstudio-model-config-recommender

python -m venv venv
source venv/bin/activate   # or use venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### 2. Run the tool

```bash
python cli.py --export output/lmstudio_config.yaml
```

You’ll be guided through:

- detecting your hardware (CPU, RAM, GPU)
- choosing your model or upload path
- expressing your intent (e.g. “I need creative writing” or “I care about precision”)

💾 Your recommended configuration will be saved to `output/lmstudio_config.yaml`

---

## 💡 Example Use Cases

- "I want to run **Mistral-7B** on my **16GB RAM MacBook** — what’s the right context size?"
- "I'm prioritizing **accuracy** over speed — what settings should I change?"
- "How do I configure **temperature** or **top-p** for **creative content generation**?"

This tool takes the guesswork out of configuring models and adapts to your local resources.

---

## 📈 Roadmap

- [x] Cross-platform support (Linux/macOS/Windows)
- [x] Basic interactive CLI
- [x] Hardware auto-detection
- [ ] GUI using `streamlit` or `textual`
- [ ] Config preview before export
- [ ] Model library with presets (e.g. LLaMA 3, Mistral, Gemma, Mixtral)

---

## 🤝 Contributing

We welcome PRs and suggestions!
To contribute:

1. Fork the repo
2. Create a new branch
3. Submit your pull request

A `CONTRIBUTING.md` guide will be added soon.

---

## 🧑‍💻 Maintainers

Developed by [@ghaffaria](https://github.com/ghaffaria).
Inspired by the challenges of configuring local LLMs properly.

---

## 📄 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
