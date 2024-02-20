# from django.http import HttpResponseRedirect
# from django.urls import reverse
# from django.utils.deprecation import MiddlewareMixin


# class LoginCheckMiddleWares(MiddlewareMixin):

#     def process_view(self,request,view_func,view_args,view_kwargs):
#         modulename=view_func.__module__

#         user=request.user
#         if user.is_authenticated:
#             if user.user_type == "1":
#                 if modulename == "student_management_app.views":
#                     pass
#                 else:
#                     return HttpResponseRedirect(reverse("hod-admin"))
                
#             elif user.user_type == "2":
#                 if modulename == "student_management_app.views":
#                     pass
#                 else:
#                     return HttpResponseRedirect(reverse("staff-admin"))
                
#             elif user.user_type == "3":
#                 if  modulename == "student_management_app.views":
#                     pass
#                 else:
#                     return HttpResponseRedirect(reverse("student-home"))
#             else:
#                 return HttpResponseRedirect(reverse("login"))

#         else:
#             if request.path == reverse("login") or request.path == reverse("login"):
#                 pass
#             else:
#                 return HttpResponseRedirect(reverse("login"))