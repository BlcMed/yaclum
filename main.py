import os
import json

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


def list_movies_by_director():
    """List all movies grouped by director."""
    root_folder = get_root_folder()
    if not root_folder:
        print("Root folder is not set. Use '--set-root <path>' to set it.")
        return

    if not os.path.exists(root_folder):
        print(f"Root folder '{root_folder}' does not exist.")
        return

    print(f"Listing movies in root folder: {root_folder}\n")
    for director in sorted(os.listdir(root_folder)):
        director_path = os.path.join(root_folder, director)
        if os.path.isdir(director_path):
            print(f"Director: {director}")
            for movie in sorted(os.listdir(director_path)):
                movie_path = os.path.join(director_path, movie)
                if os.path.isdir(movie_path):
                    print(f"  - {movie}")
            print()


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Movie Organizer CLI")
    parser.add_argument("--set-root", type=str, help="Set the root folder for movies")
    parser.add_argument(
        "--list-movies", action="store_true", help="List all movies grouped by director"
    )

    args = parser.parse_args()

    if args.set_root:
        set_root_folder(args.set_root)
    elif args.list_movies:
        list_movies_by_director()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
