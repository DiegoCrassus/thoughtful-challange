
class ThoughtfulRobot:
    MAXIMUN_VOL = 1000000
    MAXIMUN_MAS = 20

    def sort(self, width: float, height: float, length: float, mass: float) -> str:
        bulky = False
        heavy = False

        if (width * height * length) >= self.MAXIMUN_VOL:
            bulky = True

        if mass >= self.MAXIMUN_MAS:
            heavy = True

        return "REJECTED" if bulky and heavy else "SPECIAL" if bulky or heavy else "STANDARD"

if __name__ == '__main__':
    robot = ThoughtfulRobot()
    with open('examples.txt', 'r') as file:
        examples = [linha.strip().split() for linha in file.readlines()]
    
    test_examples = [{
        "width": float(example[0]),
        "height": float(example[1]),
        "length": float(example[2]),
        "mass": float(example[3])
        } for example in examples]
    
    for sample in test_examples:
        print(f"Sample: {sample}\nResult: {robot.sort(**sample)}")
