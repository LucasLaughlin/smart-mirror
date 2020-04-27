import subprocess
import datetime

class Alarm:
    _alarmTime = None
    _alarmState: int = 0

    def soundAlarm(self) -> None:
        # Triggers the alarm noise
        if _alarmTime == datetime.now():
            print("The alarm is ringing")

    def toggle(self) -> None:
        if not _alarmState:
            # Toggles the state of the alarm
            timeNow = datetime.now()
            self._alarmTime = timeNow
            alarmTime = "" + timeNow.hour + timeNow.minute

            # Updates the HTML
            subprocess.run(["export", "dynData", alarmTime])
            subprocess.run(["sed", 's/<h3 name="Alarm".+/<h3 name="Alarm" class="pt-3">$(echo $(dynData))</h3>/', "index.html"])

            _alarmState = 1
        else:
            _alarmState = 0

    def earlier(self) -> None:
        # Decrease alarm time by some constant amount
        _alarmTime = _alarmTime - datetime.timedelta(minutes=15)
        self.updateTime()

    def later(self) -> None:
        # Increase alarm time by some constant amount
        _alarmTime = _alarmTime + datetime.timedelta(minutes=15)
        self.updateTime()

    def updateTime(self) -> None:
        alarmTime = "" + self._alarmTime.hour + self._alarmTime.minute
        subprocess.run(["export", "dynData", alarmTime])
        subprocess.run(["sed", 's/<h3 name="Alarm".+/<h3 name="Alarm" class="pt-3">$(echo $(dynData))</h3>/', "index.html"])

