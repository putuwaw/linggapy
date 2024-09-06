from .pangater import rule_1, rule_2, rule_3, rule_4, rule_5, rule_6


class Pengater:
    def __init__(self) -> None:
        self.rules = []
        self.rules.append(rule_1.Rule1())
        self.rules.append(rule_2.Rule2())
        self.rules.append(rule_3.Rule3())
        self.rules.append(rule_4.Rule4())
        self.rules.append(rule_5.Rule5())
        self.rules.append(rule_6.Rule6())
