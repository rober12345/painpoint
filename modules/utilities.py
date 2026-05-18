import os
from datetime import datetime

# =========================================================
# CREATE REQUIRED FOLDERS
# =========================================================

def create_folders():

    os.makedirs(
        "database",
        exist_ok=True
    )

    os.makedirs(
        "uploads/photos",
        exist_ok=True
    )

# =========================================================
# SAVE PHOTO
# =========================================================

def save_photo(uploaded_photo):

    if uploaded_photo is None:

        return ""

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    filename = (
        f"{timestamp}_{uploaded_photo.name}"
    )

    photo_path = os.path.join(
        "uploads/photos",
        filename
    )

    with open(photo_path, "wb") as f:

        f.write(
            uploaded_photo.getbuffer()
        )

    return photo_path