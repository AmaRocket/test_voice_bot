import os
import random
import speech_recognition

sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.8

command_dict = {
    "commands": {
        "greeting": ["привет", "приветствую", "здравствуй"],
        "create_task": ["добавить задачу", "новая задача", "создать задачу", "заметка", "добавить заметку"],
        "play_music": ["включить музыку", "играть музыку", "включи музыку"]
    }
}


def listen_command():
    """
    Func will return recognizer command
    """
    try:
        with speech_recognition.Microphone() as mic:
            sr.adjust_for_ambient_noise(source=mic, duration=0.8)
            audio = sr.listen(source=mic)
            query = sr.recognize_google(audio_data=audio, language="ru-RU").lower()
        return query
    except speech_recognition.UnknownValueError:
        return "Damn... it doesn't work"


def greeting():
    """
    Greeting function
    """
    return "Hello User!"


def create_task():
    """
    Create a task
    """
    print("What add to task-notes?")
    query = listen_command()

    with open("todo-list.txt", "a") as file:
        file.write(f"{query}\n")
    return f"Task {query} added successful"


def play_music():
    """
    Play random music
    """
    files = os.listdir('music')
    random_file = f'music/{random.choice(files)}'
    os.system(f'xdg-open {random_file}')

    return f"Dancing with {random_file.split('/')[-1]}"


def main():
    query = listen_command()

    for k, v in command_dict["commands"].items():
        if query in v:
            print(globals()[k]())

if __name__ == "__main__":
    main()
