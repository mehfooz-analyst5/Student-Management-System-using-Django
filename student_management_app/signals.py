from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import User, AdminHOD, Staff, Student



@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs): 
    if created:
        if instance.user_type==1:
            AdminHOD.objects.create(admin=instance)
        if instance.user_type==2:
            Staff.objects.create(admin=instance)
        if instance.user_type==3:
            Student.objects.create(admin=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs): 
    if instance.user_type==1:
        instance.adminhod.save()
    if instance.user_type==2:
        instance.staff.save()
    if instance.user_type==3:
        instance.student.save()
