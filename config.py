from questionary import Style
from pathlib import Path

# -- user's name --
user_name = "User"

# -- user's csv name --
user_csv = "works.csv"

# -- final csv name --
final_csv = "final.csv"

# -- change the way the program greets you --
greeting = "Good morning, User" # you need to set show_greetings to True to be able to see this message

# -- csv paths --
path_user_csv = Path("./data/user/" + user_csv)
path_original_airing = Path("./data/original/airing_anime.csv")
path_modified_airing = Path("./data/modified/airing_anime_M.csv")
path_historical_csv = Path("./data/modified/anime.csv")
path_final_csv = Path("./data/final/" + final_csv)

# -- Disable/Enable some features
# set to "True" if you want to skip the verification of the files every time you run the program (that they exists, they are csv files and that they have information)
disable_file_verification = True

# Set to True is you want to see "greeting" everytime yourun the program
show_greetings = False

# Set either of them to True if you want to sort "final_csv", by default each entry will be in the order it was added.
# Take into account that if both of them are set to True, date takes priority and will be the only one applied
sort_final = {
    "date": False,
    "title": False
}

# -- match name utility --
type_mappings = {
    'anime': ['tv', 'ova', 'ona'],
    'tv': ['tv', 'ova', 'ona'],
    'movie': ['movie', 'ona', 'ova'],
    'film': ['movie', 'ona', 'ova'],
    'ona': ['tv', 'movie', 'ona'],
    'ova': ['tv', 'ova', 'movie']
}

# -- Questionery looks configuration --
blue_style = Style([
    ('qmark', 'fg:#00d7ff bold'),       # The '?' icon
    ('question', 'fg:#ffffff bold'),     # The actual question
    ('answer', 'fg:#005fff bold'),       # The result after you press enter
    ('pointer', 'fg:#00d7ff bold'),      # The arrow in lists
    ('highlighted', 'fg:#00d7ff bold'),  # The currently hovered suggestion
    ('selected', 'fg:#00afff'),          # The selected item
    ('text', 'fg:#e4e4e4'),              # What you type
    # The dropdown menu colors
    ('completion-menu.completion', 'bg:#000087 fg:#eeeeee'), 
    ('completion-menu.completion.current', 'bg:#005fff fg:#ffffff'),
])

# -- some paths used exclusively for scripts/ --
# airing_anime.csv from LeoRiosaki's github
url = "https://raw.githubusercontent.com/LeoRigasaki/Anime-dataset/refs/heads/main/data/raw/airing_anime.csv"
cleanup = Path("setup_final.cleanup_airing")
concatenate = Path("setup_final.concatenate")

# -- css used for streamlit -- 
css_dashboard = "./dashboard/style.css"


