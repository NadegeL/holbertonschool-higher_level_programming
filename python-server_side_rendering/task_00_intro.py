"""the Templating Function for send invitation"""

import os
import logging

logging.basicConfig(level=logging.INFO)

def generate_invitations(template, attendees):
    if not isinstance(template, str):
        logging.error(f"Template must be str: {type(template)}")
        return

    if not isinstance(attendees, list):
        logging.error(f"Attendees must be a list: {type(attendees)}")
        return

    if not template:
        logging.error("Template is empty, no output files generated")
        return

    if not attendees:
        logging.error("No data provided, no output files generated")
        return

    try:
        for index, attendee in enumerate(attendees, start=1):
            filled_template = template.format(
                name=attendee.get("name", "N/A"),
                event_title=attendee.get("event_title", "N/A"),
                event_date=attendee.get("event_date", "N/A"),
                event_location=attendee.get("event_location", "N/A")
            )

            output_filename = f'output_{index}.txt'

            if os.path.exists(output_filename):
                logging.warning(f"File {output_filename} already exists. Skipping...")
                continue

            with open(output_filename, 'w') as output_file:
                output_file.write(filled_template)

        logging.info(f"{len(attendees)} files generated")

    except Exception as e:
        logging.error(f"An error occurred: {e}")
