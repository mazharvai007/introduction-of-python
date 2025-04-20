from manager import Manager


class Developer(Manager):
    def display_expertise(self, lang_name: str):
        """
        It will display the employee department where he is working.
        """

        return f"He is expert on {lang_name} programming languages."


developer_obj = Developer(name="Rakib", employee_id=102)
print(developer_obj.display_info())
print(developer_obj.display_expertise(lang_name="Python, JavaScript"))
