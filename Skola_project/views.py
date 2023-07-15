from django.shortcuts import render, redirect
from django.contrib import messages
from Skola_app.models import Categories, Course, Level, UserCourse
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from Skola_app.EmailBackend import EmailBackend
from django.db.models import Sum


def BASE(req):
    return render(req, 'base.html')


def HOME(req):
    category = Categories.objects.all().order_by('id')[0:5]
    course = Course.objects.filter(status='PUBLISH').order_by('id')

    context = {
        'category': category,
        'course': course,

    }

    return render(req, 'main/home.html', context)


def SINGLE_COURSE(req):
    category = Categories.get_all_category(Categories)
    level = Level.objects.all()
    course = Course.objects.all()
    FreeCourse_count = Course.objects.filter(price=0).count()
    PaidCourse_count = Course.objects.filter(price__gte=1).count

    context = {
        'category': category,
        'level': level,
        'course': course,
        'FreeCourse_count': FreeCourse_count,
        'PaidCourse_count': PaidCourse_count,

    }
    return render(req, 'main/single_course.html', context)


def filter_data(request):
    category = request.GET.getlist('category[]')
    level = request.GET.getlist('level[]')
    price = request.GET.getlist('price[]')

    if price == ['PriceFree']:
        course = Course.objects.filter(price=0)
    elif price == ['PricePaid']:
        course = Course.objects.filter(price__gte=1)
    elif price == ['PriceAll']:
        course = Course.objects.all()

    elif category:
        course = Course.objects.filter(
            category__id__in=category).order_by('-id')

    elif level:
        course = Course.objects.filter(level__id__in=level).order_by('-id')

    else:
        course = Course.objects.all().order_by('-id')

    t = render_to_string('ajax/course.html', {'course': course})

    return JsonResponse({'data': t})


def CONTECT_US(req):
    category = Categories.get_all_category(Categories)

    context = {
        'category': category,
    }
    return render(req, 'main/contect_us.html', context)


def ABOUT_US(req):
    category = Categories.get_all_category(Categories)

    context = {
        'category': category,
    }
    return render(req, 'main/about_us.html', context)


def RESET(req):
    return render(req, 'registration/password_reset.html')


# def LOGOUT(req):
    return render(req, 'registration/logout.html')


def SEARCH_COURSE(req):
    query = req.GET['query']
    course = Course.objects.filter(title__icontains=query)
    print(course)
    context = {
        'course': course,
    }

    return render(req, 'search/search.html', context)


def COURSE_DETAILS(req, slug):
    category = Categories.get_all_category(Categories)
    # time_duration = Video.objects.filter(
    # course__slug=slug).aggregate(sum=sum('time_duration'))
    course_id = Course.objects.get(slug=slug)
    try:
        check_enroll = UserCourse.objects.get(user=req.user, course=course_id)
    except UserCourse.DoesNotExist:
        check_enroll = None
    course = Course.objects.filter(slug=slug)
    if course.exists():
        course = course.first()
    else:
        return redirect('404')

    context = {
        'course': course,
        'category': category,
        'check_enroll': check_enroll,
        # 'time_duration': time_duration,

    }

    return render(req, 'course/course_details.html', context)


def PAGE_NOT_FOUND(req):
    category = Categories.get_all_category(Categories)

    context = {
        'category': category,
    }
    return render(req, 'error/404.html', context)


def CHECKOUT(req, slug):
    course = Course.objects.get(slug=slug)

    if course.price == 0:
        course = UserCourse(
            user=req.user,
            course=course,
        )
        course.save()
        messages.success(req, 'Courses Are Successfully Enrolled !')
        return redirect('my_course')
    return render(req, 'checkout/checkout.html')


def MY_COURSE(req):
    course = UserCourse.objects.filter(user=req.user)
    context = {
        'course': course,
    }
    return render(req, 'course/my_course.html', context)


# def WATCH_COURSE(req, slug):
    course = Course.objects.filter(slug=slug)
    lecture = req.GET.get('lecture')
    video = Video.objects.get(id=lecture)

    if course.exists():
        course = course.first()
    else:
        return redirect('404')

    context = {
        'course': course,
        'video': video
    }
    return render(req, 'course/watch_course.html', context)
