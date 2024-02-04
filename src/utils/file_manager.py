import pickle

def dump_data(data, file_path: str) -> None:
    """
    Serialize and dump the data to a binary file using pickle.

    Parameters:
    - data: Any Python object to be serialized and saved.
    - file_path (str): The path to the file where data will be saved.
    """
    assert isinstance(file_path, str), "file_path must be a string"
    try:
        with open(file_path, 'wb') as file:
            pickle.dump(data, file)

    except (IOError, FileNotFoundError, PermissionError) as e:
        print(f"Error during dump_data: {e}")

def load_data_from_path(file_path: str):
    """
    Load and deserialize data from a binary file using pickle.

    Parameters:
    - file_path (str): The path to the file from which data will be loaded.

    Returns:
    - loaded_data: The deserialized data.
    """
    assert isinstance(file_path, str), "file_path must be a string"

    try:
        # Load the data from the file
        with open(file_path, 'rb') as file:
            loaded_data = pickle.load(file)
    

        return loaded_data

    except (IOError, FileNotFoundError, PermissionError, pickle.PickleError) as e:
        print(f"Error during load_data_from_path: {e}")
        return None