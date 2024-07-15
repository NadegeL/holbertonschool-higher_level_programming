#!/usr/bin/env python3

import os


def generate_invitations(template_path, attendees):
    """read the content of file"""
    try:
        with open(template_path, 'r') as file:
            template = file.read()
    except FileNotFoundError:
        print("Error: Template not found")
        return

    """verify if attendees is a list of dictionaries"""
    if not isinstance(attendees, list):
        print("attendees must be a list of dictionaries")
        return

    if not all(isinstance(i, dict) for i in attendees):
        print("attendees must be a list of dictionaries")
        return

    """verify if template is empty"""
    if not template:
        print("template is empty,no output files generated.")
        return

    """verify if attendees is empty"""
    if not attendees:
        print(" No data provided, no output files generated.")
        return

    """create output directory"""
    output_dir = "output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    """list of attendees and generate the invitation"""
    for idx, attendee in enumerate(attendees, start=1):
        output = template
        print(f"Processing {attendee['name']}")
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = str(attendee.get(key, "N/A"))
            print(f"Replacing {{{key}}} with {value}")
            output = output.replace(f"{{{key}}}", value)
        output_file_path = f"{output_dir}/invitation_{idx}.txt"
        with open(output_file_path, "w") as file:
            file.write(output)
        print(f"Generated file: {output_file_path}")


attendees = [
    {"name": "Alice", "event_title": "Python Conference",
        "event_date": "2023-07-15", "event_location": "New York"},
    {"name": "Bob", "event_title": "Data Science Workshop",
        "event_date": "2023-08-20", "event_location": "San Francisco"},
    {"name": "Charlie", "event_title": "AI Summit",
        "event_date": None, "event_location": "Boston"}
]

generate_invitations('template.txt', attendees)
