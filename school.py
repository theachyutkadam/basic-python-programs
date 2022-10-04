# Assignments
# 1. Create Class Diagram with Data Types only - Done
# 2. Add interfaces in Class Diagram - Done
# 3. Implement interface to add School - Done
# 4. Implement interface to add ClassRoom - uncheck Done
# 5. Implement interface to List ClassRooms of School - uncheck Done
# 6. Implement interface to add 1 Student in ClassRoom - uncheck Done
# 7. Implement interface to add n  Students in ClassRoom - uncheck Done
# 8. Implement interface to list Students of ClassRoom
# 9. Implement interface to sort Students of ClassRoom

class School:
  school_name = []
  def __init__(self, name) -> None:
    self.name = name

  def add(name):
    self.school_name.append(name)

  def show(self):
    print(self.name)
    print(self.school_name)

s1 = School("anisha")
# print(s1.show.name)
s1.add("microsoft")
s1.show()
