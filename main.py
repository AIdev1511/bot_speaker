import os

if __name__ == '__main__':
    print("Welcome to Bot Speaker 1.0 Created by Jatin")
    while True: 
        x = input("Tell me what to say:\n")
        if x == 'q': 
            break
        command = f"say {x} "
        os.system(command)