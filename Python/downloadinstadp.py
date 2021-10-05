import instaloader
ig = instaloader.Instaloader()
profile = input("Enter Username - ")
ig.download_profile(profile,profile_pic_only=True)
