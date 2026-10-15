# Case Study 2: Google Calendar Scheduling Using a Greedy Strategy

## 1. Introduction

Calendar applications help users organize lectures, meetings, appointments, and other events. When a user wants to attend as many events as possible without time conflicts, the Activity Selection problem provides a useful model.

A Greedy algorithm makes a locally optimal choice at each step. For Activity Selection, the standard greedy rule is to choose the compatible event that finishes earliest.

## 2. Problem statement

Given a list of events with start and end times, select the maximum number of mutually non-overlapping events.

**Assumption:** An event may begin at exactly the time the previous event ends.

## 3. Objectives

- Understand the Greedy strategy.
- Select compatible calendar events.
- Demonstrate Activity Selection.
- Analyze time complexity.

## 4. Algorithm

1. Sort all events by increasing finish time.
2. Initialize the selected-event list as empty.
3. Examine events in sorted order.
4. Select an event if its start time is greater than or equal to the end time of the last selected event.
5. Update the last selected event's end time.
6. Continue until all events have been examined.

## 5. Example

| Event | Start | End |
|---|---|---|
| A — Lecture | 9:00 AM | 10:00 AM |
| B — Meeting | 9:30 AM | 11:00 AM |
| C — Lab | 10:00 AM | 11:00 AM |
| D — Project work | 11:00 AM | 12:00 PM |
| E — Seminar | 10:30 AM | 12:00 PM |
| F — Tutorial | 12:00 PM | 1:00 PM |

The selected events are:

- A — Lecture (9:00–10:00 AM)
- C — Lab (10:00–11:00 AM)
- D — Project work (11:00 AM–12:00 PM)
- F — Tutorial (12:00–1:00 PM)

Total selected: **4 events**.

B overlaps with A. E overlaps with C. Therefore, they are not selected.

## 6. Python implementation

See [`activity_selection.py`](activity_selection.py).

## 7. Complexity analysis

| Operation | Time complexity |
|---|---|
| Sort events | O(n log n) |
| Select compatible events | O(n) |
| Total | O(n log n) |

If the events are already sorted by finishing time, the selection pass takes O(n).

## 8. Advantages

- Simple and efficient for this scheduling objective.
- Produces the maximum number of non-overlapping activities under the stated assumptions.
- Can help illustrate conflict-free scheduling.

## 9. Conclusion

The Activity Selection algorithm uses a Greedy strategy by repeatedly choosing the compatible event that finishes earliest. It finds an optimal solution when the goal is to maximize the number of non-overlapping events.

## 10. Real-world limitation

This is an educational model inspired by calendar scheduling. It does not represent the full internal scheduling system of Google Calendar, which handles invitations, time zones, recurring events, reminders, and user preferences.
