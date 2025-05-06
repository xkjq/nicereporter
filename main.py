from nicegui import ui
from report_stroke import report_stroke  # Import the report_stroke page

def main():
    ui.label('Report Generatort')
    ui.button('Stroke', on_click=lambda: ui.navigate.to('/report_stroke'))

    @ui.page('/about')
    def about_page():
        ui.label('This is the About page.')

    # Register the report_stroke page
    @ui.page('/report_stroke')
    def report_stroke_page():
        report_stroke()

    ui.run(port=5129)

if __name__ in {"__main__", "__mp_main__"}:
    main()