from account import account

class moderator_account(account):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.is_moderator = True

    def delete_post(self, post):
        # Code to delete a post
        pass

    def ban_user(self, user):
        # Code to ban a user
        pass