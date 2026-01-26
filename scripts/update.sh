#! /bin/bash

GITHUB_URL=$(python3 -c "import config; print(config.url)")
CLEANUP_FILE=$(python3 -c "import config; print(config.cleanup)")
CONCATENATE_FILE=$(python3 -c "import config; print(config.concatenate)")
AIRING_SAVE=$(python3 -c "import config; print(config.path_original_airing)")
VIRTUAL_ENVIROMENT=$(python3 -c "import config; print(config.venv_enviroment)")

# activates the virtual environment
source "$VIRTUAL_ENVIROMENT"

# download the new airing_anime.csv
curl -o "$AIRING_SAVE" "$GITHUB_URL"

# cleans that new file and concatenate it with anime.csv
python3 -m "$CLEANUP_FILE" && python3 -m "$CONCATENATE_FILE"

# closes the virtual environment
deactivate




