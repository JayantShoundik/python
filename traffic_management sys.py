import time
from threading import Thread, Event

class TrafficLight:
    def __init__(self):
        self.state = 'RED'  # Initial state
        self.stop_event = Event()
        self.night_mode = False

    def change_light(self):
        while not self.stop_event.is_set():
            if self.night_mode:
                print("Traffic Light🚥: 🟡 (Night Mode Active)")
                time.sleep(5) 
                print(time.sleep(5)) # Stay in YELLOW for 5 seconds
                continue
            
            if self.state == 'RED':
                print("\nTraffic Light🚥: 🔴 (Stop Cars, Walk for Pedestrians)")
                time.sleep(5) 
                print(time.sleep(5)) # RED for 5 seconds
                self.state = 'GREEN'
            elif self.state == 'GREEN':
                print("\nTraffic Light 🚥: 🟢 (Go Cars, Stop for Pedestrians)")
                time.sleep(5)  # GREEN for 5 seconds
                self.state = 'YELLOW'
            elif self.state == 'YELLOW':
                print("\nTraffic Light🚥: 🟡(Caution, Prepare to Stop)")
                time.sleep(2)
                print(time.sleep(2))  # YELLOW for 2 seconds
                self.state = 'RED'

    def start(self):
        self.light_thread = Thread(target=self.change_light)
        self.light_thread.start()

    def stop(self):
        self.stop_event.set()
        self.light_thread.join()

    def toggle_night_mode(self):
        self.night_mode = not self.night_mode
        if self.night_mode:
            print("\nNight mode activated. Traffic lights 🚥will stay 🟡")
        else:
            print("\nNight mode deactivated. Traffic lights🚥 will resume normal operation.")
            self.state = 'RED'  # Reset state to RED when turning off night mode

class PedestrianSignal:
    def __init__(self):
        self.state = 'DON\'T WALK'
        self.stop_event = Event()

    def change_signal(self):
        while not self.stop_event.is_set():
            if self.state == 'DON\'T WALK':
                print("\nPedestrian Signal:🚷-> DON'T WALK")
                time.sleep(5)  # DON'T WALK for 5 seconds
                self.state = 'WALK'
            elif self.state == 'WALK':
                print("\nPedestrian Signal: 🚶🏻-> WALK")
                time.sleep(5)  # WALK for 5 seconds
                self.state = 'DON\'T WALK'

    def start(self):
        self.signal_thread = Thread(target=self.change_signal)
        self.signal_thread.start()

    def stop(self):
        self.stop_event.set()
        self.signal_thread.join()

class TrafficManagementSystem:
    def __init__(self):
        self.traffic_light = TrafficLight()
        self.pedestrian_signal = PedestrianSignal()

    def start_system(self):
        self.traffic_light.start()
        self.pedestrian_signal.start()

    def stop_system(self):
        self.traffic_light.stop()
        self.pedestrian_signal.stop()

if __name__ == '__main__':
    tms = TrafficManagementSystem()
    
    try:
        tms.start_system()
        while True:
            command = input("Press 'n' to toggle night mode, 'q' to quit: ").strip().lower()
            if command == 'n':
                tms.traffic_light.toggle_night_mode()
            elif command == 'q':
                print("Stopping traffic management system...")
                tms.stop_system()
                print("System stopped.")
                
                break
    except KeyboardInterrupt:
        print("\n🛑Stopping traffic management system...")
        tms.stop_system()
        print("System stopped.🛑")
