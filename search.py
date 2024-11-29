from metadata import load_metadata


def search_movies(root_folder, query):
    """
    Search for movies in the metadata by movie name (partial match).

    Args:
        root_folder (str): Path to the root movies folder.
        query (str): Search term for the movie name.

    Returns:
        list: Matching movies with their directors and watched status.
    """
    metadata = load_metadata(root_folder)
    if not metadata:
        print("No metadata found. Run '--update-metadata' to initialize metadata.")
        return []

    results = []
    query_lower = query.lower()
    for director, movies in metadata.items():
        for movie, details in movies.items():
            if query_lower in movie.lower():
                results.append(
                    {
                        "movie": movie,
                        "director": director,
                        "watched": details["watched"],
                    }
                )

    return results
