import rumps
import subprocess

def pause():
    subprocess.run(["osascript", 'pause.scpt'])

def countdown_finised():
    pause()
    rumps.quit_application()

class SSTapp(rumps.App):
    def __init__(self):
        super(SSTapp, self).__init__(" ")

        self.icon = "icon.png"

        self.menu = [
            "5 Minutes",
            "10 minutes",
            "15 minutes",
            "30 minutes",
            "1 hour",
            "2 hours"
        ]
        self.remaining_time = 0
        self.timer = None

    def update_timer(self, _):
        if self.remaining_time > 0:
            mins, secs = divmod(self.remaining_time, 60)
            time_str = "{:02d}:{:02d}".format(mins, secs)
            self.title = time_str
            self.remaining_time -= 1
        else:
            self.remaining_time = 0
            self.timer.stop()
            countdown_finised()
            return None  # Stop the timer


    def countdown(self, seconds):
        if self.remaining_time > 0:
            self.remaining_time = 0
            self.title = ""
            if self.timer:
                self.timer.stop()
        else:
            self.remaining_time = seconds
            self.timer = rumps.Timer(self.update_timer,1)
            self.timer.start()


    @rumps.clicked("5 Minutes")
    def five_minutes(self, _):
        self.countdown(5*60)



    @rumps.clicked("10 minutes")
    def ten_minutes(self, _):
        self.countdown(10*60)


    @rumps.clicked("15 minutes")
    def fifteen_minutes(self, _):
        self.countdown(15*60)


    @rumps.clicked("30 minutes")
    def thirty_minutes(self, _):
        self.countdown(30*60)


    @rumps.clicked("1 hour")
    def one_hour(self, _):
        self.countdown(60*60)


    @rumps.clicked("2 hours")
    def two_hours(self, _):
        self.countdown(120*60)





# Run the app
if __name__ == "__main__":
    SSTapp().run()
