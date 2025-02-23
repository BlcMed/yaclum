#!/usr/bin/env python3

import os
import json
from organizer import (
    create_director_folder,
    create_movie_folder,
    move_file_to_movie_folder,
)
from metadata import update_metadata, toggle_watched_status
from search import search_movies
import argparse


CONFIG_FILE = os.path.expanduser("~/.config/yaclum.conf")


def load_config():
    """Load configuration from file."""
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    return {}


def save_config(config):
    """Save configuration to file."""
    os.makedirs(os.path.dirname(CONFIG_FILE), exist_ok=True)
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f)


def set_root_folder(path):
    """Set the root movie folder."""
    config = load_config()
    config["root_folder"] = path
    save_config(config)
    print(f"Root folder set to: {path}")


def get_root_folder():
    """Get the root movie folder."""
    config = load_config()
    return config.get("root_folder")


def main():

    parser = argparse.ArgumentParser(description="Yaclum: Your movie organizer CLI")
    parser.add_argument("--set-root", type=str, help="Set the root folder for movies")
    parser.add_argument(
        "--list-movies", action="store_true", help="List all movies by director"
    )
    parser.add_argument("--add-director", type=str, help="Add a director folder")
    parser.add_argument(
        "--add-movie", nargs=2, metavar=("DIRECTOR", "MOVIE"), help="Add a movie folder"
    )
    parser.add_argument(
        "--move-file",
        nargs=3,
        metavar=("SOURCE", "DIRECTOR", "MOVIE"),
        help="Move a file to the specified director and movie folder",
    )
    parser.add_argument(
        "--update-metadata",
        action="store_true",
        help="Update the metadata file by scanning the directory structure and adding new movies.",
    )
    parser.add_argument(
        "--search",
        metavar="QUERY",
        help="Search for movies by name (case-insensitive, partial match).",
    )
    parser.add_argument(
        "--toggle-watched",
        metavar="MOVIE_NAME",
        help="Toggle the watched/unwatched status of a movie in the metadata.",
    )

    args = parser.parse_args()

    if args.set_root:
        set_root_folder(args.set_root)

    elif args.update_metadata:
        root = get_root_folder()
        if not root:
            print("Root folder is not set. Use '--set-root <path>' to set it.")
            return
        if not os.path.exists(root):
            print(f"Root folder '{root}' does not exist.")
            return

        update_metadata(root)

    elif args.list_movies:
        root = get_root_folder()
        if not root:
            print("Root folder is not set. Use '--set-root <path>' to set it.")
            return
        if not os.path.exists(root):
            print(f"Root folder '{root}' does not exist.")
            return

        print(f"Listing movies in root folder: {root}\n")
        for director in sorted(os.listdir(root)):
            director_path = os.path.join(root, director)
            if os.path.isdir(director_path):
                print(f"Director: {director}")
                for movie in sorted(os.listdir(director_path)):
                    movie_path = os.path.join(director_path, movie)
                    if os.path.isdir(movie_path):
                        print(f"  - {movie}")
                print()

    elif args.add_director:
        root = get_root_folder()
        if not root:
            print("Root folder is not set. Use '--set-root <path>' to set it.")
            return
        create_director_folder(root, args.add_director)

    elif args.add_movie:
        root = get_root_folder()
        if not root:
            print("Root folder is not set. Use '--set-root <path>' to set it.")
            return
        director, movie = args.add_movie
        director_folder = create_director_folder(root, director)
        create_movie_folder(director_folder, movie)

    elif args.move_file:
        root = get_root_folder()
        if not root:
            print("Root folder is not set. Use '--set-root <path>' to set it.")
            return

        source, director, movie = args.move_file
        try:
            move_file_to_movie_folder(root, source, director, movie)
        except FileNotFoundError as e:
            print(e)

    elif args.toggle_watched:
        root = get_root_folder()
        if not root:
            print("Root folder is not set. Use '--set-root <path>' to set it.")
            return
        if not os.path.exists(root):
            print(f"Root folder '{root}' does not exist.")
            return
        toggle_watched_status(root, args.toggle_watched)

    elif args.search:
        root = get_root_folder()
        if not root:
            print("Root folder is not set. Use '--set-root <path>' to set it.")
            return
        if not os.path.exists(root):
            print(f"Root folder '{root}' does not exist.")
            return
        results = search_movies(root, args.search)
        if results:
            print(f"Search results for '{args.search}':")
            for result in results:
                watched_status = "Watched" if result["watched"] else "Unwatched"
                print(
                    f"  - {result['movie']} (Director: {result['director']}, {watched_status})"
                )
        else:
            print(f"No results found for '{args.search}'.")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
