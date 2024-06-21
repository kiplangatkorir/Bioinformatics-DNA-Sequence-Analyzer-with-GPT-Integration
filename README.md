# Bioinformatics DNA Sequence Analyzer with GPT Integration

This project demonstrates the integration of a GPT model into a bioinformatics application. Users can input DNA sequences and receive both a basic analysis and a GPT-generated analysis.

## Features
- Basic DNA sequence analysis (nucleotide counting)
- GPT model integration for advanced analysis

## Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/bioinformatics-gpt-analyzer.git
    cd bioinformatics-gpt-analyzer
    ```

2. Create and activate a virtual environment (optional but recommended):
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Set up your OpenAI API key:
    - Replace `'your_openai_api_key'` in `app/gpt_integration.py` with your actual OpenAI API key.

5. Run the application:
    ```sh
    export FLASK_APP=app
    flask run
    ```

6. Open your browser and go to `http://127.0.0.1:5000/` to use the application.

## Usage

- Enter a DNA sequence in the input form.
- Click "Analyze" to get the basic analysis and GPT-generated analysis.

## License
This project is licensed under the MIT License.
