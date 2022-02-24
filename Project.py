class Project:
  def __init__(self, required, score, deadline, roles):
    self.skill = required
    self.score = score
    self.deadline = deadline
    self.roles = []
  def add_role(self, new):
    self.roles.append(new)
