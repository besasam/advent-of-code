import itertools
import math


class TicketScanner:
    def __init__(self, rules):
        self.rules = dict()
        for rule in rules:
            r = rule.split()
            field = r[0][:-1]
            r1 = tuple(int(x) for x in r[1].split('-'))
            r2 = tuple(int(x) for x in r[3].split('-'))
            self.rules[field] = [r1, r2]

    def find_rule_positions(self, all_ticket_strings):
        tickets = self.get_valid_tickets(all_ticket_strings)
        ticket_values = [self.get_ticket_values_at_position(tickets, i) for i in range(len(self.rules))]
        fields = dict()
        for rule in self.rules:
            fields[rule] = []
        c = 0
        for i, vals in enumerate(ticket_values):
            for rule in fields:
                if self.validate_one_rule_all_values(vals, rule):
                    fields[rule].append(i)
                    c += 1
        while c > len(fields):
            for rule in fields:
                if len(fields[rule]) == 1:
                    p = fields[rule][0]
                    for r in fields:
                        if r != rule and p in fields[r]:
                            fields[r].remove(p)
                            c -= 1
        return fields

    def get_ticket_values_at_position(self, all_tickets, pos):
        return [ticket[pos] for ticket in all_tickets]

    def get_valid_tickets(self, all_ticket_strings):
        return [[int(x) for x in ticket.split(',')] for ticket in all_ticket_strings if not self.validate_any_rule(ticket)]

    def validate_any_rule(self, ticket_string):
        ticket = [int(x) for x in ticket_string.split(',')]
        return [n for n in ticket if not any(self.validate_one_rule_one_value(n, rule) for rule in self.rules)]

    def validate_one_rule_one_value(self, n, rule):
        r1, r2 = self.rules[rule][0], self.rules[rule][1]
        if r1[0] <= n <= r1[1] or r2[0] <= n <= r2[1]:
            return True
        return False

    def validate_one_rule_all_values(self, vals, rule):
        for v in vals:
            if not self.validate_one_rule_one_value(v, rule):
                return False
        return True


def part_1(data):
    ts = TicketScanner(data[0])
    tickets = data[2][1:]
    res = 0
    for t in tickets:
        res += sum(ts.validate_any_rule(t))
    return res


def part_2(data):
    ts = TicketScanner(data[0])
    tickets = data[2][1:]
    rules = ts.find_rule_positions(tickets)
    positions = [rules[r][0] for r in rules if r[:9] == 'departure']
    own_ticket = [int(x) for x in data[1][1:][0].split(',')]
    return math.prod([own_ticket[p] for p in positions])


with open('input.txt') as f:
    data = [list(l) for e, l in itertools.groupby(f.read().splitlines(), key=bool) if e]

print(part_2(data))
