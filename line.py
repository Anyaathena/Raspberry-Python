from line_notify import LineNotify

ACCESS_TOKEN = 'TOKEN' #?��??��???notify = LineNotify(ACCESS_TOKEN)

notify.send('hello')
notify.send("Image test", image_path='./demo.jpeg')
