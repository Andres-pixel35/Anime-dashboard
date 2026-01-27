#! /bin/bash

echo "--- Activating virtual environment ---"
source ./.venv/bin/activate
source ./scripts/helpers.sh

if [ -z "$PY_BIN" ]; then
    echo "ERROR: Python is required, but not found."
    exit 1
fi

eval $("$PY_BIN" -c "
    import config
    print(f'GREETING=\"{config.greeting}\"')
    print(f'DISABLE_VERIFICATION={str(config.disable_file_verification).lower()}')
    print(f'SHOW_GREETINGS={str(config.show_greetings).lower()}')
")
if [ "$SHOW_GREETINGS" == "true" ]; then
    figlet -f slant -t -c "$GREETING" | lolcat
fi

if [ "$DISABLE_VERIFICATION" == "false" ]; then
    ./scripts/verify_files.sh "$PY_BIN"
fi

OPTIONS=( "Sync your csv" "Add work" "Remove Work" "Dashboard" "Update Airing" "Update Final" "Exit" )
len=${#OPTIONS[@]}

while true; do
    echo ""
    echo "What do you want to do?"

    for ((i=0; i<$len; i++)); do
        echo ""$((i+1))": "${OPTIONS[$i]}""
    done

    read -p "Please enter the number: " action

    case "$action" in
        1)
            echo ""
            echo -n "This action will match your csv with anime.csv and it will create final.csv with all" 
            echo " the matches and the complete information"
            if confirm "Do you want to proceed? " "Y"; then
                "$PY_BIN" -m setup_final.match_name
                echo "final.csv was successfully created."

                if ask_continue; then
                    continue
                else
                    break
                fi
            else
                echo "Going back to actions."
                continue
            fi
        ;;
        2)
            echo ""
            "$PY_BIN" -m manually.add_work

            if ask_continue; then
                continue
            else
                break
            fi
        ;;
        3)
            echo ""
            "$PY_BIN" -m manually.remove_work

            if ask_continue; then
                continue
            else
                break
            fi
        ;;
        7)
            break
        ;;
        *)
            echo ""
            echo "You need to choose a number between 1 and "$len", please try again."
        ;;
    esac
done
        
echo ""
echo "-- Closing virtual environment ---"
deactivate
