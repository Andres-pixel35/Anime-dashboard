#!/bin/bash

# Capture Python variables into Bash environment
eval $("$1" -c "
from pathlib import Path
import config

# Map your Python variables to Bash names
vars_to_export = {
    'URL': config.url,
    'CLEANUP_SCRIPT': config.cleanup,
    'CONCAT_SCRIPT': config.concatenate,
    'SAVE_AIRING': config.path_original_airing
}

for bash_var, value in vars_to_export.items():
    # Convert Path objects to strings, keep strings as is
    val_str = value.as_posix() if isinstance(value, Path) else value
    print(f'{bash_var}=\"{val_str}\"')
")

# download the new airing_anime.csv
echo ""
echo "Downloading airing_anime.csv from Github"
echo "--------------------------------"
curl -o "$SAVE_AIRING" "$URL"

# cleans that new file and concatenate it with anime.csv
echo ""
echo "Cleaning and concatenating airing file with anime.csv"
echo "--------------------------------"
"$1" -m "$CLEANUP_SCRIPT" && "$1" -m "$CONCAT_SCRIPT"



