import unittest
from datetime import datetime


class CalendarTestAddEvent(unittest.TestCase):
    def test_add_event(self):
        calendar = CalendarUtil()
        calendar.add_event({'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0),
                            'end_time': datetime(2023, 1, 1, 1, 0), 'description': 'New Year'})
        self.assertEqual(calendar.events, [
            {'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0),
             'end_time': datetime(2023, 1, 1, 1, 0), 'description': 'New Year'}])

    def test_add_event_2(self):
        calendar = CalendarUtil()
        calendar.add_event({'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0),
                            'end_time': datetime(2023, 1, 1, 1, 0), 'description': 'New Year'})
        calendar.add_event({'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0),
                            'end_time': datetime(2023, 1, 1, 1, 0), 'description': 'New Year'})
        self.assertEqual(calendar.events, [
            {'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0),
             'end_time': datetime(2023, 1, 1, 1, 0), 'description': 'New Year'},
            {'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0),
             'end_time': datetime(2023, 1, 1, 1, 0), 'description': 'New Year'}])

    def test_add_event_3(self):
        calendar = CalendarUtil()
        calendar.add_event({'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0),
                            'end_time': datetime(2023, 1, 1, 23, 0), 'description': 'New Year'})
        self.assertEqual(calendar.events, [
            {'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0),
             'end_time': datetime(2023, 1, 1, 23, 0), 'description': 'New Year'}])

    def test_add_event_4(self):
        calendar = CalendarUtil()
        calendar.add_event({'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0),
                            'end_time': datetime(2023, 1, 1, 22, 0), 'description': 'New Year'})
        self.assertEqual(calendar.events, [
            {'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0),
             'end_time': datetime(2023, 1, 1, 22, 0), 'description': 'New Year'}])

    def test_add_event_5(self):
        calendar = CalendarUtil()
        calendar.add_event({'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0),
                            'end_time': datetime(2023, 1, 1, 20, 0), 'description': 'New Year'})
        self.assertEqual(calendar.events, [
            {'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0),
             'end_time': datetime(2023, 1, 1, 20, 0), 'description': 'New Year'}])


class CalendarTestRemoveEvent(unittest.TestCase):
    def test_remove_event(self):
        calendar = CalendarUtil()
        calendar.events = [{'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0),
                            'end_time': datetime(2023, 1, 1, 1, 0), 'description': 'New Year'}]
        calendar.remove_event({'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0),
                               'end_time': datetime(2023, 1, 1, 1, 0), 'description': 'New Year'})
        self.assertEqual(calendar.events, [])

    def test_remove_event_2(self):
        calendar = CalendarUtil()
        calendar.events = [{'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0),
                            'end_time': datetime(2023, 1, 1, 1, 0), 'description': 'New Year'},
                           {'date': datetime(2023, 1, 2, 0, 0), 'start_time': datetime(2023, 1, 2, 0, 0),
                            'end_time': datetime(2023, 1, 2, 1, 0), 'description': 'New Year'}]
        calendar.remove_event({'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0),
                               'end_time': datetime(2023, 1, 1, 1, 0), 'description': 'New Year'})
        self.assertEqual(calendar.events, [
            {'date': datetime(2023, 1, 2, 0, 0), 'start_time': datetime(2023, 1, 2, 0, 0),
             'end_time': datetime(2023, 1, 2, 1, 0), 'description': 'New Year'}])

    def test_remove_event_3(self):
        calendar = CalendarUtil()
        calendar.events = [{'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0),
                            'end_time': datetime(2023, 1, 1, 1, 0), 'description': 'New Year'},
                           {'date': datetime(2023, 1, 2, 0, 0), 'start_time': datetime(2023, 1, 2, 0, 0),
                            'end_time': datetime(2023, 1, 2, 1, 0), 'description': 'New Year'}]
        calendar.remove_event({'date': datetime(2023, 1, 2, 0, 0), 'start_time': datetime(2023, 1, 2, 0, 0),
                               'end_time': datetime(2023, 1, 2, 1, 0), 'description': 'New Year'})
        self.assertEqual(calendar.events, [
            {'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0),
             'end_time': datetime(2023, 1, 1, 1, 0), 'description': 'New Year'}])

    def test_remove_event_4(self):
        calendar = CalendarUtil()
        calendar.events = [{'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0),
                            'end_time': datetime(2023, 1, 1, 23, 0), 'description': 'New Year'},
                           {'date': datetime(2023, 1, 2, 0, 0), 'start_time': datetime(2023, 1, 2, 0, 0),
                            'end_time': datetime(2023, 1, 2, 1, 0), 'description': 'New Year'}]
        calendar.remove_event({'date': datetime(2023, 1, 2, 0, 0), 'start_time': datetime(2023, 1, 2, 0, 0),
                               'end_time': datetime(2023, 1, 2, 1, 0), 'description': 'New Year'})
        self.assertEqual(calendar.events, [
            {'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0),
             'end_time': datetime(2023, 1, 1, 23, 0), 'description': 'New Year'}])

    def test_remove_event_5(self):
        calendar = CalendarUtil()
        calendar.events = [{'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0),
                            'end_time': datetime(2023, 1, 1, 22, 0), 'description': 'New Year'},
                           {'date': datetime(2023, 1, 2, 0, 0), 'start_time': datetime(2023, 1, 2, 0, 0),
                            'end_time': datetime(2023, 1, 2, 1, 0), 'description': 'New Year'}]
        calendar.remove_event({'date': datetime(2023, 1, 2, 0, 0), 'start_time': datetime(2023, 1, 2, 0, 0),
                               'end_time': datetime(2023, 1, 2, 1, 0), 'description': 'New Year'})
        self.assertEqual(calendar.events, [
            {'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0),
             'end_time': datetime(2023, 1, 1, 22, 0), 'description': 'New Year'}])

    def test_remove_event_6(self):
        calendar = CalendarUtil()
        calendar.events = []
        calendar.remove_event({'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0),
                               'end_time': datetime(2023, 1, 1, 1, 0), 'description': 'New Year'})
        self.assertEqual(calendar.events, [])


