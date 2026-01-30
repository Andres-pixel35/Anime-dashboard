#!/bin/bash

if command -v python3 &>/dev/null; then
    export PY_BIN="python3"
elif command -v python &>/dev/null; then
    export PY_BIN="python"
else
    export PY_BIN="" # Empty if not found
fi

confirm() 
{
    local prompt="$1"
    local default="$2"
    local options
    
    [[ "$default" == "Y" ]] && options="[Y/n]" || options="[y/N]"

    echo ""
    read -p "$prompt $options: " response
    response="${response:-$default}"

    case "$response" in
        [yY][eE][sS]|[yY]) 
            return 0 
        ;;
        *) 
            return 1 
        ;;
    esac
}

ask_continue()
{
    if confirm "Do you want to continue" "Y"; then
        return 0
    else
        return 1
    fi
}

#Checks if final exists and is not empty.
#Returns True if file exists and has content, False otherwise.
final_exists()
{
    final_path="$1"
    final_name="$2"

    if [ -s "$final_path" ]; then
        return 0
    else
        echo "You can not execute this action because "$final_name" does not exists at "$final_path", or it's empty."
        return 1
    fi

}
