import logging
from typing import List, Dict

logging.basicConfig(level=logging.INFO,
                    format="%(levelname)s: %(message)s")


def generate_invitations(template: str, attendees: List[Dict[str, str]]) -> None:
    if not isinstance(template, str):
        logging.error("Invalid type: template must be str, got %s",
                      type(template).__name__)
        return

    if not (isinstance(attendees, list) and all(isinstance(a, dict) for a in attendees)):
        logging.error("Invalid type: attendees must be list of dicts")
        return

    if not template.strip():
        logging.error("Template is empty, no output files generated.")
        return

    if not attendees:
        logging.info("No data provided, no output files generated.")
        return

    required = ("name", "event_title", "event_date", "event_location")

    for idx, attendee in enumerate(attendees, start=1):
        data = {k: (str(attendee.get(k)) if attendee.get(k) not in (None, "") else "N/A")
                for k in required}
        invitation = template.format(**data)
        filename = f"output_{idx}.txt"
        try:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(invitation)
            logging.info("Created %s", filename)
        except OSError as err:
            logging.error("Failed to write %s: %s", filename, err)
