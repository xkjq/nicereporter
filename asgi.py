from main import main
from nicegui import ui

@ui.page('/')
def main_page() -> None:
    main()

app = ui.get_app()  # Expose the NiceGUI app as an ASGI application