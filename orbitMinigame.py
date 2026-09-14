import math
G = 6.67430e-11
MAX_ATTEMPTS = 3

CELESTIAL_BODIES = {
	"Earth": {"mass": 5.972e24, "radius": 6.371e6},
	"Moon": {"mass": 7.342e22, "radius": 1.737e6},
	"Mars": {"mass": 6.417e23, "radius": 3.389e6},
	"Venus": {"mass": 4.867e24, "radius": 6.052e6},
}

MISSIONS = [
	{"body": "Earth", "altitude": 400, "hint": True},
	{"body": "Moon", "altitude": 100, "hint": True},
	{"body": "Mars", "altitude": 250, "hint": True},
	{"body": "Venus", "altitude": 300, "hint": False},
]


def orbital_velocity(body_name, altitude_km):
	"""Return circular orbital velocity in km/s."""
	body = CELESTIAL_BODIES[body_name]
	distance_m = body["radius"] + altitude_km * 1000
	velocity_mps = math.sqrt(G * body["mass"] / distance_m)
	return velocity_mps / 1000


def format_velocity(velocity):
	return f"{velocity:.2f} km/s"


def read_velocity():
	while True:
		answer = input("Enter launch velocity in km/s: ").strip()
		try:
			velocity = float(answer)
			if velocity <= 0:
				raise ValueError
			return velocity
		except ValueError:
			print("Please enter a positive number, such as 7.7.")


def result_for_difference(percent_difference):
	if percent_difference <= 2:
		return "PERFECT ORBIT", 100
	if percent_difference <= 5:
		return "STABLE ORBIT", 75
	if percent_difference <= 10:
		return "UNSTABLE ORBIT", 40
	return "MISSION FAILED", 0


def play_mission(number, mission):
	body_name = mission["body"]
	altitude = mission["altitude"]
	ideal_velocity = orbital_velocity(body_name, altitude)

	print("\n" + "=" * 42)
	print(f"MISSION {number} - {body_name.upper()}")
	print("=" * 42)
	print(f"Altitude above surface: {altitude} km")
	print("Your spacecraft has three launch attempts.")

	if mission["hint"]:
		print("Hint: circular orbital velocity depends on mass and distance.")

	for attempt in range(1, MAX_ATTEMPTS + 1):
		print(f"\nAttempt {attempt} of {MAX_ATTEMPTS}")
		velocity = read_velocity()
		percent_difference = abs(velocity - ideal_velocity) / ideal_velocity * 100
		outcome, points = result_for_difference(percent_difference)

		print("Calculating trajectory...")
		print(f"Result: {outcome}")
		print(f"Your velocity: {format_velocity(velocity)}")
		print(f"Difference from ideal: {percent_difference:.1f}%")

		if outcome != "MISSION FAILED":
			print(f"Mission points: {points}")
			return points

		if attempt < MAX_ATTEMPTS:
			print("Adjust your velocity and try again.")

	print(f"The ideal velocity was {format_velocity(ideal_velocity)}.")
	return 0


def show_intro():
	print("=" * 42)
	print("                 O R B I T")
	print("=" * 42)
	print("Pilot your spacecraft into stable orbits.")
	print("Choose a velocity close to the circular-orbit speed.")
	print("\nScoring:")
	print("  0-2% difference   PERFECT ORBIT   +100")
	print("  2-5% difference   STABLE ORBIT      +75")
	print("  5-10% difference  UNSTABLE ORBIT    +40")
	print("  Over 10%          MISSION FAILED      0")


def play_game():
	show_intro()
	score = 0
	mission_number = 1

	for mission in MISSIONS:
		score += play_mission(mission_number, mission)
		print(f"Current score: {score}")
		mission_number += 1

	print("\n" + "=" * 42)
	print("MISSION COMPLETE")
	print(f"Final score: {score}/{len(MISSIONS) * 100}")
	print("Orbital velocity is higher when gravity is stronger or")
	print("when the spacecraft is closer to the body's center.")
	print("=" * 42)


play_game()
