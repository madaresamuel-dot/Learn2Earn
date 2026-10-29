def participant_cost(attendees, food_per_person, transport_per_person):
    total_participant_cost = attendees * (food_per_person + transport_per_person)
    return total_participant_cost

def event_total(attendees, food_per_person, transport_per_person, venue_cost):
    total = participant_cost(attendees, food_per_person, transport_per_person)
    return total + venue_cost