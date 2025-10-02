import os

def get_model_spi_key():
    """
    Retrieves the model's SPI key from a file.
    """
    key_file_path = os.path.join(os.path.dirname(__file__), "spi_key.txt")
    try:
        with open(key_file_path, "r") as f:
            spi_key = f.readline().strip()
        if not spi_key:
            raise ValueError(f"SPI key file '{key_file_path}' is empty.")
        return spi_key
    except FileNotFoundError:
        raise ValueError(f"SPI key file '{key_file_path}' not found. Please create it and add your key.")
    except Exception as e:
        raise ValueError(f"Error reading SPI key from file '{key_file_path}': {e}")

if __name__ == "__main__":
    try:
        key = get_model_spi_key()
        print(f"Successfully retrieved model SPI key (first 5 chars): {key[:5]}...")
        # In a real application, you would now use this key to initialize your model
        # For example:
        # model = MyModel(api_key=key)
    except ValueError as e:
        print(f"Error: {e}")
        print("Please ensure 'spi_key.txt' exists in the same directory and contains your key.")