class CalendarTestGetEvents(unittest.TestCase):
    def test_get_events(self):
        calendar = CalendarUtil()
        calendar.events = [{'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0),
                            'end_time': datetime(2023, 1, 1, 1, 0), 'description': 'New Year'}]
        self.assertEqual(calendar.get_events(datetime(2023, 1, 1)), [
            {'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0),
             'end_time': datetime(2023, 1, 1, 1, 0), 'description': 'New Year'}])

    def test_get_events_2(self):
        calendar = CalendarUtil()
        calendar.events = [{'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0),
                            'end_time': datetime(2023, 1, 1, 1, 0), 'description': 'New Year'}]
        self.assertEqual(calendar.get_events(datetime(2023, 1, 2)), [])


class CalendarTestIsAvailable(unittest.TestCase):
    def test_is_available(self):
        calendar = CalendarUtil()
        calendar.events = [{'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0),
                            'end_time': datetime(2023, 1, 1, 1, 0), 'description': 'New Year'}]
        self.assertEqual(calendar.is_available(datetime(2023, 1, 1, 0, 0), datetime(2023, 1, 1, 1, 0)), False)

    def test_is_available_2(self):
        calendar = CalendarUtil()
        calendar.events = [{'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0),
                            'end_time': datetime(2023, 1, 1, 1, 0), 'description': 'New Year'}]
        self.assertEqual(calendar.is_available(datetime(2023, 1, 1, 1, 0), datetime(2023, 1, 1, 2, 0)), True)

    def test_is_available_3(self):
        calendar = CalendarUtil()
        calendar.events = [{'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0),
                            'end_time': datetime(2023, 1, 1, 1, 0), 'description': 'New Year'}]
        self.assertEqual(calendar.is_available(datetime(2023, 1, 1, 0, 0), datetime(2023, 1, 1, 0, 30)), False)

    def test_is_available_4(self):
        calendar = CalendarUtil()
        calendar.events = [{'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0),
                            'end_time': datetime(2023, 1, 1, 1, 0), 'description': 'New Year'}]
        self.assertEqual(calendar.is_available(datetime(2023, 1, 1, 0, 30), datetime(2023, 1, 1, 1, 0)), False)

    def test_is_available_5(self):
        calendar = CalendarUtil()
        calendar.events = [{'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0),
                            'end_time': datetime(2023, 1, 1, 1, 0), 'description': 'New Year'}]
        self.assertEqual(calendar.is_available(datetime(2023, 1, 1, 1, 0), datetime(2023, 1, 1, 1, 30)), True)


