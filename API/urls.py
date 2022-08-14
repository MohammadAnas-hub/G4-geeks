from django.urls import path
from API.views import UserView, WordView

urlpatterns = [
    # ======== Users Enpoints =======
    path("get-all-users", UserView.GetAllUsersView, name="GetAllUsers"),
    path("get-user-by-id", UserView.GeUserByIDView, name="GetUserByID"),
    path("create-user", UserView.CreateUserView, name="CreateUser"),
    path("update-user", UserView.UpdateUserView, name="UpdateUser"),
    path("delete-user", UserView.DeleteUserView, name="DeleteUser"),

    # ======== Word Endpoints ========
    path("create-word-view", WordView.CreateWordView, name="CreateWord")
]