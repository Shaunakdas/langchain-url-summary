# LangChain - URL Content Summarizer

LangChain is an open-source framework designed to facilitate the development of applications that harness the capabilities of large language models (LLMs). It can be employed for a variety of tasks such as chatbots, text summarization, data generation, code understanding, question answering, evaluation, and more. This repository showcases an application that utilizes LangChain and OpenAI to summarize the content of a given URL.

## Features

- Uses the UnstructuredURLLoader class to load URL data.
- Utilizes the load_summarize_chain chain to generate a summary.
- Employs the gpt-3.5-turbo chat model, which offers improved results and cost-effectiveness compared to the default model.
- Provides a user-friendly graphical user interface (GUI) powered by Streamlit.

## Installation

To install the repository, follow the instructions below:

1. Clone the repository:

```shell
git clone https://github.com/shaunakdas/langchain-url-summary.git
```

2. Install the required dependencies by running the following command:

```shell
pip install -r requirements.txt
```

## Usage

To utilize the application, execute the following command after installing Streamlit:

```shell
streamlit run app.py
```

This will launch the Streamlit application, allowing you to input a URL and obtain a summary of its content using LangChain and OpenAI.

## Contributing

Contributions to this project are welcome! If you encounter any issues or have suggestions for improvements, please submit an issue or a pull request.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use and modify the code according to your needs.
