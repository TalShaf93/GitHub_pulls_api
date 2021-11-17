from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import json

from github_pulls.models import Pull_request

def index(request):
    response = json.dumps([{}])
    return HttpResponse(response, content_type='text/json')

@csrf_exempt
def add_pull(request):
    if request.method =='POST':
        payload = json.loads(request.body[0])
        pull_request_id = payload['id']
        number = payload['number']
        url = payload['html_url']
        state = payload['state']
        locked = payload['locked']
        title = payload['title']
        user = payload['user.login']
        is_admin = payload['user.site_admin']
        body = payload['body']
        created_at = payload['created_at']
        updated_at = payload['updated_at']
        closed_at = payload['closed_at']
        merged_at = payload['merged_at']
        pull_request = Pull_request(pull_request_id=pull_request_id,number=number, url=url, state=state, locked=locked, title=title,
                                    user=user, is_admin=is_admin, body=body, created_at=created_at, updated_at=updated_at, closed_at=closed_at, merged_at=merged_at )
        try:
            pull_request.save()
            response = json.dumps([{'Success': 'Pull addded'}])
        except:
            response = json.dumps([{'Error': 'Pull could not be added'}])
    return HttpResponse(response, content_type='text/json')

