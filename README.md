---

# ChatterAI: Intelligent Conversation Chatbot

ChatterAI is an advanced chatbot that leverages **Bag of Words** and **Weighted Embedding (LSTM)** techniques to predict user intents and generate responses. If the model cannot provide a suitable response, it seamlessly integrates with **ChatGPT** to ensure the user always gets a meaningful reply. This project is ideal for developers looking to build and deploy intelligent chatbots for various applications.

---

## Features

- **Dual Prediction Models**:
  - **Bag of Words**: A lightweight and fast method for intent classification.
  - **Weighted Embedding with LSTM**: A deep learning-based approach for more accurate intent prediction.
- **ChatGPT Integration**: Fallback to ChatGPT for generating responses when the model cannot provide a suitable answer.
- **Customizable Training**: Train the chatbot with your own dataset using JSON files.
- **Modular Code**: Easy-to-understand and extendable codebase for developers.

---

## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
3. [Project Structure](#project-structure)
4. [Training the Model](#training-the-model)
5. [Running the Chatbot](#running-the-chatbot)
6. [Example JSON File](#example-json-file)
7. [Contributing](#contributing)
8. [License](#license)

---

## Installation

### Prerequisites

Before running the project, ensure you have the following installed:

- Python 3.7 or higher
- Required Python libraries (listed in `requirements.txt`)

### Steps

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/sedwna/AI_Conversation.git
   cd AI_Conversation
   ```

2. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up OpenAI API (for ChatGPT)**:
   - If you want to use ChatGPT as a fallback, sign up for an API key at [OpenAI](https://openai.com/api/).
   - Add your API key to the `chatgpt.py` file.

---

## Usage

### Training the Model

1. Prepare your JSON file with intents and responses (see [Example JSON File](#example-json-file)).
2. Train the model using one of the following methods:

   - **Bag of Words**:
     ```python
     trainer_bag_of_word("intents")
     ```
   - **Weighted Embedding (LSTM)**:
     ```python
     trainer_weight("intents")
     ```

   The trained model and processed data will be saved in the `chat_bot_model` and `pkl_file` folders, respectively.

### Running the Chatbot

1. Start the chatbot using one of the following methods:

   - **Bag of Words**:
     ```python
     bag_chatbot_model("intents")
     ```
   - **Weighted Embedding (LSTM)**:
     ```python
     weight_chatbot_model("intents")
     ```

2. Interact with the chatbot in the terminal. Type your messages, and the chatbot will respond accordingly.

---

## Project Structure

```
ChatterAI/
├── json_file/               # Contains JSON files for intents and responses
├── pkl_file/                # Stores processed data (words, classes, tokenizers)
├── chat_bot_model/          # Contains trained TensorFlow models
├── nlp.py                   # NLP functions (tokenization, cleaning, etc.)
├── chatgpt.py               # Integration with ChatGPT
├── main.py                  # Main script to run the chatbot
├── requirements.txt         # List of dependencies
├── README.md                # Project documentation
└── LICENSE                  # License file
```

---

## Training the Model

### Bag of Words

The `trainer_bag_of_word` function trains a simple neural network using the Bag of Words approach. It creates a binary matrix of words and their corresponding intents.

### Weighted Embedding (LSTM)

The `trainer_weight` function trains an LSTM-based model using word embeddings. This approach is more advanced and suitable for complex datasets.

---

## Running the Chatbot

Once the model is trained, you can run the chatbot using the `bag_chatbot_model` or `weight_chatbot_model` functions. The chatbot will:
1. Predict the user's intent.
2. Generate a response based on the trained model.
3. Fall back to ChatGPT if no suitable response is found.

---

## Example JSON File

Here’s an example JSON file for defining intents and responses:

```json
{
  "intents": [
    {
      "tag": "greeting",
      "patterns": ["hello", "hi", "hey"],
      "responses": ["Hello!", "Hi there!", "Hey! How can I help you?"]
    },
    {
      "tag": "goodbye",
      "patterns": ["bye", "goodbye", "see you later"],
      "responses": ["Goodbye!", "See you later!", "Have a great day!"]
    },
    {
      "tag": "thanks",
      "patterns": ["thank you", "thanks", "appreciate it"],
      "responses": ["You're welcome!", "No problem!", "Happy to help!"]
    }
  ]
}
```

---

## Contributing

We welcome contributions to ChatterAI! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeatureName`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push your changes to your fork (`git push origin feature/YourFeatureName`).
5. Open a Pull Request.

---

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- **OpenAI** for providing the ChatGPT API.
- **TensorFlow** and **Keras** for enabling deep learning model training.
- **NLTK** for natural language processing utilities.

---

## Contact

For questions or feedback, feel free to reach out:

- **Email**: [sajaddehqan2002@gmail.com]
- **GitHub**: [[My GitHub Profile](https://github.com/sedwna)]
- **Project Repository**: [[ChatterAI GitHub Repo](https://github.com/sedwna/ChatterAI)]

---

