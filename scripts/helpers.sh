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

#Checks if the file exists and is not empty.
#Returns True if file exists and has content, False otherwise.
file_exists()
{
    local path="$1"
    local filename="$2"

    if [ -s "$path" ]; then
        return 0
    else
        echo "You can not execute this action because "$filename" does not exists at "$path", or it's empty."
        return 1
    fi

}

# checks the exits status to ensure the program does not carry on after an error
# the only argument received is such exit status
check_status()
{
    local status="$1"
    if [ "$status" -ne 0 ]; then
        echo "Shutting down..."
        deactivate # if usin conda, change this to conda deactivate
        exit 1
    fi
}

# funtion used to make sure the argument passed, if any, is correct
check_argument()
{
    local args="$1"
    local len_args="$2"
    local len_opt="$3"
    local pattern="^[1-$len_opt]$"

    if [ "$len_args" -eq 0 ]; then
        return 0
    elif [ "$len_args" -gt 1 ]; then
        echo ""
        echo "Usage: ./main.sh number"
        return 1
    elif [[ ! "${args[0]}" =~ $pattern ]]; then
        echo ""
        echo "Error, you should pass a number between 1 and "$len_opt"."
        return 1
    else
        return 0
    fi
}
