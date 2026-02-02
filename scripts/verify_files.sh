#!/bin/bash

# Pull all paths from Python into Bash variables in one go
# We use .as_posix() to ensure the paths use '/' regardless of OS
eval $("$1" -c "
from pathlib import Path
import config

paths = {
    'ORIGINAL_AIRING': config.path_original_airing,
    'MODIFIED_AIRING': config.path_modified_airing,
    'HISTORICAL_CSV': config.path_historical_csv
}

for var_name, path_obj in paths.items():
    print(f'{var_name}=\"{path_obj.as_posix()}\"')
")

# Put them in a list to iterate through the checks
files_paths=("$USER_CSV" "$ORIGINAL_AIRING" "$MODIFIED_AIRING" "$HISTORICAL_CSV")

echo ""
echo "--- Starting verification of data files ---"

# iterates through all the array and make several verifications with each file
for path in ${files_paths[@]}; do
    filename="${path##*/}" # extract the filename
    mime_type=$(file -b --mime-type "$path") # checks the file type
  
    # checks whether the file exists or not and whether it has at least a size of 1 byte
    if [ ! -s "$path" ]; then
        echo ""
        echo "ERROR: File "$filename" does not exists at "$path", or it's empty."
        exit 2
    # checks wheter the file is csv or not
    elif [[ "$mime_type" != "text/csv" && "$filename" != *.csv ]]; then
        echo ""
        echo "ERROR: file "$filename" is not a csv file."
        exit 2
    fi
done

echo "All the file exists and are CSVs, you can proceed"
exit 0




