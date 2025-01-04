def translate_app(language):
    translations = {
        "English": {
            "title": "PDF Toolkit",
            "upload_prompt": "Upload your files",
        },
        "Español": {
            "title": "Herramienta PDF",
            "upload_prompt": "Sube tus archivos",
        },
        "Français": {
            "title": "Outil PDF",
            "upload_prompt": "Téléchargez vos fichiers",
        }
    }
    selected_translations = translations.get(language, translations["English"])
    return selected_translations
