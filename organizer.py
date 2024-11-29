import os
import shutil
import json


def update_metadata(root_folder):
    """
    Update the metadata file by adding any new movies from the directory structure
    without overwriting existing entries or changing their watched status.
    """
    metadata_file = os.path.join(root_folder, "yaclum.json")

    # Load existing metadata or initialize it as an empty dictionary
    if os.path.exists(metadata_file):
        with open(metadata_file, "r") as f:
            metadata = json.load(f)
        print("Loaded existing metadata.")
    else:
        metadata = {}
        print("No metadata file found. Creating a new one.")

    updated = False

    # Traverse the directory structure
    for director in os.listdir(root_folder):
        director_path = os.path.join(root_folder, director)
        if os.path.isdir(director_path):
            if director not in metadata:
                metadata[director] = {}  # Add new director
                updated = True

            for movie in os.listdir(director_path):
                movie_path = os.path.join(director_path, movie)
                if os.path.isdir(movie_path):
                    if movie not in metadata[director]:
                        metadata[director][movie] = {
                            "watched": False
                        }  # Default to unwatched
                        updated = True

    # Save updated metadata only if there are changes
    if updated:
        with open(metadata_file, "w") as f:
            json.dump(metadata, f, indent=4)
        print(f"Metadata updated and saved to {metadata_file}.")
    else:
        print("No new movies or directors to add. Metadata is already up to date.")


def load_metadata(root_folder):
    """
    Load movie metadata (watched/unwatched status).
    Returns a dictionary of metadata.
    """
    metadata_file = os.path.join(root_folder, "yaclum.json")
    if os.path.exists(metadata_file):
        with open(metadata_file, "r") as f:
            return json.load(f)
    return {}


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

    # Ensure director and movie folders exist
    director_folder = create_director_folder(root_folder, director_name)
    movie_folder = create_movie_folder(director_folder, movie_name)

    # Move the file to the movie folder
    destination_path = os.path.join(movie_folder, os.path.basename(source_file))
    shutil.move(source_file, destination_path)
    print(f"Moved file '{source_file}' to '{destination_path}'")
