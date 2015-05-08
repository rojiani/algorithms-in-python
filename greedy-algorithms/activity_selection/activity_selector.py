ID = 0
S_i = 1
F_i = 2

def sort_by_endtime(activities):
    return sorted(activities, key=lambda x: x[F_i])

def activity_selection():
    # List of activities - (i, s_i, f_i)
    activities = [(1, 1, 4), (2, 3, 5),  (3, 0, 6),   (4, 5, 7),   (5, 3, 9), \
                  (6, 5, 9), (7, 6, 10), (8, 8, 11), (9, 8, 12), (10, 2, 14), \
                  (11, 12, 16)]
    schedule_activities(activities)

def schedule_activities(activities):
    activities = sort_by_endtime(activities)
    schedule = []
    schedule.append(activities[0])
    prev_event = activities[0]
    for event in activities:
        if is_compatible(prev_event, event):
            schedule.append(event)
            prev_event = event
    print_schedule(schedule)
    return schedule


# True if a2 can be scheduled after a1
def is_compatible(a1, a2):
    return a1[F_i] <= a2[S_i]

def print_schedule(schedule):
    for i in range(len(schedule)):
        print("%d: Event #%d %d - %d" % ((i+1), schedule[i][ID], schedule[i][S_i], schedule[i][F_i]))


activity_selection()