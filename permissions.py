import time
import functools
import jnius

''' 
    You can call this function with a list of permissions you want to request.
    For example, if you want to get permissions for reading from gallery
    and for the camera, you can call:

    perms = ["android.permission.READ_EXTERNAL_STORAGE", "android.permission.CAMERA"]
    haveperms = acquire_permissions(perms)

    (This function will block until the permissions dialog is answered. 
    If the app already has the permission, the function returns immediately.)

    Initialize Buildozer: Navigate to your project directory and 
    run buildozer init to create a buildozer.spec file controlling your build configuration. 
    You should edit it appropriately with your app name, etc.

    In your buildozer.spec file, you can specify the Android permissions 
    your app needs in the android.permissions option. 
    If you want to request camera and read file permissions, you can add the following line:

    android.permissions = CAMERA,READ_EXTERNAL_STORAGE

'''

def acquire_permissions(permissions, timeout=30):
    PythonActivity = jnius.autoclass('org.kivy.android.PythonActivity')
    Compat = jnius.autoclass('android.support.v4.content.ContextCompat')
    currentActivity = jnius.cast('android.app.Activity', PythonActivity.mActivity)

    checkperm = functools.partial(Compat.checkSelfPermission, currentActivity)

    def allgranted(permissions):
        return reduce(lambda a, b: a and b, [True if p == 0 else False for p in map(checkperm, permissions)])

    haveperms = allgranted(permissions)
    if haveperms:
        return True

    currentActivity.requestPermissions(permissions, 0)

    t0 = time.time()
    while time.time() - t0 < timeout and not haveperms:
        haveperms = allgranted(permissions)

    return haveperms
