
from rest_framework. exceptions import AuthenticationFailed
import jwt
from .models import CustomUser

def authentication_user(self,request, role, privacy='private'):
    token = request.COOKIES.get('jwt')
    
    if not token:
        raise AuthenticationFailed('Unauthenticated, not a token')

    try:
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        
        if privacy == 'public':
            user = CustomUser.objects.filter(id=payload['id']).first()
        else:
            user = CustomUser.objects.filter(id=payload['id'], role=role).first()

            
        
        if user is None:
            raise AuthenticationFailed("Unauthenticated, not a user")
        user_id = CustomUser.objects.filter(email=user).values_list('id')[0][0]
            
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed('Unauthenticated, expired token')

    return payload, user, user_id



powers = ['Can view user']