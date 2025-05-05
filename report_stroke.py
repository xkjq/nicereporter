from nicegui import ui

def report_stroke():
    ui.label('Please answer the following questions:')
    
    # Create a dictionary to store the selected answers and custom text
    answers = {
        'haemorrhage': '',
        'ischaemia': '',
        'lvo': '',
        'stenosis': ''
    }
    custom_text = {
        'haemorrhage': '',
        'ischaemia': '',
        'lvo': '',
        'stenosis': ''
    }

    def update_result():
        # Generate a formatted string with labels, answers, and custom text
        formatted_text = (
            f"There is evidence of intracranial haemorrhage: {answers['haemorrhage']} {custom_text['haemorrhage']}\n"
            f"There is evidence of acute ischaemia: {answers['ischaemia']} {custom_text['ischaemia']}\n"
            f"There is an intracranial LVO: {answers['lvo']} {custom_text['lvo']}\n"
            f"There is significant stenosis of the internal carotid arteries: {answers['stenosis']} {custom_text['stenosis']}"
        )
        result_box.value = formatted_text

    def toggle_visibility(button, input_field):
        input_field.visible = not input_field.visible
        button.icon = 'remove' if input_field.visible else 'add'

    def set_all_to_false():
        answers.update({
            'haemorrhage': 'False',
            'ischaemia': 'False',
            'lvo': 'False',
            'stenosis': 'False'
        })
        update_result()

    # Add the "Normal" button
    ui.button('Normal', on_click=set_all_to_false).props('flat')

    with ui.row():
        ui.label('There is evidence of intracranial haemorrhage')
        ui.radio(['True', 'False'], on_change=lambda e: (answers.update({'haemorrhage': e.value}), update_result())).props('inline')
        custom_input_haemorrhage = ui.input('Custom text', on_change=lambda e: (custom_text.update({'haemorrhage': e.value}), update_result()))
        custom_input_haemorrhage.visible = False
        toggle_button = ui.button(icon='add', on_click=lambda: toggle_visibility(toggle_button, custom_input_haemorrhage)).props('flat dense')
        ui.tooltip('Add custom text for this option').on(toggle_button)

    with ui.row():
        ui.label('There is evidence of acute ischaemia')
        ui.radio(['True', 'False'], on_change=lambda e: (answers.update({'ischaemia': e.value}), update_result())).props('inline')
        custom_input_ischaemia = ui.input('Custom text', on_change=lambda e: (custom_text.update({'ischaemia': e.value}), update_result()))
        custom_input_ischaemia.visible = False
        toggle_button = ui.button(icon='add', on_click=lambda: toggle_visibility(toggle_button, custom_input_ischaemia)).props('flat dense')
        ui.tooltip('Add custom text for this option').on(toggle_button)

    with ui.row():
        ui.label('There is an intracranial LVO')
        ui.radio(['True', 'False'], on_change=lambda e: (answers.update({'lvo': e.value}), update_result())).props('inline')
        custom_input_lvo = ui.input('Custom text', on_change=lambda e: (custom_text.update({'lvo': e.value}), update_result()))
        custom_input_lvo.visible = False
        toggle_button = ui.button(icon='add', on_click=lambda: toggle_visibility(toggle_button, custom_input_lvo)).props('flat dense')
        ui.tooltip('Add custom text for this option').on(toggle_button)

    with ui.row():
        ui.label('There is significant stenosis of the internal carotid arteries')
        ui.radio(['True', 'False'], on_change=lambda e: (answers.update({'stenosis': e.value}), update_result())).props('inline')
        custom_input_stenosis = ui.input('Custom text', on_change=lambda e: (custom_text.update({'stenosis': e.value}), update_result()))
        custom_input_stenosis.visible = False
        toggle_button = ui.button(icon='add', on_click=lambda: toggle_visibility(toggle_button, custom_input_stenosis)).props('flat dense')
        ui.tooltip('Add custom text for this option').on(toggle_button)

    # Text box to display the selected answers
    result_box = ui.textarea('Selected Answers:', value='').props('rows=10 style="width: 100%;" readonly')

