from voice_assistant import speak, listen
from installer import install_software
from software_checker import is_installed


def handle_command(command):
    command = command.lower()

    if "install" in command:
        software = command.replace("install", "").strip()
        if software:
            if is_installed(software):
                speak(
                    f"{software.capitalize()} is already installed. Would you like to proceed with the setup, or download it again? Say or type 'setup' to continue with setup, 'download' to download again, or 'no' to exit."
                )

                # Listen for voice input
                response = listen().lower()

                if not response:
                    speak("Please type your response below.")
                    response = input("Enter your choice (setup/download/no): ").lower()

                if "setup" in response:
                    handle_setup(software)
                elif "download" in response:
                    speak(f"Downloading {software} again.")
                    install_software(software)
                else:
                    speak("Okay, exiting the setup.")
            else:
                speak(f"{software.capitalize()} is not installed. Opening the download page for installation.")
                install_software(software)
        else:
            speak("Please specify the software you'd like to install.")


    elif "setup" in command:
        software = command.replace("setup", "").strip()
        if software:
            handle_setup(software)
        else:
            speak("Please specify the software you'd like to set up.")

    elif "exit" in command or "stop" in command:
        speak("Goodbye!")
        exit()
    else:
        speak("Sorry, I didn't understand that. Please try again.")


def handle_setup(software):
    """Guide the user through the setup process for the specified software."""
    speak(f"Guiding you through {software} setup.")
    # if 'java' in software:
    #     guide_java_setup()
    # elif 'python' in software:
    #     guide_python_setup()
    # elif 'intellij' in software:
    #     guide_intellij_setup()
    # elif 'android studio' in software:
    #     guide_android_studio_setup()
    # else:
    #     speak(f"Sorry, I don't have a setup guide for {software}.")


def get_input():
    """Listen for a command either by voice or text and process it."""
    command = listen()
    if command:
        return command

    speak("Please type your command below.")
    command = input("Enter command: ")
    return command


if __name__ == "__main__":
    while True:
        speak("You can either speak or type your command.")
        command = get_input()

        if command:
            handle_command(command)
        else:
            speak("Sorry, I couldn't detect any command. Please try again.")

