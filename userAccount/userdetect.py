def detectUser(user):
    if user.role==1:
        redirectUrl='venderdashbord'
        return redirectUrl
    elif user.role==2:
        redirectUrl='cousdashbord'
        return redirectUrl

        
    elif user.role==None and user.is_superuser:
        redirectUrl='/admin'
        return redirectUrl