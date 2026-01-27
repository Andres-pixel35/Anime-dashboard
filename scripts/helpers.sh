#! /bin/bash

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
