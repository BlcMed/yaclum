# Yet Another Command-Line Utility for Movies (YACLUM)

**YACLUM** is a simple and efficient command-line utility designed to help you organize your movie collection. It supports managing movies and their metadata (watched/unwatched status), searching for movies, and maintaining a structured directory layout based on directors and their works.

---

## Features
- **Organized Directory Structure**:
  - Automatically creates folders for directors and movies.
  - Easily move movies to the correct directory.
  
- **Metadata Management**:
  - Keeps track of movies you’ve watched or not.
  - Updates metadata dynamically when movies are added.
  
- **Search Functionality**:
  - Search movies by name (fuzzy matching included).
  - Filter movies by watched or unwatched status.

- **Cross-System Usability**:
  - Works on any Unix-like system (Linux, macOS) with minimal setup.

---

## Installation

### Prerequisites
- **Python 3.6+** is required.
- Ensure the `pip` package manager is installed.

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/yaclum.git
   cd yaclum
   ```

2. Install the utility:
   ```bash
   chmod +x install.sh
   sudo ./install.sh
   ```

3. You can now run the utility using:
   ```bash
   yaclum --help
   ```

---

## Directory Structure
Yaclum organizes your movies under a root directory. Here's an example structure:

```
movies/
├── Quentin Tarantino/
│   ├── Pulp Fiction/
│   │   ├── Pulp Fiction.mp4
│   │   ├── Pulp Fiction.srt
│   ├── Django Unchained/
│       ├── Django Unchained.mp4
├── Christopher Nolan/
│   ├── Inception/
│   │   ├── Inception.mp4
│   │   ├── Inception.srt
```

---

## Usage

### 1. **Set the Root Folder**
   Before using the utility, you must set the root folder where your movies are stored. Use the `--set-root` option to specify the root directory:
   ```bash
   yaclum --set-root /path/to/movies
   ```

### 2. **Initialize or Update Metadata**
   Populate or update the metadata file (`yaclum.json`) by scanning your directory structure for new movies:
   ```bash
   yaclum --update-metadata
   ```

### 3. **Add a Director**
   Add a folder for a new director under the root directory:
   ```bash
   yaclum --add-director "Director Name"
   ```

### 4. **Add a Movie**
   Add a folder for a new movie under an existing director:
   ```bash
   yaclum --add-movie "Director Name" "Movie Title"
   ```

### 5. **Move a Movie File**
   Move a movie file from any location to its proper folder under the specified director and movie:
   ```bash
   yaclum --move-file /path/to/movie.mp4 "Director Name" "Movie Title"
   ```

### 6. **Search for Movies**
   Search for movies by name (case-insensitive and partial matching):
   ```bash
   yaclum --search "Movie Title"
   ```

   To search for unwatched movies:
   ```bash
   yaclum --search "Movie Title" --unwatched
   ```

### 7. **Toggle Watched Status**
   Toggle the watched/unwatched status of a movie:
   ```bash
   yaclum --toggle-watched "Movie Title"
   ```

### 8. **List All Movies by Director**
   List all movies by a specific director:
   ```bash
   yaclum --list-movies
   ```

---

## Example Workflow

1. **Set the root folder** where your movies are stored:
   ```bash
   yaclum --set-root /path/to/movies
   ```

2. **Update the metadata** to add new movies:
   ```bash
   yaclum --update-metadata
   ```

3. **Move a movie** to the correct folder:
   ```bash
   yaclum --move-file /path/to/movie.mp4 "Quentin Tarantino" "Pulp Fiction"
   ```

4. **Search for movies**:
   ```bash
   yaclum --search "Pulp Fiction"
   ```

5. **Toggle watched status** of a movie:
   ```bash
   yaclum --toggle-watched "Pulp Fiction"
   ```

---

## Development

### File Structure
- `main.py`: Entry point of the application.
- `organizer.py`: Handles directory and file organization.
- `metadata.py`: Manages movie metadata (watched/unwatched status).
- `search.py`: Implements search functionality.
- `install.sh`: Automates the setup of the utility.

### Running Locally
If you prefer running without installation:
```bash
python3 main.py --help
```

---

## Contributing
Contributions are welcome! Feel free to submit issues or pull requests to improve Yaclum.

---

## License
This project is licensed under the GNU General Public License v3.0.
