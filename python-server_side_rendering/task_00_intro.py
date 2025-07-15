def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(item, dict) for item in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return
    if template.strip() == "":
        print("Error: Template is empty, no output files generated.")
        return
    if len(attendees) == 0:
        print("Error: No data provided, no output files generated.")
        return
    for index, attendee in enumerate(attendees, startr=1):
        templatecopy = template
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(key)
            if value is None:
                value = "N/A"
                templatecopy = templatecopy.replace("{" + key + "}", str(value))

        filename = f"output_{index}.txt"
        with open(filename, "w") as f:
            f.write(templatecopy)
