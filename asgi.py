from main import main
from nicegui import ui

@ui.page('/')
def main_page() -> None:
    main()

app = ui.run_with(uvicorn=False)  # Expose the app as an ASGI application