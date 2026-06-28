class CountFromBy:
    def increase(self) -> None:
        """Increase the count by the specified step."""
        self.count += self.step

        
    def __init__(self, count: int = 0, step: int = 1) -> None:
        """Initialize the CountFromBy object with the given count and step."""
        self.count = count
        self.step = step