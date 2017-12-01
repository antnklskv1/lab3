import Heir_classes


a = Heir_classes.GetVkUserInfo()
a.user_id_or_username = 'carpediemmm'
b = Heir_classes.GetVkFriendsInfo()
b.user_id = a.execute()
b.execute()