import datetime

from django.http import HttpResponse
from django.views.generic import TemplateView

from lessons.models import ScheduleItem
from students.models import Class
from teachers.models import Workload


class FullSchedule(TemplateView):
    template_name = 'full_schedule.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        week = int(self.request.GET.get("week")) - 1
        sep1_week = datetime.date(year=datetime.date.today().year, month=9, day=1).isocalendar().week + week
        # В случае если 1 сентября не являестя понедельником, необходим первый день недели.
        first_day_on_school_year_week = datetime.datetime.strptime(f"{datetime.date.today().year}-W{sep1_week}" + '-1', "%Y-W%W-%w")
        context["date"] = {
            "monday": first_day_on_school_year_week.strftime("%Y-%m-%d"),
            "tuesday": (first_day_on_school_year_week + datetime.timedelta(days=1)).strftime("%Y-%m-%d"),
            "wednesday": (first_day_on_school_year_week + datetime.timedelta(days=2)).strftime("%Y-%m-%d"),
            "thursday": (first_day_on_school_year_week + datetime.timedelta(days=3)).strftime("%Y-%m-%d"),
            "friday": (first_day_on_school_year_week + datetime.timedelta(days=4)).strftime("%Y-%m-%d")
        }

        classes = [*Class.objects.all().order_by("year", "letter_id")]
        for klass in classes:

            items = ScheduleItem.objects.filter(workload__klass_id=klass)

            mondays = items.filter(date=context["date"]["monday"])
            klass.l1lm = mondays.filter(lesson_no=1)
            klass.l2lm = mondays.filter(lesson_no=2)
            klass.l3lm = mondays.filter(lesson_no=3)
            klass.l4lm = mondays.filter(lesson_no=4)
            klass.l5lm = mondays.filter(lesson_no=5)
            klass.l6lm = mondays.filter(lesson_no=6)
            klass.l7lm = mondays.filter(lesson_no=7)

            tuesdays = items.filter(date=context["date"]["tuesday"])
            klass.l1ltu = tuesdays.filter(lesson_no=1)
            klass.l2ltu = tuesdays.filter(lesson_no=2)
            klass.l3ltu = tuesdays.filter(lesson_no=3)
            klass.l4ltu = tuesdays.filter(lesson_no=4)
            klass.l5ltu = tuesdays.filter(lesson_no=5)
            klass.l6ltu = tuesdays.filter(lesson_no=6)
            klass.l7ltu = tuesdays.filter(lesson_no=7)

            wednesdays = items.filter(date=context["date"]["wednesday"])
            klass.l1lwd = wednesdays.filter(lesson_no=1)
            klass.l2lwd = wednesdays.filter(lesson_no=2)
            klass.l3lwd = wednesdays.filter(lesson_no=3)
            klass.l4lwd = wednesdays.filter(lesson_no=4)
            klass.l5lwd = wednesdays.filter(lesson_no=5)
            klass.l6lwd = wednesdays.filter(lesson_no=6)
            klass.l7lwd = wednesdays.filter(lesson_no=7)

            thursdays = items.filter(date=context["date"]["thursday"])
            klass.l1lth = thursdays.filter(lesson_no=1)
            klass.l2lth = thursdays.filter(lesson_no=2)
            klass.l3lth = thursdays.filter(lesson_no=3)
            klass.l4lth = thursdays.filter(lesson_no=4)
            klass.l5lth = thursdays.filter(lesson_no=5)
            klass.l6lth = thursdays.filter(lesson_no=6)
            klass.l7lth = thursdays.filter(lesson_no=7)

            fridays = items.filter(date=context["date"]["friday"])
            klass.l1lf = fridays.filter(lesson_no=1)
            klass.l2lf = fridays.filter(lesson_no=2)
            klass.l3lf = fridays.filter(lesson_no=3)
            klass.l4lf = fridays.filter(lesson_no=4)
            klass.l5lf = fridays.filter(lesson_no=5)
            klass.l6lf = fridays.filter(lesson_no=6)
            klass.l7lf = fridays.filter(lesson_no=7)

        context["classes"] = classes
        return context


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        class_ = self.request.GET.get("class")
        week = int(self.request.GET.get("week")) - 1

        context["meta"] = Class.objects.get(id=class_)
        sep1_week = datetime.date(year=datetime.date.today().year, month=9, day=1).isocalendar().week + week
        # В случае если 1 сентября не являестя понедельником, необходим первый день недели.
        first_day_on_school_year_week = datetime.datetime.strptime(f"{datetime.date.today().year}-W{sep1_week}" + '-1', "%Y-W%W-%w")
        context["meta_date_monday"] = first_day_on_school_year_week.strftime("%Y-%m-%d")
        context["meta_date_tuesday"] = (first_day_on_school_year_week + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
        context["meta_date_wednesday"] = (first_day_on_school_year_week + datetime.timedelta(days=2)).strftime("%Y-%m-%d")
        context["meta_date_thursday"] = (first_day_on_school_year_week + datetime.timedelta(days=3)).strftime("%Y-%m-%d")
        context["meta_date_friday"] = (first_day_on_school_year_week + datetime.timedelta(days=4)).strftime("%Y-%m-%d")

        items = ScheduleItem.objects.filter(workload__klass_id=class_)

        mondays = items.filter(date=context["meta_date_monday"])
        context["1_m"] = mondays.filter(lesson_no=1)
        context["2_m"] = mondays.filter(lesson_no=2)
        context["3_m"] = mondays.filter(lesson_no=3)
        context["4_m"] = mondays.filter(lesson_no=4)
        context["5_m"] = mondays.filter(lesson_no=5)
        context["6_m"] = mondays.filter(lesson_no=6)
        context["7_m"] = mondays.filter(lesson_no=7)

        tuesdays = items.filter(date=context["meta_date_tuesday"])
        context["1_tu"] = tuesdays.filter(lesson_no=1)
        context["2_tu"] = tuesdays.filter(lesson_no=2)
        context["3_tu"] = tuesdays.filter(lesson_no=3)
        context["4_tu"] = tuesdays.filter(lesson_no=4)
        context["5_tu"] = tuesdays.filter(lesson_no=5)
        context["6_tu"] = tuesdays.filter(lesson_no=6)
        context["7_tu"] = tuesdays.filter(lesson_no=7)

        wednesdays = items.filter(date=context["meta_date_wednesday"])
        context["1_wd"] = wednesdays.filter(lesson_no=1)
        context["2_wd"] = wednesdays.filter(lesson_no=2)
        context["3_wd"] = wednesdays.filter(lesson_no=3)
        context["4_wd"] = wednesdays.filter(lesson_no=4)
        context["5_wd"] = wednesdays.filter(lesson_no=5)
        context["6_wd"] = wednesdays.filter(lesson_no=6)
        context["7_wd"] = wednesdays.filter(lesson_no=7)

        thursdays = items.filter(date=context["meta_date_thursday"])
        context["1_th"] = thursdays.filter(lesson_no=1)
        context["2_th"] = thursdays.filter(lesson_no=2)
        context["3_th"] = thursdays.filter(lesson_no=3)
        context["4_th"] = thursdays.filter(lesson_no=4)
        context["5_th"] = thursdays.filter(lesson_no=5)
        context["6_th"] = thursdays.filter(lesson_no=6)
        context["7_th"] = thursdays.filter(lesson_no=7)

        fridays = items.filter(date=context["meta_date_friday"])
        context["1_f"] = fridays.filter(lesson_no=1)
        context["2_f"] = fridays.filter(lesson_no=2)
        context["3_f"] = fridays.filter(lesson_no=3)
        context["4_f"] = fridays.filter(lesson_no=4)
        context["5_f"] = fridays.filter(lesson_no=5)
        context["6_f"] = fridays.filter(lesson_no=6)
        context["7_f"] = fridays.filter(lesson_no=7)
        return context


def five_numbers_generator():
    while True:
        for i in range(1, 6):
            yield i


def four_numbers_generator():
    while True:
        for i in range(5):
            yield 1
        for i in range(5):
            yield 2
        for i in range(5):
            yield 3
        for i in range(5):
            yield 4
        for i in range(5):
            yield 5
        for i in range(5):
            yield 6
        for i in range(5):
            yield 7


def generate(request):
    ScheduleItem.objects.all().delete()
    first_available_date = datetime.date(year=datetime.date.today().year, month=9, day=4)
    week = 1
    while week < 18:
        for klass in Class.objects.all():
            day_offset_generator = five_numbers_generator()
            lesson_no_generator = four_numbers_generator()
            for workload in Workload.objects.filter(klass=klass).order_by("workload"):
                for item in range(workload.workload):
                    ScheduleItem.objects.create(
                        date=first_available_date + datetime.timedelta(days=next(day_offset_generator), weeks=(1 * week) - 1),
                        workload=workload,
                        lesson_no=next(lesson_no_generator))
        week += 1

    return HttpResponse("ok")
