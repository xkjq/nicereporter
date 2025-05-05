from nicegui import ui

def report_stroke():
    ui.label('Please answer the following questions:')
    
    # Create a dictionary to store the selected answers and custom text
    answers = {
        'haemorrhage': 'False',
        'ischaemia': 'False',
        'lvo': 'False',
        'stenosis': 'False'
    }
    custom_text = {
        'haemorrhage': '',
        'ischaemia': '',
        'lvo': '',
        'stenosis': ''
    }

    # Text box to display the selected answers
    result_box = ui.textarea('Selected Answers:', value='').props('rows=5 readonly')

    def update_result():
        # Generate a formatted string with labels, answers, and custom text
        formatted_text = (
            f"There is evidence of intracranial haemorrhage: {answers['haemorrhage']} {custom_text['haemorrhage']}\n"
            f"There is evidence of acute ischaemia: {answers['ischaemia']} {custom_text['ischaemia']}\n"
            f"There is an intracranial LVO: {answers['lvo']} {custom_text['lvo']}\n"
            f"There is significant stenosis of the internal carotid arteries: {answers['stenosis']} {custom_text['stenosis']}"
        )
        result_box.value = formatted_text

    with ui.row():
        ui.label('There is evidence of intracranial haemorrhage')
        ui.radio(['True', 'False'], on_change=lambda e: (answers.update({'haemorrhage': e.value}), update_result())).props('inline')
        toggle_haemorrhage = ui.checkbox('Add custom text', value=False, on_change=lambda e: custom_input_haemorrhage.set_visibility(e.value))
        custom_input_haemorrhage = ui.input('Custom text', on_change=lambda e: (custom_text.update({'haemorrhage': e.value}), update_result()))
        custom_input_haemorrhage.visible = toggle_haemorrhage.value

    with ui.row():
        ui.label('There is evidence of acute ischaemia')
        ui.radio(['True', 'False'], on_change=lambda e: (answers.update({'ischaemia': e.value}), update_result())).props('inline')
        toggle_ischaemia = ui.checkbox('Add custom text', value=False, on_change=lambda e: custom_input_ischaemia.set_visibility(e.value))
        custom_input_ischaemia = ui.input('Custom text', on_change=lambda e: (custom_text.update({'ischaemia': e.value}), update_result()))
        custom_input_ischaemia.visible = toggle_ischaemia.value

    with ui.row():
        ui.label('There is an intracranial LVO')
        ui.radio(['True', 'False'], on_change=lambda e: (answers.update({'lvo': e.value}), update_result())).props('inline')
        toggle_lvo = ui.checkbox('Add custom text', value=False, on_change=lambda e: custom_input_lvo.set_visibility(e.value))
        custom_input_lvo = ui.input('Custom text', on_change=lambda e: (custom_text.update({'lvo': e.value}), update_result()))
        custom_input_lvo.visible = toggle_lvo.value

    with ui.row():
        ui.label('There is significant stenosis of the internal carotid arteries')
        ui.radio(['True', 'False'], on_change=lambda e: (answers.update({'stenosis': e.value}), update_result())).props('inline')
        toggle_stenosis = ui.checkbox('Add custom text', value=False, on_change=lambda e: custom_input_stenosis.set_visibility(e.value))
        custom_input_stenosis = ui.input('Custom text', on_change=lambda e: (custom_text.update({'stenosis': e.value}), update_result()))
        custom_input_stenosis.visible = toggle_stenosis.value