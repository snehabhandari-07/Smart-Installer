import shutil

def is_installed(software_name):
    paths = {
        "python": "python",
        "java": "java",
        "node": "node",
        "git": "git",
        "docker": "docker",
        "vs code": "code",
        "intellij": "idea",
        "mysql": "mysql",
        "mongodb": "mongo",
        "postman": "postman"
    }
    return shutil.which(paths.get(software_name.lower(), "")) is not None
