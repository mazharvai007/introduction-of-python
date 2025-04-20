from senior_developer import Senior_Developer


# Subclass inheriting from Senior_Developer
class Team_Leader(Senior_Developer):
    pass  # Inherits all attributes and methods from Senior_Developer


team_leader_obj = Team_Leader(
    name="Sakib", employee_id=104, experience_level="Team Leader"
)
print(team_leader_obj.display_info())
print(f"Salary: {team_leader_obj.salary_calculation()}")
