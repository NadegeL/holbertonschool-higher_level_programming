from flask import Flask, render_template, jsonify
import os
import json


def generate_invitations(template, attendees):
    if template is None or not isinstance(template, str):
        print("Template is not a string")
        return
    if attendees is None or not isinstance(attendees, list):
        print("Attendees is not a list")
        return

    if not template:
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    try:
        for index, attendee in enumerate(attendees, start=1):
            name_placeholder = "{name}"
            event_title_placeholder = "{event_title}"
            event_date_placeholder = "{event_date}"
            event_location_placeholder = "{event_location}"

            name_value = attendee.get("name") or "N/A"
            event_title_value = attendee.get("event_title") or "N/A"
            event_date_value = attendee.get("event_date") or "N/A"
            event_location_value = attendee.get("event_location") or "N/A"

            result = template.replace(name_placeholder, name_value).replace(event_title_placeholder, event_title_value).replace(
                event_date_placeholder, event_date_value).replace(event_location_placeholder, event_location_value)

            output_filename = f'output_{index}.txt'

            # Check if the file already exists
            if os.path.exists(output_filename):
                print(f"File {output_filename} already exists. Skipping...")
                continue  # Skip writing if the file already exists

            with open(output_filename, 'w') as output_file:
                output_file.write(result)

        print(f"{len(attendees)} files generated")

    except Exception as e:
        print(f"An error occurred: {e}")
        return


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


def load_items():
    with open('items.json') as f:
        data = json.load(f)
    return data['items']


@app.route('/items')
def items():
    items = load_items()
    return render_template('items.html')


if __name__ == '__main__':
    app.run(debug=True)
