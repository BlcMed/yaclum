import json
import os


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


def save_metadata(root_folder, metadata):
    metadata_file = os.path.join(root_folder, "yaclum.json")
    with open(metadata_file, "w") as f:
        json.dump(metadata, f, indent=4)
        print("Metadata updated successfully.")


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
                metadata[director] = {}
                updated = True

            for movie in os.listdir(director_path):
                movie_path = os.path.join(director_path, movie)
                if os.path.isdir(movie_path):
                    if movie not in metadata[director]:
                        metadata[director][movie] = {"watched": False}
                        updated = True

    if updated:
        with open(metadata_file, "w") as f:
            json.dump(metadata, f, indent=4)
        print(f"Metadata updated and saved to {metadata_file}.")
    else:
        print("No new movies or directors to add. Metadata is already up to date.")


def toggle_watched_status(root_folder, movie_name):
    """
    Toggle the watched status of a movie in the metadata file.
    If the movie is currently watched, it will be marked as unwatched, and vice versa.

    Args:
        root_folder (str): Path to the root movies folder.
        movie_name (str): Name of the movie to toggle the watched status.
    """

    metadata = load_metadata(root_folder)
    if not metadata:
        print("No metadata found. Run '--update-metadata' to initialize metadata.")
        return

    movie_found = False
    for director, movies in metadata.items():
        if movie_name in movies:
            current_status = movies[movie_name]["watched"]
            new_status = not current_status  # Toggle the watched status
            metadata[director][movie_name]["watched"] = new_status
            movie_found = True
            status_text = "Watched" if new_status else "Unwatched"
            print(
                f"Movie '{movie_name}' marked as {status_text} (Director: {director})."
            )
            break

    if not movie_found:
        print(f"Movie '{movie_name}' not found in the metadata.")

    save_metadata(root_folder, metadata)
