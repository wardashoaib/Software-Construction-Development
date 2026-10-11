def check_bonus_eligibility(active, months, rating, disciplinary_action, attendance):
    has_required_months = months >= 12
    has_required_rating = rating >= 4
    has_good_attendance = attendance >= 90
    has_no_disciplinary_action = not disciplinary_action

    return active and has_required_months and has_required_rating and has_good_attendance and has_no_disciplinary_action


print("Normal Case:")
print(check_bonus_eligibility(True, 15, 5, False, 95))

print("Boundary Case:")
print(check_bonus_eligibility(True, 12, 4, False, 90))

print("Failing Case:")
print(check_bonus_eligibility(True, 10, 4, False, 90))

print("Disciplinary Case:")
print(check_bonus_eligibility(True, 15, 5, True, 95))