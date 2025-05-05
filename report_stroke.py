from nicegui import ui

def report_stroke():
    ui.label('Please answer the following questions:')
    
    # Create a dictionary to store the selected answers and custom text
    answers = {
        'haemorrhage': '',
        'ischaemia': '',
        'lvo': '',
        'lvo_side': '',  # Added for LVO side selection
        'ica_disease': '',
        'ica_side': '',
        'quantify_stenosis': '',
        'left_stenosis': '',
        'right_stenosis': ''
    }
    custom_text = {
        'haemorrhage': '',
        'ischaemia': '',
        'lvo': '',
    }

    def update_result():
        # Generate a formatted string with labels, answers, and custom text
        formatted_text = (
            f"There is evidence of intracranial haemorrhage: {answers['haemorrhage']} {custom_text['haemorrhage']}\n"
            f"There is evidence of acute ischaemia: {answers['ischaemia']} {custom_text['ischaemia']}\n"
            f"There is an intracranial LVO: {answers['lvo']} {f'({answers["lvo_side"]})' if answers['lvo'] == 'YES' and answers['lvo_side'] else ''} {custom_text['lvo']}\n"
            f"There is significant extracranial internal carotid artery disease: {answers['ica_disease']}\n"
        )
        if answers['ica_disease'] == 'YES':
            formatted_text += (
                f"- Side of ICA disease: {answers['ica_side']}\n"
            )
            if answers['quantify_stenosis'] == 'YES':
                formatted_text += (
                    f"-- Left ICA stenosis: {answers['left_stenosis']}\n"
                    f"-- Right ICA stenosis: {answers['right_stenosis']}\n"
                )
            elif answers['quantify_stenosis'] == 'NO':
                formatted_text += (
                    "- Please discuss with a Vascular Radiologist and consider contemporaneous duplex imaging if the patient is a candidate for Carotid endarterectomy.\n"
                )
        result_box.value = formatted_text
        highlight_unanswered_questions()

    def highlight_unanswered_questions():
        # Add a red border to the left of unanswered questions
        haemorrhage_label.style('border-left: 4px solid red;' if not answers['haemorrhage'] else 'border-left: none;')
        ischaemia_label.style('border-left: 4px solid red;' if not answers['ischaemia'] else 'border-left: none;')
        lvo_label.style('border-left: 4px solid red;' if not answers['lvo'] else 'border-left: none;')
        lvo_side_row.style('border-left: 4px solid red;' if answers['lvo'] == 'YES' and not answers['lvo_side'] else 'border-left: none;')
        ica_disease_label.style('border-left: 4px solid red;' if not answers['ica_disease'] else 'border-left: none;')
        ica_side_row.style('border-left: 4px solid red;' if answers['ica_disease'] == 'YES' and not answers['ica_side'] else 'border-left: none;')
        quantify_stenosis_row.style('border-left: 4px solid red;' if answers['ica_disease'] == 'YES' and not answers['quantify_stenosis'] else 'border-left: none;')
        left_stenosis_row.style('border-left: 4px solid red;' if answers['quantify_stenosis'] == 'YES' and not answers['left_stenosis'] else 'border-left: none;')
        right_stenosis_row.style('border-left: 4px solid red;' if answers['quantify_stenosis'] == 'YES' and not answers['right_stenosis'] else 'border-left: none;')

    def toggle_visibility(button, input_field):
        input_field.visible = not input_field.visible
        button.icon = 'remove' if input_field.visible else 'add'

    def set_all_to_false():
        answers.update({
            'haemorrhage': 'NO',
            'ischaemia': 'NO',
            'lvo': 'NO',
            'lvo_side': '',
            'ica_disease': 'NO',
            'ica_side': '',
            'quantify_stenosis': '',
            'left_stenosis': '',
            'right_stenosis': ''
        })
        # Reset UI elements
        haemorrhage_radio.value = 'NO'
        ischaemia_radio.value = 'NO'
        lvo_radio.value = 'NO'
        lvo_side_row.visible = False
        ica_disease_radio.value = 'NO'
        ica_side_row.visible = False
        quantify_stenosis_row.visible = False
        left_stenosis_row.visible = False
        right_stenosis_row.visible = False
        update_result()

    # Add the "Normal" button
    ui.button('Normal', on_click=set_all_to_false).props('flat')

    with ui.row():
        haemorrhage_label = ui.label('There is evidence of intracranial haemorrhage')
        haemorrhage_radio = ui.radio(['YES', 'NO'], on_change=lambda e: (answers.update({'haemorrhage': e.value}), update_result())).props('inline')
        custom_input_haemorrhage = ui.input('Custom text', on_change=lambda e: (custom_text.update({'haemorrhage': e.value}), update_result()))
        custom_input_haemorrhage.visible = False
        toggle_button = ui.button(icon='add', on_click=lambda: toggle_visibility(toggle_button, custom_input_haemorrhage)).props('flat dense')
        ui.tooltip('Add custom text for this option').on(toggle_button)

    with ui.row():
        ischaemia_label = ui.label('There is evidence of acute ischaemia')
        ischaemia_radio = ui.radio(['YES', 'NO'], on_change=lambda e: (answers.update({'ischaemia': e.value}), update_result())).props('inline')
        custom_input_ischaemia = ui.input('Custom text', on_change=lambda e: (custom_text.update({'ischaemia': e.value}), update_result()))
        custom_input_ischaemia.visible = False
        toggle_button = ui.button(icon='add', on_click=lambda: toggle_visibility(toggle_button, custom_input_ischaemia)).props('flat dense')
        ui.tooltip('Add custom text for this option').on(toggle_button)

    with ui.row():
        lvo_label=ui.label('There is an intracranial LVO')
        lvo_radio = ui.radio(['YES', 'NO'], on_change=lambda e: (answers.update({'lvo': e.value}), update_result(), toggle_lvo_side(e.value))).props('inline')
        custom_input_lvo = ui.input('Custom text', on_change=lambda e: (custom_text.update({'lvo': e.value}), update_result()))
        custom_input_lvo.visible = False
        toggle_button = ui.button(icon='add', on_click=lambda: toggle_visibility(toggle_button, custom_input_lvo)).props('flat dense')
        ui.tooltip('Add custom text for this option').on(toggle_button)

    # Additional options for LVO side
    def toggle_lvo_side(value):
        lvo_side_row.visible = value == 'YES'

    lvo_side_row = ui.row()  # Create the row
    lvo_side_row.visible = False  # Set visibility to False
    with lvo_side_row:
        ui.label('Please indicate the side of the LVO')
        ui.radio(['Left', 'Right'], on_change=lambda e: (answers.update({'lvo_side': e.value}), update_result())).props('inline')

    with ui.row():
        ica_disease_label = ui.label('There is significant extracranial internal carotid artery disease')
        ica_disease_radio = ui.radio(['YES', 'NO'], on_change=lambda e: (answers.update({'ica_disease': e.value}), update_result(), toggle_ica_options(e.value))).props('inline')

    # Additional options for ICA disease
    def toggle_ica_options(value):
        ica_side_row.visible = value == 'YES'
        quantify_stenosis_row.visible = value == 'YES'

    ica_side_row = ui.row()  # Create the row
    ica_side_row.visible = False  # Set visibility to False
    with ica_side_row:
        ui.label('Please indicate the side of ICA disease')
        ui.radio(['R', 'L', 'Bilateral'], on_change=lambda e: (answers.update({'ica_side': e.value}), update_result())).props('inline')

    quantify_stenosis_row = ui.row()  # Create the row
    quantify_stenosis_row.visible = False  # Set visibility to False
    with quantify_stenosis_row:
        ui.label('Are you happy to quantify the degree of stenosis?')
        ui.radio(['YES', 'NO'], on_change=lambda e: (answers.update({'quantify_stenosis': e.value}), update_result(), toggle_stenosis_options(e.value))).props('inline')

    # Additional options for quantifying stenosis
    def toggle_stenosis_options(value):
        left_stenosis_row.visible = value == 'YES'
        right_stenosis_row.visible = value == 'YES'

    left_stenosis_row = ui.row()  # Create the row
    left_stenosis_row.visible = False  # Set visibility to False
    with left_stenosis_row:
        ui.label('Left ICA stenosis')
        ui.radio(['Unobstructed', 'Less than 50%', '50 to 70%', '70 to 90%', 'Greater than 90%', 'Occluded'], on_change=lambda e: (answers.update({'left_stenosis': e.value}), update_result())).props('inline')

    right_stenosis_row = ui.row()  # Create the row
    right_stenosis_row.visible = False  # Set visibility to False
    with right_stenosis_row:
        ui.label('Right ICA stenosis')
        ui.radio(['Unobstructed', 'Less than 50%', '50 to 70%', '70 to 90%', 'Greater than 90%', 'Occluded'], on_change=lambda e: (answers.update({'right_stenosis': e.value}), update_result())).props('inline')

    # Text box to display the selected answers
    result_box = ui.textarea('Report text:', value='').props('rows=10 style="width: 100%;" readonly')

    # Add a button to copy the result_box content to the clipboard
    def copy_to_clipboard():
        ui.run_javascript(f'navigator.clipboard.writeText(`{result_box.value}`)')

    ui.button('Copy to Clipboard', on_click=copy_to_clipboard).props('flat')
    highlight_unanswered_questions()