#Calendar event selection using the Greedy Activity Selection algorithm.

def select_events(events):
   
    sorted_events = sorted(events, key=lambda event: event[2])
    selected = []
    last_end = -1

    for event in sorted_events:
        name, start, end = event
        if start >= last_end:
            selected.append(event)
            last_end = end

    return selected


def to_minutes(hour, minute=0):
   
    return hour * 60 + minute


def display_time(value):
  
    hour = value // 60
    minute = value % 60
    suffix = "AM" if hour < 12 else "PM"
    hour12 = hour % 12 or 12
    return f"{hour12}:{minute:02d} {suffix}"


if __name__ == "__main__":
    events = [
        ("A - Lecture", to_minutes(9), to_minutes(10)),
        ("B - Meeting", to_minutes(9, 30), to_minutes(11)),
        ("C - Lab", to_minutes(10), to_minutes(11)),
        ("D - Project work", to_minutes(11), to_minutes(12)),
        ("E - Seminar", to_minutes(10, 30), to_minutes(12)),
        ("F - Tutorial", to_minutes(12), to_minutes(13)),
    ]

    selected = select_events(events)

    print("Calendar Event Scheduling (Greedy Strategy)")
    print("\nSelected events:")
    for name, start, end in selected:
        print(f"{name}: {display_time(start)} - {display_time(end)}")

    print(f"\nTotal selected events: {len(selected)}")
