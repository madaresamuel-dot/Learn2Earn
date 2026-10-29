def participant_cost(attendees, food_per_person, transport_per_person):
    total_participant_cost = attendees * (food_per_person + transport_per_person)
    return total_participant_cost

def event_total(attendees, food_per_person, transport_per_person, venue_cost):
    total = participant_cost(attendees, food_per_person, transport_per_person)
    return total + venue_cost

def budget_status (budget, total):
    if total < budget:
        return "Below budget"
    elif total == budget:
        return "Exactly equal to budget"
    else:
        return "Over budget"
