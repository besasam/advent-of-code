class Guard:
    def __init__(self, id: int):
        self.id = id
        self.shifts = dict()
        self.time_asleep = 0
        self.cur = None

    def start_shift(self, date):
        self.shifts[date] = []
        self.cur = date

    def sleep(self, time):
        self.shifts[self.cur].append([time])

    def wake(self, time):
        shift = self.shifts[self.cur][-1]
        shift.append(time)
        self.time_asleep += shift[1] - shift[0]

    def times_sleeping_at_minute(self, time):
        count = 0
        for shift in self.shifts:
            if self.is_asleep(shift, time):
                count += 1
        return count

    def most_sleep_at_minute(self):
        minute = 0
        times = 0
        for m in range(60):
            s = self.times_sleeping_at_minute(m)
            if s > times:
                minute = m
                times = s
        return {'minute': minute, 'times': times}

    def is_asleep(self, date, time):
        if date not in self.shifts:
            return False
        for interval in self.shifts[date]:
            if interval[0] <= time and (len(interval) == 1 or time < interval[1]):
                return True
        return False

    def __repr__(self):
        return f'{self.id} -- {self.shifts}'


def parse(line):
    res = dict()
    s = line.split()
    date = s[0].split('-')
    month = int(date[1])
    day = int(date[2])
    time = s[1].split(':')
    hour = int(time[0])
    minute = int(time[1][:-1])
    if hour == 23:
        day += 1
        minute = 0
    res['date'] = f'{month}-{day}'
    res['time'] = minute
    if s[2] == 'falls':
        action = 'sleep'
    elif s[2] == 'wakes':
        action = 'wake'
    else:
        action = 'start'
        res['guard'] = int(s[3][1:])
    res['action'] = action
    return res


def make_guards(data):
    guards = dict()
    current_guard = None
    for d in data:
        event = parse(d)
        if event['action'] == 'start':
            if event['guard'] not in guards:
                guards[event['guard']] = Guard(event['guard'])
            current_guard = guards[event['guard']]
            current_guard.start_shift(event['date'])
        elif event['action'] == 'sleep':
            current_guard.sleep(event['time'])
        else:
            current_guard.wake(event['time'])
    return guards


def part_1(data):
    guards = make_guards(data)
    total_asleep = 0
    guard = None
    for g in guards:
        if guards[g].time_asleep > total_asleep:
            total_asleep = guards[g].time_asleep
            guard = guards[g]
    minute = 0
    highest_asleep_at_minute = 0
    for m in range(60):
        s = guard.times_sleeping_at_minute(m)
        if s > highest_asleep_at_minute:
            highest_asleep_at_minute = s
            minute = m
    return guard.id * minute


def part_2(data):
    guards = make_guards(data)
    sleeping_guards = dict()
    for g in guards:
        sleeping_guards[g] = guards[g].most_sleep_at_minute()
    max_times = 0
    guard = None
    for g in sleeping_guards:
        if sleeping_guards[g]['times'] > max_times:
            max_times = sleeping_guards[g]['times']
            guard = g
    return guard*sleeping_guards[guard]['minute']


with open('input.txt') as f:
    data = sorted(f.read().splitlines())

print(part_2(data))