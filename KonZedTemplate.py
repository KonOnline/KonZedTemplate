import os
import time
import shutil
import getpass

ascii_art = [
    " ██ ▄█▀ ▒█████   ███▄    █ ▒███████▒▓█████ ▓█████▄ ",
    " ██▄█▒ ▒██▒  ██▒ ██ ▀█   █ ▒ ▒ ▒ ▄▀░▓█   ▀ ▒██▀ ██▌",
    "▓███▄░ ▒██░  ██▒▓██  ▀█ ██▒░ ▒ ▄▀▒░ ▒███   ░██   █▌",
    "▓██ █▄ ▒██   ██░▓██▒  ▐▌██▒  ▄▀▒   ░▒▓█  ▄ ░▓█▄   ▌",
    "▒██▒ █▄░ ████▓▒░▒██░   ▓██░▒███████▒░▒████▒░▒████▓ ",
    "▒ ▒▒ ▓▒░ ▒░▒░▒░ ░ ▒░   ▒ ▒ ░▒▒ ▓░▒░▒░░ ▒░ ░ ▒▒▓  ▒ ",
    "░ ░▒ ▒░  ░ ▒ ▒░ ░ ░░   ░ ▒░░░▒ ▒ ░ ▒ ░ ░  ░ ░ ▒  ▒ ",
    "░ ░░ ░ ░ ░ ░ ▒     ░   ░ ░ ░ ░ ░ ░ ░   ░    ░ ░  ░ ",
    "░  ░       ░ ░           ░   ░ ░       ░  ░   ░    ",
    "                           ░                ░       "
]

max_width = max(len(line) for line in ascii_art)

def center_text(text, width):
    return text.center(width)

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_terminal_size():
    return shutil.get_terminal_size()

def input_centered(prompt):
    return getpass.getpass(center_text(prompt, get_terminal_size().columns))

def print_menu():
    term_size = get_terminal_size()
    total_width = term_size.columns
    total_height = term_size.lines
    vertical_padding = (total_height - len(ascii_art)) // 2
    clear_console()
    for _ in range(vertical_padding):
        print()
    print(center_text("+" + "-" * (max_width + 2) + "+", total_width))
    for line in ascii_art:
        centered_line = center_text("| " + line.ljust(max_width) + " |", total_width)
        print(centered_line)
        time.sleep(0.3)
    print(center_text("+" + "-" * (max_width + 2) + "+", total_width))

def display_help():
    commands = ["help", "dir", "cls", "cd", "echo", "del", "mkdir", "exit", "quit"]
    term_size = get_terminal_size()
    total_width = term_size.columns
    clear_console()
    print(center_text("Available Commands:", total_width))
    for command in commands:
        print(center_text(command, total_width))

def list_dir():
    clear_console()
    print(center_text("Listing directory contents...", get_terminal_size().columns))

def change_dir(path):
    print(center_text(f"Changing directory to {path}...", get_terminal_size().columns))

def delete_file(filename):
    print(center_text(f"Deleting file: {filename}", get_terminal_size().columns))

def create_dir(directory):
    print(center_text(f"Creating directory: {directory}", get_terminal_size().columns))

def main_menu():
    print_menu()
    while True:
        user_input = input_centered("> Enter command: ")
        split_input = user_input.split(' ')
        command = split_input[0].lower()
        args = split_input[1:] if len(split_input) > 1 else []
        if command == 'help':
            display_help()
            time.sleep(2)
            print_menu()
        elif command == 'dir':
            list_dir()
            time.sleep(2)
            print_menu()
        elif command == 'cls':
            print_menu()
        elif command == 'cd':
            if args:
                change_dir(args[0])
            else:
                print(center_text("Usage: cd <directory>", get_terminal_size().columns))
            time.sleep(2)
            print_menu()
        elif command == 'echo':
            print(center_text(' '.join(args), get_terminal_size().columns))
            time.sleep(2)
            print_menu()
        elif command == 'del':
            if args:
                delete_file(args[0])
            else:
                print(center_text("Usage: del <file>", get_terminal_size().columns))
            time.sleep(2)
            print_menu()
        elif command == 'mkdir':
            if args:
                create_dir(args[0])
            else:
                print(center_text("Usage: mkdir <directory>", get_terminal_size().columns))
            time.sleep(2)
            print_menu()
        elif command in ['exit', 'quit']:
            break
        else:
            print(center_text(f"Unrecognized command: {user_input}", get_terminal_size().columns))
            time.sleep(1)
            print_menu()

if __name__ == "__main__":
    main_menu()
