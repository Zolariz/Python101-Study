class Job:
    def __init__(self, job_name, description, skills):
        self.job_name = job_name
        self.description = description
        self.skills = skills

    def get_job_name(self):
        return self.job_name

    def get_description(self):
        return self.description

    def get_skills(self):
        return self.skills


class Thief(Job):
    def __init__(self):
        job_name = "Thief"
        description = "A sneaky and agile fighter who is adept at stealing and hiding."
        skills = ["Double Attack", "Steal", "Hiding"]
        super().__init__(job_name, description, skills)


class Swordsman(Job):
    def __init__(self):
        job_name = "Swordsman"
        description = "A melee fighter who wields a sword."
        skills = ["Bash", "Magnum Break", "Provoke"]
        super().__init__(job_name, description, skills)


class Mage(Job):
    def __init__(self):
        job_name = "Mage"
        description = "A spellcaster who can cast powerful spells."
        skills = ["Fire Bolt", "Cold Bolt", "Lightning Bolt"]
        super().__init__(job_name, description, skills)


class Character:
    def __init__(self, name, level, job):
        self.name = name
        self.level = level
        self.job = job

    def get_name(self):
        return self.name

    def get_level(self):
        return self.level

    def get_job_name(self):
        return self.job.get_name()

    def get_job_description(self):
        return self.job.get_description()

    def get_skills(self):
        return self.job.get_skills()


# Instance
# สร้าง object ของ Swordman และ Mage
job1 = Thief()
job2 = Swordsman()
job3 = Mage()

print('===================')

char1 = Character('Zolariz', 59, job1)
print(f'ชื่อตัวละคร {char1.get_name()}')
print(f'เลเวล {char1.get_level()}')
print(f'อาชีพ {job1.get_job_name()}')
print(f'รายละเอียดอาชีพ {char1.get_job_description()}')
print(f'สกิลที่สามารถใช้ได้ {char1.get_skills()}')
print('===================')

char2 = Character('Zephyr', 72, job2)
print(f'ชื่อตัวละคร {char2.get_name()}')
print(f'เลเวล {char2.get_level()}')
print(f'อาชีพ {job2.get_job_name()}')
print(f'รายละเอียดอาชีพ {char2.get_job_description()}')
print(f'สกิลที่สามารถใช้ได้ {char2.get_skills()}')
print('===================')

char3 = Character('Cloud', 99, job3)
print(f'ชื่อตัวละคร {char3.get_name()}')
print(f'เลเวล {char3.get_level()}')
print(f'อาชีพ {job3.get_job_name()}')
print(f'รายละเอียดอาชีพ {char3.get_job_description()}')
print(f'สกิลที่สามารถใช้ได้ {char3.get_skills()}')
print('===================')
