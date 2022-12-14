import datetime

from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse
from django.views.generic import TemplateView

from lessons.models import ScheduleItem
from students.models import Class
from teachers.models import Workload

from loguru import logger


class FullSchedule(TemplateView):
    template_name = 'full_schedule.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        week = int(self.request.GET.get("week")) - 1
        context["week"] = {
            "next": week + 2,
            "prev": week
        }

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
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["classes"] = Class.objects.all().order_by("year", "letter_id")
        return context


class FullScheduleV2(TemplateView):
    template_name = "full_schedule_v2.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        week = int(self.request.GET.get("week")) - 1
        context["week"] = {
            "next": week + 2,
            "prev": week
        }

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


class PerClassScheduleView(TemplateView):
    template_name = 'per_class_schedule.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        class_ = self.request.GET.get("class")
        week = int(self.request.GET.get("week")) - 1

        context["week"] = {
            "next": week + 2,
            "prev": week
        }
        context["class"] = class_

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
    for i in range(1, 6):
        yield i
    yield 5


def week_day_generator():
    while True:
        for i in range(1, 8):
            for _ in range(5):
                yield i


def get_available_lesson_num_week(monday_date: datetime.datetime | datetime.date, workload: Workload):
    gen = iter(range(0, 6))
    iteration = next(gen)
    print(iteration)
    date = monday_date + datetime.timedelta(days=iteration)
    while True:
        available_lessons_no = workload.teacher.get_available_lessons(date)
        query = ScheduleItem.objects.filter(workload__klass=workload.klass,
                                            date=date).values_list("lesson_no")
        query = set(map(lambda x: int(x[0]), query))
        available_lessons_no = list(set(available_lessons_no).difference(query))
        if available_lessons_no is None:
            try:
                next(gen)
            except StopIteration:
                raise Exception(f"Слишком много часов у {workload.teacher}")
            continue
        break
    return available_lessons_no


@user_passes_test(lambda user: user.is_superuser, login_url="/home/")
def generate(request):
    WEEK_AMOUNT = 2

    # Delete all the cells in schedule
    ScheduleItem.objects.all().delete()

    first_available_date = datetime.date(year=datetime.date.today().year, month=9, day=4)
    for week in range(1, WEEK_AMOUNT):

            for workload in Workload.objects.filter(workload__range=[1, 40]).order_by("workload"):
                day_offset_generator_int = five_numbers_generator()

                for item in range(int(workload.workload)):

                    try:
                        date_to_create = first_available_date + datetime.timedelta(
                            days=next(day_offset_generator_int),
                            weeks=(1 * week) - 1
                        )
                    except StopIteration:
                        day_offset_generator_int = five_numbers_generator()
                        date_to_create = first_available_date + datetime.timedelta(
                            days=next(day_offset_generator_int),
                            weeks=(1 * week) - 1
                        )

                    # Finding the available lesson number
                    while True:
                        available_lessons_no = workload.teacher.get_available_lessons(date_to_create)
                        logger.debug(f"Date {date_to_create} | {workload} | iter {item}")

                        if available_lessons_no is None:
                            available_lessons_no = {}

                        query = ScheduleItem.objects.filter(workload__klass=workload.klass,
                                                            date=date_to_create).values_list("lesson_no")
                        query = set(map(lambda x: int(x[0]), query))
                        available_lessons_no = list(set(available_lessons_no).difference(query))
                        logger.debug(f"Lesson No. {available_lessons_no}")

                        if available_lessons_no is None or not available_lessons_no:

                            try:
                                date_to_create = first_available_date + datetime.timedelta(
                                    days=next(day_offset_generator_int),
                                    weeks=(1 * week) - 1
                                )
                            except StopIteration:
                                date_monday = first_available_date + datetime.timedelta(weeks=(1 * week) - 1)
                                available_lessons_no = get_available_lesson_num_week(date_monday, workload)
                                break

                            continue
                        break

                    lesson_no_to_create = available_lessons_no[0]

                    ScheduleItem.objects.create(date=date_to_create,
                                                workload=workload,
                                                lesson_no=lesson_no_to_create)

    return HttpResponse("<h1>Рассписание успешно сгенерировано!</h1><a href='/home'>← Домой</a>")
