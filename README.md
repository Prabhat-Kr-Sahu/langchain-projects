# Qwen-4B Math Reasoning Model using GRPO

This repository contains a Colab notebook demonstrating how to fine-tune the `unsloth/Qwen3-4B-Base` model into a specialized math problem solver and reasoning agent using Generative Reranking Policy Optimization (GRPO). The project leverages the Unsloth library for efficient, high-performance training and uses a custom reward mechanism to teach the model structured reasoning.

## Project Overview

The primary goal of this project is to transform a base language model into a specialized reasoning agent capable of solving math and logic problems. The model is trained to first "think" through a problem by generating a reasoning trace, and then provide a final, clean solution.

This is achieved through a two-stage fine-tuning process:

1.  **Pre-Fine-Tuning:** A small, supervised fine-tuning (SFT) step is performed on a curated dataset to teach the model the specific chat format, including custom tags for reasoning (`<start_working_out>`, `<end_working_out>`) and solutions (`<SOLUTION>`, `</SOLUTION>`). This primes the model for the more complex GRPO stage.

2.  **GRPO Training:** The model is then trained using GRPO on a larger dataset of math problems. GRPO is a reinforcement learning-based algorithm that rewards the model for generating correct and well-formatted answers, allowing it to learn effective problem-solving policies.

## Key Features

* **Efficient Training:** Utilizes the **Unsloth** library to enable 2x faster LoRA fine-tuning with significantly less memory.
* **Advanced RL Algorithm:** Implements **GRPO** to optimize the model's generation policy based on custom rewards.
* **Structured Reasoning:** A custom chat template and reward functions are used to train the model to produce explicit "chain-of-thought" reasoning traces before giving the final answer.
* **Multi-Faceted Reward System:** The model is rewarded based on a combination of factors:
    * Correctness of the final numerical answer.
    * Adherence to the custom reasoning and solution format.
    * Proximity to the correct answer (for numerical problems).
* **Datasets:** Uses high-quality math and reasoning datasets, including `unsloth/OpenMathReasoning-mini` and `open-r1/DAPO-Math-17k-Processed`.

## How to Use

The entire process is contained within the `solver_Qwen3_(4B)_GRPO.ipynb` notebook. To run this project, you can open it directly in Google Colab.

### Steps to Run:

1.  **Installation:** The first few cells handle the installation of all necessary libraries, including `unsloth`, `vllm`, `trl`, and `transformers`. The notebook automatically detects if it's running in Colab and installs the correct dependencies.
2.  **Model Setup:** The notebook initializes the `Qwen3-4B-Base` model using Unsloth's `FastLanguageModel` class and prepares it for LoRA training.
3.  **Pre-Fine-Tuning:** The model is first trained with a standard `SFTTrainer` on a small, formatted dataset to learn the custom chat structure. This significantly speeds up the subsequent GRPO step.
4.  **GRPO Data Preparation:** The main dataset (`DAPO-Math-17k-Processed`) is loaded and formatted for the GRPO trainer. Custom reward functions are defined to evaluate the model's generations.
5.  **GRPO Training:** The `GRPOTrainer` is configured and launched. During this phase, the model generates multiple possible solutions (`num_generations`), which are then scored by the reward functions to update the model's policy.
6.  **Inference:** After training, the notebook demonstrates how to load the trained LoRA adapter and run inference to solve new math problems.
7.  **Saving the Model:** The final cells provide code to save the trained LoRA adapters locally or push them to the Hugging Face Hub.

## Results

After a short training run (100 steps), the model demonstrates a clear ability to follow the custom reasoning format and shows improved accuracy in solving math problems compared to the base model. While not always perfect, the GRPO-trained model is significantly better at structuring its thoughts and arriving at correct numerical answers. Longer training runs would further enhance its capabilities.
