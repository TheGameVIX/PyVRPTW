```python
import sys
from PyQt5.QtWidgets import QApplication
from ui import VRP_UI
from vrp_solver import VRPSolver
from geocoding import Geocoder
from distance_matrix import DistanceMatrix
from cluster import Cluster
from map_generator import MapGenerator
from schedule_writer import ScheduleWriter
from logger import Logger

class MainApp:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.ui = VRP_UI()
        self.vrp_solver = VRPSolver()
        self.geocoder = Geocoder()
        self.distance_matrix = DistanceMatrix()
        self.cluster = Cluster()
        self.map_generator = MapGenerator()
        self.schedule_writer = ScheduleWriter()
        self.logger = Logger()

    def run(self):
        self.ui.upload_button.clicked.connect(self.handle_upload)
        self.ui.enter_button.clicked.connect(self.handle_enter)
        sys.exit(self.app.exec_())

    def handle_upload(self):
        try:
            file_path = self.ui.get_file_path()
            self.data = self.ui.read_file(file_path)
            self.ui.confirm_upload()
        except Exception as e:
            self.logger.log_error(str(e))

    def handle_enter(self):
        try:
            self.ui.show_progress("Geocoding addresses...")
            geocoded_data, failed_to_geocode = self.geocoder.geocode(self.data)
            self.geocoder.cache_geocodes(geocoded_data)
            self.geocoder.handle_failed_geocodes(failed_to_geocode)

            self.ui.show_progress("Creating clusters...")
            clusters = self.cluster.create_clusters(geocoded_data, self.ui.num_techs)

            self.ui.show_progress("Calculating distance matrix...")
            distance_matrix = self.distance_matrix.calculate(clusters)

            self.ui.show_progress("Solving VRP...")
            solution = self.vrp_solver.solve(distance_matrix, self.ui.get_constraints())

            self.ui.show_progress("Generating map...")
            map = self.map_generator.generate(clusters, solution)

            self.ui.show_progress("Writing schedule...")
            self.schedule_writer.write(solution)

            self.ui.show_optimization_complete()
        except Exception as e:
            self.logger.log_error(str(e))

if __name__ == "__main__":
    app = MainApp()
    app.run()
```