from django.shortcuts import render
from . import models
# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# make free to POST regardless of Token request from Django
from django.http import JsonResponse


def like_image(request, image_id):
    try:
        existing_like = models.Like.objects.get(
            image__id=image_id, user__id=request.user.id)
        # iamge__id /for searchig of 'image.id'
        existing_like.delete() 
        response = HttpResponse(status=204)

    except models.Like.DoesNotExist:
        found_image = models.Image.objects.get(id=image_id)
        new_like = models.Like.objects.create(
            user=request.user,
            image=found_image
        )
        new_like.save()
        response = HttpResponse(status=200)

    return response

@csrf_exempt
def comment_image(request, image_id):
    
    comment_to_save=request.POST.get('comment', None)

    if comment_to_save is not None:

        image = models.Image.objects.get(id=image_id)

        new_comment = models.Comment.objects.create(
            comment=comment_to_save,
            user=request.user,
            image=image
        )

        new_comment.save()

        response = JsonResponse({
            'comment': new_comment.comment,
            'user': new_comment.user.username
        })

    else:
        response = HttpResponse(status=406)

    return response

# 0) Create a url like: '/images/{ID_OF_IMAGE}/like/
# 1) Find a Like that exists with the image_id and the user_id
# 2) If the like doesnt exist, create a like
# 3) If the like is create return an HttpResponse with the status of 200
# 4) If it already exists don't creatie the like and return  an HttpResponse with the status of 400


def explore(request):
    if request.user.is_authenticated:
        users =  models.User.objects.exclude(id=request.user.id)
        context = {
            'users': users
        }
        return render(request, 'explore.html', context)
    else:
        response = HttpResponseRedirect(reverse('login'))
    return response