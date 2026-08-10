#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "icalendar>=6",
#   "recurring-ical-events>=3",
# ]
# ///
"""Fetch a public .ics calendar and convert it to a flat JSON array for Hugo.

Usage: ics_to_data.py <ics-url> <output-json-path>

Expands recurring events within [-3 months, +3 months] around now. Output is
a single list (past and future events together, sorted ascending by start),
so Hugo templates can filter/split as needed.
"""

from __future__ import annotations

import json
import re
import sys
import urllib.request
from datetime import date, datetime, timedelta, timezone

import icalendar  # ty: ignore[unresolved-import]
import recurring_ical_events  # ty: ignore[unresolved-import]

WINDOW_FUTURE = timedelta(days=90)
WINDOW_PAST = timedelta(days=60)


def to_iso(value: date | datetime) -> tuple[str, bool]:
    """Return (RFC3339 string, all_day flag) for an ics date/datetime value."""
    if isinstance(value, datetime):
        if value.tzinfo is None:
            value = value.replace(tzinfo=timezone.utc)
        return value.isoformat(), False
    return value.isoformat(), True


def slugify(summary: str, start: str) -> str:
    """Build a stable, readable slug for use as an HTML anchor id."""
    base = re.sub(r"[^a-z0-9]+", "-", summary.lower()).strip("-")
    return f"{start[:10]}-{base}"


def main() -> None:
    if len(sys.argv) != 3:
        sys.exit(f"Usage: {sys.argv[0]} <ics-url> <output-json-path>")
    ics_url, output_path = sys.argv[1], sys.argv[2]

    with urllib.request.urlopen(ics_url) as response:
        calendar = icalendar.Calendar.from_ical(response.read())

    now = datetime.now(timezone.utc)
    occurrences = recurring_ical_events.of(calendar).between(
        now - WINDOW_PAST, now + WINDOW_FUTURE
    )

    events = []
    for component in occurrences:
        start, all_day = to_iso(component["DTSTART"].dt)
        end, _ = (
            to_iso(component["DTEND"].dt)
            if component.get("DTEND")
            else (start, all_day)
        )
        if all_day and component.get("DTEND"):
            # All-day DTEND is exclusive per RFC 5545; shift back to the actual last day.
            end, _ = to_iso(component["DTEND"].dt - timedelta(days=1))
        summary = str(component.get("SUMMARY", ""))
        events.append(
            {
                "uid": str(component.get("UID", "")),
                "slug": slugify(summary, start),
                "summary": summary,
                "description": str(component.get("DESCRIPTION", "")),
                "location": str(component.get("LOCATION", "")),
                "start": start,
                "end": end,
                "all_day": all_day,
            }
        )

    events.sort(key=lambda event: event["start"])

    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(events, file, indent=2, ensure_ascii=False)
        file.write("\n")

    print(f"Wrote {len(events)} events to {output_path}")


if __name__ == "__main__":
    main()
