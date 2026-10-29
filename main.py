def participant_cost(attendees, food_per_person, transport_per_person):
    total_participant_cost = attendees * (food_per_person + transport_per_person)
    return total_participant_cost

# Component: participant_cost
# Returns: Total participant cost calculated by multiplying the number of attendees by the sum of food cost per person and transport cost per person.
# Tests run: Verified that the function calculates the total cost correctly using the provided inputs.
# Issue: None. The function works as expected.

def event_total(attendees, food_per_person, transport_per_person, venue_cost):
    total = participant_cost(attendees, food_per_person, transport_per_person)
    return total + venue_cost

# Component: event_total
# Returns: The total event cost, calculated by adding the venue cost to the total participant cost.
# Tests run: Verified that the function correctly calls participant_cost() and adds the venue cost to calculate the overall event budget.
# Issue: None. The function works as expected.

def budget_status (budget, total):
    if total < budget:
        return "Below budget"
    elif total == budget:
        return "Exactly equal to budget"
    else:
        return "Over budget" 
#Component: budget_status
#Returns: "Within budget" when total < budget, "Exactly equal to budget" when total == budget, otherwise "Over budget"
#Tests: below budget, exactbudget, over budget
#Issue: none


def event_summary(event_name, total, status):
    return f"{event_name}: total {total} naira. {status}." 

# Handover note
# Component: event_summary
# Returns: Exact readable summary:study day: total 15000 naira. Within budget
# Tests: "study day: total 15000 naira. Within budget."
# Issues: none   

attendees = 10
food_per_person = 800
transport_per_person = 200
venue_cost = 5000
budget = 16000

#Arguments from slide
people_cost = participant_cost(10, 800, 200)
print (people_cost)
total = event_total(10, 800, 200, 5000)
print (total)
status = budget_status(16000, total)
print (status)
summary = event_summary("Study Day", total, status)
print (summary)

# Example 1: participant_cost with a normal number of attendees
people_cost = participant_cost(10, 800, 200)
print(people_cost)  # Expected: 10000

# Example 2: participant_cost with zero attendees
people_cost_zero = participant_cost(0, 800, 200)
print(people_cost_zero)  # Expected: 0

# Example 3: event_total with normal attendee costs plus venue cost
total = event_total(10, 800, 200, 5000)
print(total)  # Expected: 15000

# Example 4: event_total with zero attendees but a non-zero venue cost
total_zero_attendees = event_total(0, 800, 200, 5000)
print(total_zero_attendees)  # Expected: 5000

# Example 5: budget_status when the total is below the budget
status_below = budget_status(16000, 15000)
print(status_below)  # Expected: Below budget

# Example 6: budget_status when the total equals the budget
status_equal = budget_status(16000, 16000)
print(status_equal)  # Expected: Exactly equal to budget

# Example 7: budget_status when the total is over the budget
status_over = budget_status(16000, 20000)
print(status_over)  # Expected: Over budget

# Example 8: event_summary using the required example
summary = event_summary("Study Day", 15000, "Below budget")
print(summary)  # Expected: Study Day: total 15000 naira, Below budget.

# Example 9: event_summary with a different event name and total
different_summary = event_summary("Wedding Party", 25000, "Over budget")
print(different_summary)  
# Expected: Wedding Party: total 25000 naira, Over budget.  