import os
import shutil
from metadata import update_metadata


def create_director_folder(root_folder, director_name):
    """
    Create a folder for the director if it doesn't already exist.
    Returns the path to the director's folder.
    """
    director_folder = os.path.join(root_folder, director_name)
    if not os.path.exists(director_folder):
        os.makedirs(director_folder)
        print(f"Created director folder: {director_folder}")
    else:
        print(f"Director folder already exists: {director_folder}")
    return director_folder


def create_movie_folder(director_folder, movie_name):
    """
    Create a folder for the movie under the given director's folder if it doesn't exist.
    Returns the path to the movie's folder.
    """
    movie_folder = os.path.join(director_folder, movie_name)
    if not os.path.exists(movie_folder):
        os.makedirs(movie_folder)
        print(f"Created movie folder: {movie_folder}")
    else:
        print(f"Movie folder already exists: {movie_folder}")
    return movie_folder


def move_file_to_movie_folder(root_folder, source_file, director_name, movie_name):
    """
    Move a file to the specified director and movie folder.
    Creates the folders if they don't exist.
    """
    if not os.path.exists(source_file):
        raise FileNotFoundError(f"Source file does not exist: {source_file}")

    director_folder = create_director_folder(root_folder, director_name)
    movie_folder = create_movie_folder(director_folder, movie_name)

    destination_path = os.path.join(movie_folder, os.path.basename(source_file))
    shutil.move(source_file, destination_path)
    print(f"Moved file '{source_file}' to '{destination_path}'")

    update_metadata(root_folder)
