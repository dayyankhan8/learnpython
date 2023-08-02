def get_media_type(filename):
    suffixes = [".gif", ".jpg", ".jpeg", ".png", ".pdf", ".txt", ".zip"]

    for suffix in suffixes:
        if filename.lower().endswith(suffix):
            return f"{get_mime_type(suffix)}"
    
    return "media type: application/octet-stream"

def get_mime_type(suffix):
    mime_types = {
        ".gif": "image/gif",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".pdf": "application/pdf",
        ".txt": "text/plain",
        ".zip": "application/zip",
    }
    return mime_types.get(suffix, "application/octet-stream")

def main():
    filename = input("Please enter the name of the file: ")

    media_type = get_media_type(filename)
    print(media_type)

main()
