# Dashboard Anime

A comprehensive dashboard to analyze and visualize key statistics of your watched anime. This program calculates detailed metrics by matching your personal watch history (`works.csv`) with a historical database (`anime.csv`). It enriches your data with information such as start dates, seasons, episodes, duration, genres, and tags, presenting it all in an interactive Streamlit dashboard.

If you want to see how the dashboard will look like, head over my [personal dashboard](https://personaldashboardanime-eshawkuivkvnxkkxpyvao8.streamlit.app/) or watch this [video](https://www.youtube.com/watch?v=_RlKXeZYyIw) that shows off a bit of this program usage and installation.

> [!CAUTION]
> **Disclaimer:** This program likely will only work in a terminal environment (Linux/Unix), and surely not in Windows (unless using WSL).

## Requirements

### System Dependencies
You will need a few system tools. You can install them with your package manager (e.g., `pacman`, `apt`, `brew`).

```bash
sudo pacman -S curl figlet lolcat
```

*Note: Change `pacman` to the package manager for your distribution (e.g., `apt` for Ubuntu/Debian).*

- **curl**: Essential for downloading airin_anime.csv.
- **figlet & lolcat**: Completely optional. These are used only for the colorful greeting feature.

### Python
**Python 3** is the only essential language dependency.

## Input Data Format
The program expects an optional matching text file (default: `works.csv`) if you wish to import an existing list move your csv to data/user/.
- **Format**: A CSV file with exactly **2 columns** in this order: `title`, `type`.
  - The specific column *header names* do not matter, only the order.
- **Type Matching**: The `type` column is essential for accurate matching (e.g., distinguishing between a TV show and a Movie).
  - You can customize accepted types in `config.py` under `type_mappings` (e.g., if your CSV uses "serie" instead of "tv").
- **Optional**: This file is not required. You can start from scratch and add entries manually using the **Add work** menu option.

## Configuration (config.py)
You can customize the behavior of the application by modifying `config.py`.

### User Customization
- **`user_name`**: Change this to display your name in the Streamlit dashboard.

### File Paths & Names
You can change the location and names of your input and output files if you prefer to organize them differently:
- **User CSV**: Change `user_csv` (filename) and `path_user_csv` (full path) to point to your personal watch list.
- **Final CSV**: Change `final_csv` (filename) and `path_final_csv` (full path) if you want the processed database saved elsewhere.

### Features
You can enable or disable specific features by toggling the boolean variables:
- **`disable_file_verification`**: Set to `True` to skip the startup check for file existence (useful if you know everything is in place).
- **`show_greetings`**: Set to `True` to enable the fancy `figlet` + `lolcat` startup greeting.
- **`sort_final`**: Toggle sorting options for your final dataset (by date or title).
- **`show_unmatched`**: Controls whether you see titles that couldn't be automatically matched during synchronization.
- **`update_one_piece`**: Set to `True` if you specifically want to keep *One Piece* entries up to date (enables specific handling for this long-running series).

## Installation

1. Clone the repository.
    ```bash
    git clone https://github.com/Andres-pixel35/Anime-dashboard.git
    ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
   *Note: You only need to activate it manually **once** to install the requirements. After that, `main.sh` will automatically activate the environment for you each time you run it.*
3. Install the requirements:
   ```bash
   pip install -r requirements.txt
   ```
4. Grant execution permissions:
   ```bash
   chmod +x main.sh scripts/*.sh
   ```
   > I encourage you to check the contents of these files before granting them permissions. Always verify what you are about to execute!

## Usage

Run the main entry script:

```bash
./main.sh
```

### Menu Options
1. **Sync your csv**: Matches your personal list with the historical database to create/update the final dataset with enriched metadata.
2. **Add work**: Manually add a new anime to your final list.
3. **Remove Work**: Remove an entry from your final list.
4. **Dashboard**: Launches the Streamlit dashboard to visualize your statistics.
5. **Update Airing**: Downloads the latest airing data, cleans it, and updates the historical dataset.
6. **Update Final**: Updates airing works in your final dataset with the latest episode counts and scores.
7. **Fetch From Anilist**: Fetches missing data from the Anilist API.
8. **Exit**: Closes the application.

## Data Processing
The historical dataset (`anime.csv`) used in this project has been processed to handle missing values (fillna) and includes some manually added titles that were missing from the original source.
- For details on how null values were handled, check [notes/fillin.md](./notes/fillin.md).
- For a list of manually added works, check [notes/added_manually.txt](./notes/added_manually.txt).

## Project Structure

```text
.
├── api/                # Anilist API integration
├── dashboard/          # Streamlit dashboard code
├── data/               # CSV data storage (User, Original, Modified, Final)
├── manually/           # Scripts for manual addition/removal of works
├── notes/              # Documentation on data cleaning & manual entries
├── scripts/            # Helper shell scripts (verification, update)
├── setup_final/        # Core logic for matching and merging datasets
├── config.py           # Configuration settings
├── main.sh             # Main entry point application script
└── requirements.txt    # Python dependencies
```

## Acknowledgements

- **Anilist**: For providing the API used to fetch anime metadata.
- **Streamlit**: For providing the tool to create the web app and host the dashboard.
- **LeoRigasaki**: For the core datasets used in this project.
  - `anime.csv`: Original historical dataset (cleaned slightly for this dashboard).
  - `airing_anime.csv`: Maintained and updated by them.
  - Repository: [Anime-Dataset](https://github.com/LeoRigasaki/Anime-dataset)

## License

This project is provided **"as is"** for **personal and academic purposes**.

## Contact 
If you encounter errors or have suggestions for improvement, please contact me at:
**yumioharaka@gmail.com**

If you found an anime missing in anime.csv and you decided to added, please let me know so I can also added here.
