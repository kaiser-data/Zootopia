# Zootopia (Project Masterschool Software Engineering Program)

**Zootopia** is a Python command-line application that retrieves animal information from an external API, filters the data based on user input, and generates an HTML file displaying the results.

## Features

- **Data Retrieval:** Fetches animal data using an API.
- **Filtering:** Allows filtering by characteristics like skin type.
- **HTML Generation:** Creates a structured HTML file with the fetched data.
- **Environment Configuration:** Uses `.env` for secure API key management.
- **Type Annotations:** Utilizes Python's `typing` module for better code clarity.

## Prerequisites

- **Python 3.7+**
- **pip** package manager
- **Git** (optional, for cloning the repository)

## Installation

1. **Clone the Repository**

    ```bash
    git clone https://github.com/kaiser-data/Zootopia.git
    cd Zootopia
    ```

2. **Create a Virtual Environment (Optional but Recommended)**

    ```bash
    python -m venv env
    ```

    Activate the virtual environment:

    - **On Windows:**

        ```bash
        env\Scripts\activate
        ```

    - **On macOS/Linux:**

        ```bash
        source env/bin/activate
        ```

3. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

## Configuration

1. **Set Up Environment Variables**

    Create a `.env` file in the project root:

    ```env
    API_KEY=your_api_key_here
    ```

2. **Ensure `.env` is Ignored by Git**

    Add `.env` to your `.gitignore`:

    ```gitignore
    .env
    ```

## Usage

Run the main script:

```bash
python3 animals_web_generator
```

**Steps:**

1. **Enter Animal Name:** Input the name of the animal you want information about.
2. **View Skin Types:** The script displays available skin types.
3. **Filter (Optional):** Choose a skin type to filter the results.
4. **Generate HTML:** An `animals.html` file is created with the fetched data.

## Project Structure

```
Zootopia/
├── data_fetcher.py          # Module to fetch data from the API
├── animals_template.html    # HTML template with a placeholder
├── animals.html             # Generated HTML file
├── animals_web_generator.py # Main Python script
├── requirements.txt         # Python dependencies
├── .env                     # Environment variables (not committed)
├── README.md                # Project documentation
└── .gitignore               # Git ignore rules
```

## Dependencies

- **[requests](https://pypi.org/project/requests/):** For making HTTP requests.
- **[python-dotenv](https://pypi.org/project/python-dotenv/):** To load environment variables from `.env`.
- **[typing](https://pypi.org/project/typing/):** Provides type hints (included in Python 3.7+, not needed to install separately).

*Example `requirements.txt`:*

```plaintext
requests==2.32.3
python-dotenv==1.0.1
```

## Contributing

1. **Fork the Repository**
2. **Create a Feature Branch**

    ```bash
    git checkout -b feature/YourFeature
    ```

3. **Commit Your Changes**

    ```bash
    git commit -m "Add Your Feature"
    ```

4. **Push to Your Fork**

    ```bash
    git push origin feature/YourFeature
    ```

5. **Open a Pull Request**

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For questions or support, contact [martinkaiser.bln@gmail.com](mailto:your.email@example.com).


