
class Material:
    def __init__(self) -> None:
        pass

class ThinFilm:
    def __init__(self, material: Material, thicknessNm: int) -> None:
        self.thickness = 1e-3 * thicknessNm
        self.material = material

class Wafer:
    def __init__(self, diameterMm=100, thicknessUm=525) -> None:
        self.diameter = diameterMm * 1e-6
        self.thickness = thicknessUm
