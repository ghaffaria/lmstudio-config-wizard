# LM Studio Configuration Recommender

## Overview

LM Studio Configuration Recommender is a Python-based CLI tool designed to recommend optimal configuration settings for running large language models (LLMs) in LM Studio. The tool automatically detects system hardware and gathers user-defined model usage goals to generate tailored recommendations. It supports cross-platform functionality (macOS, Linux, and Windows).

## Features

- **Automatic Hardware Detection**: Detects CPU, RAM, GPU, and GPU memory.

- **Interactive User Input**: Guides users through selecting model details, quantization types, formats, and usage goals.

- **Tailored Recommendations**: Generates configurations based on hardware and user preferences.

- **YAML Export**: Saves recommended configurations to YAML files with dynamic filenames.

- **Cross-Platform Support**: Works seamlessly on macOS, Linux, and Windows.

## Project Structure

```plaintext
├── cli.py                # Main entry point for the CLI tool
├── hardware_utils.py     # Hardware detection logic
├── model_profile.py      # Interactive user input for model details
├── recommender.py        # Recommendation logic
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
├── output/               # Directory for exported YAML configurations
├── templates/            # YAML configuration templates
```

## How to Use

### Setup

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/ghaffaria/lmstudio-config-wizard.git
   cd lmstudio-config-wizard
   ```

2. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

### Run the Tool

To start the CLI tool:

```bash
python cli.py
```

### Example Commands

- Export configuration to YAML:

  ```bash
  python --export output/lmstudio_config.yaml
  ```

## Example Use Cases

1. **Creative Writing**:

   - Select "Creative" as the usage goal to optimize for storytelling and brainstorming.

2. **Coding Assistance**:

   - Choose "Coding" as the use case to tailor configurations for code generation.

3. **Chatbot Development**:

   - Set "Natural Dialogue" as the goal for conversational AI.

## Roadmap

- **Validation Enhancements**: Improve edge case handling for hardware detection.

- **Advanced Recommendations**: Incorporate additional parameters for fine-tuning.

- **GUI Version**: Develop a graphical interface for easier interaction.

- **Cloud Integration**: Enable cloud-based configuration generation.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.

2. Create a new branch for your feature or bug fix.

3. Submit a pull request with a detailed description of changes.

## Maintainers

- [Alireza Ghaffari](https://github.com/ghaffaria)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
