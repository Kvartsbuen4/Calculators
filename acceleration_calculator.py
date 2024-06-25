class MotionSimulator:
    def __init__(self):
        self.start_speed = 0.0
        self.max_speed = 0.0
        self.max_acceleration = 0.0
        self.acceleration_curve_percent = 0.0
        self.goal_type = ""
        self.goal_value = 0.0

    def get_inputs(self):
        # Get starting speed
        start_speed_input = input("Enter the starting speed of the object in kph (or leave empty for 0): ")
        self.start_speed = float(start_speed_input) if start_speed_input else 0.0

        # Get maximum speed
        self.max_speed = float(input("Enter the maximum speed in kph: "))

        # Get maximum acceleration
        self.max_acceleration = float(input("Enter the maximum acceleration in kph per second: "))

        # Get acceleration curve percentage
        self.acceleration_curve_percent = float(input("Enter the acceleration curve percentage (0-100): "))

        # Get goal type and value
        self.goal_type = input("Enter the goal type (seconds, speed, distance): ").strip().lower()
        self.goal_value = float(input(f"Enter the goal value for {self.goal_type}: "))

    def calculate_acceleration_rate(self, time_elapsed, total_time_to_max_acceleration):
        if time_elapsed >= total_time_to_max_acceleration:
            return self.max_acceleration
        else:
            return (time_elapsed / total_time_to_max_acceleration) * self.max_acceleration

    def simulate(self):
        current_speed = self.start_speed
        total_distance = 0.0
        time_elapsed = 0

        # Calculate the time required to reach the max acceleration rate based on the curve percentage
        total_time_to_max_acceleration = (100 / self.acceleration_curve_percent)  # e.g., 5% means 20 seconds to max

        while True:
            # Convert speed from kph to km/s for distance calculation
            speed_in_kps = current_speed / 3600.0

            # Calculate distance covered in this second
            total_distance += speed_in_kps

            # Update time
            time_elapsed += 1

            # Update speed with current acceleration rate
            current_acceleration_rate = self.calculate_acceleration_rate(time_elapsed, total_time_to_max_acceleration)
            if current_speed < self.max_speed:
                current_speed += current_acceleration_rate
                if current_speed > self.max_speed:
                    current_speed = self.max_speed

            # Print the current state
            print(f"sec {time_elapsed}: dis = {total_distance:.8f} km, speed = {current_speed:.1f} kph, acc = {current_acceleration_rate:.1f} kph/s")

            # Check goal conditions
            if self.goal_type == "seconds" and time_elapsed >= self.goal_value:
                break
            elif self.goal_type == "speed" and current_speed >= self.goal_value:
                break
            elif self.goal_type == "distance" and total_distance >= self.goal_value:
                break

        print("Simulation ended.")

if __name__ == "__main__":
    simulator = MotionSimulator()
    simulator.get_inputs()
    simulator.simulate()