class CalendarTestGetAvailableSlots(unittest.TestCase):
    def test_get_available_slots(self):
        calendar = CalendarUtil()
        calendar.events = [{'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0),
                            'end_time': datetime(2023, 1, 1, 23, 0), 'description': 'New Year'}]
        self.assertEqual(calendar.get_available_slots(datetime(2023, 1, 1)),
                         [(datetime(2023, 1, 1, 23, 0), datetime(2023, 1, 2, 0, 0))])

    def test_get_available_slots_2(self):
        calendar = CalendarUtil()
        calendar.events = [{'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 1, 0),
                            'end_time': datetime(2023, 1, 1, 2, 0), 'description': 'New Year'}]
        self.assertEqual(len(calendar.get_available_slots(datetime(2023, 1, 1))), 23)

    def test_get_available_slots_3(self):
        calendar = CalendarUtil()
        calendar.events = [{'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 2, 1, 0),
                            'end_time': datetime(2023, 1, 2, 2, 0), 'description': 'New Year'}]
        self.assertEqual(len(calendar.get_available_slots(datetime(2023, 1, 1))), 24)

    def test_get_available_slots_4(self):
        calendar = CalendarUtil()
        calendar.events = [{'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 2, 1, 0),
                            'end_time': datetime(2023, 1, 2, 2, 0), 'description': 'New Year'}]
        self.assertEqual(len(calendar.get_available_slots(datetime(2023, 1, 1))), 24)

    def test_get_available_slots_5(self):
        calendar = CalendarUtil()
        calendar.events = [{'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 2, 1, 0),
                            'end_time': datetime(2023, 1, 2, 2, 0), 'description': 'New Year'}]
        self.assertEqual(len(calendar.get_available_slots(datetime(2023, 1, 1))), 24)


class CalendarTestGetUpcomingEvents(unittest.TestCase):
    def test_get_upcoming_events(self):
        calendar = CalendarUtil()
        calendar.events = [{'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0),
                            'end_time': datetime(2023, 1, 1, 23, 0), 'description': 'New Year'}]
        self.assertEqual(calendar.get_upcoming_events(1), [])

    def test_get_upcoming_events_2(self):
        calendar = CalendarUtil()
        calendar.events = [{'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 1, 0),
                            'end_time': datetime(2023, 1, 1, 2, 0), 'description': 'New Year'}]
        self.assertEqual(calendar.get_upcoming_events(1), [])

    def test_get_upcoming_events_3(self):
        calendar = CalendarUtil()
        calendar.events = [{'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 2, 1, 0),
                            'end_time': datetime(2023, 1, 2, 2, 0), 'description': 'New Year'}]
        self.assertEqual(calendar.get_upcoming_events(1), [])

    def test_get_upcoming_events_4(self):
        calendar = CalendarUtil()
        calendar.events = [{'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 2, 1, 0),
                            'end_time': datetime(2023, 1, 2, 2, 0), 'description': 'New Year'}]
        self.assertEqual(calendar.get_upcoming_events(2), [])

    def test_get_upcoming_events_5(self):
        calendar = CalendarUtil()
        calendar.events = [{'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0),
                            'end_time': datetime(2023, 1, 1, 23, 0), 'description': 'New Year'},
                           {'date': datetime(2024, 1, 2, 0, 0), 'start_time': datetime(2024, 1, 2, 1, 0),
                            'end_time': datetime(2024, 1, 2, 2, 0),
                            'description': 'New Year 2'}]
        self.assertEqual(calendar.get_upcoming_events(1), [
            {'date': datetime(2024, 1, 2, 0, 0), 'start_time': datetime(2024, 1, 2, 1, 0),
             'end_time': datetime(2024, 1, 2, 2, 0), 'description': 'New Year 2'}])


class CalendarTestMain(unittest.TestCase):
    def test_main(self):
        calendar = CalendarUtil()
        calendar.add_event({'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0),
                            'end_time': datetime(2023, 1, 1, 1, 0), 'description': 'New Year'})
        self.assertEqual(calendar.events, [
            {'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0),
             'end_time': datetime(2023, 1, 1, 1, 0), 'description': 'New Year'}])
        calendar.remove_event({'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0),
                               'end_time': datetime(2023, 1, 1, 1, 0), 'description': 'New Year'})
        self.assertEqual(calendar.events, [])
        calendar.events = [{'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0),
                            'end_time': datetime(2023, 1, 1, 23, 0), 'description': 'New Year'}]
        self.assertEqual(calendar.get_events(datetime(2023, 1, 1)), [
            {'date': datetime(2023, 1, 1, 0, 0), 'start_time': datetime(2023, 1, 1, 0, 0),
             'end_time': datetime(2023, 1, 1, 23, 0), 'description': 'New Year'}])
        self.assertEqual(calendar.is_available(datetime(2023, 1, 1, 0, 0), datetime(2023, 1, 1, 1, 0)), False)
        self.assertEqual(calendar.get_available_slots(datetime(2023, 1, 1)),
                         [(datetime(2023, 1, 1, 23, 0), datetime(2023, 1, 2, 0, 0))])
        self.assertEqual(calendar.get_upcoming_events(1), [])

