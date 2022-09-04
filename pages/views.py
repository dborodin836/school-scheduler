import datetime

from django.http import HttpResponse
from django.views.generic import TemplateView

from lessons.models import ScheduleItem
from students.models import Class
from teachers.models import Workload


class FullSchedule(TemplateView):
    template_name = 'full_schedule.html'


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
        context["4_f"] = fridays.filter(lesson_no=5)
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
    first_available_date = datetime.date(year=datetime.date.today().year, month=9, day=4)
    week = 1
    while week < 18:
        day_offset_generator = five_numbers_generator()
        lesson_no_generator = four_numbers_generator()
        for workload in Workload.objects.all().order_by('workload'):
            for item in range(workload.workload):
                ScheduleItem.objects.create(
                    date=first_available_date + datetime.timedelta(days=next(day_offset_generator), weeks=(1 * week) - 1),
                    workload=workload,
                    lesson_no=next(lesson_no_generator))
        week += 1

    return HttpResponse("ok")
